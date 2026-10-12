"""Telegram-бот собственника: одобрения роликов, отчёты, указания директору.

Что умеет собственник в чате с ботом:
  кнопки ✅ / 🔁 под роликом      — одобрить или вернуть на доработку
  ответ текстом на ролик          — объяснить, что исправить
  любое сообщение                 — указание директору (попадёт в company/inbox.md)
  /status   — как дела в компании        /budget  — сколько потрачено
  /run      — начать рабочий день сейчас  /pause, /resume — остановить или продолжить работу
  /auto on|off — автопубликация без одобрения
  /revenue 25 brand Заметка — записать доход (источник: platform, brand, affiliate, product, other)

Команды для агентов:
  python tools/telegram_bot.py send "Текст"
  python tools/telegram_bot.py send-file media/ep-0003/qc/sheet.jpg --caption "Лист кадров"
  python tools/telegram_bot.py approval ep-0003     # отправить ролик на одобрение
  python tools/telegram_bot.py poll                 # обработать ответы собственника (делает GitHub раз в 30 минут)
"""
from __future__ import annotations

import argparse
import html
import json
import os
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import budget  # noqa: E402
from common import (COMPANY_DIR, ROOT, STATE_DIR, all_episodes, approval_required, die,  # noqa: E402
                    dry_run, env, load_config, load_episode, load_json, now_iso, save_config,
                    save_episode, save_json, today_msk)
from common import office as _office  # noqa: E402

STATE = STATE_DIR / "telegram.json"
INBOX = COMPANY_DIR / "inbox.md"


def _token() -> str:
    return env("TELEGRAM_BOT_TOKEN", required=True)


def _owner() -> str | None:
    return env("TELEGRAM_OWNER_ID")


def api(method: str, data: dict | None = None, files: dict | None = None, timeout: int = 60) -> dict:
    if dry_run():
        print(f"[DRY_RUN telegram.{method}] {json.dumps(data or {}, ensure_ascii=False)[:300]}")
        return {"message_id": 0, "video": {"file_id": "dry"}}
    url = f"https://api.telegram.org/bot{_token()}/{method}"
    r = requests.post(url, data=data, files=files, timeout=timeout)
    payload = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
    if not payload.get("ok"):
        raise RuntimeError(f"Telegram {method}: {payload.get('description') or r.text[:300]}")
    return payload["result"]


def send(text: str, chat_id: str | None = None, reply_markup: dict | None = None) -> dict:
    chat = chat_id or _owner()
    if not chat:
        print("(Telegram не настроен: нет TELEGRAM_OWNER_ID — сообщение не отправлено)")
        return {}
    data = {"chat_id": chat, "text": text[:4096], "parse_mode": "HTML", "disable_web_page_preview": "true"}
    if reply_markup:
        data["reply_markup"] = json.dumps(reply_markup)
    return api("sendMessage", data)


def send_file(path: str, caption: str = "") -> dict:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        die(f"Файл не найден: {p}")
    method, field = ("sendPhoto", "photo") if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"} \
        else ("sendVideo", "video") if p.suffix.lower() in {".mp4", ".mov"} else ("sendDocument", "document")
    with open(p, "rb") as f:
        return api(method, {"chat_id": _owner(), "caption": caption[:1024], "parse_mode": "HTML"},
                   files={field: f}, timeout=300)


def _esc(value) -> str:
    return html.escape(str(value or ""))


