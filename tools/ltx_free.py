"""Бесплатная генерация клипа через открытую модель LTX-2.3 (Lightricks) в Hugging Face Space.

Без водяного знака, со звуком и речью. Лицензия LTX: бесплатно при выручке < $10 млн/год.
Ключ берётся из переменной окружения HF_TOKEN (бесплатный аккаунт HF даёт больше GPU-квоты);
без ключа работает анонимно, но квоты хватает примерно на 1 клип.

    python tools/ltx_free.py --image kadr.png --prompt "..." --out clip.mp4 [--duration 5]
    python tools/ltx_free.py --after prev.mp4 --prompt "..." --out next.mp4   # старт с последнего кадра prev.mp4

Нужен сетевой доступ к huggingface.co и *.hf.space. Ключ никогда не печатается.

Известный брак (тест 2026-10-26): реплика в кавычках иногда рисуется в кадре нечитаемыми
субтитрами, даже с «No subtitles» в промпте. Каждый клип проверять глазами (кадр 3–4 с);
не писать в промпте слово «subtitles», просить «clean picture, nothing written anywhere».
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import urllib.request
import uuid

SPACE = "https://lightricks-ltx-2-3.hf.space"


def _headers(extra=None):
    h = dict(extra or {})
    token = os.environ.get("HF_TOKEN")
    if token:
        h["Authorization"] = "Bearer " + token
    return h


def _upload(path):
    boundary = "----ltx" + uuid.uuid4().hex
    data = open(path, "rb").read()
    body = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"files\"; "
        f"filename=\"{os.path.basename(path)}\"\r\nContent-Type: image/png\r\n\r\n"
    ).encode() + data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        SPACE + "/gradio_api/upload", data=body,
        headers=_headers({"Content-Type": "multipart/form-data; boundary=" + boundary}))
    return json.load(urllib.request.urlopen(req, timeout=60))[0]


def last_frame(video, out_png):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-sseof", "-0.1", "-i", video,
                    "-frames:v", "1", out_png], check=True)


def generate(image, prompt, out, duration=5.0, width=576, height=1024, seed=42):
    path = _upload(image)
    payload = {"data": [{"path": path, "meta": {"_type": "gradio.FileData"}}, prompt,
                        float(duration), False, seed, False, height, width]}
    req = urllib.request.Request(
        SPACE + "/gradio_api/call/generate_video", data=json.dumps(payload).encode(),
        headers=_headers({"Content-Type": "application/json"}))
    event_id = json.load(urllib.request.urlopen(req, timeout=60))["event_id"]
    stream = urllib.request.urlopen(
        urllib.request.Request(SPACE + "/gradio_api/call/generate_video/" + event_id,
                               headers=_headers()), timeout=900).read().decode()
    if "event: complete" not in stream:
        raise RuntimeError("LTX отказал (скорее всего, кончилась GPU-квота): " + stream[-200:])
    result = json.loads(stream.split("event: complete")[1].split("data:", 1)[1].strip().split("\n")[0])
    urllib.request.urlretrieve(result[0]["url"], out)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--image", help="стартовый кадр (png/jpg)")
    src.add_argument("--after", help="клип, с последнего кадра которого продолжить")
    ap.add_argument("--prompt", required=True, help="действие, камера, реплика в кавычках (до ~12 слов на 5 с)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--duration", type=float, default=5.0)
    a = ap.parse_args()
    image = a.image
    if a.after:
        image = os.path.join(tempfile.mkdtemp(), "last.png")
        last_frame(a.after, image)
    try:
        generate(image, a.prompt, a.out, a.duration)
    except Exception as e:  # noqa: BLE001
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    print(a.out)


if __name__ == "__main__":
    main()
