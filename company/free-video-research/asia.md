# Бесплатные ИИ-видеогенераторы из Азии (Китай, Япония, Корея)

Дата исследования: 23.10.2026. Отдел трендов (trend-scout).
Метод: только поисковая выдача (WebSearch). Официальные страницы открыть не удалось (WebFetch не работает),
поэтому почти все цифры взяты из сторонних обзоров, и источники часто расходятся.
Уверенность: **В** — высокая (подтверждает официальный сайт, пресс-релиз или репозиторий),
**С** — средняя (несколько обзоров сходятся), **Н** — низкая (один источник или противоречия).
Ничего не регистрировали и не оплачивали.

## Главный вывод

1. **У всех крупных азиатских сервисов бесплатный тариф даёт видео с видимым водяным знаком**, и почти везде он только
   для некоммерческого использования: Kling, Hailuo, Vidu, PixVerse, Dreamina/Jimeng, Doubao, Vidnoz, DeepBrain, Perso, Kakao.
   Наш канал монетизируется, это коммерческое использование, поэтому выкладывать ролики с бесплатных тарифов нельзя.
2. **Китайские приложения для внутреннего рынка** (Jimeng, Doubao, Qwen, Yuanbao, Qingying, Huixiang) с 01.09.2025 по закону
   обязаны ставить видимую метку «ИИ» при скачивании (《人工智能生成合成内容标识办法》) (В). Кроме того, для регистрации обычно
   нужен китайский номер телефона (С).
3. **Без водяного знака и бесплатно** реально получить видео только двумя способами:
   - **открытые модели** (MIT или Apache) через бесплатные демо на Hugging Face (ZeroGPU): у таких демо есть дневной лимит GPU,
     но знака нет и коммерческое использование разрешено;
   - отдельные сервисы, о которых **заявляют**, что знака нет (SkyReels, PixVerse по одному обзору), но это не проверено.
4. Японские и корейские компании в 2026 году **не дают бесплатного готового генератора с речью на английском**.
   Из Японии есть только открытая аниме-модель AnimeGen (без звука), из Кореи — сервисы аватаров с водяным знаком.

## Таблица

