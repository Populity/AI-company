# SMM-пакет: сезон 1 «Still Clocked In» (30 серий, 23.10–21.11.2026)

Автор: publisher, 22.10.2026. Основа: `company/character/season-plan.md` (названия, время МСК, номера дней, CTA), `company/trends/audience-hook-model.md` (хуки, аудитория), `company/bizdev/season-1-money.md` (CTA и продукты). Карточки эпизодов не созданы: перед публикацией текст переносится в `youtube.title`, `youtube.description`, `instagram.caption`, `hashtags` соответствующей карточки, публикация только через `python tools/publish.py <id>` после одобрения. Все тексты ниже готовы к копированию, на английском.

## 1. Правила оформления канала

### Единая формула
- **Заголовок YouTube:** `<Episode title> | Day <N>`, где N с запятой-разделителем (Day 14,254). Заголовок ≤ 60 символов (проверено: максимум 49). Номер дня считается как `14 253 + (дата − 22.10.2026)`; в серии 30 счёт начинается заново: `Day 1`. Без капса, без обещаний, которых нет в серии.
- Серии арки называются `Form 27-B, Step N: ...`. Шаг 3 вышел под названием «Costume...» (серия 9), поэтому в её описании стоит «Form 27-B, Step 3», а в названии шага нет. Номер серии стоит в первой строке описания: «Season 1, Episode N of 30».
- **Описание YouTube:** строка с номером серии и сутью (1–2 предложения), вопрос зрителю, строка CTA (только в сериях 12, 18, 24, 30), строка «New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.», строка `AI-generated character. Original series.`
- **Подпись Instagram:** первая строка - хук (до 125 знаков, виден до «ещё»), вторая - «Day N of Walt's diary» + фраза, третья - вопрос, в конце 5–8 хэштегов с `#aigenerated`.
- **Хэштеги:** всегда `#StillClockedIn #OfficeGhost #OfficeHumor` + 1–3 по теме серии + `#aigenerated` (5–8 всего). Без `#fyp`, `#viral`, чужих брендов, названий чужих сериалов, имён реальных людей. Для YouTube хэштеги не нужны: теги задаются в карточке (базовый набор: office comedy, office humor, ghost, workplace comedy, 1987, ai generated character, short series, Still Clocked In).
- **Тематические запреты:** без выборов и политики (03.11), без упоминания Дня ветеранов (серия 20), без брендов (принтеры, кофемашины, календари - только общие слова), без обещаний продуктов, которых к дате нет (CTA-серии: если продукт не готов, строку CTA и первую фразу закреплённого комментария удалить).
- **Закреплённый комментарий:** публикует и закрепляет собственник вручную (устав, правило 3: агенты не комментируют). Текст готов; в комментариях вопрос другой по форме, чем в подписи (выбор из вариантов, он проще, чем «что думаете?»; это гипотеза, проверит аналитик).
- **Время публикации МСК** взято из плана: 19:00 до 31.10, с 01.11 - 20:00; вторники 27.10, 03.11, 10.11, 17.11 - тест слота 15:00. Даты 01.11 и позже: US-аудитория смещается на час, слот 20:00 это учитывает.

### Шапка и описание канала (English)

**YouTube, channel name:** `Still Clocked In`

**YouTube, channel description:**
```
Walt is an accountant who died at his desk in 1987 and never closed his timecard. He is still clocked in. Every day he records a new entry in a video diary about the modern office, and about one goal: getting Form 27-B approved, his first day off in 39 years.

Season 1: 30 entries, October 23 - November 21, 2026. Each one works on its own, but they add up.

Subscribe to follow Walt's diary.
AI-generated character. Original series.
```

**YouTube, playlist:** название `Season 1`, описание:
```
Season 1 of Still Clocked In: 30 diary entries, October 23 - November 21, 2026. Watch in order for the Form 27-B storyline, or jump in anywhere.
```
Добавлять каждую серию в плейлист при загрузке. Порядок - по возрастанию номера (старые сверху).

**Instagram, имя профиля:** `Still Clocked In`

**Instagram, био (≤ 150 знаков, 106):**
```
Office ghost since 1987. New diary entry daily. Filing for my first day off. AI-generated original series.
```
Ссылка в профиле: пока заглушка `[LINK PLACEHOLDER: owner adds]`. Менять на ссылку продукта только когда продукт готов: PDF - к 02.11, обои - к 09.11, стикеры - к 16.11 (по season-1-money).

### Инструкция собственнику (по-русски)

Точные названия пунктов в приложениях меняются от версии к версии: ниже то, что подтверждает поиск 22.10.2026, и то, в чём я не уверен. Ориентируйтесь на экран.

