"""Общие функции для всех инструментов компании.

Здесь пути, чтение конфига, работа с JSON, время и секреты.
Секреты берутся из переменных окружения (в GitHub Actions — из Secrets),
а при запуске на своём компьютере — из файла .env в корне репозитория.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"
COMPANY_DIR = ROOT / "company"
EPISODES_DIR = COMPANY_DIR / "episodes"
STATE_DIR = COMPANY_DIR / "state"
MEDIA_DIR = ROOT / "media"  # не попадает в git, только рабочие файлы

MSK = timezone(timedelta(hours=3))

# Windows-консоль по умолчанию не любит кириллицу и эмодзи
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _load_dotenv() -> None:
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for raw in env_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv()


def env(name: str, required: bool = False, default: str | None = None) -> str | None:
    value = os.environ.get(name, default)
    if value is not None:
        value = value.strip()
    if required and not value:
        die(f"Не задан секрет {name}. Добавь его в GitHub → Settings → Secrets and variables → Actions "
            f"(или в файл .env при запуске на своём компьютере). Подробно — в SETUP.md.")
    return value or None


def dry_run() -> bool:
    """Сухой режим: ничего не тратим и никуда не публикуем, только проверяем конвейер."""
    return os.environ.get("DRY_RUN", "").lower() in {"1", "true", "yes"}


def die(message: str, code: int = 1) -> None:
    print(f"ОШИБКА: {message}", file=sys.stderr)
    sys.exit(code)


def load_json(path: Path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return default
    return json.loads(text)


def save_json(path: Path, data) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def load_config() -> dict:
    return load_json(CONFIG_DIR / "company.json", {})


def save_config(cfg: dict) -> None:
    save_json(CONFIG_DIR / "company.json", cfg)


def load_models() -> dict:
    return load_json(CONFIG_DIR / "models.json", {})


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def now_iso() -> str:
    return now_utc().replace(microsecond=0).isoformat()


def today_msk() -> str:
    return datetime.now(MSK).strftime("%Y-%m-%d")


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def approval_required(cfg: dict | None = None) -> bool:
    """Нужно ли одобрение собственника перед публикацией."""
    cfg = cfg or load_config()
    approval = cfg.get("approval", {})
    mode = approval.get("mode", "manual")
    if mode == "manual":
        return True
    if mode == "auto":
        return False
    # manual_until: вручную до даты, потом автопилот
    until = approval.get("manual_until")
    if not until:
        return True
    return today_msk() <= until


def episode_path(episode_id: str) -> Path:
    return EPISODES_DIR / f"{episode_id}.json"


def load_episode(episode_id: str) -> dict:
    data = load_json(episode_path(episode_id))
    if data is None:
        die(f"Эпизод {episode_id} не найден в company/episodes/")
    return data


def save_episode(ep: dict) -> None:
    ep["updated"] = now_iso()
    save_json(episode_path(ep["id"]), ep)


def all_episodes() -> list[dict]:
    if not EPISODES_DIR.exists():
        return []
    items = []
    for f in sorted(EPISODES_DIR.glob("ep-*.json")):
        data = load_json(f)
        if data:
            items.append(data)
    return items


def office(*args: str) -> None:
    """Тихо обновить офис из другого инструмента (ошибки офиса не роняют работу)."""
    subprocess.run([sys.executable, str(ROOT / "tools" / "office.py"), *args], check=False,
                   stdout=subprocess.DEVNULL)


def next_run_iso() -> str:
    """Когда по расписанию следующий рабочий день (время из config → schedule.daily_cycle_msk)."""
    hh, mm = (load_config().get("schedule", {}).get("daily_cycle_msk", "09:17")).split(":")
    now = datetime.now(MSK)
    run = now.replace(hour=int(hh), minute=int(mm), second=0, microsecond=0)
    if run <= now:
        run += timedelta(days=1)
    return run.astimezone(timezone.utc).isoformat()
