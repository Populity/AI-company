# Бесплатное видео с говорящим ИИ-персонажем: открытые модели и бесплатные мощности

Дата: 2026-10-23. Метод: веб-поиск (WebFetch и прямой доступ к Hugging Face из контейнера не сработали,
поэтому карточки моделей лично не открывал). Уверенность: **В** — высокая (несколько независимых источников
или первоисточник в выдаче), **С** — средняя (вторичные источники сходятся), **Н** — низкая (один источник,
противоречия или моя оценка). Ничего не регистрировал и не платил.

Задача: 30-секундный видеодневник призрака Уолта (говорит в камеру, американский английский, 3–4 клипа,
вертикаль 9:16), агент делает сам, без водяного знака, с правом монетизации.

---

## Главный вывод

1. **Говорящая голова по фото + аудио бесплатно — реально.** Лучший кандидат: **InfiniteTalk** (MeiGen, на базе
   Wan 2.1 14B, Apache 2.0). Есть готовый Colab под бесплатный T4: 480p, ~12,7 ГБ видеопамяти, ~0,5–1 кадр/с.
   Тот же код запускается в ноутбуке **Kaggle**, а Kaggle, в отличие от Colab, официально управляется по API.
2. **Голос бесплатно и легально — Kokoro-82M** (Apache 2.0). Работает на процессоре прямо в нашем контейнере
   (4 ядра, 15 ГБ ОЗУ, без видеокарты), голос детерминированный, водяного знака нет.
3. **Видео со звуком одной моделью — LTX-2 / LTX-2.3** (Lightricks). Бесплатно для коммерции, пока выручка
   компании меньше $10 млн. Но на T4 почти не влезает: текстовый энкодер Gemma 3 12B требует ~24 ГБ. Реально
   только через чужой HF Space (ZeroGPU) или Modal.
4. **Новые Wan (2.5, 2.6, 2.7, 3.0) не открыты**, это платные API. Последние открытые веса — Wan 2.2 (С–В).
5. **Colab не годится для агента**: нет API для бесплатного запуска, нужен браузер; бесплатный тариф рассчитан
   на интерактивную работу. **Kaggle годится**: `kaggle kernels push/status/output`.
6. Без собственника не обойтись: аккаунты Kaggle и Hugging Face должен **зарегистрировать он**
   (правило 1 устава), подтвердить телефон в Kaggle и выдать токены как секреты окружения.

---

## 1. Открытые видеомодели

### 1а. Говорящие головы (фото + аудио → видео с липсинком) — главное для нас

| Модель | Что делает | Лицензия весов | Коммерция | Мин. GPU | Время на 10 с (оценка) | Уверенность |
|---|---|---|---|---|---|---|
| **InfiniteTalk** (MeiGen, 2025) | фото или видео + аудио → говорящий персонаж, губы, голова, тело; длина не ограничена (скользящие окна) | Apache 2.0; база Wan 2.1 Apache 2.0; LoRA ускорения lightx2v — своя лицензия | да (проверить лицензии компонентов: wav2vec, LoRA) | T4 16 ГБ в 480p (12,7 ГБ, Colab-проект); официально ≥24–28 ГБ без квантизации | T4: 250 кадров при 0,5–1 кадр/с ≈ **4–8 мин** + 5–10 мин загрузка весов. H200: ~3,5 мин на 81 кадр при 40 шагах | лицензия С, T4 Н–С |
| **MultiTalk** (MeiGen) | предшественник InfiniteTalk, 2+ говорящих | Apache 2.0 (README на HF) | да | как у InfiniteTalk | чуть медленнее | С |
| **Wan2.2-S2V-14B** (Alibaba, авг. 2025) | фото + аудио → видео 480/720p, кино-качество, движение тела | Apache 2.0 (агрегатор, на карточке не видел) | вероятно да | официально 80 ГБ; с выгрузкой в ОЗУ меньше | на T4 непрактично | лицензия Н–С |
| **SkyReels-V3-A2V-19B** (Skywork, янв. 2026) | портрет + аудио до 200 с, липсинк, мультяшные и реальные стили | **не подтверждена** (у V2 источники пишут то Skywork Community License, то Apache 2.0) | проверить | флаг `--low_vram` для <24 ГБ, 540p | неизвестно | Н |
| **OmniAvatar** (2025) | аудио → аватар во весь рост, на Wan 2.1 14B | не нашёл | проверить | ~как Wan 14B | неизвестно | Н |
| **HunyuanVideo-Avatar** (Tencent) | портрет + аудио, эмоции | Tencent Hunyuan Community License: **не действует в ЕС, Великобритании и Южной Корее** | рискованно: аудитория мировая | ~24 ГБ (форумы) | RTX 3090: 5–6 мин на 5 с | лицензия С, остальное Н |
| **LatentSync 1.5 / 1.6** (ByteDance) | перекладывает губы на готовое видео (липсинк поверх клипа) | Apache 2.0 | да | 1.5: ~8 ГБ, 1.6: ~18 ГБ | T4: 1–3 мин (Н) | С |
| **MuseTalk 1.5** (Tencent Music) | липсинк поверх видео, почти real-time | код MIT, в README «модели можно коммерчески»; на HF указана OpenRAIL-M — противоречие | скорее да | ~6–8 ГБ | >30 кадр/с на V100 (заявка) | С |
| **Hallo3** (Fudan) | портрет + аудио, высокое качество | код MIT (вторично), но база CogVideoX-5B, у которой коммерция только после регистрации | **сомнительно** | ≥24–40 ГБ | медленно | Н |
| **SadTalker** | старый 3DMM-аватар, качает голову | Apache 2.0 + сторонние компоненты | условно | 4–6 ГБ | <1 мин | С. Качество 2023 года, для сериала слабо |
| **Wav2Lip** | — | README запрещает коммерцию | **нет** | — | — | В |