def request_approval(ep_id: str) -> None:
    ep = load_episode(ep_id)
    final = ep.get("assets", {}).get("final_path")
    if not final or not (ROOT / final).exists():
        die(f"У {ep_id} нет собранного ролика (assets.final_path)")
    yt = ep.get("youtube") or {}
    caption = (
        f"🎬 <b>{_esc(ep.get('title'))}</b> · {ep_id}\n"
        f"{_esc(ep.get('logline'))}\n\n"
        f"⏱ {ep.get('assets', {}).get('duration_s')} с · 💵 ${ep.get('cost_usd', 0):.2f}\n"
        f"YouTube: {_esc(yt.get('title'))}\n\n"
        f"Публикуем? Чтобы объяснить, что исправить, ответь на это сообщение текстом."
    )
    markup = {"inline_keyboard": [[
        {"text": "✅ Публикуем", "callback_data": f"approve:{ep_id}"},
        {"text": "🔁 Переделать", "callback_data": f"reject:{ep_id}"},
    ]]}
    with open(ROOT / final, "rb") as f:
        msg = api("sendVideo", {"chat_id": _owner(), "caption": caption[:1024], "parse_mode": "HTML",
                                "supports_streaming": "true", "reply_markup": json.dumps(markup)},
                  files={"video": f}, timeout=300)
    ep["approval"].update({"required": True, "requested_at": now_iso(), "decision": None,
                           "message_id": msg.get("message_id"),
                           "telegram_file_id": (msg.get("video") or {}).get("file_id")})
    ep["status"] = "awaiting_approval"
    ep.setdefault("history", []).append({"t": now_iso(), "status": "awaiting_approval"})
    save_episode(ep)
    _office("pipeline")
    _office("event", "publisher", f"{ep_id} отправлен собственнику на одобрение")
    print(f"{ep_id} отправлен на одобрение")


def _find_episode_by_message(message_id: int) -> dict | None:
    for ep in all_episodes():
        if (ep.get("approval") or {}).get("message_id") == message_id:
            return ep
    return None


def _decide(ep_id: str, decision: str, comment: str | None = None) -> str:
    ep = load_episode(ep_id)
    ep["approval"].update({"decision": decision, "decided_at": now_iso()})
    if comment:
        ep["approval"]["comment"] = comment
    if decision == "approved":
        ep["status"] = "approved"
        ep["history"].append({"t": now_iso(), "status": "approved"})
        save_episode(ep)
        _office("event", "owner", f"Собственник одобрил {ep_id}", "--kind", "success")
        import publish  # noqa: WPS433 — ленивый импорт, чтобы не было циклов
        result = publish.publish_episode(ep_id)
        return result
    ep["status"] = "rejected"
    ep["history"].append({"t": now_iso(), "status": "rejected", "note": comment})
    save_episode(ep)
    _office("event", "owner", f"Собственник вернул {ep_id} на доработку" + (f": {comment}" if comment else ""),
            "--kind", "warning")
    _office("pipeline")
    return "Вернул на доработку. Ответь на сообщение с роликом текстом — что исправить. Директор учтёт завтра."


def _status_text() -> str:
    cfg = load_config()
    b = budget.status()
    eps = all_episodes()
    last = eps[-5:]
    lines = [f"🏢 <b>{_esc(cfg.get('company_name'))}</b>",
             f"Ниша: {_esc(cfg.get('niche') or 'ещё не выбрана')}",
             f"Режим: {'⏸ пауза' if cfg.get('paused') else '▶️ работает'} · "
             f"{'одобрение собственника' if approval_required(cfg) else 'автопубликация'}",
             f"💵 Потрачено за месяц: ${b['spent_usd']} из ${b['monthly_limit_usd']}",
             "", "<b>Последние ролики:</b>"]
    from episodes import LABELS  # noqa: WPS433
    for ep in reversed(last):
        lines.append(f"• {ep['id']} — {_esc(ep.get('title'))} ({LABELS.get(ep.get('status'), ep.get('status'))})")
    if not last:
        lines.append("пока нет")
    return "\n".join(lines)


def _dispatch_daily() -> str:
    token, repo = os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        return "Не могу запустить отсюда: нет доступа к GitHub Actions."
    r = requests.post(f"https://api.github.com/repos/{repo}/actions/workflows/daily-cycle.yml/dispatches",
                      headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
                      json={"ref": os.environ.get("GITHUB_REF_NAME", "main")}, timeout=30)
    if r.status_code in (200, 204):
        return "Запускаю рабочий день. Через минуту офис оживёт."
    return f"GitHub не дал запустить: {r.status_code} {r.text[:200]}"


