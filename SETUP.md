# Настройка компании — пошагово

Около часа. Делай по порядку. Шаги 1–4 обязательные, без них компания не запустится.
Шаги 5–7 можно сделать позже: компания будет работать, просто без статистики и автопубликации.

## Как добавить «секрет»

Секрет — это ключ доступа, который видят только твои рабочие процессы на GitHub.
Его не видно в коде, и никто, кто смотрит репозиторий, его не узнает.

1. Открой https://github.com/Populity/AI-company/settings/secrets/actions
2. Нажми **New repository secret**.
3. В поле **Name** впиши имя (например `FAL_KEY`), в поле **Secret** вставь значение.
4. Нажми **Add secret**.

Дальше в инструкции «добавь секрет `ИМЯ`» означает именно это.

---

## Шаг 1. Офис (2 минуты)

1. Открой https://github.com/Populity/AI-company/settings/pages
2. В разделе **Build and deployment**: Source — **Deploy from a branch**, Branch — **main**, папка — **/docs**.
   Нажми **Save**. Если там уже стоит `main` и `/docs` — ничего не меняй.
3. Через 1–2 минуты офис откроется по адресу https://populity.github.io/AI-company/
   Пока компания не начала работу, там показывается демонстрация.

Добавь ссылку на офис на главный экран телефона: в браузере «Поделиться» → «На экран Домой».

## Шаг 2. Мозг компании — Claude (10 минут)

Директор и сотрудники работают на твоей подписке Claude Pro. Нужно один раз получить ключ.

1. Установи **Git для Windows**: https://git-scm.com/download/win → скачай, установи со всеми
   настройками по умолчанию (Next → Next → Install).
2. Нажми **Пуск**, набери `PowerShell`, открой **Windows PowerShell**.
3. Вставь команду и нажми Enter:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
4. Закрой PowerShell и открой заново. Вставь:
   ```
   claude setup-token
   ```
5. Откроется браузер — войди в тот аккаунт Claude, где у тебя Pro, и разреши доступ.
6. В PowerShell появится длинный ключ, который начинается на `sk-ant-oat01-`. Выдели его и скопируй
   (правой кнопкой мыши или Ctrl+C).
7. Добавь секрет `CLAUDE_CODE_OAUTH_TOKEN` с этим ключом.

Ключ действует долго (около года). Когда истечёт, повтори шаги 4–7.

## Шаг 3. Генерация видео — fal.ai (5 минут)

Через fal.ai компания делает картинки и видео со звуком. Это единственное место, куда уходят деньги.