### 1б. Общие image-to-video / text-to-video (немые клипы, перебивки, движение камеры)

| Модель | Звук | Лицензия | Коммерция | Мин. GPU | Комментарий | Уверенность |
|---|---|---|---|---|---|---|
| **Wan 2.1 / 2.2** (I2V-A14B, T2V-A14B, TI2V-5B, Animate) | нет (кроме S2V) | Apache 2.0 | да | TI2V-5B: 24 ГБ официально, ~8–16 ГБ с GGUF/выгрузкой; 14B GGUF Q4 на T4 при ≤480p | TI2V-5B 720p 5 с ≈ **9 мин на RTX 4090** | В |
| **Wan 2.5 / 2.6 / 2.7 / 3.0** | да | **весов нет**, только платный API | — | — | 2.7: источники спорят, свежий разбор говорит «весов нет» | С |
| **LTX-2 / LTX-2.3** (Lightricks, 19–22B) | **да, видео+звук за один проход**, до ~20 с | LTX-2 Community License: бесплатно при выручке < $10 млн | да (наш случай) | 16 ГБ — минимум для превью в FP8, но Gemma 3 12B энкодер ~24 ГБ; у 2.3 нужен CUDA 13+; на T4 нет FP8 | на T4 пока никто не подтвердил | лицензия В, железо С |
| **LTX-2.5** | да | не проверил | ? | ? | новее, мультишот | Н |
| **HunyuanVideo / 1.5** (8,3B) | нет (Foley отдельно) | Tencent Hunyuan Community: без ЕС, Великобритании, Кореи | риск | 1.5: ~14 ГБ | хорошее качество, но лицензия | С |
| **FramePack** (lllyasviel) | нет | код Apache 2.0, веса на базе HunyuanVideo → лицензия Tencent | риск | **6 ГБ** | длинные i2v на слабых картах | С |
| **SkyReels V2** | нет | Skywork Community / Apache (спорно) | вероятно | 14B: 24+ ГБ, 1.3B: меньше | бесконечная длина (Diffusion Forcing) | Н |
| **MAGI-1** (Sand AI, 4,5B distill / 24B) | нет | Apache 2.0 | да | 4,5B distill: ≥12 ГБ | авторегрессия, длинные клипы | С |
| **Mochi 1** (Genmo, 10B) | нет | Apache 2.0 | да | ~22+ ГБ | устарела | С |
| **CogVideoX-5B** | нет | CogVideoX License: коммерция только после регистрации у Zhipu | **нет без регистрации** | 12–16 ГБ | 2B — Apache 2.0 | С |
| **Open-Sora 2.0** (11B) | нет | Apache 2.0 (по памяти, не проверил) | вероятно | высокие | качество на уровне HunyuanVideo | Н |
| **Step-Video-T2V** (30B) | нет | MIT (по памяти, не проверил) | вероятно | ~80 ГБ | бесплатно не запустить | Н |
| **Kandinsky 5.0 Video Lite 2B** (Сбер) | нет | Apache 2.0 по вторичному источнику; где-то пишут MIT | вероятно | 12–24 ГБ | 768×512, 5 и 10 с, i2v есть в ComfyUI | Н–С |
| **AIdeaLab VideoJP** (Япония, на CogVideoX ~2B) | нет | обучена на CC-BY/CC0 картинках, лицензия весов не подтверждена | ? | ~12 ГБ | слабое качество, 7 скачиваний в месяц, нам не нужна | Н |