| Сервис (страна, компания) | Что бесплатно | Водяной знак на бесплатном | Коммерция на бесплатном | Звук и английская речь | Длина и формат 9:16 | API или MCP для агента | Китайский номер или VPN | Уверенность |
|---|---|---|---|---|---|---|---|---|
| **Kling 3.0 / O3** (Китай, Kuaishou) | ~66 кредитов в день, без переноса (≈2–6 коротких клипов) | **Видимый** (без знака только у подписчиков) | Нет | Да: родной звук и липсинк, английский поддерживается; липсинк на бесплатном не подтверждён | 5–10 с, вертикаль есть; разрешение на бесплатном 720p (по данным разных источников 540p–1080p) | Официальный MCP Kling (OAuth, тратит кредиты аккаунта), **он уже подключён в нашей сессии**; платное API | Нет, есть глобальный сайт | С |
| **Hailuo / MiniMax** (Китай; модели Hailuo 02, H3 = Hailuo 3.0) | Сейчас разовые ~150 кредитов при регистрации; в старых обзорах — ежедневные | **Видимый** | Нет | H3: родной стереозвук, 11 языков | 6–15 с, 720p на бесплатном | Официальный MiniMax MCP (по API-ключу, платно) | Нет | С |
| **MiniMax H3, открытые веса** (Китай) | Бесплатно, если запускать самим; веса H3-Base открыты (дата выхода спорная) | Нет | Лицензия ограничительная («community») | Да, родной звук | До 15 с, 2K только через API | ComfyUI, vLLM; на бесплатном Space не найден | Нет | Н |
| **Vidu Q2 / Q3** (Китай, Shengshu) | 40–80 кредитов в месяц (данные расходятся); бесплатный «Off-Peak» скорее только на тарифе за $99 | **Видимый**, в правом нижнем углу | Нет | Q3: звук и речь за один проход; качество диалогов спорное | 8 с бесплатно (16 с платно), 720p, 9:16 есть | Платное API (≈$0.07 за секунду); MCP не найден | Нет | С |
| **PixVerse V5/V6** (Китай, AISphere) | 90 кредитов при регистрации, плюс 30–60 в день | **Видимый** по большинству обзоров (один обзор пишет, что знака нет) | Нет | Звук и SFX есть, есть липсинк | 5–8 с, низкое разрешение, вертикаль есть | Официальный PixVerse MCP (по данным каталогов); платное API | Нет | С |
| **Dreamina** (ByteDance, глобальная версия, Seedance 2.0 / 2.5, OmniHuman-аватары) | **120 кредитов в день** (официальный FAQ, 09.2026); старая цифра — 225 | **Видимый** на бесплатном | Только личное использование | Seedance 2.5: звук вместе с картинкой; OmniHuman: говорящий аватар по фото и английскому аудио | Seedance 2.5 до 30 с (бета до 180 с); 9:16 есть | Официального бесплатного API нет; платно через fal или Atlas (≈$0.13 за секунду) | Нет | С |
| **Jimeng 即梦** (ByteDance, Китай) | 60–100 кредитов в день (≈2 клипа по 5 с), Seedance 2.0 / 2.5 | **Видимый** плюс обязательная метка ИИ по закону КНР | Официально разрешено по соглашению, но знак остаётся | Да | До 30 с | Только неофициальные обратные API по sessionid: **нельзя**, это риск бана и нарушение правил | **Китайский номер** | С |
| **Doubao 豆包** (ByteDance, Китай) | Бесплатная генерация видео в приложении (лимиты не опубликованы) | **Видимый**, в правом нижнем углу; убрать можно только платно | Неясно | Да (Seedance) | Короткие клипы | Volcano Engine API (платно, нужна китайская регистрация) | Китайский номер | С |
| **Qwen App + Wan 2.6 / 2.7** (Alibaba, Китай) | Бесплатно для всех пользователей Qwen App (с 12.2025, Wan 2.7 с 04.2026) | Не найдено; по закону КНР нужна видимая метка ИИ | Неясно | Да: синхронный звук, видео по голосу, «роли» | До 15 с, 1080p | Платное API Alibaba Cloud (Model Studio / 百炼) | Китайский номер (С) | Н |
| **create.wan.video** (Alibaba, глобальный сайт) | Бесплатный тариф с ежедневными кредитами за отметку | **Видимый** (скачивание без знака только платно) | Нет | Wan 2.6+ со звуком | До 15 с | Платное API | Нет | С |
| **Wan 2.2 S2V / Animate, открытые веса** (Alibaba) | Бесплатно (Apache 2.0); демо на HF Spaces | **Нет** | **Да** | Видео по голосу (S2V): липсинк по нашему аудио | ~5 с за запуск, 720p | gradio API на HF Space | Нет | С |
| **Tencent HunyuanVideo 1.5 / Yuanbao 元宝** (Китай) | Открытые веса (≈14 ГБ видеопамяти) и бесплатно в приложении Yuanbao | Yuanbao: не найдено (по закону нужна метка); у открытых весов знака нет | Лицензия Tencent; **исключает ЕС, Великобританию и Южную Корею** | Встроенной речи нет | 5–10 с | Свой запуск или HF | Yuanbao: китайский номер | С |
| **Baidu MuseSteamer 蒸汽机 / Huixiang 绘想** (Китай) | В 2025 году бесплатный бета-тест, «без знака, без лимита»; данных за 2026 год нет | В API параметр watermark по умолчанию выключен | Неясно | Есть версия со звуком | Вплоть до длинного видео | Qianfan API (платно, китайский аккаунт) | Китайский номер | Н |
| **Zhipu Qingying 清影 / CogVideoX** (Китай) | Бесплатно в Zhipu Qingyan (данные 2024 года); веса CogVideoX-2B под Apache 2.0 | Не найдено | 2B: да (Apache) | Нет | ~6 с | Платное API Zhipu | Китайский номер | Н |
| **SkyReels** (Китай/Сингапур, Skywork; SkyReels V3) | ~100 кредитов при регистрации; аватар 720p стоит 4 кредита за секунду (≈25 с) | **Нет, по 2 обзорам** (не проверено) | Неясно; права на коммерцию есть у платных тарифов | Говорящий аватар по фото и аудио (V3 A2V) | Вертикаль есть | Dev API (1 USD = 100 кредитов); открытые веса V3 (A2V-19B, тяжёлые) | Нет | Н |
| **Meituan LongCat-Video-Avatar 1.5** (Китай, Meituan) | Бесплатно: официальный демо-Space на HF (ZeroGPU) и веса | **Нет** | **Да (MIT)** | **Липсинк по нашему английскому аудио**, длинные ролики стабильны (по заявлению Meituan) | ~5 с за запуск в демо, локально длиннее | gradio API на Space, есть ComfyUI | Нет | В (репозиторий и Space) |
| **Vidnoz** (Гонконг) | ~3 минуты аватар-видео в день | **Видимый**, слева внизу, 720p | Нет | Английский TTS, аватары | Минуты | Платное API | Нет | С |
| **Haiper** (Великобритания, не Азия) | **Закрыт** в феврале 2025 года | — | — | — | — | — | — | С |
| **Япония: AIdeaLab AnimeGen** (основан на Wan 2.2) | Веса бесплатно (Apache 2.0, 13.07.2026), демо на HF Space, бета веб-сервиса (вход через Google) | У весов нет | **Да**, кроме запрещённых сценариев | **Нет звука** | Короткие аниме-клипы | HF Space | Нет | В |
| **Япония: NoLang** (Mavericks) | Бесплатный тариф, мало кредитов | **Видимый** | Спорно | Озвучка на 18–19 языках, но это слайд-видео, а не генерация сцены | До ~1 мин | — | Нет | С |
| **Япония: Sakana AI, rinna, CyberAgent, LY, PFN, Stability AI Japan, AI Picasso, Sony, NTT, SB Intuitions, Kotoba** | Публичного бесплатного text-to-video на 2026 год не найдено | — | — | — | — | — | — | С |
| **Корея: Kakao Kinema by Kanana** | Внутри KakaoTalk, только готовые шаблонные промпты; отдельное приложение Kanana закрыто | **Видимый** знак «kanana» (по корейскому закону об ИИ) | — | Нет | Короткие | Нет | Корейский аккаунт Kakao | С |
| **Корея: Naver HyperCLOVA X, LG EXAONE / K-EXAONE 2.0** | Это языковые модели, генерации видео нет (у Naver есть только Omni 8B без видеовыхода) | — | — | — | — | — | — | С |
| **Корея: DeepBrain AI Studios / Perso AI (ESTsoft)** | DeepBrain: ~3 видео до 1 минуты; Perso: 1 генерация | **Видимый** | Нет | Английские аватары и дубляж | Минуты | Платное API | Нет | С |
| **Корея: Twelve Labs, Krafton** | Twelve Labs делает модели для анализа видео (Marengo, Pegasus), не для генерации; у Krafton генератора видео не найдено | — | — | — | — | — | — | С |

