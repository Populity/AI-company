"""Офис в прямом эфире.

Каждый агент сообщает сюда, чем занят. Состояние офиса — один файл office.json,
который отправляется в отдельную ветку `office-live` репозитория. Страница офиса
(docs/index.html на GitHub Pages) читает эту ветку и рисует, кто что делает.

Примеры:
  python tools/office.py cycle start
  python tools/office.py agent producer working "Генерирую клип 1 из 2 для ep-0004"
  python tools/office.py agent producer done "Ролик ep-0004 собран, 10 с"
  python tools/office.py event director "Решил: сегодня серия про кофе-машину"
  python tools/office.py pipeline        # пересобрать конвейер из эпизодов
  python tools/office.py metrics         # обновить цифры из company/metrics и бюджета
  python tools/office.py cycle end
  python tools/office.py show            # показать текущее состояние

Переменная OFFICE_PUSH=0 отключает отправку в GitHub (для тестов на своём компьютере).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (COMPANY_DIR, ROOT, all_episodes, load_config, load_json,  # noqa: E402
                    next_run_iso, now_iso, now_utc, parse_iso, save_json)

BRANCH = "office-live"
LOCAL = ROOT / ".office" / "office.json"
FEED_LIMIT = 80

AGENTS = {
    "director":    {"name": "Директор",        "role": "Управляет компанией, принимает решения"},
    "trend-scout": {"name": "Трендвотчер",     "role": "Ищет тренды, форматы и звуки"},
    "showrunner":  {"name": "Шоураннер",       "role": "Придумывает серии и пишет сценарии"},
    "producer":    {"name": "Продакшн",        "role": "Генерирует и монтирует видео"},
    "publisher":   {"name": "SMM",             "role": "Готовит публикации и выкладывает"},
    "analyst":     {"name": "Аналитик",        "role": "Считает просмотры и находит, что работает"},
    "cfo":         {"name": "Финансы",         "role": "Следит за бюджетом и доходами"},
    "bizdev":      {"name": "Монетизация",     "role": "Ищет рекламу, партнёрки и продукты"},
}
STATES = {"idle", "working", "waiting", "done", "error", "offline"}
STAGES = ["idea", "script", "production", "review", "approval", "approved", "published", "rejected", "failed"]
STATUS_TO_STAGE = {
    "idea": "idea", "scripted": "script", "producing": "production", "review": "review",
    "awaiting_approval": "approval", "approved": "approved", "published": "published",
    "rejected": "rejected", "failed": "failed",
}


def _git(*args: str, check: bool = True, capture: bool = True) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, check=check,
                            capture_output=capture, text=True)
    return (result.stdout or "").strip()


def _push_enabled() -> bool:
    return os.environ.get("OFFICE_PUSH", "1") not in {"0", "false", "no"}


def _blank_state() -> dict:
    cfg = load_config()
    return {
        "version": 1,
        "company": {
            "name": cfg.get("company_name", "AI Company"),
            "owner": cfg.get("owner_name", "Собственник"),
            "niche": cfg.get("niche"),
            "founded": cfg.get("founded"),
        },
        "updated_at": now_iso(),
        "cycle": {"status": "idle", "started_at": None, "finished_at": None,
                  "next_run": None, "run_url": None},
        "agents": {k: {**v, "state": "idle", "task": "Ждёт начала рабочего дня", "since": now_iso()}
                   for k, v in AGENTS.items()},
        "pipeline": [],
        "metrics": {},
        "feed": [],
    }


def _fetch_remote() -> dict | None:
    if not _push_enabled():
        return None
    try:
        _git("fetch", "--quiet", "origin", f"+refs/heads/{BRANCH}:refs/remotes/origin/{BRANCH}")
        raw = _git("show", f"origin/{BRANCH}:office.json")
        return json.loads(raw)
    except Exception:
        return None


def load_state() -> dict:
    state = load_json(LOCAL)
    # локальная копия годится только в пределах одного рабочего дня
    if state is not None:
        updated = parse_iso(state.get("updated_at"))
        if updated is None or now_utc() - updated > timedelta(hours=2):
            state = None
    if state is None:
        state = _fetch_remote() or _blank_state()
    # добавить агентов, которых не было в старом состоянии
    for key, meta in AGENTS.items():
        state["agents"].setdefault(key, {**meta, "state": "idle", "task": "", "since": now_iso()})
        state["agents"][key].update({k: v for k, v in meta.items()})
    cfg = load_config()
    state["company"].update({"name": cfg.get("company_name", state["company"].get("name")),
                             "niche": cfg.get("niche"), "founded": cfg.get("founded")})
    return state


def publish(state: dict) -> None:
    state["updated_at"] = now_iso()
    save_json(LOCAL, state)
    if not _push_enabled():
        return
    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "office.json"
            path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
            blob = _git("hash-object", "-w", str(path))
            tree = subprocess.run(["git", "mktree"], cwd=ROOT, input=f"100644 blob {blob}\toffice.json\n",
                                  capture_output=True, text=True, check=True).stdout.strip()
            env = {**os.environ,
                   "GIT_AUTHOR_NAME": "AI Office", "GIT_AUTHOR_EMAIL": "office@users.noreply.github.com",
                   "GIT_COMMITTER_NAME": "AI Office", "GIT_COMMITTER_EMAIL": "office@users.noreply.github.com"}
            commit = subprocess.run(["git", "commit-tree", tree, "-m", "office update"], cwd=ROOT,
                                    capture_output=True, text=True, check=True, env=env).stdout.strip()
            subprocess.run(["git", "push", "--quiet", "--force", "origin", f"{commit}:refs/heads/{BRANCH}"],
                           cwd=ROOT, check=True, capture_output=True, text=True, timeout=60)
    except Exception as exc:  # офис не должен ронять рабочий процесс
        print(f"(офис не обновился в GitHub: {exc})", file=sys.stderr)


def add_event(state: dict, agent: str, text: str, kind: str = "info") -> None:
    state["feed"].insert(0, {"t": now_iso(), "agent": agent, "text": text[:280], "kind": kind})
    del state["feed"][FEED_LIMIT:]


def rebuild_pipeline(state: dict) -> None:
    items = []
    for ep in all_episodes()[-30:]:
        items.append({
            "id": ep["id"],
            "title": ep.get("title") or ep["id"],
            "stage": STATUS_TO_STAGE.get(ep.get("status", "idea"), "idea"),
            "updated": ep.get("updated") or ep.get("created"),
            "links": {k: v.get("url") for k, v in (ep.get("publish") or {}).items()
                      if isinstance(v, dict) and v.get("url")},
        })
    state["pipeline"] = items


def rebuild_metrics(state: dict) -> None:
    latest = load_json(COMPANY_DIR / "metrics" / "latest.json", {}) or {}
    ledger = load_json(COMPANY_DIR / "ledger.json", {"entries": []}) or {"entries": []}
    cfg = load_config()
    month = now_utc().strftime("%Y-%m")
    spent = sum(e.get("cost_usd", 0) for e in ledger.get("entries", []) if str(e.get("date", "")).startswith(month))
    revenue = load_json(COMPANY_DIR / "revenue.json", {"entries": []}) or {"entries": []}
    earned = sum(e.get("amount_usd", 0) for e in revenue.get("entries", []))
    published = sum(1 for ep in all_episodes() if ep.get("status") == "published")
    state["metrics"] = {
        **{k: v for k, v in latest.items() if isinstance(v, (int, float, str))},
        "episodes_published": published,
        "budget_spent_usd": round(spent, 2),
        "budget_limit_usd": cfg.get("budget", {}).get("monthly_usd"),
        "revenue_total_usd": round(earned, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Офис в прямом эфире")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("agent", help="обновить статус агента")
    p.add_argument("key", choices=sorted(AGENTS))
    p.add_argument("state", choices=sorted(STATES))
    p.add_argument("task", nargs="?", default="")
    p.add_argument("--quiet", action="store_true", help="не писать в ленту")

    p = sub.add_parser("event", help="запись в ленту событий")
    p.add_argument("agent", choices=sorted(AGENTS) + ["owner", "system"])
    p.add_argument("text")
    p.add_argument("--kind", default="info", choices=["info", "success", "warning", "error", "money"])

    p = sub.add_parser("cycle", help="начало/конец рабочего дня")
    p.add_argument("action", choices=["start", "end", "fail"])
    p.add_argument("--next-run", default=None, help="ISO-время следующего запуска")

    sub.add_parser("pipeline", help="пересобрать конвейер из эпизодов")
    sub.add_parser("metrics", help="обновить цифры")
    sub.add_parser("show", help="показать состояние")
    sub.add_parser("reset", help="начать офис с чистого листа")

    args = parser.parse_args()

    if args.cmd == "reset":
        state = _blank_state()
        rebuild_pipeline(state)
        rebuild_metrics(state)
        add_event(state, "system", "Офис открыт")
        publish(state)
        print("Офис сброшен")
        return

    state = load_state()

    if args.cmd == "agent":
        a = state["agents"][args.key]
        a.update({"state": args.state, "task": args.task, "since": now_iso()})
        if not args.quiet and args.task:
            kind = {"done": "success", "error": "error", "waiting": "warning"}.get(args.state, "info")
            add_event(state, args.key, args.task, kind)
    elif args.cmd == "event":
        add_event(state, args.agent, args.text, args.kind)
    elif args.cmd == "cycle":
        cyc = state["cycle"]
        run_url = None
        if os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_REPOSITORY"):
            run_url = (f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/"
                       f"{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}")
        if args.action == "start":
            cyc.update({"status": "working", "started_at": now_iso(), "finished_at": None, "run_url": run_url})
            for a in state["agents"].values():
                a.update({"state": "idle", "task": "На месте, ждёт задач", "since": now_iso()})
            state["agents"]["director"].update({"state": "working", "task": "Читает отчёты и почту собственника"})
            add_event(state, "director", "Рабочий день начался", "success")
        else:
            cyc.update({"status": "idle", "finished_at": now_iso()})
            nxt = args.next_run or next_run_iso()
            cyc["next_run"] = nxt
            for a in state["agents"].values():
                if a["state"] in {"working", "waiting"}:
                    a.update({"state": "idle", "since": now_iso()})
                if args.action == "end":
                    a["task"] = "Рабочий день окончен"
            if args.action == "end":
                add_event(state, "director", "Рабочий день окончен", "success")
            else:
                state["agents"]["director"].update({"state": "error", "task": "Рабочий день прервался с ошибкой"})
                add_event(state, "system", "Рабочий день прервался с ошибкой — собственнику отправлено сообщение", "error")
        rebuild_pipeline(state)
        rebuild_metrics(state)
    elif args.cmd == "pipeline":
        rebuild_pipeline(state)
    elif args.cmd == "metrics":
        rebuild_metrics(state)
    elif args.cmd == "show":
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return

    publish(state)
    print("Офис обновлён")


if __name__ == "__main__":
    main()