**Вывод по моделям:** для говорящего Уолта брать **InfiniteTalk** (основной) и **LatentSync 1.5** (дешёвый вариант
поверх готового клипа). Для немых перебивок брать **Wan 2.2 (5B/14B GGUF)** и **MAGI-1 4.5B**. **LTX-2** нужен,
когда нужен звук мира (скрип, гул ламп), только на мощном железе. Hunyuan-семейство не брать: юридический
риск с ЕС и Великобританией.

---

## 2. Где запускать бесплатно

| Площадка | Реально бесплатно? | Лимиты (по выдаче) | Агент может сам? | Что настроить | Уверенность |
|---|---|---|---|---|---|
| **Kaggle Notebooks** | да | ~30 ч GPU в неделю (квота «плавает»), сессия 9–12 ч, GPU T4×2 (2 карты по 16 ГБ, **не объединяются** в 32 ГБ) или P100; ~29 ГБ ОЗУ (по памяти) | **да**: `kaggle kernels push -p dir` (в `kernel-metadata.json`: `enable_gpu: true`, `enable_internet: true`), потом `kaggle kernels status`, `kaggle kernels output` | собственник: аккаунт, **подтверждение телефона** (без него нет GPU и интернета), API-токен в секреты (`KAGGLE_USERNAME`, `KAGGLE_KEY`) | квота С, API С |
| **Google Colab free** | да, T4 16 ГБ | 12 ч сессия, отключение при простое 30–90 мин, недельная квота не публикуется, GPU не гарантирован | **нет**: нет API запуска, только браузер; автоматизация противоречит духу бесплатного тарифа | — | В |
| **HF Spaces (ZeroGPU)** через `gradio_client` | да | в день: без входа ~2 мин GPU, бесплатный аккаунт 3,5–5 мин, PRO ($9/мес) 25–40 мин; сверх квоты PRO платит $1 за 10 мин | **да**: `Client("owner/space", token=HF_TOKEN).predict(...)` | собственник: аккаунт HF + токен на чтение. На форуме жалобы, что токен через `gradio_client` иногда не засчитывается и вызов идёт по «гостевой» квоте | С |
| **Modal** (Starter) | $30 кредитов в месяц | T4 $0,59/ч, A100 40 ГБ $2,10/ч, H100 $3,95/ч → ~7,5 ч H100 или ~50 ч T4 в месяц; по одному источнику без карты только $5 | **да**, полностью из Python (`modal run`) | собственник: аккаунт, вероятно карта; поставить лимит трат | С |
| **Lightning.ai** | почти нет | с 21.09.2026 вместо ежемесячных ~80 ч разовые 30 кредитов (5 за регистрацию + 25 за привязку карты) на 12 мес, T4 подорожал до $0,55/ч | частично (SDK) | карта | Н–С |
| **Paperspace (Gradient free)** | бесплатный тариф, по моим данным, свёрнут после покупки DigitalOcean | — | — | — | Н (не искал отдельно) |
| **fal.ai** (у нас уже есть) | пробные кредиты: $1–20, источники спорят | дальше по факту | да (`tools/fal_gen.py`) | — | Н |
| **WaveSpeed** | $1 при регистрации без карты (вторично) | InfiniteTalk у них ~$0,15 за 5 с 480p → $1 ≈ 30 с | да | регистрация | С |
| **SiliconFlow** | $1 + бесплатные текстовые модели (100 запросов в день) | на видео бесплатного нет | — | регистрация | Н |
| **Novita** | $0,5 (вторично) или реферальные $10 | — | — | — | Н |
| **Segmind** | **нет** бонуса при регистрации (их собственный блог) | рефералка $10 после оплаты | — | — | С |
| **Runware** | нет; минимум пополнения $20; программы для стартапов и креаторов по заявке | — | — | заявку подаёт собственник | С |
| **Replicate** | данных о бесплатном тарифе нет | — | — | — | Н |
| **Together** | под видео нет бесплатных кредитов (не нашёл) | — | — | — | Н |
| **Cloudflare Workers AI** | да, 10 000 «нейронов» в день | **видеомоделей нет**; TTS: MeloTTS ~19 нейронов за минуту (то есть сотни минут в день), Deepgram Aura ~7000 символов в день | да (REST) | аккаунт CF + токен | С |