## 5 лучших вариантов для нашего сериала (призрак-клерк, видеодневник на 30 с, английская речь)

Порядок выбран по трём критериям: можно ли публиковать (нет знака, разрешена коммерция), подходит ли под формат
«персонаж говорит в камеру», можно ли автоматизировать.

1. **LongCat-Video-Avatar 1.5 (Meituan, MIT), бесплатный Space на Hugging Face.** Даём кадр с призраком и английскую реплику,
   получаем липсинк без знака, коммерция разрешена. 30 с собираем из 6 кусков по ~5 с (`assemble.py`). Минусы: лимит ZeroGPU
   на бесплатном аккаунте HF, очередь, аккаунт HF должен завести собственник. Агент может вызывать демо через `gradio_client`.
2. **Wan 2.2 S2V (Alibaba, Apache 2.0) через HF Spaces.** Тот же сценарий «картинка плюс голос», запасной вариант к пункту 1.
   Подходит и для бессловесных вставок (призрак летит по офису).
3. **SkyReels (Skywork), аватар V3.** По двум обзорам знака на бесплатном нет; ~100 кредитов при регистрации ≈ 25 с аватара 720p.
   Нужно вручную проверить отсутствие знака и права на коммерцию. Регистрация — только собственник.
4. **Dreamina (Seedance 2.5 и OmniHuman) — только для проб.** 120 кредитов в день, клипы до 30 с со звуком, китайский номер
   не нужен, но знак видимый и использование только личное. Подходит для отработки промптов и превизуализации серий. Для публикации
   нужна подписка или платный API через наш `fal_gen.py`.
