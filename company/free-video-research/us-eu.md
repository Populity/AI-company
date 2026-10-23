# Бесплатные ИИ-видео без видимого водяного знака — США и Европа

Дата исследования: 23.10.2026. Отдел: Тренды (`trend-scout`).
Метод: веб-поиск (WebFetch не работал — страницы напрямую не открывались). Почти все цифры —
из обзоров и новостей, а не с официальных страниц цен, поэтому у каждой строки стоит уровень уверенности.
**Перед тем как на что-то опереться, проверить на месте** (лимиты в 2026 менялись каждые 1–2 месяца).

Обозначения водяного знака: **ВИДИМЫЙ** — логотип на кадре (нам мешает); **невидимый** — SynthID / C2PA
(нам не мешает, мы и так помечаем ИИ).

## Главное за 2026

- **Sora закрыта:** приложение — 26.04.2026, API — 24.09.2026. Бесплатного Sora больше нет (только Sora 2 внутри Bing).
- **Google Gemini Omni (1.1) Flash** — новая видеомодель Google (май 2026). С 23.09.2026 бесплатна в Google Vids
  (около 6 клипов в месяц), а также бесплатна в YouTube Shorts и в приложении YouTube Create (клипы до 10 с, со звуком, только SynthID).
- **Amazon Nova Reel** снята с поддержки 30.09.2026.
- **У всех «чистых» платформ видео** (Runway, Luma, Pika, HeyGen, Synthesia, D-ID, Captions, Krea) на бесплатном тарифе
  есть видимый знак и/или запрет на коммерческое использование.
- **Единственный бесплатный путь, который агент может запускать сам (без ручного клика), —** открытая модель
  **LTX-2.3 от Lightricks** (Израиль/США) в официальном Hugging Face Space (Gradio API). Ограничение — малая дневная квота GPU.

## Таблица