1. Открой https://fal.ai и зарегистрируйся (кнопка **Sign up**, удобно через Google или GitHub).
2. Пополни баланс: **Billing** → **Add credits** → начни с $10.
3. Создай ключ: **API Keys** (https://fal.ai/dashboard/keys) → **Add key** → любое имя → **Create**.
   Скопируй ключ сразу — второй раз его не покажут.
4. Добавь секрет `FAL_KEY`.

Компания сама не потратит больше лимита из `config/company.json` (2 000 ₽ ≈ $22 в месяц):
каждая генерация сначала проверяет бюджет. Пополнять fal.ai нужно только тебе — агенты этого не умеют.

## Шаг 4. Связь с тобой — Telegram-бот (5 минут)

1. В Telegram найди **@BotFather** → **Start** → отправь `/newbot`.
2. Придумай имя (например «Моя AI-компания») и адрес бота — латиницей, в конце `bot`
   (например `my_ai_company_bot`).
3. BotFather пришлёт токен вида `1234567890:AA...`. Добавь секрет `TELEGRAM_BOT_TOKEN`.
4. Найди **@userinfobot** → **Start**. Он пришлёт твой **Id** (число). Добавь секрет `TELEGRAM_OWNER_ID`.
5. Найди своего нового бота и нажми **Start** — иначе он не сможет тебе писать.

## Шаг 5. YouTube (20 минут, можно позже)

Без этого шага ролики всё равно будут приходить тебе для ручной загрузки, но директор не увидит
статистику YouTube.

**5.1. Канал.** На https://youtube.com нажми на аватар → **Создать канал**. Название потом поменяешь
на то, что предложит директор.

**5.2. Проект в Google Cloud.**
1. Открой https://console.cloud.google.com → вверху выбор проекта → **New project** → имя `ai-company` → **Create**.
2. Открой https://console.cloud.google.com/apis/library/youtube.googleapis.com → **Enable**.
3. Открой https://console.cloud.google.com/auth/overview → **Get started**:
   имя приложения `AI Company`, твой email, тип аудитории **External**, контакт — твой email → **Create**.
4. Слева **Audience** → **Publish app** → **Confirm**. Статус должен стать **In production**.
   Это важно: в режиме Testing ключ перестаёт работать через 7 дней.

**5.3. Ключи приложения.**
1. Слева **Clients** → **Create client** → тип **Web application**.
2. В **Authorized redirect URIs** нажми **Add URI** и вставь `https://developers.google.com/oauthplayground` → **Create**.
3. Скопируй **Client ID** → секрет `YOUTUBE_CLIENT_ID`, **Client secret** → секрет `YOUTUBE_CLIENT_SECRET`.

**5.4. Доступ к каналу.**
1. Открой https://developers.google.com/oauthplayground
2. Справа вверху шестерёнка ⚙ → галочка **Use your own OAuth credentials** → вставь Client ID и Client secret.
3. Слева внизу в поле **Input your own scopes** вставь:
   ```
   https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.readonly
   ```
   → **Authorize APIs**.
4. Выбери Google-аккаунт с каналом. Google предупредит, что приложение не проверено, — это твоё же
   приложение: **Дополнительно** → **Перейти на страницу AI Company** → **Продолжить**.
5. Нажми **Exchange authorization code for tokens**. Скопируй **Refresh token** → секрет `YOUTUBE_REFRESH_TOKEN`.

**5.5. Автопубликация в YouTube (по желанию).** Пока проект не прошёл проверку Google,
YouTube делает всё, что загружено через API, приватным. Поэтому компания работает в ручном режиме:
бот присылает тебе ролик, название и описание, а ты выкладываешь их в приложении YouTube.
Чтобы публикация шла сама, подай заявку на проверку: https://support.google.com/youtube/contact/yt_api_form
Проверка занимает несколько недель. Когда одобрят, напиши боту: «переключи YouTube на автозагрузку».

## Шаг 6. Instagram (15 минут, можно позже)

1. В приложении Instagram: **Настройки** → **Тип аккаунта и инструменты** →
   **Переключиться на профессиональный аккаунт** → **Автор**.
2. Открой https://developers.facebook.com/apps → **Create app** → в сценариях выбери
   **Manage messaging & content on Instagram** → дальше по шагам, тип **Business** → **Create app**.
3. В приложении слева **Instagram** → **API setup with Instagram login**.
4. В блоке **Generate access tokens** нажми **Add account** и войди в свой Instagram, разреши всё.
5. Нажми **Generate token** напротив аккаунта, скопируй токен → секрет `INSTAGRAM_ACCESS_TOKEN`.
   Число рядом с аккаунтом можешь добавить как секрет `INSTAGRAM_USER_ID` (необязательно).

Если кнопка Add account не срабатывает: слева **App roles** → **Roles** → **Add People** → **Instagram Tester** →
твой ник. Затем в Instagram: **Настройки** → **Сайты и приложения** → **Приглашения тестировщика** → принять.

## Шаг 7. Автопродление ключа Instagram (5 минут, необязательно)

Ключ Instagram живёт 60 дней. Компания продлевает его сама, но записать новый ключ в секреты
может только с этим разрешением. Без него раз в два месяца повторяй шаг 6.5.

1. Открой https://github.com/settings/personal-access-tokens/new
2. Имя `ai-company-secrets`, срок — максимальный.
3. **Repository access** → **Only select repositories** → `AI-company`.
4. **Permissions** → **Repository permissions** → **Secrets** → **Read and write**.
5. **Generate token** → скопируй → секрет `GH_PAT`.

---

## Проверка

1. Открой https://github.com/Populity/AI-company/actions/workflows/doctor.yml
2. **Run workflow** → **Run workflow**.
3. Через минуту бот пришлёт отчёт: ✅ — работает, ❌ — нужно доделать, ⚪ — необязательно.

## Первый рабочий день

1. Открой https://github.com/Populity/AI-company/actions/workflows/daily-cycle.yml
2. **Run workflow**. Для пробы без трат поставь галочку **Сухой прогон**. Для настоящей работы — без галочки.
3. Открой офис https://populity.github.io/AI-company/ и смотри: директор выберет нишу, придумает героя,
   нарисует его и, если хватит дневного бюджета, снимет пилотную серию.
4. Герой и план придут в Telegram.

Дальше компания работает сама каждый день в 09:17 по Москве.

## Если что-то пошло не так

- **Рабочий день упал** — бот пришлёт ссылку. Открой её: внизу красным будет причина.
  Чаще всего это пропущенный или неверный секрет — исправь и запусти снова.
- **Офис не открывается** — проверь шаг 1 и подожди пару минут.
- **Офис показывает демонстрацию** — компания ещё не провела ни одного рабочего дня.
- **Бот молчит** — ты не нажал Start у своего бота (шаг 4.5), или неверный `TELEGRAM_OWNER_ID`.
- **Ошибка `invalid_grant` у YouTube** — приложение в Google осталось в режиме Testing (шаг 5.2.4).
  Переведи в In production и получи новый refresh token (шаг 5.4).
- Остановить всё: напиши боту `/pause`. Продолжить: `/resume`.
