"""Генерация картинок и видео через fal.ai (один ключ FAL_KEY на все модели).

Каждый вызов: оценивает цену → спрашивает у бюджета → генерирует → скачивает
результат → записывает расход. Модели и цены — в config/models.json.

Примеры:
  # эталонный портрет персонажа (день основания)
  python tools/fal_gen.py image --prompt "..." --out media/character/ref_front.png

  # кадр сцены с персонажем по эталону
  python tools/fal_gen.py edit --ref company/character/ref_front.png --prompt "..." \
      --out media/ep-0003/key1.png --episode ep-0003

  # оживить кадр в видео со звуком и репликой
  python tools/fal_gen.py video --image media/ep-0003/key1.png --duration 8 \
      --prompt 'He looks at the camera and says: "Monday again?"' \
      --out media/ep-0003/clip1.mp4 --episode ep-0003

  # выложить файл в публичное хранилище fal (нужно Instagram)
  python tools/fal_gen.py upload media/ep-0003/final.mp4

  python tools/fal_gen.py price video --duration 8   # сколько будет стоить

DRY_RUN=1 — ничего не тратит, делает заглушки (для проверки конвейера).
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import budget  # noqa: E402
from common import ROOT, die, dry_run, env, load_models  # noqa: E402


def _model(kind: str) -> dict:
    models = load_models()
    if kind not in models:
        die(f"В config/models.json нет модели '{kind}'")
    return models[kind]


def estimate(kind: str, duration: float | None = None) -> float:
    m = _model(kind)
    if "price_usd_per_second" in m:
        return round(m["price_usd_per_second"] * float(duration or m.get("default_duration", 5)), 4)
    return float(m.get("price_usd", 0))


def _is_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def upload(path: str) -> str:
    if _is_url(path):
        return path
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        die(f"Файл не найден: {p}")
    if dry_run():
        return f"https://example.invalid/dry-run/{p.name}"
    env("FAL_KEY", required=True)
    import fal_client  # noqa: WPS433
    for attempt in range(3):
        try:
            return fal_client.upload_file(str(p))
        except Exception as exc:  # сеть иногда моргает
            if attempt == 2:
                die(f"Не удалось загрузить {p.name} в fal: {exc}")
            time.sleep(3 * (attempt + 1))
    raise RuntimeError("unreachable")


def _download(url: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(out, "wb") as f:
            for chunk in r.iter_content(1 << 16):
                f.write(chunk)


def _call(endpoint: str, arguments: dict) -> dict:
    env("FAL_KEY", required=True)
    import fal_client  # noqa: WPS433
    last_exc = None
    for attempt in range(2):
        try:
            return fal_client.subscribe(endpoint, arguments=arguments, with_logs=False)
        except Exception as exc:
            last_exc = exc
            time.sleep(5)
    die(f"fal.ai вернул ошибку на {endpoint}: {last_exc}")
    raise RuntimeError("unreachable")


def _placeholder(out: Path, kind: str, duration: float = 5) -> None:
    """Заглушка для сухого режима: цветной кадр/видео без затрат."""
    out.parent.mkdir(parents=True, exist_ok=True)
    if not shutil.which("ffmpeg"):
        out.write_bytes(b"")
        return
    if kind == "image":
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=0x2f6f9f:s=720x1280",
               "-frames:v", "1", str(out)]
    else:
        cmd = ["ffmpeg", "-y", "-loglevel", "error",
               "-f", "lavfi", "-i", f"testsrc2=s=720x1280:d={duration}:r=24",
               "-f", "lavfi", "-i", f"sine=frequency=330:duration={duration}",
               "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(out)]
    subprocess.run(cmd, check=True)


def _guard(cost: float, use_reserve: bool) -> None:
    ok, msg = budget.can_spend(cost, use_reserve)
    if not ok:
        die(msg, code=2)


def _out_path(value: str) -> Path:
    p = Path(value)
    return p if p.is_absolute() else ROOT / p


def cmd_image(args) -> dict:
    kind = "image_t2i"
    cost = estimate(kind)
    _guard(cost, args.use_reserve)
    out = _out_path(args.out)
    m = _model(kind)
    if dry_run():
        _placeholder(out, "image")
        url = f"https://example.invalid/dry-run/{out.name}"
    else:
        res = _call(m["endpoint"], {**m.get("params", {}), "prompt": args.prompt,
                                    "aspect_ratio": args.aspect, "num_images": 1})
        url = res["images"][0]["url"]
        _download(url, out)
    budget.record(args.label or f"картинка {out.name}", cost, args.episode, m["endpoint"], dry=dry_run())
    return {"url": url, "path": str(out.relative_to(ROOT)), "cost_usd": cost}


def cmd_edit(args) -> dict:
    kind = "image_edit"
    cost = estimate(kind)
    _guard(cost, args.use_reserve)
    out = _out_path(args.out)
    m = _model(kind)
    refs = [upload(r) for r in args.ref]
    if dry_run():
        _placeholder(out, "image")
        url = f"https://example.invalid/dry-run/{out.name}"
    else:
        res = _call(m["endpoint"], {**m.get("params", {}), "prompt": args.prompt, "image_urls": refs,
                                    "aspect_ratio": args.aspect, "num_images": 1})
        url = res["images"][0]["url"]
        _download(url, out)
    budget.record(args.label or f"кадр {out.name}", cost, args.episode, m["endpoint"], dry=dry_run())
    return {"url": url, "path": str(out.relative_to(ROOT)), "cost_usd": cost}


def cmd_video(args) -> dict:
    kind = "video_i2v"
    m = _model(kind)
    allowed = m.get("durations") or []
    duration = int(args.duration)
    if allowed and duration not in allowed:
        die(f"Длительность {duration} с не поддерживается моделью. Можно: {allowed}")
    cost = estimate(kind, duration)
    _guard(cost, args.use_reserve)
    out = _out_path(args.out)
    image_url = upload(args.image)
    if dry_run():
        _placeholder(out, "video", duration)
        url = f"https://example.invalid/dry-run/{out.name}"
    else:
        payload = {**m.get("params", {}), "prompt": args.prompt, "image_url": image_url,
                   "duration": str(duration)}
        if args.end_image:
            payload["end_image_url"] = upload(args.end_image)
        res = _call(m["endpoint"], payload)
        url = res["video"]["url"]
        _download(url, out)
    budget.record(args.label or f"клип {out.name} ({duration} с)", cost, args.episode, m["endpoint"],
                  dry=dry_run())
    return {"url": url, "path": str(out.relative_to(ROOT)), "cost_usd": cost, "duration": duration}


def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация через fal.ai")
    sub = parser.add_subparsers(dest="cmd", required=True)

    def common_args(p):
        p.add_argument("--out", required=True, help="куда сохранить файл")
        p.add_argument("--episode", help="id эпизода для учёта расходов")
        p.add_argument("--label", help="подпись в бухгалтерии")
        p.add_argument("--use-reserve", action="store_true", help="разрешить трату из резерва (решение Финансов)")

    p = sub.add_parser("image", help="картинка по тексту")
    p.add_argument("--prompt", required=True)
    p.add_argument("--aspect", default="9:16")
    common_args(p)

    p = sub.add_parser("edit", help="картинка по эталону(ам) + тексту")
    p.add_argument("--prompt", required=True)
    p.add_argument("--ref", action="append", required=True, help="эталон: путь или URL (можно несколько)")
    p.add_argument("--aspect", default="9:16")
    common_args(p)

    p = sub.add_parser("video", help="видео со звуком из кадра")
    p.add_argument("--image", required=True, help="стартовый кадр: путь или URL")
    p.add_argument("--end-image", help="финальный кадр (необязательно)")
    p.add_argument("--prompt", required=True, help="движение, действие и реплика в кавычках")
    p.add_argument("--duration", type=int, default=8)
    common_args(p)

    p = sub.add_parser("upload", help="выложить файл и получить публичную ссылку")
    p.add_argument("path")

    p = sub.add_parser("price", help="оценить цену")
    p.add_argument("kind", choices=["image", "edit", "video"])
    p.add_argument("--duration", type=float, default=None)

    args = parser.parse_args()
    if args.cmd == "image":
        result = cmd_image(args)
    elif args.cmd == "edit":
        result = cmd_edit(args)
    elif args.cmd == "video":
        result = cmd_video(args)
    elif args.cmd == "upload":
        result = {"url": upload(args.path)}
    else:
        kind = {"image": "image_t2i", "edit": "image_edit", "video": "video_i2v"}[args.kind]
        result = {"kind": kind, "estimated_usd": estimate(kind, args.duration)}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