| Сервис | Что бесплатно | Видимый знак на free | Коммерция / монетизация на free | Звук / речь | Длина клипа | 9:16 | API / MCP для агента | Из России | Уверенность |
|---|---|---|---|---|---|---|---|---|---|
| **YouTube Shorts / YouTube Create** (Gemini Omni Flash; раньше Veo 3 Fast) | генерация в кнопке «Создать» → значок искры; дневной лимит не опубликован | нет, только SynthID + C2PA | ролик публикуется у нас в Shorts, монетизация по обычным правилам YouTube; YouTube сам ставит метку ИИ | да, видео со звуком; работает и с картинкой/озвучкой на входе; диалоги не подтверждены | до 10 с (Omni), 8 с (Veo 3 Fast) | да, Shorts вертикальные | нет, только вручную в телефоне | нужен VPN + зарубежный аккаунт; функция выкатывалась по странам (США, Великобритания, Канада, Австралия, Новая Зеландия) | средняя |
| **Google Vids** (vids.new) | около 6 генераций в месяц на личный аккаунт (клипы + аватары вместе), сброс 1-го числа; раньше было 10 в месяц на Veo 3.1 | нет, только SynthID | по общим правилам Google права на результат не забираются; отдельного запрета не нашёл | Omni — видео со звуком; есть ИИ-аватары с голосом (личный аватар — только платно, не в ЕС и Великобритании) | 3–10 с, есть продление сцены | да (16:9 и 9:16) | нет (только сайт на компьютере) | Google-ИИ в РФ закрыт → VPN + зарубежный аккаунт | средняя |
| **Google Flow** (Veo 3.1 Lite/Fast/Quality) | 50 кредитов в день без подписки (Lite около 10, Fast около 20, Quality около 100 кредитов за ролик) → до 2–5 роликов в день | **ВИДИМЫЙ «Veo»** в углу у всех, кроме Ultra (по сообщениям, есть переключатель — не подтверждено) + SynthID | права на результат у пользователя; знак мешает | да, звук и речь с липсинком (Veo 3.1) | 8 с, есть продление | да (с января 2026 нативная вертикаль в Veo 3.1 + опорные картинки персонажа) | нет (API Veo платный) | VPN + зарубежный аккаунт; список стран ограничен | средняя (по знаку — низкая) |
| **Gemini app** (Omni / Veo) | постоянной бесплатной квоты нет; была акция «10 видео» 30.07–11.08.2026 | при акциях был видимый знак + SynthID | — | да | 8–10 с | да | нет | VPN | средняя |
| **Gemini API / AI Studio** (Veo 3.1, Omni Flash) | **бесплатного уровня для видео нет**; Omni около $0,10 за секунду (720p) | невидимый SynthID | да, платно | да | 8–10 с | да | **да, API** (у нас уже есть платный путь через fal) | VPN | высокая |
| **Студенческий Google AI Pro** | 12 мес. бесплатно для студентов 18+ (США, Япония, Индонезия, Корея, Бразилия, часть Африки и арабских стран) | у Pro во Flow есть видимый знак | — | да | 8 с | да | нет | нет (нужен студент из этих стран) | средняя; нам не подходит |
| **Bing Video Creator** (Sora 2, с 05.03.2026) | 10 быстрых генераций, дальше без лимита в медленном режиме (или за баллы Microsoft Rewards) | **ВИДИМЫЙ** + C2PA | по правилам Bing Image/Video Creator — скорее только некоммерческое использование | да, со звуком (Sora 2) | 5 с | да (только вертикаль) | нет (приложение Bing) | **не работает в России** | средняя |
| **Microsoft Copilot** | видео — то же, что Bing Video Creator; отдельного бесплатного видео не нашёл | — | — | — | — | — | нет | VPN | низкая |
| **Meta AI Vibes / Meta AI app** | бесплатно, лимиты не опубликованы | обзоры пишут «без знака», но Meta может ставить видимую метку «ИИ» + метаданные | права неясны, официальных правил не нашёл | есть музыка/звук; речь не подтверждена | короткие (до ~10 с) | да | нет | Meta запрещена в РФ → VPN | низкая |
| **Meta Edits** (аналог CapCut от Instagram) | бесплатно (на май 2026): оживить фото, Restyle, Lip Sync | не подтверждено | для Reels — да | есть Lip Sync | до ~10 с | да | нет | VPN | низкая |
| **Adobe Firefly** | ограниченное число генераций в день на бесплатном тарифе (число не публикуется), есть сторонние модели (в т.ч. Luma Ray) | про видео не нашёл; на картинках видимого знака нет; Content Credentials (C2PA) | Adobe разрешает коммерцию, но без страховки от исков по авторским правам | зависит от модели | ~5 с | да | нет на free | Adobe ушёл из РФ → VPN + зарубежный аккаунт | низкая |
| **Canva** | 5 бесплатных видеогенераций на всю жизнь аккаунта (Magic Media, без звука); Veo 3 — только Pro | нет (если не брать Pro-элементы) | да, по лицензии Canva | на free — без звука; Veo 3 в Pro — 8 с со звуком | 6–8 с | на free по 16:9 | нет на free (MCP Canva есть, но генерация видео — Pro) | работает с ограничениями / VPN | средняя |
| **LTX-2.3 (Lightricks), открытая модель** — официальный HF Space `Lightricks/LTX-2-3` | бесплатно в пределах дневной квоты ZeroGPU на HF: около 3,5 мин GPU в день (без входа — 2 мин, ~3 запроса), т.е. 1–3 клипа в день; без лимита на своём GPU | **нет** (открытая модель) | **да** — лицензия LTX-2: бесплатно для коммерции при выручке < $10 млн в год | **да, видео со звуком в одной генерации**; липсинк слабее, чем у Veo | 1–10 с | задаётся размером кадра | **да: Gradio API (`gradio_client`) — агент может вызывать сам**; бесплатный аккаунт HF без оплаты | HF обычно открывается из РФ | средняя |
| **LTX Studio** (сайт Lightricks) | одноразовые тестовые кредиты | не подтверждено | **нет** — только личное использование | да | до 10 с | да | нет | VPN | средняя |
| **Runway** | 125 кредитов один раз, без пополнения | **ВИДИМЫЙ**, 720p | нет коммерческой лицензии | на старших моделях | 5–10 с | да | API только платно | VPN | средняя |
| **Luma Dream Machine** | несколько черновых генераций в месяц | **ВИДИМЫЙ** | **нет** (с тарифа Plus) | Ray3 — частично | 5–10 с | да | API платный | VPN | средняя |
| **Pika** | 80 кредитов в месяц, 480p | **ВИДИМЫЙ** (по большинству источников) | **нет** | звуковые эффекты | 5–10 с | да | нет | VPN | средняя |
| **HeyGen** | ~3 видео в месяц, 720p; бесплатные кредиты API убраны в феврале 2026 | **ВИДИМЫЙ** | для тестов, не для публикации | да, говорящий аватар | до 1–3 мин | да | нет на free | VPN | средняя |
| **Synthesia** (Великобритания) | ~10 мин в месяц (по другим данным — 1 видео до 3 мин) | **ВИДИМЫЙ** | ограничено | да, аватар | минуты | да | нет на free | VPN | средняя |
| **D-ID** | пробные ~5 мин | **ВИДИМЫЙ** | **нет** | да | короткие | да | API платный | VPN | средняя |
| **Captions / Mirage** | 60–200 кредитов на всю жизнь, клипы до 15 с | **ВИДИМЫЙ** (ИИ-актёры и монтаж) | — | да, говорящий ИИ-актёр | до 15 с | да | нет | VPN | средняя |
| **Krea** | 100 единиц в день, 480p | **ВИДИМЫЙ** | **нет** | зависит от модели | 5 с | да | нет на free | VPN | средняя |
| **Ideogram** | видео не нашёл (только картинки) | — | — | — | — | — | — | — | низкая |
| **Mistral** | видеогенерации не нашёл | — | — | — | — | — | — | — | низкая |
| **Stability AI** | новых бесплатных видеосервисов в 2026 не нашёл; старые открытые веса SVD (без звука, нужен свой GPU) | нет | лицензия Stability Community (< $1 млн выручки) | нет | 2–4 с | — | только свой GPU | — | низкая |
| **Amazon Nova Reel** | **снята 30.09.2026** | — | — | — | — | — | — | — | средняя |
| **OpenAI Sora** | **закрыта** (приложение — 26.04.2026, API — 24.09.2026) | — | — | — | — | — | — | — | высокая |

