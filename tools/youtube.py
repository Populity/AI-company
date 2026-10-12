"""YouTube: загрузка Shorts, статистика канала, тренды.

Нужны секреты YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN (см. SETUP.md).

ВАЖНО: пока проект Google Cloud не прошёл проверку YouTube API (audit), всё, что
загружено через API, YouTube принудительно делает приватным. Поэтому в config/company.json
по умолчанию platforms.youtube.mode = "manual": бот присылает собственнику готовый
ролик и текст, а собственник выкладывает его в приложении YouTube за минуту.
После одобрения проверки поменяй mode на "api" — дальше всё будет само.

Примеры:
  python tools/youtube.py check                  # проверить доступ и канал
  python tools/youtube.py stats                  # цифры канала и роликов → company/metrics
  python tools/youtube.py trending --region US   # популярные короткие видео
  python tools/youtube.py search "office prank"  # что залетает по теме за неделю (дорого по квоте!)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import COMPANY_DIR, ROOT, all_episodes, die, env, load_config, now_iso, now_utc, save_json  # noqa: E402

API = "https://www.googleapis.com/youtube/v3"
UPLOAD = "https://www.googleapis.com/upload/youtube/v3/videos"
_token_cache: dict = {}


def configured() -> bool:
    return bool(env("YOUTUBE_REFRESH_TOKEN") and env("YOUTUBE_CLIENT_ID") and env("YOUTUBE_CLIENT_SECRET"))


def access_token() -> str:
    if _token_cache.get("token"):
        return _token_cache["token"]
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": env("YOUTUBE_CLIENT_ID", required=True),
        "client_secret": env("YOUTUBE_CLIENT_SECRET", required=True),
        "refresh_token": env("YOUTUBE_REFRESH_TOKEN", required=True),
        "grant_type": "refresh_token",
    }, timeout=30)
    if r.status_code != 200:
        die(f"Google не выдал доступ к YouTube ({r.status_code}): {r.text[:300]}. "
            f"Если ошибка invalid_grant — токен протух: приложение OAuth должно быть в статусе "
            f"«In production», а не «Testing». Получи новый токен по SETUP.md.")
    _token_cache["token"] = r.json()["access_token"]
    return _token_cache["token"]


def _get(path: str, params: dict) -> dict:
    headers = {}
    key = env("YOUTUBE_API_KEY")
    if configured():
        headers["Authorization"] = f"Bearer {access_token()}"
    elif key:
        params = {**params, "key": key}
    else:
        die("YouTube не настроен: нет ни YOUTUBE_REFRESH_TOKEN, ни YOUTUBE_API_KEY")
    r = requests.get(f"{API}/{path}", params=params, headers=headers, timeout=30)
    if r.status_code != 200:
        die(f"YouTube API {path}: {r.status_code} {r.text[:300]}")
    return r.json()


def iso_duration_seconds(value: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", value or "")
    if not m:
        return 0
    d, h, mi, s = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def upload(path: str, title: str, description: str, tags: list[str], privacy: str = "public") -> dict:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        die(f"Нет файла {p}")
    cfg = load_config().get("platforms", {}).get("youtube", {})
    if "#shorts" not in (title + description).lower():
        description = (description or "").rstrip() + "\n\n#Shorts"
    body = {
        "snippet": {
            "title": title[:100],
            "description": description[:5000],
            "tags": [t.lstrip("#") for t in tags][:30],
            "categoryId": str(cfg.get("category_id", "23")),
            "defaultLanguage": "en",
            "defaultAudioLanguage": "en",
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": True,  # честная пометка «создано ИИ» — требование YouTube
        },
    }
    size = p.stat().st_size
    r = requests.post(UPLOAD, params={"uploadType": "resumable", "part": "snippet,status"},
                      headers={"Authorization": f"Bearer {access_token()}",
                               "Content-Type": "application/json; charset=UTF-8",
                               "X-Upload-Content-Type": "video/mp4",
                               "X-Upload-Content-Length": str(size)},
                      data=json.dumps(body), timeout=60)
    if r.status_code not in (200, 201) or "Location" not in r.headers:
        die(f"YouTube не начал загрузку: {r.status_code} {r.text[:300]}")
    with open(p, "rb") as f:
        up = requests.put(r.headers["Location"], data=f,
                          headers={"Authorization": f"Bearer {access_token()}", "Content-Type": "video/mp4",
                                   "Content-Length": str(size)}, timeout=900)
    if up.status_code not in (200, 201):
        die(f"YouTube не принял файл: {up.status_code} {up.text[:300]}")
    video = up.json()
    return {"id": video["id"], "url": f"https://youtube.com/shorts/{video['id']}",
            "privacy": video.get("status", {}).get("privacyStatus")}


def stats() -> dict:
    ch = _get("channels", {"part": "statistics,snippet", "mine": "true"}) if configured() else {"items": []}
    result = {"updated": now_iso()}
    if ch.get("items"):
        s = ch["items"][0]["statistics"]
        result.update({
            "youtube_channel": ch["items"][0]["snippet"]["title"],
            "youtube_subscribers": int(s.get("subscriberCount", 0)),
            "youtube_views_total": int(s.get("viewCount", 0)),
            "youtube_videos": int(s.get("videoCount", 0)),
        })
    if ch.get("items"):
        _link_manual_uploads()
    ids = {}
    for ep in all_episodes():
        yt = (ep.get("publish") or {}).get("youtube") or {}
        if yt.get("id"):
            ids[yt["id"]] = ep["id"]
    per_video = {}
    id_list = list(ids)
    for i in range(0, len(id_list), 50):
        data = _get("videos", {"part": "statistics", "id": ",".join(id_list[i:i + 50])})
        for item in data.get("items", []):
            st = item.get("statistics", {})
            per_video[ids[item["id"]]] = {k: int(st.get(k, 0)) for k in ("viewCount", "likeCount", "commentCount")}
    result["youtube_per_episode"] = per_video
    return result


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def _link_manual_uploads() -> None:
    """Ролики, выложенные собственником вручную, находим на канале по названию и связываем с эпизодами."""
    pending = [ep for ep in all_episodes()
               if ((ep.get("publish") or {}).get("youtube") or {}).get("status") == "manual_pending"]
    if not pending:
        return
    ch = _get("channels", {"part": "contentDetails", "mine": "true"})
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    items = _get("playlistItems", {"part": "snippet", "playlistId": uploads, "maxResults": 50}).get("items", [])
    by_title = {_norm(it["snippet"]["title"]): it["snippet"]["resourceId"]["videoId"] for it in items}
    from common import save_episode  # noqa: WPS433
    for ep in pending:
        title = _norm((ep.get("youtube") or {}).get("title") or ep.get("title"))
        vid = by_title.get(title) or next((v for t, v in by_title.items() if title and title[:40] in t), None)
        if vid:
            ep["publish"]["youtube"] = {"id": vid, "url": f"https://youtube.com/shorts/{vid}",
                                        "status": "published", "at": now_iso(), "manual": True}
            save_episode(ep)


def trending(region: str = "US", limit: int = 25) -> list[dict]:
    data = _get("videos", {"part": "snippet,statistics,contentDetails", "chart": "mostPopular",
                           "regionCode": region, "maxResults": 50})
    out = []
    for it in data.get("items", []):
        dur = iso_duration_seconds(it["contentDetails"].get("duration", ""))
        if dur and dur <= 180:
            out.append({"title": it["snippet"]["title"], "channel": it["snippet"]["channelTitle"],
                        "views": int(it["statistics"].get("viewCount", 0)), "duration_s": dur,
                        "url": f"https://youtube.com/shorts/{it['id']}",
                        "tags": it["snippet"].get("tags", [])[:8]})
    return sorted(out, key=lambda x: -x["views"])[:limit]


def search(query: str, days: int = 7, limit: int = 15) -> list[dict]:
    after = (now_utc() - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    found = _get("search", {"part": "snippet", "q": query, "type": "video", "videoDuration": "short",
                            "order": "viewCount", "publishedAfter": after, "maxResults": limit,
                            "relevanceLanguage": "en"})
    ids = [it["id"]["videoId"] for it in found.get("items", []) if it.get("id", {}).get("videoId")]
    if not ids:
        return []
    data = _get("videos", {"part": "snippet,statistics", "id": ",".join(ids)})
    return [{"title": it["snippet"]["title"], "channel": it["snippet"]["channelTitle"],
             "views": int(it["statistics"].get("viewCount", 0)),
             "likes": int(it["statistics"].get("likeCount", 0)),
             "url": f"https://youtube.com/shorts/{it['id']}"} for it in data.get("items", [])]


def main() -> None:
    parser = argparse.ArgumentParser(description="YouTube")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("stats")
    p = sub.add_parser("trending")
    p.add_argument("--region", default="US")
    p.add_argument("--limit", type=int, default=25)
    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("--days", type=int, default=7)
    args = parser.parse_args()

    if args.cmd == "check":
        if not configured():
            print("YouTube не настроен (нет секретов). Публикация пойдёт в ручном режиме.")
            return
        ch = _get("channels", {"part": "snippet,statistics", "mine": "true"})
        if not ch.get("items"):
            die("Доступ есть, но канала нет. Создай канал YouTube на этом Google-аккаунте.")
        print(f"OK: канал «{ch['items'][0]['snippet']['title']}»")
    elif args.cmd == "stats":
        if not configured() and not env("YOUTUBE_API_KEY"):
            print("YouTube не настроен — пропускаю")
            return
        data = stats()
        path = COMPANY_DIR / "metrics" / "youtube.json"
        save_json(path, data)
        print(json.dumps({k: v for k, v in data.items() if k != "youtube_per_episode"}, ensure_ascii=False))
    elif args.cmd == "trending":
        print(json.dumps(trending(args.region, args.limit), ensure_ascii=False, indent=1))
    elif args.cmd == "search":
        print(json.dumps(search(args.query, args.days), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