**Пробные кредиты на 30 с говорящего видео — капля.** $1 даёт 1–2 серии, не более.

---

## 3. Бесплатная английская озвучка без водяного знака

| Движок | Бесплатно? | Коммерция | Качество | Где работает | Что настроить | Уверенность |
|---|---|---|---|---|---|---|
| **Kokoro-82M** | да, локально | **Apache 2.0** | очень хорошее для своего размера; американские мужские голоса `am_onyx`, `am_michael`, `am_eric`, `am_fenrir` (низкий, сухой подойдёт) | **CPU в нашем контейнере**, ~реальное время и быстрее | `pip install kokoro soundfile` + espeak-ng; голос и скорость (0,85–0,9) зафиксировать в библии | В |
| **Chatterbox / Turbo** (Resemble) | да, локально | **MIT** | отличное, эмоции, теги `[sigh]`, `[chuckle]`, клон голоса по 10 с образца | лучше GPU (Kaggle); на CPU медленно, но для 30 с терпимо (Н) | встроен **неслышимый** водяной знак PerTh (метка ИИ-происхождения, не звук и не логотип); мы и так не скрываем ИИ | С |
| **Piper** | да, CPU | движок MIT/GPL; голоса разные: `ryan`, `joe` (LibriTTS, CC-BY, нужна атрибуция); `lessac` спорный (Blizzard, некоммерческий) | роботизированно | CPU, мгновенно | выбрать голос с чистой лицензией | С |
| **Edge TTS** (`edge-tts`) | да, без ключа | **неясно**: неофициальный доступ к голосам Microsoft Edge, коммерческих прав никто не даёт | очень хорошее (нейроголоса Azure) | любой, через интернет | ничего | риск В. Только черновики и тест таймингов |
| **F5-TTS** | да | веса **CC-BY-NC-4.0** (из-за датасета Emilia) | отличное, клонирование | GPU | — | **нельзя**, В |
| **XTTS-v2** (Coqui) | да | **CPML, некоммерческая**; Coqui закрылась, лицензию купить не у кого | хорошее | GPU | — | **нельзя**, В |
| **Gemini TTS** (free tier) | да | API разрешает использовать выходные данные; бесплатный тариф идёт на обучение Google; для пользователей в ЕЭС/UK/Швейцарии нужен платный тариф (по памяти) | отличное, управление стилем | API | ключ AI Studio от собственника; лимит у TTS-моделей очень мал (жалоба: **10 запросов в день** у gemini-3.1-flash-tts) | С |
| **ElevenLabs free** | 10 000 кредитов (~10 мин) в месяц | **нет**: только некоммерческое использование с атрибуцией; сгенерированное на free нельзя монетизировать даже после покупки тарифа | лучшее | API | — | В |
| **Cloudflare MeloTTS** | да, 10 000 нейронов в день | MIT (MeloTTS) | среднее | API | аккаунт CF | С |

**Рекомендация:** основной голос Уолта — **Kokoro `am_onyx` или `am_michael`, скорость ~0,88**, плюс лёгкая
обработка в ffmpeg: низкие частоты, лёгкий «шум VHS-камеры», реверберация пустого офиса. Если нужна
эмоциональность (вздохи) — **Chatterbox на Kaggle-GPU** с клоном голоса Kokoro как образцом. Так голос будет наш,
без чужих прав.

---

## 4. Особая оценка двух вариантов

### Вариант А: «Ноутбук Kaggle + InfiniteTalk (или Wan / LTX-2), агент запускает через Kaggle API»

**Как работает:**
1. Агент локально делает голос (Kokoro, 16 кГц WAV) и берёт эталонный кадр Уолта.
2. Загружает их как приватный Kaggle Dataset (`kaggle datasets version`).
3. Пушит ноутбук (`kaggle kernels push`), внутри: `pip install` → скачать веса (InfiniteTalk + Wan2.1-I2V-14B-480P
   в fp8 или GGUF Q4–Q8, wav2vec2) с HF → генерация 480×832 → mp4 в `/kaggle/working`.
