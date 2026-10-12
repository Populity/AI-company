"""Публикация эпизода на все включённые площадки.

Защита: ролик выходит, только если собственник его одобрил, либо включена
автопубликация (после испытательного срока) и ролик прошёл проверку качества.
Если компания на паузе (/pause в Telegram) — ничего не публикуется.

  python tools/publish.py ep-0003
"""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (ROOT, approval_required, die, dry_run, env, load_config, load_episode,  # noqa: E402
                    now_iso, save_episode)
from common import office as _office  # noqa: E402


def _ensure_local_file(ep: dict) -> Path:
    rel = ep.get("assets", {}).get("final_path") or f"media/{ep['id']}/final.mp4"
    path = ROOT / rel
    if path.exists():
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    url = ep.get("assets", {}).get("final_url")
    if url and not url.startswith("https://example.invalid"):
        with requests.get(url, stream=True, timeout=300) as r:
            r.raise_for_status()
            path.write_bytes(r.content)
        return path
    file_id = (ep.get("approval") or {}).get("telegram_file_id")
    token = env("TELEGRAM_BOT_TOKEN")
    if file_id and token and file_id != "dry":
        info = requests.get(f"https://api.telegram.org/bot{token}/getFile", params={"file_id": file_id},
                            timeout=30).json()
        fp = info["result"]["file_path"]
        data = requests.get(f"https://api.telegram.org/file/bot{token}/{fp}", timeout=300).content
        path.write_bytes(data)
        return path
    die(f"Не нашёл файл ролика {ep['id']}: ни на диске, ни по ссылке, ни в Telegram")
    raise RuntimeError("unreachable")


def _check_allowed(ep: dict, cfg: dict) -> None:
    if cfg.get("paused"):
        die("Компания на паузе (/pause) — публикации остановлены собственником")
    if ep.get("status") == "published":
        die(f"{ep['id']} уже опубликован")
    if approval_required(cfg):
        if (ep.get("approval") or {}).get("decision") != "approved":
            die(f"{ep['id']} не одобрен собственником. Сначала: python tools/telegram_bot.py approval {ep['id']}")
    elif not (ep.get("qc") or {}).get("passed"):
        die(f"{ep['id']} не прошёл проверку качества (qc.passed != true)")


def publish_episode(ep_id: str) -> str:
    cfg = load_config()
    ep = load_episode(ep_id)
    _check_allowed(ep, cfg)
    platforms = cfg.get("platforms", {})
    video = _ensure_local_file(ep)
    tags = [t if t.startswith("#") else f"#{t}" for t in (ep.get("hashtags") or [])]
    results, problems = [], []
    ep.setdefault("publish", {})

    # --- YouTube ---
    yt_cfg = platforms.get("youtube", {})
    if yt_cfg.get("enabled"):
        yt = ep.get("youtube") or {}
        title = yt.get("title") or ep.get("title") or ep_id
        description = (yt.get("description") or "") + ("\n\n" + " ".join(tags) if tags else "")
        import youtube  # noqa: WPS433
        if yt_cfg.get("mode") == "api" and youtube.configured() and not dry_run():
            try:
                res = youtube.upload(str(video), title, description, yt.get("tags") or [],
                                     yt_cfg.get("privacy", "public"))
                ep["publish"]["youtube"] = {**res, "status": "published", "at": now_iso()}
                results.append(f"YouTube: {res['url']}")
                if res.get("privacy") == "private" and yt_cfg.get("privacy", "public") != "private":
                    problems.append("YouTube сделал ролик приватным — проект ещё не прошёл проверку API. "
                                    "Переключи platforms.youtube.mode на \"manual\" или дождись проверки.")
            except SystemExit:
                problems.append("YouTube: загрузка не удалась (подробности в логе GitHub Actions)")
        else:
            ep["publish"]["youtube"] = {"status": "manual_pending", "at": now_iso()}
            _send_manual_youtube(ep, video, title, description)
            results.append("YouTube: отправил тебе ролик и текст — выложи вручную в приложении YouTube")

    # --- Instagram ---
    ig_cfg = platforms.get("instagram", {})
    if ig_cfg.get("enabled"):
        import instagram  # noqa: WPS433
        if instagram.configured() and not dry_run():
            try:
                url = ep.get("assets", {}).get("final_url")
                if not url or url.startswith("https://example.invalid"):
                    import fal_gen  # noqa: WPS433
                    url = fal_gen.upload(str(video))
                    ep["assets"]["final_url"] = url
                caption = ((ep.get("instagram") or {}).get("caption") or ep.get("title") or "")
                caption = caption.rstrip() + ("\n\n" + " ".join(tags) if tags else "")
                res = instagram.publish_reel(url, caption)
                ep["publish"]["instagram"] = {**res, "status": "published", "at": now_iso()}
                results.append(f"Instagram: {res.get('url')}")
            except Exception as exc:
                problems.append(f"Instagram: {exc}")
        else:
            problems.append("Instagram не настроен (нет токена) — пропустил")

    published_somewhere = any((v or {}).get("status") in {"published", "manual_pending"}
                              for v in ep["publish"].values())
    if published_somewhere:
        ep["status"] = "published"
        ep.setdefault("history", []).append({"t": now_iso(), "status": "published"})
    save_episode(ep)
    _office("pipeline")
    _office("metrics")
    _office("event", "publisher", f"{ep_id} опубликован: " + "; ".join(results) if results else
            f"{ep_id}: публикация не удалась", "--kind", "success" if published_somewhere else "error")
    message = f"📣 {ep_id} «{html.escape(ep.get('title') or '')}»\n" + "\n".join(results + problems)
    _notify(message)
    return message


def _send_manual_youtube(ep: dict, video: Path, title: str, description: str) -> None:
    import telegram_bot  # noqa: WPS433
    if not env("TELEGRAM_BOT_TOKEN") or dry_run():
        print("(ручная публикация YouTube: Telegram не настроен)")
        return
    text = (f"📺 <b>YouTube — выложи вручную</b> ({ep['id']})\n"
            f"1) Сохрани видео ниже → приложение YouTube → «+» → «Создать Short»\n"
            f"2) Название:\n<code>{html.escape(title[:100])}</code>\n"
            f"3) Описание:\n<code>{html.escape(description[:900])}</code>\n"
            f"4) В «Дополнительно» отметь «Изменённый или синтетический контент: Да»")
    file_id = (ep.get("approval") or {}).get("telegram_file_id")
    if file_id and file_id != "dry":
        telegram_bot.api("sendVideo", {"chat_id": env("TELEGRAM_OWNER_ID"), "video": file_id})
    else:
        telegram_bot.send_file(str(video))
    telegram_bot.send(text)


def _notify(text: str) -> None:
    try:
        import telegram_bot  # noqa: WPS433
        if env("TELEGRAM_BOT_TOKEN"):
            telegram_bot.send(text)
    except Exception as exc:
        print(f"(уведомление не отправлено: {exc})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Публикация эпизода")
    parser.add_argument("episode", help="id эпизода, или mode — узнать текущий режим")
    args = parser.parse_args()
    if args.episode == "mode":
        cfg = load_config()
        if cfg.get("paused"):
            print("paused — компания на паузе, публиковать нельзя")
        elif approval_required(cfg):
            print("approval — нужен ролик на одобрение: python tools/telegram_bot.py approval <id>")
        else:
            print("auto — автопилот: python tools/publish.py <id>")
        return
    print(publish_episode(args.episode))


if __name__ == "__main__":
    main()
