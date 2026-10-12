"""Монтаж эпизода: склейка клипов, субтитры, громкость, кадры для проверки качества.

Берёт клипы из эпизода (assets.clips) и реплики из сценария (script.scenes[].dialogue),
собирает вертикальный ролик media/<id>/final.mp4 и лист кадров media/<id>/qc/sheet.jpg,
чтобы Продакшн мог глазами проверить брак (лишние пальцы, «поплывшее» лицо, обрывы).

Примеры:
  python tools/assemble.py ep-0003
  python tools/assemble.py ep-0003 --no-captions
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import MEDIA_DIR, ROOT, die, load_episode, save_episode  # noqa: E402

W, H, FPS = 720, 1280, 30


def _run(cmd: list[str], cwd: Path | None = None) -> str:
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        die(f"ffmpeg: {res.stderr.strip()[-800:]}")
    return res.stdout


def probe(path: Path) -> dict:
    out = _run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type",
                "-of", "json", str(path)])
    data = json.loads(out)
    return {
        "duration": float(data.get("format", {}).get("duration", 0) or 0),
        "has_audio": any(s.get("codec_type") == "audio" for s in data.get("streams", [])),
    }


def _ass_time(t: float) -> str:
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def _chunks(text: str, size: int = 4) -> list[str]:
    words = text.replace("\n", " ").split()
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]


def write_ass(path: Path, segments: list[tuple[float, float, str]]) -> None:
    """Динамические субтитры: реплика бьётся на куски по 4 слова и показывается по очереди."""
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Main,DejaVu Sans,54,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,2,2,60,60,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for start, end, text in segments:
        parts = _chunks(text)
        if not parts:
            continue
        span = (end - start) / len(parts)
        for i, part in enumerate(parts):
            s, e = start + i * span, start + (i + 1) * span
            safe = part.replace("{", "(").replace("}", ")")
            lines.append(f"Dialogue: 0,{_ass_time(s)},{_ass_time(e)},Main,,0,0,0,,{safe}")
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def assemble(ep_id: str, captions: bool = True) -> dict:
    if not shutil.which("ffmpeg"):
        die("Не найден ffmpeg. На GitHub он ставится автоматически; на Windows — см. SETUP.md")
    ep = load_episode(ep_id)
    clips = [ROOT / c for c in (ep.get("assets", {}).get("clips") or [])]
    if not clips:
        die(f"У {ep_id} нет клипов в assets.clips")
    for c in clips:
        if not c.exists():
            die(f"Клип не найден: {c}")
    scenes = (ep.get("script") or {}).get("scenes") or []

    work = MEDIA_DIR / ep_id
    work.mkdir(parents=True, exist_ok=True)

    # 1) привести клипы к одному формату
    norm = []
    segments = []
    t = 0.0
    for i, clip in enumerate(clips):
        info = probe(clip)
        out = work / f"norm_{i}.mp4"
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black,fps={FPS},setsar=1")
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(clip)]
        if not info["has_audio"]:
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest"]
        cmd += ["-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-ar", "44100", "-ac", "2", str(out)]
        _run(cmd)
        dur = probe(out)["duration"]
        dialogue = scenes[i].get("dialogue", "") if i < len(scenes) else ""
        if dialogue:
            segments.append((t + 0.15, t + dur - 0.1, dialogue))
        t += dur
        norm.append(out)

    # 2) склейка
    list_file = work / "concat.txt"
    list_file.write_text("".join(f"file '{p.name}'\n" for p in norm), encoding="utf-8")
    joined = work / "joined.mp4"
    _run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", list_file.name,
          "-c", "copy", joined.name], cwd=work)

    # 3) субтитры + громкость
    final = work / "final.mp4"
    vf = []
    if captions and segments:
        write_ass(work / "captions.ass", segments)
        vf = ["-vf", "subtitles=captions.ass"]
    _run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined.name, *vf,
          "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
          "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
          "-c:a", "aac", "-b:a", "160k", "-ar", "44100", "-movflags", "+faststart", final.name], cwd=work)

    # 4) лист кадров для проверки качества
    qc = work / "qc"
    qc.mkdir(exist_ok=True)
    total = probe(final)["duration"]
    step = max(total / 8, 0.5)
    _run(["ffmpeg", "-y", "-loglevel", "error", "-i", final.name,
          "-vf", f"fps=1/{step:.3f},scale=240:-1,tile=4x2", "-frames:v", "1", "qc/sheet.jpg"], cwd=work)

    for tmp in norm + [joined, list_file]:
        tmp.unlink(missing_ok=True)

    rel = str(final.relative_to(ROOT)).replace("\\", "/")
    ep.setdefault("assets", {})["final_path"] = rel
    ep["assets"]["duration_s"] = round(total, 2)
    save_episode(ep)
    return {"final": rel, "duration_s": round(total, 2), "size_mb": round(final.stat().st_size / 1e6, 2),
            "qc_sheet": str((qc / "sheet.jpg").relative_to(ROOT)).replace("\\", "/")}


def main() -> None:
    parser = argparse.ArgumentParser(description="Монтаж эпизода")
    parser.add_argument("episode")
    parser.add_argument("--no-captions", action="store_true")
    args = parser.parse_args()
    print(json.dumps(assemble(args.episode, not args.no_captions), ensure_ascii=False))


if __name__ == "__main__":
    main()
