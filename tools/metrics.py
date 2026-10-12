"""Сводные цифры компании для Аналитика и офиса.

  python tools/metrics.py update   # собрать YouTube + Instagram → company/metrics/latest.json и history.json
  python tools/metrics.py table    # таблица по эпизодам: просмотры, лайки, комментарии
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import COMPANY_DIR, ROOT, all_episodes, load_json, now_iso, office, save_json, today_msk  # noqa: E402

M = COMPANY_DIR / "metrics"


def _run(script: str, *args: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "tools" / script), *args], check=False)


def update() -> dict:
    _run("youtube.py", "stats")
    _run("instagram.py", "stats")
    yt = load_json(M / "youtube.json", {}) or {}
    ig = load_json(M / "instagram.json", {}) or {}
    per_ep = {}
    for ep in all_episodes():
        if ep.get("status") != "published":
            continue
        y = (yt.get("youtube_per_episode") or {}).get(ep["id"], {})
        i = (ig.get("instagram_per_episode") or {}).get(ep["id"], {})
        per_ep[ep["id"]] = {
            "title": ep.get("title"), "format": ep.get("format"), "hook": ep.get("hook"),
            "published": next((h["t"] for h in ep.get("history", []) if h.get("status") == "published"), None),
            "yt_views": y.get("viewCount"), "yt_likes": y.get("likeCount"), "yt_comments": y.get("commentCount"),
            "ig_views": i.get("views") or i.get("reach"), "ig_likes": i.get("likes"),
            "ig_shares": i.get("shares"), "ig_saved": i.get("saved"),
        }
    views_total = sum((v.get("yt_views") or 0) + (v.get("ig_views") or 0) for v in per_ep.values())
    latest = {
        "updated": now_iso(),
        "youtube_subscribers": yt.get("youtube_subscribers"),
        "instagram_followers": ig.get("instagram_followers"),
        "views_on_our_episodes": views_total,
    }
    latest = {k: v for k, v in latest.items() if v is not None}
    save_json(M / "latest.json", latest)
    save_json(M / "episodes.json", per_ep)
    hist = load_json(M / "history.json", []) or []
    hist = [h for h in hist if h.get("date") != today_msk()]
    hist.append({"date": today_msk(), **{k: v for k, v in latest.items() if k != "updated"}})
    save_json(M / "history.json", hist[-180:])
    office("metrics")
    return latest


def table() -> None:
    per_ep = load_json(M / "episodes.json", {}) or {}
    if not per_ep:
        print("Пока нет опубликованных эпизодов с цифрами")
        return
    print(f"{'эпизод':8} {'YT просм':>9} {'YT лайк':>8} {'IG просм':>9} {'IG лайк':>8}  название")
    for ep_id, v in sorted(per_ep.items()):
        print(f"{ep_id:8} {v.get('yt_views') or '-':>9} {v.get('yt_likes') or '-':>8} "
              f"{v.get('ig_views') or '-':>9} {v.get('ig_likes') or '-':>8}  {v.get('title')}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Метрики")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("update")
    sub.add_parser("table")
    args = parser.parse_args()
    if args.cmd == "update":
        print(json.dumps(update(), ensure_ascii=False))
    else:
        table()


if __name__ == "__main__":
    main()