## Топ-5 для сериала «призрак-клерк», 30 с, видеодневник

Серия = 3–4 клипа по 8–10 с + склейка `tools/assemble.py`. Внешность героя держим через опорный кадр (image-to-video).

1. **YouTube Shorts / YouTube Create (Gemini Omni Flash)** — бесплатно, со звуком, вертикаль, без видимого знака, 10 с;
   3 клипа = серия. Минус: только вручную в телефоне, нужен зарубежный аккаунт / VPN, в Instagram — через скачивание из YouTube Studio (проверить).
2. **Google Vids (Omni 1.1 Flash)** — около 6 клипов в месяц без видимого знака, 9:16, со звуком, до 1080p (на тестах — 720p).
   Хватает на 1–2 серии в месяц. Только вручную на компьютере.
3. **LTX-2.3 в Hugging Face Space** — единственный бесплатный вариант, который **агент запускает сам** (Gradio API),
   звук + видео, без знака, коммерция разрешена. Минус: квота 1–3 клипа в день, качество и липсинк ниже Veo. Годится для фоновых
   кадров и «тихих» планов дневника; речь лучше накладывать отдельной озвучкой.
4. **Google Flow (50 кредитов в день)** — лучшее качество речи и липсинка (Veo 3.1), опорные картинки персонажа, вертикаль.
   **Но на free — видимый знак «Veo»**: подходит для черновиков и раскадровки. В публикацию — только если подтвердится выключение знака.
   Срезать знак не стоит: это может нарушать правила Google.
5. **Adobe Firefly (бесплатные генерации в день)** — коммерция разрешена, знак — C2PA. Уверенность низкая: проверить вживую,
   есть ли видимый знак на видео и сколько генераций дают.

**Не подходят:** Bing/Sora 2 (видимый знак, скорее некоммерческое использование, не работает в РФ), Runway, Luma, Pika, HeyGen, Synthesia, D-ID,
Captions, Krea, LTX Studio (знак и/или запрет коммерции на free), Sora и Nova Reel (закрыты). Gemini API — платный (наш fal и так платный).

## Источники

**Google**
- Gemini Omni в Vids, бесплатно: https://blog.google/products-and-platforms/products/workspace/gemini-omni-in-google-vids/ ·
  https://www.techrepublic.com/article/news-google-vids-free-ai-video-generation-limits/ · https://www.unite.ai/google-brings-free-gemini-omni-1-1-video-generation-to-google-vids/ ·
  https://decrypt.co/379353/google-free-1080p-ai-video-generation · https://www.androidauthority.com/google-vids-omni-flash-lite-3714767/ ·
  https://pro.edgex.exchange/en-US/news/article/google-gemini-omni-video-generation-free-vids · https://projedefteri.com/en/blog/is-google-vids-free/ ·
  https://incrypted.com/en/guide-gemini-omni-google-vids/ · https://9to5google.com/2026/06/17/google-vids-ai-avatars-free/ ·
  https://workspaceupdates.googleblog.com/2026/07/cast-yourself-in-ai-video-clips-using-your-personal-avatar-with-Gemini-Omni-in-Vids.html
