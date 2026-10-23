# Сезон 1 «Still Clocked In»: сценарии серий 11-20 (часть 2)

Автор: showrunner, 22.10.2026. Строго по `company/character/season-plan.md` (даты, номера дней, секунды, шаги арки). Серии 1-10 и 21-30 пишутся параллельно другими сценаристами; стыки: серия 11 начинается с последствий серии 10 (лишний час, нашёл слово «апелляция», ждёт письменного отказа), серия 20 заканчивается крючком «нужен архив, завтра спускаюсь вниз» (серия 21: Deep Dive). Карточки эпизодов не созданы.

Итого: 10 серий, 31 клип, 316 с видео. Оценка по ценам $0.055/с + $0.039/кадр: 316 x 0.055 + 31 x 0.039 = около $18.6 (без переделок).

## Общие правила и фиксированные строки

- Формат каждой серии: клип «у стола» (камера на штативе: номер дня голосом + хук) -> «ручная» съёмка (камера в вытянутой руке, Walt в кадре на переднем плане лицом к объективу, место происшествия за ним) -> снова у стола (панчлайн + крючок), щелчок часов/лампа, обрыв записи. Холодный старт серии 20 — у кофемашины.
- Номер дня произносится голосом и **входит** в подсчёт слов реплики (6-7 слов).
- Лимит речи: (duration - 1) с x 2.5 слова/с; 10 с -> до 22 слов, 11 с -> до 25 слов. Реплики написаны с запасом на паузы и шёпот.
- Говорит только Walt. Priya, Dot, Gable и люди на фоне звука не издают (Priya на муте: губы двигаются без звука; Dot только писк).
- В кадре нет текста и цифр: экраны, листы, схемы — пустые прямоугольники и линии; субтитры вшивает монтаж.
- Эталона героя (`ref_*.png`) в репозитории нет: продакшн без эталона невозможен, пока его не сгенерируют.

Фиксированные строки (вставлять в промпты дословно; у Priya, подчинённой APPEAL-формы и PEN в плане/библии описания нет, строки ниже введены этим файлом: если часть 1/3 даст другие, согласовать):

- **Walt (кадр):** the same man from the reference image (translucent ghost, faint cyan glow, toothbrush moustache, round horn-rimmed glasses with blue tape on the left temple, rust tie with tiny paperclips, mustard-brown 1987 suit)
- **Walt (движение):** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow).
- **Dot:** Dot, a round low charcoal-grey robot vacuum with a small blue indicator light
- **Mr. Gable:** Mr. Gable, a tall faceless silhouette of dark haze with round glasses and a dark tie
- **Видеокамера:** the old 1987 shoulder-mounted camcorder, massive black-and-grey with a carry handle
- **Форма 27-B:** Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top and an empty frame, no text
- **Форма апелляции (серии 12, 19):** the appeal form, a pale lemon-yellow sheet like Form 27-B but with a blue stripe across the top and an empty frame, no text
- **Priya:** Priya Nair, a woman of about 30 with dark shoulder-length hair, an olive cardigan and a wireless headset (blurred, seen from behind or in profile)
- **Ручка Dot (серии 16, 19):** an old stubby ballpoint pen with a faded blue cap
- **Стол Walt:** Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind
- **Стиль кадра:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away.

---

## Серия 11. 247 Unread: 1987 vs Now