4. Опрашивает `kaggle kernels status`, забирает `kaggle kernels output`.
5. Дальше обычный `tools/assemble.py`: апскейл до 720×1280, субтитры, «VHS-фильтр 1987».

**Плюсы:**
- 0 ₽, Apache 2.0, без водяного знака.
- ~30 ч в неделю — с запасом на 1–2 серии в день.
- Говорящий Уолт с эталонной внешностью из одного кадра, движение головы и плеч.
- Формат дневника на камеру 1987 года прощает 480p и артефакты.

**Минусы и риски:**
- T4 — архитектура Turing: нет bf16 и FP8 в железе, нет FlashAttention 2. Медленно: 30 с видео ≈ **15–30 мин**
  генерации плюс 5–15 мин на скачивание весов в каждой сессии. Ускорение: держать веса в Kaggle Dataset/Model, (Н).
- Две T4 не складываются в 32 ГБ. Второй картой можно распараллелить клипы: два клипа одновременно.
- Нужны подтверждённый телефон и токен от собственника.
- Нет официального способа узнать остаток квоты по API.
- Возможны баны за автоматизацию (явного запрета не нашёл, Н).
- Нестабильные версии ComfyUI и Wan-оберток: придётся один раз отладить ноутбук.

**LTX-2 на Kaggle:** пока **не рекомендую**. Gemma-энкодер не влезает в 16 ГБ, у 2.3 требование CUDA 13.
**Wan 2.2 TI2V-5B или 14B GGUF** на T4 для немых перебивок — да, но 5 с клип ≈ 15–40 мин (Н).

**Вердикт: лучший бесплатный вариант. Готовность — после 1 дня отладки.**

### Вариант Б: «HF Space через `gradio_client`»

**Как работает:** агент вызывает публичный Space (например, LTX-2.3 Turbo с видео и звуком на ZeroGPU,
Spaces с InfiniteTalk / Wan 2.2 / LatentSync) как API.

**Плюсы:**
- Ноль настройки и железо уровня H200.
- LTX-2 со звуком реально доступен только так.

**Минусы:**
- Квота бесплатного аккаунта 3,5–5 мин GPU в день: это примерно **1–3 коротких клипа** (Н).
- Чужие Spaces пропадают, меняют API, стоят в очереди.
- Дублировать Space на ZeroGPU можно только с PRO.
- Жалобы, что токен не засчитывается (тогда квота гостевая, ~2 мин).
- Для 30 с говорящей головы квоты не хватит: Space ограничивает длительность вызова (обычно 60–120 с GPU).

**Вердикт: резерв и источник коротких перебивок со звуком, не основной конвейер.** Если собственник купит HF PRO
($9/мес, 25–40 мин в день), вариант станет рабочим на 1 серию в день. Это решение и покупка собственника.

---

## 5. Рейтинг 5 лучших схем для «Still Clocked In» (30 с, говорящий Уолт, английский)

Каждая серия: 3–4 клипа по 8–10 с. Эталонный кадр Уолта уже есть (берём кадр из библии и эпизодов).

| # | Схема | Цена | Качество | Скорость на серию | Надёжность | Что нужно от собственника |
|---|---|---|---|---|---|---|
| **1** | **Kokoro (голос на CPU) → Kaggle API: InfiniteTalk 480p (Wan2.1-14B fp8/GGUF + lightx2v 4–8 шагов) → апскейл + VHS-фильтр в `assemble.py`** | 0 | хорошее: губы и мимика по аудио, внешность из эталона; призрачное свечение и прозрачность нужно проверить | ~30–60 мин машинного времени (Н), агент не ждёт | средняя | аккаунт Kaggle + телефон + API-токен |
| **2** | **Kokoro → Modal (бесплатные $30 в месяц): InfiniteTalk 720p на A100/H100** | 0 в пределах $30 (≈7,5 ч H100 ≈ 20–40 серий в месяц, Н) | лучше: 720p, быстрее | ~5–15 мин | высокая | аккаунт Modal, вероятно карта + жёсткий лимит трат. Риск выхода за $30 — решение собственника |
| **3** | **Немой клип (Wan 2.2 i2v на Kaggle или уже купленный клип) + LatentSync 1.5 / MuseTalk для губ, голос Kokoro** | 0 | среднее: двигаются только губы и низ лица, зато тело, свет и фон любые | ~10–20 мин на Kaggle | высокая (лёгкие модели) | то же, что в схеме 1 |
| **4** | **HF Space (`gradio_client`): LTX-2.3 со звуком для 1–2 перебивок + Kokoro для речи Уолта** | 0 (или $9/мес PRO) | высокое у перебивок, звук мира из модели | минуты, если есть квота | низкая (чужие Spaces) | аккаунт HF + токен; по желанию PRO |
| **5** | **Kaggle: SkyReels-V3-A2V (`--low_vram`, 540p) или Wan2.2-S2V с выгрузкой в ОЗУ** | 0 | потенциально лучшее движение тела и кино-картинка | медленно, на T4 может не влезть | низкая; **лицензия SkyReels не подтверждена** | как в схеме 1 + юридическая проверка лицензии |