def _handle_command(text: str) -> str:
    parts = text.strip().split()
    cmd = parts[0].split("@")[0].lower()
    cfg = load_config()
    if cmd in {"/start", "/help"}:
        return ("Я бот твоей компании. Присылаю ролики на одобрение и отчёты директора.\n"
                "Любое сообщение — указание директору.\n"
                "/status /budget /run /pause /resume /auto on|off\n/revenue 25 brand заметка")
    if cmd == "/status":
        return _status_text()
    if cmd == "/budget":
        b = budget.status()
        return (f"💵 Месяц {b['month']}: потрачено ${b['spent_usd']} из ${b['monthly_limit_usd']} "
                f"(≈{cfg.get('budget', {}).get('monthly_rub')} ₽)\n"
                f"Сегодня можно ещё ${b['today_remaining_usd']} · резерв ${b['reserve_usd']}")
    if cmd == "/run":
        return _dispatch_daily()
    if cmd in {"/pause", "/resume"}:
        cfg["paused"] = cmd == "/pause"
        save_config(cfg)
        return "⏸ Компания на паузе. /resume — продолжить." if cfg["paused"] else "▶️ Работаем дальше."
    if cmd == "/auto":
        arg = parts[1].lower() if len(parts) > 1 else ""
        if arg not in {"on", "off"}:
            return "Напиши /auto on или /auto off"
        cfg.setdefault("approval", {})["mode"] = "auto" if arg == "on" else "manual"
        save_config(cfg)
        return ("🤖 Автопубликация включена: ролики выходят без одобрения, тебе приходит уведомление."
                if arg == "on" else "✋ Теперь каждый ролик сначала приходит тебе на одобрение.")
    if cmd == "/revenue":
        try:
            amount = float(parts[1].replace(",", "."))
            source = parts[2] if len(parts) > 2 else "other"
            if source not in {"platform", "brand", "affiliate", "product", "other"}:
                source = "other"
            note = " ".join(parts[3:])
        except (IndexError, ValueError):
            return "Формат: /revenue 25 brand Заметка (сумма в долларах)"
        from common import load_json as _lj, save_json as _sj  # noqa: WPS433
        rev = _lj(COMPANY_DIR / "revenue.json", {"entries": []}) or {"entries": []}
        rev["entries"].append({"date": now_iso(), "amount_usd": amount, "source": source, "note": note})
        _sj(COMPANY_DIR / "revenue.json", rev)
        _office("event", "cfo", f"Доход +${amount:.2f} ({source})", "--kind", "money")
        _office("metrics")
        return f"Записал доход ${amount:.2f} ({source})."
    return "Не знаю такой команды. /help"


def _to_inbox(text: str) -> None:
    INBOX.parent.mkdir(parents=True, exist_ok=True)
    existing = INBOX.read_text(encoding="utf-8") if INBOX.exists() else "# Указания собственника\n"
    lines = existing.rstrip("\n").split("\n")
    if "## Новые" not in lines:
        lines += ["", "## Новые", ""]
    start = lines.index("## Новые")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    while end > start + 1 and not lines[end - 1].strip():
        end -= 1  # вставляем сразу после последнего пункта, до пустых строк
    entry = f"- [{today_msk()}] {' '.join(text.split())}"
    lines.insert(end, entry)
    INBOX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def poll() -> None:
    owner = _owner()
    state = load_json(STATE, {"offset": 0}) or {"offset": 0}
    updates = api("getUpdates", {"offset": state.get("offset", 0), "timeout": 0,
                                 "allowed_updates": json.dumps(["message", "callback_query"])})
    if not updates:
        print("Новых сообщений нет")
        return
    for upd in updates:
        state["offset"] = upd["update_id"] + 1
        save_json(STATE, state)  # сохраняем сразу, чтобы не обработать дважды
        try:
            _handle_update(upd, owner)
        except Exception as exc:  # одно сообщение не должно ломать остальные
            print(f"Ошибка обработки обновления {upd.get('update_id')}: {exc}", file=sys.stderr)
            try:
                send(f"⚠️ Не смог обработать сообщение: {_esc(exc)}")
            except Exception:
                pass
    print(f"Обработано обновлений: {len(updates)}")