5. **Kling 3.0 — только для проб.** 66 кредитов в день, родная английская речь, MCP уже подключён к сессии. Знак и запрет коммерции
   на бесплатном, поэтому публиковать с бесплатного тарифа нельзя. Если собственник когда-нибудь возьмёт тариф Standard, это самый простой
   путь для агента (MCP).

Не рекомендуем: Jimeng, Doubao, Qwen App, Yuanbao и Huixiang (нужен китайский номер, метка ИИ обязательна по закону, неофициальные
API нарушают правила), Hunyuan (лицензия исключает ЕС, Великобританию и Корею), японские и корейские сервисы (нет английской
генерации сцен без знака). **Удалять водяные знаки сторонними «removers» нельзя:** это нарушает условия сервисов и наше правило
о честности.

## Источники

- Kling: [eesel](https://www.eesel.ai/blog/kling-ai-pricing), [aireiter](https://aireiter.com/blog/kling-ai-free-tier-2026), [crepal](https://crepal.ai/blog/aivideo/kling-ai-watermark/), [kling.ai lipsync](https://kling.ai/explore/lipsync_kling), [atlascloud Kling 3.0](https://www.atlascloud.ai/blog/tips/kling-3.0-review-features-pricing-ai-alternatives)
- Hailuo / MiniMax: [youraifinder (10.2026)](https://youraifinder.com/blog/hailuo-ai-free-plan-india-2026), [costbench](https://costbench.com/software/ai-video-generators/hailuo-ai/free-plan/), [atlascloud](https://www.atlascloud.ai/blog/guides/hailuo-ai-free-credits), [fal H3](https://fal.ai/minimax-h3), [Comfy H3](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui), [HF blog H3](https://huggingface.co/blog/ResterChed/minimax-h3-hailuo-3-0)
- Vidu: [flowith](https://flowith.io/blog/vidu-pricing-2026-free-vs-pro-vs-enterprise-cost/), [aitoolsbakery (08.2026)](https://aitoolsbakery.com/blog/vidu-pricing/), [costbench](https://costbench.com/software/ai-video-generators/vidu/free-plan/), [novita Q3](https://blogs.novita.ai/vidu-q3-pro-on-novita-ai)
- PixVerse: [atlascloud](https://www.atlascloud.ai/blog/guides/pixverse-ai-free), [aivario](https://aivario.com/tools/pixverse), [costbench](https://costbench.com/software/ai-video-generators/pixverse/)
- Dreamina / Seedance: [Dreamina FAQ](https://dreamina.capcut.com/ai-video/free-image-to-video-generator-credits-faq), [Seedance 2.5 launch](https://dreamina.capcut.com/resource/seedance-2-5-launch), [PR Newswire](https://www.prnewswire.com/news-releases/creating-longer-ai-videos-is-still-difficult-dreamina-the-tool-of-ai-video-maker-launches-seedance-2-5-with-30-second-generation-and-50-reference-inputs-302841251.html), [vmake](https://vmake.ai/blog/seedance-2-5-release), [mindstudio](https://www.mindstudio.ai/blog/seedance-2-runway-vs-dreamina-best-value), [OmniHuman](https://dreamina.capcut.com/resource/omnihuman-ai)
- Jimeng / Doubao: [jimeng Seedance 2.0](https://jimeng.jianying.com/tools/seedance-2-0), [acaiy](https://acaiy.cn/articles/Design%20%C3%97%20AI/%E5%8D%B3%E6%A2%A6Seedance/seedance-2.0-%E5%AE%8C%E5%85%A8%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C), [aitoollab](https://www.aitoollab.cn/articles/jimeng-ai-complete-guide-2026/), [cnblogs Doubao](https://www.cnblogs.com/xingtianxia/p/20136571)
- Закон КНР о маркировке: [PwC](https://www.pwccn.com/zh/tmt/method-identifying-synthetic-content-generated-ai-sep2025.pdf), [news.cn](https://www.news.cn/tech/20250319/a572ec4366f149c1b0b04a07ebf4931b/c.html)
- Wan / Qwen: [create.wan.video pricing](https://create.wan.video/pricing), [tooldirectory](https://tooldirectory.ai/tools/wan), [NBD, Qwen + Wan 2.6](https://www.nbd.com.cn/articles/2025-12-17/4184045.html), [Sohu, Wan 2.7](https://www.sohu.com/a/1005473126_408876), [runpod Wan 2.7 (веса не открыты)](https://www.runpod.io/articles/guides/wan-2-7-runpod)
- Hunyuan: [GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5), [chatforest (лицензия)](https://chatforest.com/reviews/hunyuanvideo-tencent-open-source-video-generation/), [aibase](https://news.aibase.com/news/22986)
- Baidu: [zhihu (2025)](https://zhuanlan.zhihu.com/p/1933441765232338444), [Qianfan API](https://cloud.baidu.com/doc/qianfan-api/s/Xme6ul5g4), [news.cn](http://www.news.cn/tech/20250822/18c2d24c42724e82a2e3f1902d0ea8a1/c.html)
- Zhipu: [ithome (2024)](https://www.ithome.com/0/784/379.htm), [vantaige](https://vantaige.io/ai-tool/cogvideox)
- SkyReels: [filmora](https://filmora.wondershare.com/video-editor-review/skyreels-review.html), [dev pricing](https://www.skyreels.ai/dev/pricing), [comparebestai](https://comparebestai.com/tools/skyreels-ai), [GitHub V3](https://github.com/SkyworkAI/SkyReels-V3)
- LongCat: [HF Space](https://huggingface.co/spaces/meituan-longcat/LongCat-Video-Avatar-1.5-Demo), [HF model](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar), [X Meituan](https://x.com/Meituan_LongCat/status/2000929976917615040)
- Vidnoz: [kjetilfuras](https://kjetilfuras.com/vidnoz-ai-review), [aivideopicks](https://aivideopicks.com/posts/vidnoz-review-2026.html)
- Haiper: [plisio](https://plisio.net/pl/ai/haiper-ai), [filmora](https://filmora.wondershare.fr/video-editor-review/haiper-ai-review.html)
- MCP: [json2video](https://json2video.com/claude-video/video-mcp-servers/), [revid](https://www.revid.ai/blog/best-video-mcp-servers)
- Япония: [AIdeaLab PR](https://prtimes.jp/main/html/rd/p/000000026.000084222.html), [ITmedia](https://www.itmedia.co.jp/aiplus/article/2607/13/2000000187/), [HF AnimeGen](https://huggingface.co/aidealab/AnimeGen-I2V), [NoLang (weel)](https://weel.co.jp/media/innovator/nolang/), [ai-hack (сравнение)](https://ai-hack.jp/articles/free-ai-video-generator)
- Корея: [Kakao Kinema (threads)](https://www.threads.com/@unclejobs.ai/post/DXqE_ctia4u), [itdaily (Kanana закрыт)](https://www.itdaily.kr/news/articleView.html?idxno=242367), [K-EXAONE 2.0](https://en.sedaily.com/finance/2026/08/01/lg-releases-koreas-largest-ai-model-k-exaone-20-as-open), [siftino DeepBrain](https://siftino.com/deepbrain-ai-studios-pricing/), [Perso](https://tooldirectory.ai/tools/perso-ai), [Twelve Labs](https://siliconangle.com/?p=774445)