**План внедрения (предложение директору):**
1. Собственник регистрирует Kaggle (с телефоном) и HF, кладёт токены в секреты окружения. Это 10 минут.
2. Продакшн собирает `tools/kaggle_gen.py` (push → status → output) и ноутбук InfiniteTalk. Первый тест в сухом режиме:
   один клип 8 с.
3. Голос: зафиксировать в библии голос Kokoro, скорость и цепочку ffmpeg-фильтров, чтобы Уолт звучал одинаково.
4. Платный fal оставить для ключевых серий и подстраховки, когда Kaggle недоступен.

**Что проверить при первом прогоне:**
- держит ли InfiniteTalk полупрозрачное голубое свечение и тающий низ тела (может «очеловечить» Уолта; тогда
  накладывать свечение в монтаже);
- реальное время на T4;
- лицензии wav2vec2 и lightx2v-LoRA на карточках HF;
- открыт ли из контейнера доступ к kaggle.com и huggingface.co.

**Правила устава:**
- Регистрация аккаунтов и привязка карт — только собственник (правило 1).
- Токены не выводить в лог (правило 5).
- В Instagram ставить `#aigenerated`, YouTube помечает автоматически.
- Шаблонность: с июля 2025 правило называется inauthentic content, с июля 2026 YouTube отдельно не монетизирует
  «шаблонный» контент. Бесплатный конвейер не повод выпускать больше 1–2 серий в день.

---

## Источники (из выдачи поиска)