- **№:** 11 | **Дата:** 02.11.2026 (Пн), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred sixty-four.
- **Формат:** Then vs Now | **Хук:** #10 немой гэг (после номера дня 7 с молчания) | **Секунды:** 30 (3x10) | **Сегмент ЦА:** A + B, вторично D (ностальгия по лотку для бумаг)
- **Элементы (≤2):** Скрепка | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: лишний час, в мелком шрифте нашёл слово «апелляция» -> Сегодня: ждёт письменного отказа, получает тишину -> Завтра: если отказ можно обжаловать, форма лежит в кладовке.
- **Подпись/обложка (≤7 слов):** 247 unread. Zero from the boss.
- **Вопрос зрителю:** Be honest: how many unread emails do you have right now?
- **Петля:** Классический щелчок часов + лампа; запись обрывается на поднятом взгляде в объектив.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, mouth closed, staring straight into the lens with patient dread. To the left, on the neighbouring empty desk, a modern flat monitor turned toward him shows a long list of blurred unread rows with a small blank red bubble in the corner. No paperclip on the desk yet.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: he stares unblinking into the lens. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred sixty-four." 3-8s: he says nothing; he slowly turns his head to the monitor where tiny envelope rows fill the list faster and faster and the red bubble swells; his eyes follow them. 8-10s: he lays one paperclip on the desk edge, perfectly straight, and slowly blinks at the lens. Camera: locked-off medium close-up, slow push-in. Audio: office hum, soft mail pings accelerating, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred sixty-four.
- **слов / секунд речи:** 6 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, Walt's face in the foreground half-turned to the lens, mouth closed, tired eyes. Beside him an empty old metal mesh wire in-tray on the desk corner; in the background the modern monitor on the neighbouring desk glows with a crowded inbox list.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he looks at the empty wire in-tray. 1-5s: he taps the tray and says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Nineteen eighty-seven: denials arrived in this tray. Today: two hundred forty-seven unread. None from the boss." 5-8s: the camera swings with him to the glowing monitor full of unread rows, he says the rest. 8-10s: he sighs, shoulders drop. Camera: handheld, slight shake, one quick pan from the tray to the monitor. Audio: office hum, soft pings, fabric rustle. No music, no on-screen text.
- **dialogue:** Nineteen eighty-seven: denials arrived in this tray. Today: two hundred forty-seven unread. None from the boss.
- **слов / секунд речи:** 16 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, composed and resigned, mouth closed, eyes into the lens; one paperclip lies straight on the desk edge; the modern monitor to the left is dark.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: slow blink at the lens. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Silence is also an answer. So I'll appeal the silence. Tomorrow: the supply closet. Noted." (a beat of silence before the last word). 9-10s: the lamp buzzes, still. Camera: locked-off medium close-up, slow push-in. Audio: office hum, lamp buzz, one soft keyboard click. No music, no on-screen text.
- **dialogue:** Silence is also an answer. So I'll appeal the silence. Tomorrow: the supply closet. Noted.
- **слов / секунд речи:** 15 / 9 (лимит 22)
- **end-frame (петля):** Walt at the desk looking into the lens, paperclip beside the keyboard, monitor dark, lamp glowing: same composition as clip 1, so the loop reads as the start.

Сумма: 30 с.

---

## Серия 12. Form 27-B, Step 4: Over His Head

- **№:** 12 | **Дата:** 03.11.2026 (Вт), публикация 15:00 МСК (тест слота) | **Day (голосом):** Day fourteen thousand two hundred sixty-five.
- **Формат:** Day Off Quest | **Хук:** #12 продолжение (с кладовки, сразу на форме) | **Секунды:** 33 (3x11) | **Сегмент ЦА:** A + C
- **Элементы (≤2):** Форма, Скрепка | **CTA:** да: бесплатно/платно PDF-шаблон формы, «copy in my profile» (если PDF не готов, см. запасную реплику)
- **Вчера -> сегодня -> завтра:** Вчера: ждал письма, отказа не пришло -> Сегодня: находит бланк апелляции в кладовке, делится копией -> Завтра: подаёт, канцелярия скажет «we'll circle back».
- **Подпись/обложка (≤7 слов):** There's a form for going higher.
- **Вопрос зрителю:** Which office form should Walt turn into a template next?
- **Петля:** Щелчок часов приглушён бумагой (форма накрывает объектив на долю секунды), лампа гудит.

### Клип 1 (11 с)

- **duration:** 11
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, holding the appeal form, a pale lemon-yellow sheet like Form 27-B but with a blue stripe across the top and an empty frame, no text up toward the lens with both hands like a small trophy, mouth closed, tired triumphant eyes. One paperclip rests on the desk beside the lamp.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: he holds the form up, eyes on the lens. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred sixty-five. Of course there's a form for going over his head." (the second sentence after a short pause). 9-11s: he lowers the form and looks slowly up at the ceiling; the paperclip rises from the desk and floats upward. Camera: locked-off medium close-up, slow push-in. Audio: office hum, faint paper crackle, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred sixty-five. Of course there's a form for going over his head.
- **слов / секунд речи:** 16 / 10 (лимит 25)

### Клип 2 (11 с)

- **duration:** 11
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, inside a narrow supply closet: Walt's face in the foreground, mouth closed, eyebrows raised; behind him metal shelves of dusty boxes and a mop; on one shelf a clean rectangular outline in the dust, the size of the old 1987 shoulder-mounted camcorder, massive black-and-grey with a carry handle; a bare bulb gives harsh light with warm film glow. A corner of the appeal form, a pale lemon-yellow sheet like Form 27-B but with a blue stripe across the top and an empty frame, no text sticks out from under a dead stapler on a lower shelf.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he squints at the shelf. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Found it in the supply closet, on the shelf beside where this camera sat. Thirty-nine years. One shelf." while pointing with his free hand at the dust outline, then at the lower shelf. 9-11s: he slides the appeal form out from under the stapler and holds it near the lens. Camera: handheld, slight shake, slow drift toward the shelf. Audio: closet hum, dust-soft rustle, paper slide. No music, no on-screen text.
- **dialogue:** Found it in the supply closet, on the shelf beside where this camera sat. Thirty-nine years. One shelf.
- **слов / секунд речи:** 18 / 10 (лимит 25)

### Клип 3 (11 с)

