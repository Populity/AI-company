"""Сбор сырых трендов для Трендвотчера.

Источники: Google Trends (ежедневные поисковые тренды) и популярные короткие видео YouTube.
Остальное (TikTok, Reels, Reddit, новости) Трендвотчер ищет сам через веб-поиск.

  python tools/trends.py collect --geo US
  → company/trends/raw-YYYY-MM-DD.json
"""
from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import COMPANY_DIR, env, now_iso, save_json, today_msk  # noqa: E402

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ai-company-trends/1.0)"}


def google_trends(geo: str = "US") -> list[dict]:
    try:
        r = requests.get("https://trends.google.com/trending/rss", params={"geo": geo},
                         headers=HEADERS, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.content)
    except Exception as exc:
        return [{"error": f"Google Trends недоступен: {exc}"}]
    ns = {"ht": "https://trends.google.com/trending/rss"}
    items = []
    for item in root.iter("item"):
        news = [n.findtext("ht:news_item_title", default="", namespaces=ns)
                for n in item.findall("ht:news_item", ns)][:2]
        items.append({
            "query": item.findtext("title", default=""),
            "traffic": item.findtext("ht:approx_traffic", default="", namespaces=ns),
            "news": [n for n in news if n],
        })
    return items[:25]


def youtube_shorts(geo: str = "US") -> list[dict]:
    if not (env("YOUTUBE_REFRESH_TOKEN") or env("YOUTUBE_API_KEY")):
        return [{"note": "YouTube не настроен — пропущено"}]
    try:
        import youtube  # noqa: WPS433
        return youtube.trending(geo, 20)
    except SystemExit:
        return [{"error": "YouTube API вернул ошибку"}]


def main() -> None:
    parser = argparse.ArgumentParser(description="Сбор трендов")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("collect")
    p.add_argument("--geo", default="US")
    args = parser.parse_args()
    data = {"collected_at": now_iso(), "geo": args.geo,
            "google_trends": google_trends(args.geo), "youtube_popular_shorts": youtube_shorts(args.geo)}
    out = COMPANY_DIR / "trends" / f"raw-{today_msk()}.json"
    save_json(out, data)
    print(f"Сохранено: {out.relative_to(COMPANY_DIR.parent)}")
    print(json.dumps({"google_trends": [t.get("query") for t in data["google_trends"]][:15],
                      "youtube_popular_shorts": [v.get("title") for v in data["youtube_popular_shorts"]][:10]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