- InfiniteTalk: [Colab-проект под T4](https://github.com/sruckh/InfiniteTalk-Google-Collab), [ComfyUI-гайд](https://lilting.ch/en/articles/infinitetalk-comfyui-lipsync), [Atlas Cloud](https://www.atlascloud.ai/infinitetalk), [SourcePulse (Apache 2.0)](https://www.sourcepulse.org/projects/12893512), [WaveSpeed цены](https://wavespeed.ai/blog/posts/introducing-infinitetalk-infinite-conversations-maximum-realism/), [MultiTalk README](https://huggingface.co/MeiGen-AI/MeiGen-MultiTalk/blob/refs%2Fpr%2F3/README.md)
- Wan: [Wan open weights stopped at 2.2](https://howaiworks.ai/blog/alibaba-wan-open-weights-stopped-at-2-2), [Wan 2.6 not open](https://www.wan27.org/blog/wan-2-6-open-source-guide), [Wan2.2-S2V](https://huggingface.co/wan-ai/wan2.2-s2v-14b), [S2V на AMD (80 ГБ)](https://rocm.blogs.amd.com/artificial-intelligence/audio-driven-videogen/README.html), [Wan2.2 TI2V-5B на 4090](https://computingforgeeks.com/run-wan-video-generation-locally/)
- LTX-2: [Comfy LTX-2.3](https://comfy.org/workflows/model/ltx-2-3/), [Lightricks open-sources LTX-2](https://thedeadpixelssociety.com/lightricks-open-sources-ltx-2-the-production-ready-audio-and-video-generation-model/), [LTX hardware guide](https://ltx.io/blog/hardware-for-ai-video-models), [Gemma-энкодер OOM на 16 ГБ](https://github.com/Lightricks/ComfyUI-LTXVideo/issues/303), [HF Space LTX-2.3 Turbo](https://huggingface.co/Sanio7791/spaces)
- SkyReels V3: [HF карточка](https://huggingface.co/Skywork/SkyReels-V3-A2V-19B), [SourcePulse](https://www.sourcepulse.org/projects/25003051)
- Hunyuan: [обзор лицензии (без ЕС/UK/Кореи)](https://chatforest.com/reviews/hunyuanvideo-tencent-open-source-video-generation/), [HunyuanVideo-Foley NOTICE](https://huggingface.co/tencent/HunyuanVideo-Foley/blob/main/NOTICE), [Fora Soft self-hosting](https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/self-hosting-hunyuanvideo-cogvideox-mochi-ltx)
- Липсинк: [лицензии lip-sync 2026](https://www.creativeainews.com/articles/open-source-lip-sync-licenses-commercial-use-2026/), [MuseTalk GitHub](https://github.com/TMElyralab/MuseTalk), [LatentSync GitHub](https://github.com/bytedance/LatentSync), [LatentSync 18 ГБ](https://news.creeta.com/en/open-source-lip-sync-models-2026/), [TalkingHeadBench (Hallo3 MIT)](https://arxiv.org/pdf/2505.24866), [OmniAvatar arXiv](https://arxiv.org/abs/2506.18866)
- Прочие модели: [MAGI-1 GitHub](https://github.com/SandAI-org/MAGI-1), [Kandinsky 5.0](https://arxiv.org/abs/2511.14993), [Kandinsky 5 i2v ComfyUI](https://comfy.org/workflows/video_kandinsky5_i2v-56e17946ef8c/), [AIdeaLab VideoJP](https://huggingface.co/aidealab/aidealab-videojp)
- Площадки: [HF Spaces API docs](https://huggingface.co/docs/hub/spaces-api-endpoints), [ZeroGPU квоты (форум)](https://discuss.huggingface.co/t/free-account-zerogpu-quota-issue/175180/9), [токен через gradio_client](https://discuss.huggingface.co/t/use-authentication-in-huggingface-gradio-api-hosting-on-zerogpu/115565), [ZeroGPU overquota](https://api-inference.huggingface.co/changelog/zerogpu-overquota), [Free cloud GPUs 2026](https://gpuperhour.com/blog/free-cloud-gpus-and-credits), [kagglex (квота не видна по API)](https://pypi.org/project/kagglex/), [kaggle-action](https://github.com/frederisk/kaggle-action), [Kaggle телефон](https://neuroai.neuromatch.io/tutorial-kaggle), [Colab гайд](https://www.hivenet.com/post/google-colaboratory-gpu-complete-guide-to-free-cloud-gpu-access-and-limitations), [Modal pricing](https://modal.com/pricing), [Modal $5 без карты](https://www.mintlify.com/cheahjs/free-llm-api-resources/providers/trial/modal), [Lightning repricing 09.2026](https://www.usagepricing.com/blueprint/activity/lightning-ai-2026-09-21-gpu-rate-card-reprice), [Cloudflare Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), [WaveSpeed free](https://wavespeed.ai/blog/cost-and-billing/is-wavespeedai-free-to-use/), [Segmind без бонуса](https://blog.segmind.com/seedance-2-0-free-credits-how-to-actually-stretch-a-10-top-up/), [Runware платежи](https://help.runware.ai/articles/7648578038-payments-and-credits), [SiliconFlow](https://agentdeals.dev/vendor/siliconflow), [Novita](https://yangmao.ai/en/providers/novita/free-tier/), [fal free plan](https://www.costbench.com/software/ai-ml-platforms/fal/free-plan/)
- Озвучка: [гид по open-source TTS 2026](https://tts.ai/blog/open-source-text-to-speech-guide-2026/?lang=uk), [Chatterbox Turbo](https://tts.ai/voices/chatterbox-turbo/), [F5-TTS лицензия](https://huggingface.co/SWivid/F5-TTS/commit/0a5fb316c4188d42de2456ce94c7b21893e94974), [XTTS после закрытия Coqui](https://github.com/coqui-ai/TTS/discussions/4145), [Piper лицензии голосов](https://github.com/rhasspy/piper/discussions/271), [Edge TTS (Microsoft Q&A)](https://learn.microsoft.com/en-us/answers/questions/2392491/unofficial-edge-tts-api), [Gemini лимиты](https://ai.google.dev/pricing?hl=sl), [Gemini TTS 10 RPD](https://discuss.ai.google.dev/t/gemini-lies-about-free-tier-quota-limits-sudden-resource-exhausted-blockers-on-tts-models/177531), [ElevenLabs free](https://dupple.com/learn/is-elevenlabs-free)
- YouTube: [inauthentic content 2026](https://logie.ai/news/youtube-ai-slop-crackdown-2026-monetization/), [хронология](https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline)