- **duration:** 11
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, smoothing the appeal form, a pale lemon-yellow sheet like Form 27-B but with a blue stripe across the top and an empty frame, no text flat on the desk blotter with one hand, mouth closed, looking into the lens; a paperclip beside the lamp.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he smooths the form flat. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "A blank copy is in my profile. Everyone deserves an appeal. Tomorrow I submit mine. They'll say they'll circle back." 9-11s: he pins the form with the paperclip and blinks slowly at the lens. Camera: locked-off medium close-up, slow push-in. Audio: office hum, paper smooth, lamp buzz. No music, no on-screen text.
- **dialogue:** A blank copy is in my profile. Everyone deserves an appeal. Tomorrow I submit mine. They'll say they'll circle back.
- **слов / секунд речи:** 20 / 10 (лимит 25)
- **end-frame (петля):** Walt at the desk, appeal form pinned with a paperclip, eyes into the lens; same composition as clip 1.
- **Запасной вариант CTA:** Запасная реплика без CTA, если PDF не готов (13 слов, остальное время тихая пауза): Everyone deserves an appeal. Tomorrow I submit mine. They'll say they'll circle back.

Сумма: 33 с.

---

## Серия 13. Circle Back

- **№:** 13 | **Дата:** 04.11.2026 (Ср), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred sixty-six.
- **Формат:** Jargon Translator | **Хук:** #4 буквализация жаргона (Walt ходит по кругу) | **Секунды:** 30 (3x10) | **Сегмент ЦА:** C + A
- **Элементы (≤2):** нет | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: нашёл бланк апелляции -> Сегодня: канцелярия сказала «we'll circle back», Walt обошёл этаж по кругу -> Завтра: нужно пронести бумаги мимо созвона Priya.
- **Подпись/обложка (≤7 слов):** Circle back: translated by Walt.
- **Вопрос зрителю:** What's the longest you've waited for someone to circle back?
- **Петля:** Классический щелчок с лёгким эхом пустого этажа.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, mouth closed, right index finger raised as if about to draw a circle in the air, patient look into the lens. In the soft-focus distance behind him a service hatch in a grey wall with a small bell on its counter and a roll-down shutter half open.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: he looks into the lens, finger raised. 0.3-7s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred sixty-six. Let's circle back, they said. In nineteen eighty-seven." 7-10s: he draws one slow circle in the air with his finger and lowers it. Camera: locked-off medium close-up, slow push-in. Audio: office hum, distant hatch bell ding, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred sixty-six. Let's circle back, they said. In nineteen eighty-seven.
- **слов / секунд речи:** 14 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, Walt's face in the foreground, mouth closed, mid-stride; behind him a long open-plan floor with grey partitions curving around a central concrete pillar, a service hatch with a closed shutter far behind, blurred coworkers.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he looks back at the hatch. 1-8s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "I submitted the form. They said, we'll circle back. So I did. One lap. Back already." while walking briskly one full circle around the pillar, the camera sweeping with him. 8-10s: he arrives back at the hatch, the shutter now fully closed; he taps the little bell once. Camera: handheld, slight shake, a sweeping circular walk. Audio: footsteps on carpet, office hum, one bell ding. No music, no on-screen text.
- **dialogue:** I submitted the form. They said, we'll circle back. So I did. One lap. Back already.
- **слов / секунд речи:** 16 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, hand resting on a stack of papers, resigned look into the lens, mouth closed.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: slow blink. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Translation: never, with a calendar invite. Tomorrow I deliver the papers past Priya's call. I'll tiptoe. Technically, I float." (dry beat before the last sentence). 9-10s: a small lamp flicker, he looks away. Camera: locked-off medium close-up, slow push-in. Audio: office hum, lamp buzz, distant phone ring. No music, no on-screen text.
- **dialogue:** Translation: never, with a calendar invite. Tomorrow I deliver the papers past Priya's call. I'll tiptoe. Technically, I float.
- **слов / секунд речи:** 19 / 9 (лимит 22)
- **end-frame (петля):** Walt at the desk, hand on the stack of papers, eyes into the lens; same composition as clip 1 (no finger raised).

Сумма: 30 с.

---

## Серия 14. You're on Mute

