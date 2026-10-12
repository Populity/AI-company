"""Instagram Reels через официальный API (Instagram API with Instagram Login).

Нужны: профессиональный аккаунт Instagram (Автор или Бизнес) и секрет INSTAGRAM_ACCESS_TOKEN
(как получить — SETUP.md). Ролик должен лежать по публичной ссылке, поэтому publish.py
сначала выкладывает его в хранилище fal.ai.

Токен живёт 60 дней. Раз в неделю workflow продлевает его командой refresh-token;
если задан секрет GH_PAT, новый токен сам запишется в секреты репозитория.

Примеры:
  python tools/instagram.py check
  python tools/instagram.py stats
  python tools/instagram.py refresh-token
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import COMPANY_DIR, STATE_DIR, all_episodes, die, env, load_config, now_iso, save_json  # noqa: E402


def _base() -> str:
    version = load_config().get("platforms", {}).get("instagram", {}).get("api_version", "v25.0")
    return f"https://graph.instagram.com/{version}"


def configured() -> bool:
    return bool(env("INSTAGRAM_ACCESS_TOKEN"))


def _req(method: str, path: str, **params) -> dict:
    params["access_token"] = env("INSTAGRAM_ACCESS_TOKEN", required=True)
    url = f"{_base()}/{path}"
    r = requests.request(method, url, params=params if method == "GET" else None,
                         data=params if method != "GET" else None, timeout=60)
    data = r.json() if r.content else {}
    if r.status_code != 200 or "error" in data:
        err = data.get("error", {})
        raise RuntimeError(f"Instagram API {path}: {err.get('message') or r.text[:300]}")
    return data


def me() -> dict:
    return _req("GET", "me", fields="user_id,username,followers_count,media_count,account_type")


def user_id() -> str:
    if env("INSTAGRAM_USER_ID"):
        return env("INSTAGRAM_USER_ID")
    info = me()
    return str(info.get("user_id") or info.get("id"))


def publish_reel(video_url: str, caption: str, share_to_feed: bool = True) -> dict:
    uid = user_id()
    container = _req("POST", f"{uid}/media", media_type="REELS", video_url=video_url,
                     caption=caption[:2200], share_to_feed="true" if share_to_feed else "false")
    cid = container["id"]
    status = "IN_PROGRESS"
    for _ in range(60):  # до 10 минут на обработку
        time.sleep(10)
        status = _req("GET", cid, fields="status_code,status").get("status_code", "")
        if status in {"FINISHED", "ERROR", "EXPIRED"}:
            break
    if status != "FINISHED":
        raise RuntimeError(f"Instagram не обработал видео (статус {status})")
    media = _req("POST", f"{uid}/media_publish", creation_id=cid)
    info = _req("GET", media["id"], fields="permalink")
    return {"id": media["id"], "url": info.get("permalink")}


def insights(media_id: str) -> dict:
    for metrics in ("views,reach,likes,comments,shares,saved", "reach,likes,comments,shares,saved"):
        try:
            data = _req("GET", f"{media_id}/insights", metric=metrics)
            return {d["name"]: (d.get("values") or [{}])[0].get("value", d.get("total_value", {}).get("value"))
                    for d in data.get("data", [])}
        except RuntimeError:
            continue
    return {}


def stats() -> dict:
    acc = me()
    result = {"updated": now_iso(), "instagram_username": acc.get("username"),
              "instagram_followers": acc.get("followers_count"), "instagram_media": acc.get("media_count")}
    per = {}
    for ep in all_episodes():
        ig = (ep.get("publish") or {}).get("instagram") or {}
        if ig.get("id"):
            per[ep["id"]] = insights(ig["id"])
    result["instagram_per_episode"] = per
    return result


def _update_github_secret(name: str, value: str) -> bool:
    pat, repo = env("GH_PAT"), os.environ.get("GITHUB_REPOSITORY")
    if not pat or not repo:
        return False
    from nacl import encoding, public  # noqa: WPS433
    headers = {"Authorization": f"Bearer {pat}", "Accept": "application/vnd.github+json"}
    key = requests.get(f"https://api.github.com/repos/{repo}/actions/secrets/public-key",
                       headers=headers, timeout=30).json()
    sealed = public.SealedBox(public.PublicKey(key["key"].encode(), encoding.Base64Encoder()))
    encrypted = base64.b64encode(sealed.encrypt(value.encode())).decode()
    r = requests.put(f"https://api.github.com/repos/{repo}/actions/secrets/{name}", headers=headers,
                     json={"encrypted_value": encrypted, "key_id": key["key_id"]}, timeout=30)
    return r.status_code in (201, 204)


def refresh_token() -> str:
    token = env("INSTAGRAM_ACCESS_TOKEN", required=True)
    r = requests.get("https://graph.instagram.com/refresh_access_token",
                     params={"grant_type": "ig_refresh_token", "access_token": token}, timeout=30)
    data = r.json()
    if "access_token" not in data:
        raise RuntimeError(f"Не удалось продлить токен Instagram: {data}")
    new = data["access_token"]
    days = int(data.get("expires_in", 0)) // 86400
    saved = new == token or _update_github_secret("INSTAGRAM_ACCESS_TOKEN", new)
    save_json(STATE_DIR / "instagram.json", {"refreshed_at": now_iso(), "expires_in_days": days,
                                            "secret_updated": bool(saved)})
    if saved:
        return f"Токен Instagram продлён на {days} дн."
    return (f"Токен Instagram продлён на {days} дн., но новый токен не удалось записать в секреты "
            f"(нет GH_PAT). Обнови секрет INSTAGRAM_ACCESS_TOKEN вручную в течение {days} дн.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Instagram")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("stats")
    sub.add_parser("refresh-token")
    args = parser.parse_args()
    if not configured():
        print("Instagram не настроен (нет INSTAGRAM_ACCESS_TOKEN) — пропускаю")
        return
    try:
        if args.cmd == "check":
            acc = me()
            print(f"OK: @{acc.get('username')} ({acc.get('account_type')}), подписчиков {acc.get('followers_count')}")
        elif args.cmd == "stats":
            data = stats()
            save_json(COMPANY_DIR / "metrics" / "instagram.json", data)
            print(json.dumps({k: v for k, v in data.items() if k != "instagram_per_episode"}, ensure_ascii=False))
        elif args.cmd == "refresh-token":
            print(refresh_token())
    except RuntimeError as exc:
        die(str(exc))


if __name__ == "__main__":
    main()
