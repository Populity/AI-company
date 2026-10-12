"""Проверка настройки: какие ключи заданы и работают ли подключения.

  python tools/doctor.py            # проверить всё
  python tools/doctor.py --telegram # заодно отправить отчёт в Telegram

Значения секретов никогда не печатаются — только «есть / нет / работает».
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT, dry_run, env, load_config  # noqa: E402

CHECKS = [
    ("CLAUDE_CODE_OAUTH_TOKEN", True, "Мозг компании. SETUP.md, шаг 2"),
    ("FAL_KEY", True, "Генерация картинок и видео. SETUP.md, шаг 3"),
    ("TELEGRAM_BOT_TOKEN", True, "Связь с тобой. SETUP.md, шаг 4"),
    ("TELEGRAM_OWNER_ID", True, "Твой ID в Telegram. SETUP.md, шаг 4"),
    ("YOUTUBE_CLIENT_ID", False, "YouTube: статистика и автозагрузка. SETUP.md, шаг 5"),
    ("YOUTUBE_CLIENT_SECRET", False, "YouTube. SETUP.md, шаг 5"),
    ("YOUTUBE_REFRESH_TOKEN", False, "YouTube. SETUP.md, шаг 5"),
    ("INSTAGRAM_ACCESS_TOKEN", False, "Instagram: публикация Reels. SETUP.md, шаг 6"),
    ("GH_PAT", False, "Автопродление токена Instagram. SETUP.md, шаг 7 (необязательно)"),
]


def _run(*args: str) -> tuple[bool, str]:
    res = subprocess.run([sys.executable, str(ROOT / "tools" / args[0]), *args[1:]],
                         capture_output=True, text=True)
    out = (res.stdout + res.stderr).strip().splitlines()
    return res.returncode == 0, (out[-1] if out else "")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--telegram", action="store_true")
    args = parser.parse_args()

    lines = ["🩺 Проверка настройки компании", ""]
    missing_required = []
    for name, required, hint in CHECKS:
        if env(name):
            lines.append(f"✅ {name}")
        else:
            mark = "❌" if required else "⚪"
            lines.append(f"{mark} {name} — нет. {hint}")
            if required and not (dry_run() and name == "FAL_KEY"):
                missing_required.append(name)

    lines.append("")
    lines.append(f"{'✅' if shutil.which('ffmpeg') else '❌'} ffmpeg (монтаж)")
    if env("TELEGRAM_BOT_TOKEN"):
        ok, msg = _run("telegram_bot.py", "whoami")
        lines.append(f"{'✅' if ok else '❌'} Telegram-бот: {'отвечает' if ok else msg}")
    if env("YOUTUBE_REFRESH_TOKEN"):
        ok, msg = _run("youtube.py", "check")
        lines.append(f"{'✅' if ok else '❌'} YouTube: {msg}")
    if env("INSTAGRAM_ACCESS_TOKEN"):
        ok, msg = _run("instagram.py", "check")
        lines.append(f"{'✅' if ok else '❌'} Instagram: {msg}")

    cfg = load_config()
    yt_mode = cfg.get("platforms", {}).get("youtube", {}).get("mode")
    lines += ["", f"Режим YouTube: {'автозагрузка' if yt_mode == 'api' else 'ручной (бот присылает ролик, выкладываешь ты)'}",
              f"Бюджет: {cfg.get('budget', {}).get('monthly_rub')} ₽ ≈ ${cfg.get('budget', {}).get('monthly_usd')} в месяц",
              f"Ниша: {cfg.get('niche') or 'ещё не выбрана — директор выберет в первый рабочий день'}"]
    if missing_required:
        lines += ["", "Без обязательных ключей (❌) компания работать не сможет."]
    else:
        lines += ["", "Обязательное всё на месте. Можно запускать рабочий день."]

    report = "\n".join(lines)
    print(report)
    if args.telegram and env("TELEGRAM_BOT_TOKEN") and env("TELEGRAM_OWNER_ID"):
        import telegram_bot  # noqa: WPS433
        try:
            telegram_bot.api("sendMessage", {"chat_id": env("TELEGRAM_OWNER_ID"), "text": report})
        except Exception as exc:
            print(f"(не отправилось в Telegram: {exc})")
    sys.exit(1 if missing_required else 0)


if __name__ == "__main__":
    main()
