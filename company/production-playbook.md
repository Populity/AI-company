# Как компания сейчас снимает серию (рабочая инструкция, 2026-10-26)

Заменяет шаги генерации из `daily-cycle.md`, пока нет ключа fal.ai. Источник правды о ценах — `company/decisions.md`.

## Инструменты
- **Higgsfield (коннектор, подписка собственника Basic 70 кр./мес):** кадры `gpt_image_2_5` с эталоном
  Walt (`502401a4-7764-4088-8228-f013480b5d51`, роль `image_references`) — 0.25 кр.; видео `kling3_0_turbo`
  (start_image) — 12 кр./8 с 720p; озвучка `seed_audio` с клоном голоса Walt (`ebf55bf3-cbfb-4892-b691-0568e6ebcb4f`,
  роль `audio_references`) — ~0.8 кр.; песочница `sandbox_exec` — бесплатно: ffmpeg, whisper, загрузка готового ролика.
- **Hugging Face (коннектор, бесплатная квота аккаунта собственника, ~5 видео/день):** `dynamic_space`
  `zerogpu-aoti/wan2-2-fp8da-aoti-faster` (видео из кадра без звука, ≤4 с, steps 4 — иначе таймаут 60 с);
  `ResembleAI/Chatterbox` (озвучка ≤300 символов, клон голоса по URL
  `https://d2ol7oe51mr4n9.cloudfront.net/user_3KH7fGSpLnltbinp8xOjxx8fD2m/ebf55bf3-cbfb-4892-b691-0568e6ebcb4f.mp3`).

## Порядок серии (30–33 с)
1. Сценарий — `company/character/season-1-scripts-part*.md` (серия по дате из `season-plan.md`).
2. 3 кадра Higgsfield с эталоном (лицо крупно, без текста). Посмотреть глазами (песочница, image_paths).
3. Голос: Chatterbox (бесплатно), проверить распознаванием (whisper) каждую фразу; битую фразу — seed_audio.
4. Видео: сначала Wan 2.2 бесплатно (в промпте НЕ писать camera/tripod/camcorder; «subtle motion only»;
   negative: face change, new objects, text). Брак → один повтор → затем Kling Turbo (12 кр.) для самой важной сцены,
   остальное — кадр с медленным наездом (zoompan) бесплатно.
5. Голос за кадром (видеодневник), гул офиса, писк Dot, щелчок табельных часов в конце, субтитры (whisper, MarginV=110),
   720×1280. Минимум 30 с (паузы после реплик).
6. Загрузить в Higgsfield (media_upload → PUT → media_confirm), ссылку — в `assets.final_url` карточки.
7. Тексты публикации — из `company/smm-season-1.md` в поля карточки (youtube/instagram/hashtags), статус `review`.

## Жёсткие лимиты
- Higgsfield: не больше 15 кр. в день, только из уже купленного остатка. Покупки, подписки, пополнения — никогда.
- Брак не публикуется. Одобрение собственника — пока действует режим одобрения (`config/company.json → approval`).
- Публикация — только `python tools/publish.py <id>`.
