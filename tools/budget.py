"""Бюджет компании: сколько потрачено, сколько можно тратить сегодня.

Все платные генерации проходят через этот модуль: перед запуском fal_gen.py
проверяет, хватает ли денег, а после — записывает расход в company/ledger.json.

Примеры:
  python tools/budget.py status                      # сводка за месяц
  python tools/budget.py check 0.65                  # можно ли потратить $0.65 (код выхода 0 = да)
  python tools/budget.py record --item "клип 1" --cost 0.52 --episode ep-0003 --model seedance
  python tools/budget.py revenue --amount 12.5 --source affiliate --note "Amazon, сентябрь"
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import COMPANY_DIR, load_config, load_json, now_iso, now_utc, save_json  # noqa: E402

LEDGER = COMPANY_DIR / "ledger.json"
REVENUE = COMPANY_DIR / "revenue.json"


def _ledger() -> dict:
    return load_json(LEDGER, {"entries": []}) or {"entries": []}


def month_key() -> str:
    return now_utc().strftime("%Y-%m")


def month_spent(month: str | None = None) -> float:
    month = month or month_key()
    return round(sum(e.get("cost_usd", 0.0) for e in _ledger()["entries"]
                     if str(e.get("date", "")).startswith(month)), 4)


def today_spent() -> float:
    day = now_utc().strftime("%Y-%m-%d")
    return round(sum(e.get("cost_usd", 0.0) for e in _ledger()["entries"]
                     if str(e.get("date", "")).startswith(day)), 4)


def status() -> dict:
    cfg = load_config().get("budget", {})
    monthly = float(cfg.get("monthly_usd", 0))
    reserve_share = float(cfg.get("reserve_share", 0.1))
    spent = month_spent()
    now = now_utc()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    days_left = days_in_month - now.day + 1  # включая сегодня
    operating = monthly * (1 - reserve_share)
    spent_before_today = spent - today_spent()
    daily_allowance = max(0.0, (operating - spent_before_today) / days_left)
    return {
        "month": month_key(),
        "monthly_limit_usd": round(monthly, 2),
        "monthly_limit_rub": cfg.get("monthly_rub"),
        "reserve_usd": round(monthly * reserve_share, 2),
        "spent_usd": round(spent, 2),
        "spent_today_usd": round(today_spent(), 2),
        "remaining_usd": round(monthly - spent, 2),
        "days_left": days_left,
        "daily_allowance_usd": round(daily_allowance, 2),
        "today_remaining_usd": round(max(0.0, daily_allowance - today_spent()), 2),
    }


def can_spend(amount: float, use_reserve: bool = False) -> tuple[bool, str]:
    s = status()
    if amount > s["remaining_usd"]:
        return False, f"Не хватает месячного бюджета: нужно ${amount:.2f}, осталось ${s['remaining_usd']:.2f}"
    if not use_reserve and amount > s["today_remaining_usd"] + 0.01:
        return False, (f"Превышен дневной лимит: нужно ${amount:.2f}, сегодня можно ещё "
                       f"${s['today_remaining_usd']:.2f}. Финансы могут разрешить резерв (--use-reserve).")
    return True, "ok"


def record(item: str, cost: float, episode: str | None = None, model: str | None = None,
           dry: bool = False) -> None:
    ledger = _ledger()
    ledger["entries"].append({
        "date": now_iso(), "item": item, "cost_usd": round(cost, 4),
        "episode": episode, "model": model, "dry_run": dry or None,
    })
    if dry:
        ledger["entries"][-1]["cost_usd"] = 0.0
    save_json(LEDGER, ledger)


def main() -> None:
    parser = argparse.ArgumentParser(description="Бюджет компании")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    p = sub.add_parser("check")
    p.add_argument("amount", type=float)
    p.add_argument("--use-reserve", action="store_true")
    p = sub.add_parser("record")
    p.add_argument("--item", required=True)
    p.add_argument("--cost", type=float, required=True)
    p.add_argument("--episode")
    p.add_argument("--model")
    p = sub.add_parser("revenue", help="записать доход (сообщил собственник)")
    p.add_argument("--amount", type=float, required=True, help="в долларах")
    p.add_argument("--source", required=True,
                   choices=["platform", "brand", "affiliate", "product", "other"])
    p.add_argument("--note", default="")
    args = parser.parse_args()

    if args.cmd == "status":
        print(json.dumps(status(), ensure_ascii=False, indent=2))
    elif args.cmd == "check":
        ok, msg = can_spend(args.amount, args.use_reserve)
        print("Можно" if ok else msg)
        sys.exit(0 if ok else 2)
    elif args.cmd == "record":
        record(args.item, args.cost, args.episode, args.model)
        print("Записано")
    elif args.cmd == "revenue":
        rev = load_json(REVENUE, {"entries": []}) or {"entries": []}
        rev["entries"].append({"date": now_iso(), "amount_usd": args.amount,
                               "source": args.source, "note": args.note})
        save_json(REVENUE, rev)
        print("Доход записан")


if __name__ == "__main__":
    main()