**YouTube: пометка «изменённый или синтетический контент» при загрузке** (официальная справка: https://support.google.com/youtube/answer/14328491). Пока канал в режиме `manual`, вы загружаете ролики сами, поэтому ставить пометку каждый раз нужно вам.
1. Откройте YouTube Studio (studio.youtube.com) с компьютера и нажмите «Создать» (Create), затем «Добавить видео» (Upload videos) и выберите файл.
2. На шаге «Информация» (Details) вставьте название и описание из этого файла.
3. Прокрутите вниз до блока «Изменённый контент» (в английском интерфейсе «Altered content»; в справке в других версиях встречается название «Altered or synthetic content», в одном стороннем описании он лежит в разделе «Атрибуты»). Ответьте «Да» на вопрос о реалистичном изменённом или синтетическом контенте.
4. В блоке «Плейлисты» выберите «Season 1», затем дальше до публикации.
5. Не уверен: показывает ли YouTube эту пометку для стилизованного призрака (формально правило относится к реалистичному контенту), но устав требует пометки, поэтому ставим «Да» всегда. Если пункт не нашли, пришлите скриншот экрана «Информация».

**Instagram: метка «AI-generated profile» (на весь аккаунт)**
1. В приложении Instagram откройте свой профиль и нажмите «Редактировать профиль» (Edit profile).
2. Найдите переключатель с названием «AI-generated profile» (раньше метка называлась «AI creator», так могут называться и в вашей версии) и включите его.
3. Не уверен: в каком именно разделе он лежит (в самом «Редактировании профиля» или в «Настройках и активности» > «Аккаунт»/«Профессиональный аккаунт»). Метка раскатывается постепенно, у вас её может ещё не быть. Если не нашли за 2–3 минуты, пришлите скриншот меню профиля, я не буду гадать. Без метки Instagram может ограничить показы профиля с ИИ-героем.

**Instagram: пометка на каждом Reels**
1. При публикации Reels на последнем экране (где подпись) найдите пункт «Label as made with AI» / «Label this content as made with AI» (по справке Instagram https://help.instagram.com/761121959519495 он называется так; в части версий он спрятан в «Расширенных настройках» > «Advanced settings»). Включите его.
2. Хэштег `#aigenerated` в подписи остаётся в любом случае.

**Закреплённый комментарий (Instagram и YouTube):** после публикации оставьте комментарий из пакета от имени канала и закрепите его. Instagram: нажмите и удерживайте комментарий (на iPhone - смахнуть влево) и выберите значок булавки. YouTube: в Studio или в приложении нажмите три точки у комментария и «Закрепить» (Pin). Точные жесты зависят от версии, если не получилось - пришлите скриншот.

## 2. Расписание и CTA на одном экране

| Неделя | Серии | Время МСК | CTA |
|---|---|---|---|
| Н1 | 1–7 (23–29.10) | 19:00 (вт 27.10, серия 5, тест 15:00) | нет |
| Н2 | 8–14 (30.10–05.11) | 19:00 до 31.10, затем 20:00 (вт 03.11, серия 12, тест 15:00) | серия 12 |
| Н3 | 15–21 (06–12.11) | 20:00 (вт 10.11, серия 19, тест 15:00) | серия 18 |
| Н4 | 22–28 (13–19.11) | 20:00 (вт 17.11, серия 26, тест 15:00) | серия 24 |
| Н5 | 29–30 (20–21.11) | 20:00 | серия 30 |

Проверки: не больше 1 ролика в день (устав); хуки первых строк подписи не повторяются; слово «meeting/email» в названии только в серии 1; в закреплённых комментариях нет личных данных; цифр о просмотрах и доходах в пакете нет.

## 3. Серии

### 1. 23.10.2026 (Fri), 19:00 MSK
Note: pilot, rewrite to diary format

**YouTube Shorts**
- Title (43): `This Meeting Could Be an Email | Day 14,254`
- Description:
```
Season 1, Episode 1 of 30. Walt found a video camera from 1987 in the supply closet and started a diary. Entry one: a meeting, and a plan to file for his first day off in 39 years.
What's the longest meeting you've ever survived?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Dead for 39 years, and this meeting could still be an email.
Day 14,254 of Walt's diary. Meet Walt: office ghost, video diarist, still clocked in.
What's the longest meeting you've ever survived?

#StillClockedIn #OfficeGhost #OfficeHumor #MeetingHumor #aigenerated
```
- Hashtags (5): #StillClockedIn #OfficeGhost #OfficeHumor #MeetingHumor #aigenerated
- Pinned comment (owner posts it): `Poll: a meeting that could have been an email, or an email that could have been a meeting? Which one is worse? Tomorrow: Priya wants to 'touch base.'`

### 2. 24.10.2026 (Sat), 19:00 MSK

**YouTube Shorts**
- Title (23): `Touch Base | Day 14,255`
- Description:
```
Season 1, Episode 2 of 30. Priya says she wants to touch base. Walt takes it literally and goes looking for the base of the lamp, the cabinet, the plant. Something under the cabinet is beeping.
Which office phrase should Walt translate next?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Priya wants to 'touch base.' Walt is on it.
Day 14,255 of Walt's diary. Jargon, translated by a man from 1987.
Which office phrase should Walt translate next?

#StillClockedIn #OfficeGhost #OfficeHumor #OfficeJargon #CorporateSpeak #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #OfficeJargon #CorporateSpeak #aigenerated
- Pinned comment (owner posts it): `Drop an office phrase you'd like Walt to take literally. Tomorrow: who is beeping under the cabinet?`

### 3. 25.10.2026 (Sun), 19:00 MSK

**YouTube Shorts**
- Title (45): `Form 27-B, Step 1: Find the Form | Day 14,256`
- Description:
```
Season 1, Episode 3 of 30. The beeping under the cabinet is Dot, and she's pushing a dusty form that went missing in 1991. It has three blanks: a boss's signature, the right ink, and a witness.
Would you sign Walt's form, no questions asked?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Ignore the paperclips. They float when Walt is hopeful.
Day 14,256 of Walt's diary. Form 27-B, Step 1: the day-off quest begins.
Would you sign Walt's form, no questions asked?

#StillClockedIn #OfficeGhost #OfficeHumor #Form27B #DayOffQuest #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Form27B #DayOffQuest #aigenerated
- Pinned comment (owner posts it): `Signature, ink or witness: which of the three blanks on Form 27-B would be hardest to get at your job? Tomorrow: Priya has been staring at a screen for six hours.`

### 4. 26.10.2026 (Mon), 19:00 MSK

**YouTube Shorts**
- Title (48): `Why Does Priya Talk to a Rectangle? | Day 14,257`
- Description:
```
Season 1, Episode 4 of 30. Walt watches a video call from the outside and has questions. A note on Priya's monitor hints at when his boss's boss signs things.
How many hours a day do you talk to a rectangle?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Why does Priya talk to a rectangle for six hours?
Day 14,257 of Walt's diary. Walt observes the video call. Politely. Since 1987.
How many hours a day do you talk to a rectangle?

#StillClockedIn #OfficeGhost #OfficeHumor #VideoCalls #RemoteWork #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #VideoCalls #RemoteWork #aigenerated
- Pinned comment (owner posts it): `Honest count: how many hours were you on video calls yesterday? 0-2, 3-5 or 6+? Tomorrow: the printer is thinking.`

### 5. 27.10.2026 (Tue), 15:00 MSK
Note: slot test 15:00 MSK

**YouTube Shorts**
- Title (36): `The Printer Is Thinking | Day 14,258`
- Description:
```
Season 1, Episode 5 of 30. Walt holds the door for a printer that is 'thinking' and praises it for printing one page. The page turns out to be a flyer for Friday's office party.
Does your office printer have a name?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Shh. He's thinking. Give him a minute.
Day 14,258 of Walt's diary. Some printers need encouragement. Walt is patient.
Does your office printer have a name?

#StillClockedIn #OfficeGhost #OfficeHumor #PrinterProblems #aigenerated
```
- Hashtags (5): #StillClockedIn #OfficeGhost #OfficeHumor #PrinterProblems #aigenerated
- Pinned comment (owner posts it): `Tell us your office printer's name (or what you call it when nobody's listening). Tomorrow: Walt inspects the party preparations.`

### 6. 28.10.2026 (Wed), 19:00 MSK

**YouTube Shorts**
- Title (35): `Halloween: 1987 vs Now | Day 14,259`
- Description:
```
Season 1, Episode 6 of 30. 1987: one bowl of candy. Today: the candy has a committee. Walt inspects the party preparations and makes a plan to finally get close to Mr. Gable.
Candy bowl or committee: what does your office have?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Halloween, 1987: one bowl of candy. Today: a committee.
Day 14,259 of Walt's diary. Then vs Now, office Halloween edition.
Candy bowl or committee: what does your office have?

#StillClockedIn #OfficeGhost #OfficeHumor #Halloween #ThenVsNow #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Halloween #ThenVsNow #aigenerated
- Pinned comment (owner posts it): `Bowl or committee? Reply 'bowl' or 'committee.' Tomorrow: Walt slides a form under a door.`

### 7. 29.10.2026 (Thu), 19:00 MSK

**YouTube Shorts**
- Title (45): `Form 27-B, Step 2: The Signature | Day 14,260`
- Description:
```
Season 1, Episode 7 of 30. Walt confesses in a whisper: he slid Form 27-B under Mr. Gable's door. It came back with a red smudge and a short reply about Halloween night. Everyone will be in costume.
What would you wear to ask your boss for a day off?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Don't tell Mr. Gable. Walt slid the form under his door.
Day 14,260 of Walt's diary. Form 27-B, Step 2: the signature.
What would you wear to ask your boss for a day off?

#StillClockedIn #OfficeGhost #OfficeHumor #Form27B #Halloween #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Form27B #Halloween #aigenerated
- Pinned comment (owner posts it): `Costume ideas for asking a boss for a day off? Walt is taking notes. Tomorrow: a coworker shows up dressed as a ghost.`

### 8. 30.10.2026 (Fri), 19:00 MSK

**YouTube Shorts**
- Title (38): `A Ghost Is Not a Bedsheet | Day 14,261`
- Description:
```
Season 1, Episode 8 of 30. A coworker comes to the party dressed as a ghost: a bedsheet with two holes. Walt explains what a ghost really is. (An unclosed timecard.)
What's the best office Halloween costume you've seen?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
He thinks a ghost is a bedsheet.
Day 14,261 of Walt's diary. A ghost would like a word about this costume.
What's the best office Halloween costume you've seen?

#StillClockedIn #OfficeGhost #OfficeHumor #Halloween #GhostComedy #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Halloween #GhostComedy #aigenerated
- Pinned comment (owner posts it): `Best office costume you've ever seen, in five words or fewer. Tomorrow: Walt needs a costume of his own.`

### 9. 31.10.2026 (Sat), 19:00 MSK
Note: key episode, 40 s, Halloween (Sat)

**YouTube Shorts**
- Title (49): `Costume: A Man Who Went Home on Time | Day 14,262`
- Description:
```
Season 1, Episode 9 of 30. Form 27-B, Step 3. Halloween night in an empty office. Walt's costume: a man who went home on time. He walks up to Mr. Gable's door. The stamp is waiting.
Where does Walt go next: up to the boss's boss, or down to HR?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Walt's Halloween costume: a man who went home on time.
Day 14,262 of Walt's diary. Happy Halloween from the office ghost.
Where does Walt go next: up to the boss's boss, or down to HR?

#StillClockedIn #OfficeGhost #OfficeHumor #Halloween #Form27B #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Halloween #Form27B #aigenerated
- Pinned comment (owner posts it): `Vote in one word: UP (the boss's boss) or DOWN (HR)? Tomorrow: Walt reads the fine print.`

### 10. 01.11.2026 (Sun), 20:00 MSK

**YouTube Shorts**
- Title (27): `The Extra Hour | Day 14,263`
- Description:
```
Season 1, Episode 10 of 30. The clocks went back in the US, so everyone got an extra hour. Walt spent his reading the fine print on Form 27-B and found a word he never noticed: appeal.
What did you do with your extra hour?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
You got an extra hour today. Walt gets one every day. It's called overtime.
Day 14,263 of Walt's diary. Clocks went back. Walt's did not.
What did you do with your extra hour?

#StillClockedIn #OfficeGhost #OfficeHumor #ClocksBack #DaylightSaving #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #ClocksBack #DaylightSaving #aigenerated
- Pinned comment (owner posts it): `Extra-hour poll: slept, scrolled or worked? Tomorrow: Walt waits for a letter. Patiently. Professionally.`

### 11. 02.11.2026 (Mon), 20:00 MSK

**YouTube Shorts**
- Title (36): `247 Unread: 1987 vs Now | Day 14,264`
- Description:
```
Season 1, Episode 11 of 30. 1987: a rejection letter lands in the in-tray within the hour. Today: 247 unread emails and none from Mr. Gable. Walt says nothing. Almost nothing.
Be honest: how many unread emails do you have right now?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Walt waits for a reply. The counter says 247.
Day 14,264 of Walt's diary. Then vs Now: waiting for a letter.
Be honest: how many unread emails do you have right now?

#StillClockedIn #OfficeGhost #OfficeHumor #EmailOverload #ThenVsNow #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #EmailOverload #ThenVsNow #aigenerated
- Pinned comment (owner posts it): `Your unread count right now? Walt is not judging. He is noting. Tomorrow: a form for going over his boss's head.`

### 12. 03.11.2026 (Tue), 15:00 MSK
Note: CTA (PDF templates), slot test 15:00 MSK. If the PDF is not ready: delete the CTA line and the first sentence of the pinned comment

**YouTube Shorts**
- Title (45): `Form 27-B, Step 4: Over His Head | Day 14,265`
- Description:
```
Season 1, Episode 12 of 30. Of course there's a form for going over your boss's head. Walt finds it in the same closet where he found the camera, and he turned it into a template for you.
Which office form should Walt turn into a template next?
Ghost-Approved Office Templates: [LINK PLACEHOLDER: link in profile, owner adds the link once the PDF is ready]
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Of course there's a form for going over his boss's head.
Day 14,265 of Walt's diary. Walt found the appeal form. You can get the template too.
Which office form should Walt turn into a template next?

#StillClockedIn #OfficeGhost #OfficeHumor #Form27B #OfficeTemplates #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Form27B #OfficeTemplates #aigenerated
- Pinned comment (owner posts it): `The Form 27-B template is linked in our profile. Which form would you steal from the supply closet? Tomorrow: the appeals office says it will 'circle back.'`

### 13. 04.11.2026 (Wed), 20:00 MSK

**YouTube Shorts**
- Title (24): `Circle Back | Day 14,266`
- Description:
```
Season 1, Episode 13 of 30. The appeals office will 'circle back.' Walt walks a full circle and ends up exactly where he started. In 1987 someone told him the same thing.
What's the longest you've waited for someone to circle back?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Let's circle back, they said. In 1987.
Day 14,266 of Walt's diary. Walt circled back. Alone.
What's the longest you've waited for someone to circle back?

#StillClockedIn #OfficeGhost #OfficeHumor #OfficeJargon #CircleBack #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #OfficeJargon #CircleBack #aigenerated
- Pinned comment (owner posts it): `'Circle back' means: (a) soon, (b) eventually, (c) never. Which one? Walt voted already. Tomorrow: Priya is on a call. On mute.`

### 14. 05.11.2026 (Thu), 20:00 MSK

**YouTube Shorts**
- Title (27): `You're on Mute | Day 14,267`
- Description:
```
Season 1, Episode 14 of 30. Priya has been talking for four minutes. She's on mute. Walt knows that feeling well, so he presses the spacebar on her laptop. She stops and looks at his chair.
When was the last time you talked on mute?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
POV: she's been talking for four minutes. She's on mute.
Day 14,267 of Walt's diary. Walt has been on mute for 39 years.
When was the last time you talked on mute?

#StillClockedIn #OfficeGhost #OfficeHumor #OnMute #VideoCalls #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #OnMute #VideoCalls #aigenerated
- Pinned comment (owner posts it): `Mute stories go here. What's the longest you talked before somebody told you? Tomorrow: three copies, one printer.`

### 15. 06.11.2026 (Fri), 20:00 MSK
Note: key episode, 40 s

**YouTube Shorts**
- Title (41): `Form 27-B, Step 5: The Queue | Day 14,268`
- Description:
```
Season 1, Episode 15 of 30. An appeal needs three copies. The printer answers with a river of paper across the floor, thousands of pages from somebody else's queue. Dot clears a path.
How long would you wait in a queue for a day off?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
A river of paper is pouring out of the printer.
Day 14,268 of Walt's diary. Form 27-B, Step 5: three copies, one very long queue.
How long would you wait in a queue for a day off?

#StillClockedIn #OfficeGhost #OfficeHumor #Form27B #PrinterProblems #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Form27B #PrinterProblems #aigenerated
- Pinned comment (owner posts it): `What's the longest queue you've ever waited in? Walt's is 39 years. Tomorrow: Dot has a secret.`

### 16. 07.11.2026 (Sat), 20:00 MSK

**YouTube Shorts**
- Title (30): `Dot's Night Shift | Day 14,269`
- Description:
```
Season 1, Episode 16 of 30. Every night the office vacuum circles Walt's chair and beeps goodnight. Tonight she brings him an old pen from under the cabinet. Nobody else knows.
What would you name the office vacuum?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Don't tell Priya. Dot says goodnight to Walt every night.
Day 14,269 of Walt's diary. Some coworkers don't talk. They beep.
What would you name the office vacuum?

#StillClockedIn #OfficeGhost #OfficeHumor #RobotVacuum #OfficeFriends #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #RobotVacuum #OfficeFriends #aigenerated
- Pinned comment (owner posts it): `Name the office vacuum. (Dot is taken.) Tomorrow: a Sunday-night feeling, translated.`

### 17. 08.11.2026 (Sun), 20:00 MSK

**YouTube Shorts**
- Title (39): `Sunday Scaries, Translated | Day 14,270`
- Description:
```
Season 1, Episode 17 of 30. Walt translates the Sunday scaries for anyone who has never had a Monday that lasted 39 years. Then he rehearses tomorrow's filing out loud.
What time on Sunday does your dread start?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
What's a Sunday scary? Allow me.
Day 14,270 of Walt's diary. Jargon translator, Sunday edition.
What time on Sunday does your dread start?

#StillClockedIn #OfficeGhost #OfficeHumor #SundayScaries #JargonTranslator #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #SundayScaries #JargonTranslator #aigenerated
- Pinned comment (owner posts it): `Sunday dread starts at: noon, 6 pm, or 'when the weekend ends'? Tomorrow: a 'quick sync.' Bring snacks.`

### 18. 09.11.2026 (Mon), 20:00 MSK
Note: CTA (meeting checklist). If it is not ready: delete the CTA line and the first sentence of the pinned comment

**YouTube Shorts**
- Title (27): `The Quick Sync | Day 14,271`
- Description:
```
Season 1, Episode 18 of 30. A quick sync is a fifteen-minute lie. Walt sits through the hour-long version and spots something on the shared screen: an org chart with a box above Mr. Gable. He leaves you a three-question meeting checklist.
What's the longest 'quick sync' you've ever had?
Ghost-Approved meeting checklist: [LINK PLACEHOLDER: link in profile, owner adds the link once the checklist is ready]
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
A quick sync is a fifteen-minute lie.
Day 14,271 of Walt's diary. Walt sat through all of it so you don't have to.
What's the longest 'quick sync' you've ever had?

#StillClockedIn #OfficeGhost #OfficeHumor #MeetingHumor #QuickSync #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #MeetingHumor #QuickSync #aigenerated
- Pinned comment (owner posts it): `Walt's meeting checklist is linked in our profile. What's the longest 'quick sync' you've survived? Tomorrow: the appeal comes back.`

### 19. 10.11.2026 (Tue), 15:00 MSK
Note: slot test 15:00 MSK

**YouTube Shorts**
- Title (41): `Form 27-B, Step 6: Wrong Ink | Day 14,272`
- Description:
```
Season 1, Episode 19 of 30. The appeal came back: wrong shade of blue. Walt tries every pen in his pocket, and Dot's pen too. All of them are slightly wrong.
Blue or black: which ink deserves a day off?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
When the form needs one exact ink and all your pens are slightly wrong.
Day 14,272 of Walt's diary. Form 27-B, Step 6: it is always the ink.
Blue or black: which ink deserves a day off?

#StillClockedIn #OfficeGhost #OfficeHumor #Form27B #DayOffQuest #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Form27B #DayOffQuest #aigenerated
- Pinned comment (owner posts it): `Blue or black? Settle it in the comments. Tomorrow: Walt needs coffee and a plan.`

### 20. 11.11.2026 (Wed), 20:00 MSK
Note: neutral episode, Veterans Day: do not mention it

**YouTube Shorts**
- Title (47): `The Coffee Machine Wants an Update | Day 14,273`
- Description:
```
Season 1, Episode 20 of 30. Night in the office. The coffee machine wants to install an update before it will make coffee. In 1987 Walt had a pot and a refill. He waits, and he thinks about where to go next.
What does your coffee machine do when you're in a hurry?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
I don't need an update. I need a refill.
Day 14,273 of Walt's diary. Then vs Now: coffee edition.
What does your coffee machine do when you're in a hurry?

#StillClockedIn #OfficeGhost #OfficeHumor #OfficeCoffee #ThenVsNow #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #OfficeCoffee #ThenVsNow #aigenerated
- Pinned comment (owner posts it): `Your coffee order, no brand names: black, with milk, or 'whatever is in the pot'? Tomorrow: Walt goes to the archive.`

### 21. 12.11.2026 (Thu), 20:00 MSK

**YouTube Shorts**
- Title (22): `Deep Dive | Day 14,274`
- Description:
```
Season 1, Episode 21 of 30. Priya says 'let's deep dive.' Walt understands it literally and sinks through the floor into the archive. Down there he finds an instruction nobody was meant to find.
Which phrase should Walt take literally next: 'drill down' or 'low-hanging fruit'?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
A deep dive. Understood.
Day 14,274 of Walt's diary. Walt takes jargon literally. The floor takes it personally.
Which phrase should Walt take literally next: 'drill down' or 'low-hanging fruit'?

#StillClockedIn #OfficeGhost #OfficeHumor #OfficeJargon #JargonTranslator #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #OfficeJargon #JargonTranslator #aigenerated
- Pinned comment (owner posts it): `Vote: 'drill down' or 'low-hanging fruit'? Tomorrow is Friday the 13th, and the building has an unexpected floor.`

### 22. 13.11.2026 (Fri), 20:00 MSK
Note: key episode, 40 s, Friday the 13th

**YouTube Shorts**
- Title (46): `Form 27-B, Step 7: Floor Thirteen | Day 14,275`
- Description:
```
Season 1, Episode 22 of 30. The building has twelve floors. Today the elevator shows a thirteenth. Walt presses it. The registry office is open, and it names its conditions: three stamps and a witness who has seen him work.
Would you press the button?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
The building has twelve floors. Today it has thirteen.
Day 14,275 of Walt's diary. Form 27-B, Step 7: Friday the 13th at the office.
Would you press the button?

#StillClockedIn #OfficeGhost #OfficeHumor #Friday13th #Form27B #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Friday13th #Form27B #aigenerated
- Pinned comment (owner posts it): `Press the button or skip it? Yes or no. Tomorrow: Walt wonders who has actually seen him work.`

### 23. 14.11.2026 (Sat), 20:00 MSK
Note: silent gag

**YouTube Shorts**
- Title (29): `The Chair Squeak | Day 14,276`
- Description:
```
Season 1, Episode 23 of 30. No words this time. An empty chair squeaks. Priya freezes. After a long moment she puts a paperclip on the edge of Walt's desk.
Who at your work actually notices you?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Priya hears an empty chair squeak. Nobody says a word.
Day 14,276 of Walt's diary. A quiet one. Turn the sound up.
Who at your work actually notices you?

#StillClockedIn #OfficeGhost #OfficeHumor #SilentComedy #OfficeLife #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #SilentComedy #OfficeLife #aigenerated
- Pinned comment (owner posts it): `No dialogue today. What do you think Priya heard? Tomorrow: Walt wonders whether she could be his witness.`

### 24. 15.11.2026 (Sun), 20:00 MSK
Note: CTA (wallpapers/stickers, only what is ready). If nothing is ready: delete the CTA line and the first sentence of the pinned comment

**YouTube Shorts**
- Title (32): `Name Tag vs Sticker | Day 14,277`
- Description:
```
Season 1, Episode 24 of 30. 1987: a name tag on your pocket. Today: stickers on your laptop. Priya's laptop has a paperclip sticker, and Walt shows you his own.
What sticker is on your laptop?
'I'm still clocked in' wallpapers / stickers: [LINK PLACEHOLDER: link in profile. Per season-1-money the wallpapers are due 09.11 and stickers 16.11: link only what is ready]
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
1987: a name tag. Today: stickers.
Day 14,277 of Walt's diary. Walt would like to see your laptop.
What sticker is on your laptop?

#StillClockedIn #OfficeGhost #OfficeHumor #LaptopStickers #ThenVsNow #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #LaptopStickers #ThenVsNow #aigenerated
- Pinned comment (owner posts it): `Walt's 'I'm still clocked in' wallpapers and stickers are linked in our profile. Describe the sticker on your laptop. Tomorrow: three stamps.`

### 25. 16.11.2026 (Mon), 20:00 MSK

**YouTube Shorts**
- Title (44): `Form 27-B, Step 8: Three Stamps | Day 14,278`
- Description:
```
Season 1, Episode 25 of 30. To get past the registry, the form needs three stamps: Facilities, Compliance, Payroll. Walt walks from desk to desk with a paperclip in his hand.
Which desk should Walt visit first: Facilities, Compliance or Payroll?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
How many stamps does it take to leave a building?
Day 14,278 of Walt's diary. Form 27-B, Step 8: three desks, three stamps.
Which desk should Walt visit first: Facilities, Compliance or Payroll?

#StillClockedIn #OfficeGhost #OfficeHumor #Form27B #Bureaucracy #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Form27B #Bureaucracy #aigenerated
- Pinned comment (owner posts it): `Facilities, Compliance or Payroll first? Pick one. Tomorrow: Payroll gives Walt an answer he knows very well.`

### 26. 17.11.2026 (Tue), 15:00 MSK
Note: slot test 15:00 MSK

**YouTube Shorts**
- Title (29): `Per My Last Memo | Day 14,279`
- Description:
```
Season 1, Episode 26 of 30. Payroll won't stamp anything until a timecard from 1987 is closed. The answer starts with 'per my last memo,' a phrase Walt says he invented. He would like credit.
What's the most passive-aggressive phrase you've heard at work?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Walt invented 'per my last memo.' In 1987.
Day 14,279 of Walt's diary. The original passive-aggressive office phrase, explained by its author.
What's the most passive-aggressive phrase you've heard at work?

#StillClockedIn #OfficeGhost #OfficeHumor #PassiveAggressive #OfficeJargon #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #PassiveAggressive #OfficeJargon #aigenerated
- Pinned comment (owner posts it): `Rank them: 'per my last email,' 'as discussed,' 'friendly reminder.' Which hurts most? Tomorrow: the form has an expiry date.`

### 27. 18.11.2026 (Wed), 20:00 MSK

**YouTube Shorts**
- Title (48): `Form 27-B, Step 9: Expires Saturday | Day 14,280`
- Description:
```
Season 1, Episode 27 of 30. Fourteen thousand days of waiting, and the form expires in three. Three stamps secured, no witness yet, and Mr. Gable isn't answering.
Will Walt make it in time? Yes or no?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
Fourteen thousand days. The form expires in three.
Day 14,280 of Walt's diary. Form 27-B, Step 9: the deadline is Saturday.
Will Walt make it in time? Yes or no?

#StillClockedIn #OfficeGhost #OfficeHumor #Deadline #Form27B #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Deadline #Form27B #aigenerated
- Pinned comment (owner posts it): `Yes or no: will Walt make it by Saturday midnight? Tomorrow: cake.`

### 28. 19.11.2026 (Thu), 20:00 MSK

**YouTube Shorts**
- Title (30): `The Farewell Cake | Day 14,281`
- Description:
```
Season 1, Episode 28 of 30. The whole office gathers for someone's last day. Walt hasn't had cake in 39 years. He quietly decides to leave something on Priya's desk before Friday.
Farewell cake: which is better, the cake or the leaving?
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
When the whole office gathers for someone's last day.
Day 14,281 of Walt's diary. Walt would like a slice. Just one.
Farewell cake: which is better, the cake or the leaving?

#StillClockedIn #OfficeGhost #OfficeHumor #FarewellCake #OfficeParty #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #FarewellCake #OfficeParty #aigenerated
- Pinned comment (owner posts it): `Be honest: the cake or the leaving? Tomorrow is Friday, and Walt's last real chance.`

### 29. 20.11.2026 (Fri), 20:00 MSK
Note: key episode, 40 s

**YouTube Shorts**
- Title (44): `Form 27-B, Step 10: Six Seconds | Day 14,282`
- Description:
```
Season 1, Episode 29 of 30. Priya finds something on her desk and starts to watch. Then she reaches for a pen in the exact blue Walt needed. Mr. Gable lifts the stamp and holds it. Don't blink.
Approved or denied? One word.
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
He's holding the stamp. Don't blink.
Day 14,282 of Walt's diary. Form 27-B, Step 10: six seconds.
Approved or denied? One word.

#StillClockedIn #OfficeGhost #OfficeHumor #Cliffhanger #Form27B #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #Cliffhanger #Form27B #aigenerated
- Pinned comment (owner posts it): `Approved or denied? One word. Tomorrow, same time: the season finale.`

### 30. 21.11.2026 (Sat), 20:00 MSK
Note: key episode, 40 s, finale, CTA (templates + thanks). If the PDF is not ready: delete the CTA line and the last sentence of the pinned comment

**YouTube Shorts**
- Title (35): `Form 27-B, Step 11: Day Off | Day 1`
- Description:
```
Season 1, Episode 30 of 30. The stamp lands. Walt closes his timecard and steps outside for the first time in 39 years. Thank you for 30 days with him. Dot has one more form.
Where should Walt go on his first day off?
Ghost-Approved Office Templates: [LINK PLACEHOLDER: link in profile, owner adds the link once the PDF is ready]
New entry every day. Subscribe to follow Walt's diary and the Form 27-B storyline.
AI-generated character. Original series.
```

**Instagram Reels**
- Caption:
```
The stamp lands. Walt walks out. Day one.
Season 1, finale. Season 1 finale. Thank you for 30 days.
Where should Walt go on his first day off?

#StillClockedIn #OfficeGhost #OfficeHumor #SeasonFinale #Form27B #aigenerated
```
- Hashtags (6): #StillClockedIn #OfficeGhost #OfficeHumor #SeasonFinale #Form27B #aigenerated
- Pinned comment (owner posts it): `Thank you for 30 days with Walt. Where should he spend his first day off? Follow to see what Dot is holding. Our templates are linked in our profile.`