- Omni в Shorts и YouTube Create: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/ ·
  https://findskill.ai/blog/gemini-omni-youtube-shorts-tutorial/ · https://wavespeed.ai/blog/posts/gemini-omni-flash-shipped-what-actually-launched/ ·
  https://www.michydev.com/gemini-omni-flash-youtube-create/
- Veo 3 Fast в Shorts (2025): https://blog.youtube/news-and-events/generative-ai-creation-tools-made-on-youtube-2025/ ·
  https://chromeunboxed.com/youtube-is-getting-powerful-new-ai-tools-including-free-veo-3-video-generation-in-shorts/
- Вертикаль в Veo 3.1: https://techcrunch.com/2026/01/13/googles-update-for-veo-3-1-lets-users-create-vertical-videos-through-reference-images
- Flow — кредиты и знак: https://costgoat.com/pricing/google-flow · https://www.toolcolumn.com/pricing/google-flow-pricing ·
  https://whiskailabs.net/google-flow-veo-watermark-guide-2026/ · https://help.apiyi.com/en/veo-3-1-watermark-google-flow-video-generation-synthid-guide-en.html
- Gemini app, акция: https://www.androidauthority.com/free-gemini-omni-videos-3695658/ · https://apidog.com/blog/how-to-use-gemini-omni-for-free/
- API (без бесплатного уровня): https://www.eesel.ai/blog/gemini-omni-1-1-flash-pricing · https://www.cloudzero.com/blog/veo-3-pricing/
- Студенты: https://geekflare.com/news/google-is-offering-its-ai-pro-plan-free-for-students

**OpenAI / Microsoft**
- Закрытие Sora: https://en.wikipedia.org/wiki/Sora_(text-to-video_model)
- Bing Video Creator на Sora 2: https://www.neowin.net/news/bing-video-creator-is-now-powered-by-openais-sora-2/ ·
  https://www.techloy.com/microsoft-bing-now-features-a-free-sora-powered-ai-video-generator/ ·
  https://alternativeto.net/news/2025/6/bing-video-creator-adds-free-ai-video-generation-via-sora-to-its-mobile-app ·
  https://www.bing.com/new/termsofuseimagecreator · https://learn.microsoft.com/en-us/answers/questions/2346822/commercial-use-of-images-generated-using-copilot-b

**Meta / Adobe / Amazon / Canva**
- Meta: https://futurefactors.ai/meta-vibes-ai-video-content-marketing-guide/ · https://felloai.com/meta-ai-video-generator/ · https://www.inro.social/blog/edits-new-meta-app
- Adobe: https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html · https://zsky.ai/blog/is-adobe-firefly-free
- Amazon: https://docs.aws.eu/bedrock/latest/userguide/model-card-amazon-nova-reel.html
- Canva: https://morphed.app/blog/canva-ai-video-maker · https://fluxnote.io/guides/canva-ai-video-generator-review

**Lightricks / Hugging Face**
- https://en.wikipedia.org/wiki/LTX-2 · https://huggingface.co/spaces/Lightricks/LTX-2-3 ·
  https://static.lightricks.com/legal/ltx-2-open-weights-license-0.X.pdf · https://scancode-licensedb.aboutcode.org/ltx-2-cla-2026.html ·
  https://vidmuse.ai/blog/ltx-studio-review · https://huggingface.co/docs/hub/spaces-zerogpu.md ·
  https://discuss.huggingface.co/t/what-is-the-free-zerogpu-quota-for-1-space/178610

**Остальные**
- Runway: https://creatify.ai/blog/runway-pricing-(2026)-plans-credits-and-what-you-ll-actually-pay
- Luma: https://lumalabs.ai/learning-hub/licensing · https://academy.techpresso.co/reviews/is-luma-dream-machine-worth-it
- Pika: https://eesel.ai/blog/pika-ai-pricing · https://magichour.ai/blog/pika-labs-pricing
- HeyGen: https://www.arcade.software/post/heygen-pricing · https://marcandrews.com/heygen-free-plan-review-2026-what-you-get-without-paying/
- Synthesia / D-ID: https://marcandrews.com/synthesia-free-plan-2026-review-what-you-get-before-paying/ · https://www.argil.ai/blog/d-id-pricing-5be73
- Captions: https://www.hooked.so/compare/captions-ai-pricing
- Krea / Ideogram: https://costbench.com/software/ai-design-tools/krea-ai/free-plan/ · https://www.krea.ai/blog/what-is-ideogram-ai-features-pricing-and-alternatives-in-2026
- Stability: https://metavert.io/compare/runway-vs-stability-ai