- **№:** 14 | **Дата:** 05.11.2026 (Чт), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred sixty-seven.
- **Формат:** Meeting Autopsy | **Хук:** #7 POV | **Секунды:** 30 (3x10) | **Сегмент ЦА:** B + A
- **Элементы (≤2):** Фраза («I'm still clocked in.»), Лампа | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: круг по этажу -> Сегодня: Priya говорит четыре минуты на муте, Walt нажимает пробел, она смотрит на его стул (нить Priya) -> Завтра: подача трёх копий.
- **Подпись/обложка (≤7 слов):** POV: she's talking. She's muted.
- **Вопрос зрителю:** When was the last time you talked on mute?
- **Петля:** Щелчок + мигание лампы от вздоха.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium shot, the same man from the reference image seated in the foreground at his corner desk, mouth closed, deadpan POV stare into the lens; in the blurred background behind him Priya Nair, a woman of about 30 with dark shoulder-length hair, an olive cardigan and a wireless headset (blurred, seen from behind or in profile) sits at her desk facing a glowing laptop, mouth open mid-sentence, hands gesturing.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: deadpan stare into the lens. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred sixty-seven. POV: she's been talking for four minutes. She's on mute." (second sentence as he glances back at Priya over his shoulder). Behind him Priya's lips move and her hands gesture, but she makes no sound at all. 8.5-10s: slow blink at the lens. Camera: locked-off medium shot, slow push-in. Audio: quiet office hum, soft keyboard clicks, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred sixty-seven. POV: she's been talking for four minutes. She's on mute.
- **слов / секунд речи:** 16 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, Walt's face in the foreground, mouth closed, wry; behind him Priya Nair, a woman of about 30 with dark shoulder-length hair, an olive cardigan and a wireless headset (blurred, seen from behind or in profile) at a laptop showing a grid of small blurred video tiles; his free long arm reaches back toward her keyboard.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he steps up behind Priya. 1-6s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Four minutes. I know that feeling. Thirty-nine years on mute. Allow me." 6-8s: his free hand taps the space bar once; a soft chime; Priya, still silent, stops mid-word and goes still. 8-10s: she slowly turns her head toward his empty chair across the room. Camera: handheld, slight shake, steadies as he reaches. Audio: office hum, soft key tap, one gentle chime. No music, no on-screen text.
- **dialogue:** Four minutes. I know that feeling. Thirty-nine years on mute. Allow me.
- **слов / секунд речи:** 12 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium shot at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image standing beside his empty swivel chair, one hand resting on its back, leaning toward the lens conspiratorially, mouth closed.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he glances at the empty chair, which turns a few degrees by itself. 1-9s: he says in a low hushed whisper, American voice, dry and polite: "She looked at my chair. Nobody has since nineteen eighty-seven. Tomorrow, three copies. I'm still clocked in." 9-10s: he sighs; the lamp flickers. Camera: locked-off medium shot, slow push-in. Audio: office hum, faint chair creak, lamp buzz. No music, no on-screen text.
- **dialogue:** She looked at my chair. Nobody has since nineteen eighty-seven. Tomorrow, three copies. I'm still clocked in.
- **слов / секунд речи:** 17 / 9 (лимит 22)
- **end-frame (петля):** Walt standing beside his empty chair, hand on it, eyes into the lens, lamp mid-flicker; similar to clip 1 composition (Priya blurred behind).

Сумма: 30 с.

---

## Серия 15. Form 27-B, Step 5: The Queue

- **№:** 15 | **Дата:** 06.11.2026 (Пт), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred sixty-eight.
- **Формат:** Day Off Quest | **Хук:** #3 визуальная странность (бумажная река) | **Секунды:** 40 (4x10), ключевая | **Сегмент ЦА:** A + D
- **Элементы (≤2):** Форма | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: Priya почти услышала -> Сегодня: апелляции нужны три копии, принтер заливает пол бумагой, Dot расчищает путь -> Завтра: у Dot для него сюрприз.
- **Подпись/обложка (≤7 слов):** The print queue has a river.
- **Вопрос зрителю:** How long would you wait in a queue for a day off?
- **Петля:** Щелчок + писк принтера вдали, Dot в нижнем углу кадра.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium shot at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, mouth closed, calm deadpan look into the lens; the grey carpet around his desk legs is covered by a shallow slow river of white paper sheets flowing in from the left, sheets overlapping and drifting like water, a few curling in the air; warm lamp light on the paper.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: calm stare into the lens as the paper river flows past his feet. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred sixty-eight. That's not a flood. That's the print queue. Mine is in there." (the rest after a short pause). 8-10s: one sheet floats up and lands on his lap; he looks down at it, then back to the lens. Camera: locked-off medium shot, slow push-in. Audio: paper rustling like running water, distant printer whir, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred sixty-eight. That's not a flood. That's the print queue. Mine is in there.
- **слов / секунд речи:** 18 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, Walt's face in the foreground, mouth closed, wading calf-deep through the river of blank white sheets down a corridor between grey partitions toward a large grey office printer at the end with a blinking green light, sheets pouring from its tray.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he wades forward. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Every page belongs to someone who is still waiting. We have so much in common." lifting one sheet and letting it go; it rejoins the flow. 9-10s: the printer's green light blinks. Camera: handheld, slight shake, following forward. Audio: paper rustle, printer chug, one beep. No music, no on-screen text.
- **dialogue:** Every page belongs to someone who is still waiting. We have so much in common.
- **слов / секунд речи:** 15 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, low angle; Walt's face in the right foreground, mouth closed; behind him Dot, a round low charcoal-grey robot vacuum with a small blue indicator light, pushing through the paper river and ploughing a clear lane in the carpet as sheets fan out to both sides like a snow plough.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: Dot rolls forward with two chirps. 1-8s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Dot is clearing a path. Nobody asked her to. Nobody ever asks Dot." following behind Dot through the clear lane. 8-10s: Dot chirps; Walt gives a tiny respectful nod. Camera: handheld, low angle, following Dot. Audio: paper rustle, small motor whir, Dot's two chirps. No music, no on-screen text.
- **dialogue:** Dot is clearing a path. Nobody asked her to. Nobody ever asks Dot.
- **слов / секунд речи:** 13 / 9 (лимит 22)

### Клип 4 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, mouth closed, holding three warm printed copies of Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top and an empty frame, no text fanned in one hand; the paper river is gone; Dot, a round low charcoal-grey robot vacuum with a small blue indicator light is parked at the desk edge in the blurred background, blue light on.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he squares the three copies on the desk. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Three copies. Eleven hours. Fast, for here. Dot has a surprise for me. Tomorrow." 9s: Dot chirps once. 9-10s: lamp buzz, still. Camera: locked-off medium close-up, slow push-in. Audio: office hum, paper tap, Dot chirp, lamp buzz. No music, no on-screen text.
- **dialogue:** Three copies. Eleven hours. Fast, for here. Dot has a surprise for me. Tomorrow.
- **слов / секунд речи:** 14 / 9 (лимит 22)
- **end-frame (петля):** Walt at the desk, three squared copies in front of him, eyes into the lens, Dot a small blue light at the lower corner.

Сумма: 40 с.

---

## Серия 16. Dot's Night Shift

- **№:** 16 | **Дата:** 07.11.2026 (Сб), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred sixty-nine.
- **Формат:** Ghost on Duty | **Хук:** #5 шёпот-признание | **Секунды:** 30 (3x10) | **Сегмент ЦА:** B + D, тёплая серия для всех
- **Элементы (≤2):** Скрепка | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: Dot расчистила путь -> Сегодня: ночью Dot желает ему спокойной ночи и приносит потерянную ручку -> Завтра: воскресенье, тревога, и подача копий.
- **Подпись/обложка (≤7 слов):** The vacuum says goodnight. Every night.
- **Вопрос зрителю:** What would you name the office vacuum?
- **Петля:** Тихий щелчок, поверх лёгкий двойной писк Dot «спокойной ночи».

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Night office, only Walt's warm desk lamp lit, the rest in dim blue darkness with empty desks; the same man from the reference image seated at the desk leaning toward the lens in a conspiratorial hush, mouth closed.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: he leans in toward the lens. 0.3-3s: he whispers in a low hushed whisper, American voice, dry and polite: "Day fourteen thousand two hundred sixty-nine. Don't tell Priya. Dot says goodnight to me. Every night." (whispered, Day first, then the confession after a pause). 8-10s: he glances over his shoulder; far away on the dark floor a small blue light approaches. Camera: locked-off medium close-up, slow push-in. Audio: night hum, distant vacuum whir, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred sixty-nine. Don't tell Priya. Dot says goodnight to me. Every night.
- **слов / секунд речи:** 16 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, in the dark office; Walt's face in the foreground lit by his own cool cyan glow and the dim blue night light, mouth closed; behind him Dot, a round low charcoal-grey robot vacuum with a small blue indicator light circling the legs of his empty swivel chair on the carpet.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: Dot circles. 1-8s: he whispers in a low hushed whisper, American voice, dry and polite: "Every night she cleans around my feet. She never cleans through them. Respect." while Dot makes a careful loop around the chair legs and around his translucent feet. 8-10s: Dot stops and chirps two rising notes. Camera: handheld, low, slow orbit. Audio: soft vacuum hum, two rising chirps. No music, no on-screen text.
- **dialogue:** Every night she cleans around my feet. She never cleans through them. Respect.
- **слов / секунд речи:** 13 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind at night, lamp light only, the same man from the reference image seated, mouth closed, holding an old stubby ballpoint pen with a faded blue cap in his long fingers; Dot, a round low charcoal-grey robot vacuum with a small blue indicator light parked at the desk edge in the blurred background with its blue indicator on; one paperclip on the desk.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he turns the pen over in the lamp light; the paperclip drifts upward from the desk. 1-9s: he whispers in a low hushed whisper, American voice, dry and polite: "She found my pen. Missing since nineteen eighty-seven. Tomorrow is Sunday. Apparently that's a feeling. Don't tell Priya." Dot chirps once. 9-10s: slow blink. Camera: locked-off medium close-up, slow push-in. Audio: night hum, one Dot chirp, lamp buzz. No music, no on-screen text.
- **dialogue:** She found my pen. Missing since nineteen eighty-seven. Tomorrow is Sunday. Apparently that's a feeling. Don't tell Priya.
- **слов / секунд речи:** 18 / 9 (лимит 22)
- **end-frame (петля):** Walt at the dim desk with the pen, a paperclip floating beside him, Dot as a blue dot behind; similar to clip 1.

Сумма: 30 с.

---

## Серия 17. Sunday Scaries, Translated

- **№:** 17 | **Дата:** 08.11.2026 (Вс), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred seventy.
- **Формат:** Jargon Translator | **Хук:** #2 вопрос | **Секунды:** 30 (3x10) | **Сегмент ЦА:** C + B
- **Элементы (≤2):** Фраза («I'm still clocked in.» в финале) | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: Dot вернула ручку -> Сегодня: Walt переводит «Sunday scaries» и репетирует завтрашнюю подачу -> Завтра: понедельник, и «quick sync».
- **Подпись/обложка (≤7 слов):** Sunday scaries, translated by a ghost.
- **Вопрос зрителю:** What time on Sunday does your dread start?
- **Петля:** Классический щелчок + лампа.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Sunday dusk: orange low sun through the blinds across an empty open office; the same man from the reference image seated at his corner desk, mouth closed, one eyebrow raised, one hand lifted palm-up as an invitation.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: eyebrow raised, hand lifted. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred seventy. What's a Sunday scary? Allow me." (the question after a short pause). 6-10s: he rises, straightens his tie and nods toward the empty floor behind the lens. Camera: locked-off medium shot, slow push-in. Audio: empty-office hum, distant air conditioning, lamp buzz. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred seventy. What's a Sunday scary? Allow me.
- **слов / секунд речи:** 12 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, Walt's face in the foreground in amber dusk light, mouth closed, behind him long rows of empty desks with closed laptops and long amber shafts of light, some ceiling light banks already off.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he walks slowly along the aisle of empty desks. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "It's the dread that Monday exists. For you, it starts Sunday evening. For me, it's every evening." 7-8s: at 'every evening' the ceiling lights in the far section click off one bank at a time. 9-10s: he stops and looks into the lens. Camera: handheld, slight shake, slow walk along the aisle. Audio: footsteps, hum, light-bank clunks. No music, no on-screen text.
- **dialogue:** It's the dread that Monday exists. For you, it starts Sunday evening. For me, it's every evening.
- **слов / секунд речи:** 17 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind in evening lamp light, the same man from the reference image standing holding three printed copies of Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top and an empty frame, no text against his chest, polite rehearsed smile, looking into the lens as if it were a clerk, mouth closed.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he clears his throat silently, straightens his tie. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Tomorrow I submit the copies. Rehearsal: good morning. Three copies. No hard feelings. I'm still clocked in." with a small polite bow on 'Good morning'. 9-10s: lamp buzz. Camera: locked-off medium close-up, slow push-in. Audio: office hum, lamp buzz. No music, no on-screen text.
- **dialogue:** Tomorrow I submit the copies. Rehearsal: good morning. Three copies. No hard feelings. I'm still clocked in.
- **слов / секунд речи:** 17 / 9 (лимит 22)
- **end-frame (петля):** Walt at the desk, copies on the blotter, hand on his tie, eyes into the lens; evening lamp light.

Сумма: 30 с.

---

## Серия 18. The Quick Sync

- **№:** 18 | **Дата:** 09.11.2026 (Пн), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred seventy-one.
- **Формат:** Meeting Autopsy | **Хук:** #1 утверждение | **Секунды:** 33 (3x11) | **Сегмент ЦА:** A (основной)
- **Элементы (≤2):** Скрепка, Лампа | **CTA:** да: чек-лист встреч «full list is in my profile» (если файл не готов, замени последнюю фразу: см. запасной вариант)
- **Вчера -> сегодня -> завтра:** Вчера: репетиция подачи -> Сегодня: «quick sync» длится час, на экране схема, над Gable ещё один квадрат -> Завтра: ответ на апелляцию.
- **Подпись/обложка (≤7 слов):** A quick sync is a lie.
- **Вопрос зрителю:** What's the longest "quick sync" you've ever had?
- **Петля:** Щелчок + мигание лампы на вздохе.

### Клип 1 (11 с)

- **duration:** 11
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, flat unamused stare into the lens, mouth closed; through a glass wall in the soft-focus background a meeting room with blurred seated people facing a bright wall screen.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: flat stare into the lens. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred seventy-one. A quick sync is a fifteen-minute lie. This one started an hour ago." (second sentence after a beat; at the third he glances at the glass room and back). Camera: locked-off medium close-up, slow push-in. Audio: muffled drone of a conference call through glass, lamp hum. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred seventy-one. A quick sync is a fifteen-minute lie. This one started an hour ago.
- **слов / секунд речи:** 19 / 10 (лимит 25)

### Клип 2 (11 с)

- **duration:** 11
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, at the back of a glass meeting room: Walt's face in the foreground, mouth closed, eyebrows slightly raised; behind him blurred backs of heads facing a large wall screen showing an organisation chart of pale rectangles joined by lines, no text; one rectangle holds a tiny dark silhouette icon, and directly above it sits an empty faintly glowing rectangle.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-1s: he points over his shoulder at the screen. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Look at the chart. Gable has a box above him. An empty box. Someone signs for Gable." 9-11s: the empty rectangle on the screen pulses once; he raises his eyebrows at the lens. Camera: handheld, slight shake, slow drift past his shoulder toward the screen. Audio: muffled call drone, a distant mouse click, chair creaks. No music, no on-screen text.
- **dialogue:** Look at the chart. Gable has a box above him. An empty box. Someone signs for Gable.
- **слов / секунд речи:** 17 / 10 (лимит 25)

### Клип 3 (11 с)

- **duration:** 11
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, resolute, mouth closed, eyes into the lens; three paperclips lined up in a neat row on the desk blotter in front of him.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he looks at the three paperclips. 1-10s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "What are we deciding? Who decides? When does it end? Full list is in my profile. Tomorrow, my appeal. Hopefully shorter." tapping the paperclips one by one on each question; on the last question he exhales and the lamp flickers. 10-11s: still, lamp buzz. Camera: locked-off medium close-up, slow push-in. Audio: office hum, tiny taps of paperclips, lamp buzz. No music, no on-screen text.
- **dialogue:** What are we deciding? Who decides? When does it end? Full list is in my profile. Tomorrow, my appeal. Hopefully shorter.
- **слов / секунд речи:** 21 / 10 (лимит 25)
- **end-frame (петля):** Walt at the desk, three paperclips in a row, lamp mid-flicker, eyes into the lens; same composition as clip 1.
- **Запасной вариант CTA:** Запасная реплика без CTA: What are we deciding? Who decides? When does it end? Tomorrow, my appeal. Hopefully shorter.

Сумма: 33 с.

---

## Серия 19. Form 27-B, Step 6: Wrong Ink

- **№:** 19 | **Дата:** 10.11.2026 (Вт), публикация 15:00 МСК (тест слота) | **Day (голосом):** Day fourteen thousand two hundred seventy-two.
- **Формат:** Day Off Quest | **Хук:** #8 «When…» | **Секунды:** 30 (3x10) | **Сегмент ЦА:** A + D
- **Элементы (≤2):** Форма, Скрепка | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: нашёл схему с пустым квадратом над Gable -> Сегодня: апелляцию вернули, чернила не того синего, ручки не те -> Завтра: нужен кофе и план.
- **Подпись/обложка (≤7 слов):** One blue. Every pen is wrong.
- **Вопрос зрителю:** Blue or black: which ink deserves a day off?
- **Петля:** Классический щелчок.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated, mouth closed; in front of him on the blotter lies the appeal form, a pale lemon-yellow sheet like Form 27-B but with a blue stripe across the top and an empty frame, no text returned, with a pale-blue circle drawn over its signature frame; lined up before it four pens: his three from the breast pocket and an old stubby ballpoint pen with a faded blue cap, each with a slightly different blue, navy or teal cap.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-0.3s: he stares at the form. 0.3-3s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Day fourteen thousand two hundred seventy-two. When the form needs one exact blue, and every pen is wrong." (second sentence after a pause, as his eyes move down the row of pens). 9-10s: slow blink at the lens. Camera: locked-off medium close-up, slow push-in. Audio: office hum, lamp buzz, one pen rolling. No music, no on-screen text.
- **dialogue:** Day fourteen thousand two hundred seventy-two. When the form needs one exact blue, and every pen is wrong.
- **слов / секунд речи:** 18 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, tilted down so both Walt's face and the desk are in frame; he holds a pen over a scrap sheet that shows a fan of scribbled ink swatches in different blues; the returned appeal form lies to the side.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. He scribbles a swatch with each pen in turn on the scrap and says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Too bright. Too dark. Too sad. Dot's pen: almost. Almost doesn't count." 0-2s: first pen, bright blue swatch. 2-4s: second pen, dark navy. 4-6s: third pen, grey-blue. 6-8s: the old pen, nearly right. 8-10s: he sets it down, face falling. Camera: handheld, slight shake, tilted down to the desk. Audio: pen scratching, office hum, a soft sigh. No music, no on-screen text.
- **dialogue:** Too bright. Too dark. Too sad. Dot's pen: almost. Almost doesn't count.
- **слов / секунд речи:** 12 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Medium close-up at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind, the same man from the reference image seated clipping the returned appeal form with a paperclip, weary look into the lens, mouth closed.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he clips the form with a paperclip and sighs. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "One exact blue. Somewhere, someone has it. I need coffee, and a plan. Tomorrow." 9-10s: slow blink. Camera: locked-off medium close-up, slow push-in. Audio: office hum, lamp buzz. No music, no on-screen text.
- **dialogue:** One exact blue. Somewhere, someone has it. I need coffee, and a plan. Tomorrow.
- **слов / секунд речи:** 14 / 9 (лимит 22)
- **end-frame (петля):** Walt at the desk, returned form clipped on the blotter, pens in a row, eyes into the lens; same composition as clip 1.

Сумма: 30 с.

---

## Серия 20. The Coffee Machine Wants an Update

- **№:** 20 | **Дата:** 11.11.2026 (Ср), публикация 20:00 МСК | **Day (голосом):** Day fourteen thousand two hundred seventy-three.
- **Формат:** Then vs Now | **Хук:** #11 холодный старт (щелчок часов в начале) | **Секунды:** 30 (3x10) | **Сегмент ЦА:** A + D (нейтральная серия, без отсылок к празднику 11.11)
- **Элементы (≤2):** Лампа | **CTA:** нет
- **Вчера -> сегодня -> завтра:** Вчера: чернила не те -> Сегодня: ночью кофемашина просит обновление, Walt остаётся без кофе и думает, как идти «выше» -> Завтра: нужна карта в архиве.
- **Подпись/обложка (≤7 слов):** Update available. Coffee unavailable.
- **Вопрос зрителю:** What does your coffee machine do when you're in a hurry?
- **Петля:** Холодный старт: щелчок часов В НАЧАЛЕ (до первого кадра речи). В конце щелчка нет: запись обрывается на гудении лампы.

### Клип 1 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Dark office kitchenette at night, lit by the cold glow of a modern coffee machine whose touchscreen shows only a spinning blue progress ring; the same man from the reference image stands in profile facing the machine, holding an empty paper cup, mouth closed. Seen from a camcorder placed on the counter.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0s: a sharp mechanical clack of an old punch clock. 0.2-4s: he says to the coffee machine in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "I don't need an update. I need a refill. Day fourteen thousand two hundred seventy-three. It has been updating since midnight." (first two sentences to the machine). Mid-line he turns his head to the lens for the Day and the last sentence. 8-10s: he lowers the empty cup. Camera: locked-off medium shot, slow push-in. Audio: clock clack at start, machine chimes, night hum. No music, no on-screen text.
- **dialogue:** I don't need an update. I need a refill. Day fourteen thousand two hundred seventy-three. It has been updating since midnight.
- **слов / секунд речи:** 21 / 9 (лимит 22)

### Клип 2 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Handheld arm's-length selfie-style shot (Walt holds the camcorder pointed at himself), slightly shaky, Walt's face in the foreground, mouth closed, weary; behind him the coffee machine with its progress ring almost complete, a glowing tick icon ready to appear, kitchenette in cold night light.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). Handheld, slight shake. 0-2s: he points at the machine with his thumb. 2-8s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Nineteen eighty-seven: a pot, a warm plate, no opinions. This one wants to restart and reflect. Complete. Now another." The progress ring fills, a tick icon appears, a cheerful chime; 8-10s: the ring starts spinning again and he closes his eyes. Camera: handheld, slight shake, small push toward the machine. Audio: machine chime, hum, quiet footsteps. No music, no on-screen text.
- **dialogue:** Nineteen eighty-seven: a pot, a warm plate, no opinions. This one wants to restart and reflect. Complete. Now another.
- **слов / секунд речи:** 19 / 9 (лимит 22)

### Клип 3 (10 с)

- **duration:** 10
- **keyframe_prompt:** Vertical 9:16 frame, warm grainy 1987 camcorder footage look: soft focus toward the edges, slight color bleed, faint scanlines, warm tungsten lamp light mixed with cold fluorescent office light. No text, numbers or logos anywhere in the frame; people in the background are blurred and turned away. Night, only the warm desk lamp lit at Walt's corner desk: beige 1987 desktop computer, warm desk lamp, a stack of papers, a dry potted plant, grey cubicle partitions behind; the same man from the reference image seated, an empty paper cup in front of him on the blotter, mouth closed, looking into the lens then down.
- **motion_prompt:** The same ghost man from the image (toothbrush moustache, taped glasses, paperclip tie, faint cyan glow). 0-1s: he sighs; the lamp flickers. 1-9s: he says in a low, dry, slightly hoarse, polite American voice, slow pace, dropping on the last words: "Going up needs a map. Maps live in the archive. No coffee, so I had to think. Terrible. Tomorrow, downstairs." he looks down at the floor on 'downstairs'. 9-10s: lamp hum only. Camera: locked-off medium close-up, slow push-in. Audio: night hum, lamp buzz; recording cuts out on the hum. No music, no on-screen text.
- **dialogue:** Going up needs a map. Maps live in the archive. No coffee, so I had to think. Terrible. Tomorrow, downstairs.
- **слов / секунд речи:** 20 / 9 (лимит 22)
- **end-frame (петля):** Walt at the desk in lamp light, looking down toward the floor, empty cup on the blotter; recording cuts on the lamp hum, no click.

Сумма: 30 с.
