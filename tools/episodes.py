"""Учёт эпизодов (роликов). Каждый эпизод — файл company/episodes/ep-XXXX.json.

Статусы по порядку:
  idea → scripted → producing → review → awaiting_approval → approved → published
  плюс rejected (собственник вернул на доработку) и failed (брак, не удалось сделать).

Примеры:
  python tools/episodes.py new --title "The Coffee Machine Betrayal"
  python tools/episodes.py stage ep-0003 scripted
  python tools/episodes.py set ep-0003 youtube.title "He trusted the coffee machine"
  python tools/episodes.py set ep-0003 hashtags '["#shorts", "#comedy"]'
  python tools/episodes.py list --status rejected
  python tools/episodes.py show ep-0003
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (EPISODES_DIR, all_episodes, die, load_episode, now_iso,  # noqa: E402
                    save_episode)
from common import office as _office  # noqa: E402

STATUSES = ["idea", "scripted", "producing", "review", "awaiting_approval",
            "approved", "published", "rejected", "failed"]
LABELS = {
    "idea": "идея", "scripted": "сценарий готов", "producing": "в производстве", "review": "проверка качества",
    "awaiting_approval": "ждёт одобрения собственника", "approved": "одобрен", "published": "опубликован",
    "rejected": "возвращён на доработку", "failed": "брак",
}

TEMPLATE = {
    "series": None,
    "status": "idea",
    "title": None,
    "logline": None,
    "hook": None,
    "format": None,
    "trend_refs": [],
    "script": {"scenes": []},
    "youtube": {"title": None, "description": None, "tags": []},
    "instagram": {"caption": None},
    "hashtags": [],
    "assets": {"keyframes": [], "clips": [], "final_path": None, "final_url": None, "duration_s": None},
    "cost_usd": 0.0,
    "qc": {"passed": None, "notes": None},
    "approval": {"required": None, "requested_at": None, "decision": None, "comment": None, "decided_at": None},
    "publish": {},
    "history": [],
}


def next_id() -> str:
    nums = [int(p.stem.split("-")[1]) for p in EPISODES_DIR.glob("ep-*.json") if p.stem.split("-")[1].isdigit()]
    return f"ep-{(max(nums) + 1 if nums else 1):04d}"


def new(title: str, series: str | None = None) -> dict:
    EPISODES_DIR.mkdir(parents=True, exist_ok=True)
    ep = json.loads(json.dumps(TEMPLATE))
    ep.update({"id": next_id(), "created": now_iso(), "title": title, "series": series})
    ep["history"].append({"t": now_iso(), "status": "idea"})
    save_episode(ep)
    _office("pipeline")
    return ep


def stage(ep_id: str, status: str, note: str | None = None) -> dict:
    if status not in STATUSES:
        die(f"Неизвестный статус {status}. Можно: {', '.join(STATUSES)}")
    ep = load_episode(ep_id)
    ep["status"] = status
    ep.setdefault("history", []).append({"t": now_iso(), "status": status, "note": note})
    save_episode(ep)
    _office("pipeline")
    return ep


def set_value(ep_id: str, path: str, raw: str) -> dict:
    ep = load_episode(ep_id)
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        value = raw
    node = ep
    keys = path.split(".")
    for key in keys[:-1]:
        node = node.setdefault(key, {})
    node[keys[-1]] = value
    save_episode(ep)
    return ep


def main() -> None:
    parser = argparse.ArgumentParser(description="Учёт эпизодов")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new")
    p.add_argument("--title", required=True)
    p.add_argument("--series")
    p = sub.add_parser("stage")
    p.add_argument("id")
    p.add_argument("status", choices=STATUSES)
    p.add_argument("--note")
    p = sub.add_parser("set")
    p.add_argument("id")
    p.add_argument("path", help="поле через точку, например youtube.title")
    p.add_argument("value", help="строка или JSON")
    p = sub.add_parser("list")
    p.add_argument("--status", choices=STATUSES)
    p = sub.add_parser("show")
    p.add_argument("id")
    args = parser.parse_args()

    if args.cmd == "new":
        ep = new(args.title, args.series)
        print(ep["id"])
    elif args.cmd == "stage":
        ep = stage(args.id, args.status, args.note)
        print(f"{ep['id']}: {LABELS[ep['status']]}")
    elif args.cmd == "set":
        set_value(args.id, args.path, args.value)
        print("Сохранено")
    elif args.cmd == "list":
        for ep in all_episodes():
            if args.status and ep.get("status") != args.status:
                continue
            print(f"{ep['id']}  [{LABELS.get(ep.get('status'), ep.get('status'))}]  {ep.get('title')}")
    elif args.cmd == "show":
        print(json.dumps(load_episode(args.id), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