def _handle_update(upd: dict, owner: str | None) -> None:
    if "callback_query" in upd:
        cq = upd["callback_query"]
        if str(cq["from"]["id"]) != str(owner):
            api("answerCallbackQuery", {"callback_query_id": cq["id"], "text": "Это закрытый бот"})
            return
        action, _, ep_id = cq.get("data", "").partition(":")
        api("answerCallbackQuery", {"callback_query_id": cq["id"], "text": "Принято"})
        msg = cq.get("message") or {}
        if msg:
            try:
                api("editMessageReplyMarkup", {"chat_id": msg["chat"]["id"], "message_id": msg["message_id"],
                                               "reply_markup": json.dumps({"inline_keyboard": []})})
            except Exception:
                pass
        ep = load_episode(ep_id)
        if ep.get("approval", {}).get("decision"):
            send(f"{ep_id}: решение уже принято ({ep['approval']['decision']}).")
            return
        result = _decide(ep_id, "approved" if action == "approve" else "rejected")
        send(result)
        return

    message = upd.get("message") or {}
    sender = str((message.get("from") or {}).get("id", ""))
    text = message.get("text") or message.get("caption") or ""
    if not text:
        return
    if not owner:
        send(f"Твой Telegram ID: <code>{sender}</code>\nДобавь его в секрет TELEGRAM_OWNER_ID (см. SETUP.md).",
             chat_id=message["chat"]["id"])
        return
    if sender != str(owner):
        send("Это закрытый бот компании.", chat_id=message["chat"]["id"])
        return
    if text.startswith("/"):
        send(_handle_command(text))
        return
    reply_to = (message.get("reply_to_message") or {}).get("message_id")
    if reply_to:
        ep = _find_episode_by_message(reply_to)
        if ep:
            if ep.get("approval", {}).get("decision") in (None, "rejected"):
                if ep.get("approval", {}).get("decision") is None:
                    _decide(ep["id"], "rejected", text)
                else:
                    ep["approval"]["comment"] = text
                    save_episode(ep)
                send(f"Понял, {ep['id']} переделаем с учётом: «{_esc(text)}»")
            else:
                _to_inbox(f"По {ep['id']}: {text}")
                send("Передал директору.")
            return
    _to_inbox(text)
    _office("event", "owner", f"Указание собственника: {text[:120]}")
    send("📨 Передал директору — учтёт в ближайший рабочий день.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Telegram-бот собственника")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("send")
    p.add_argument("text")
    p = sub.add_parser("send-file")
    p.add_argument("path")
    p.add_argument("--caption", default="")
    p = sub.add_parser("approval")
    p.add_argument("episode")
    sub.add_parser("poll")
    sub.add_parser("whoami", help="проверить, что бот настроен")
    args = parser.parse_args()

    if not env("TELEGRAM_BOT_TOKEN") and not dry_run():
        print("(Telegram не настроен: нет TELEGRAM_BOT_TOKEN — пропускаю)")
        return
    if args.cmd == "send":
        send(args.text)
    elif args.cmd == "send-file":
        send_file(args.path, args.caption)
    elif args.cmd == "approval":
        request_approval(args.episode)
    elif args.cmd == "poll":
        poll()
    elif args.cmd == "whoami":
        print(json.dumps(api("getMe"), ensure_ascii=False))


if __name__ == "__main__":
    main()
