# Сезон 1 «Still Clocked In»: полные сценарии, часть 1 (серии 1-10, 23.10-01.11.2026)

Автор: showrunner, 22.10.2026. Основа: `season-plan.md`, библия (раздел «Формат сериала: видеодневник Walt»), `audience-hook-model.md`, `video-breakdowns.md`. Карточки эпизодов не созданы (по одной в день, когда директор берёт серию в работу). Серия 1 заменяет пилот ep-0001 (2 клипа, 11 с).

## Как читать

- Каждая серия = запись видеодневника: клип 1 (штатив, у стола: номер дня + хук), клип 2 (ручная съёмка, место происшествия, поворот), клип 3 (снова у стола: панчлайн + крючок + обрыв записи). Серия 9 - 4 клипа.
- Номер дня звучит голосом первой фразой клипа 1 и входит в `dialogue` (субтитры) и в счёт слов.
- Режимы: «штатив» = камера на штативе, Walt смотрит в объектив; «ручная, селфи» = Walt держит камеру на вытянутой руке, лицо крупно на переднем плане, место происшествия за спиной (так сохраняются лицо и липсинк).
- Лимит слов: не больше 2,5 слова/с речи, речь = duration минус 1 с. В таблице «слов / речь, с / макс.» по каждому клипу. Реплики говорит только Walt; Priya, Dot, Gable в кадре молчат (Dot пищит, Gable шелестит бумагой).
- Для ручных клипов `fal_gen.py`/Higgsfield: в промпте уже есть «handheld, slight shake». Для последнего клипа: `--end-image` = кадр из пункта «End-frame».
- Цена (по $0.055/с + $0.039/кадр): 33 с = $1.93; 30 с = $1.77; 40 с = $2.36. Серии 1-10: 313 с, 31 клип, ≈ $18.7 (серии 1-9: 283 с, 28 клипов, ≈ $16.7, как в плане).

## Постоянные описания (вставлять дословно)

Эталонов у второстепенных нет, поэтому описание всегда одно и то же. Если модель их не держит, нужен отдельный эталон (вопрос директору).

| Что | Строка для keyframe_prompt |
|---|---|
| Стиль кадра (в конце каждого keyframe_prompt) | Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away. |
| Walt (в начале каждого keyframe_prompt) | The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. |
| Стол Walt | Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions |
| Режим «штатив» | Tripod framing, medium close-up, Walt at eye level looking straight into the lens. |
| Режим «ручная, селфи» | Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. |
| Priya | Priya, a woman of about 30 with shoulder-length dark hair, an olive cardigan and a headset, blurred or seen from behind |
| Dot | Dot, a knee-high round charcoal-grey robot vacuum with one small glowing blue indicator light |
| Mr. Gable | Mr. Gable, a tall faceless silhouette of dark smoke with round glasses and a narrow dark tie |
| Форма 27-B | Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text |
| Видеокамера 1987 (в кадре почти не видна: мы смотрим её глазами; в ручных клипах она на вытянутой руке за кадром) | a heavy black-and-grey 1987 shoulder camcorder with a carry handle |
| Табельные часы | an old grey metal wall punch-clock with a card rack |

Строки для motion_prompt:

| Что | Строка |
|---|---|
| Начало (приметы Walt) | The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. |
| Голос | in a low, dry, slightly hoarse American voice, slow and polite |
| Шёпот | in a hushed, dry, hoarse whisper, slow and polite |
| Конец | No music, no on-screen text. |
| Штатив | Camera: locked-off medium close-up on a tripod, very slow push-in. |
| Ручная | Camera: handheld, slight shake, ... |
| Щелчок в конце | a metallic punch-clock click on the last frame |

Правила кадра: рот закрыт и лицо ровно освещено на первом кадре каждого клипа; читаемого текста и цифр нет (бейдж нечитаем, лист формы без печатного текста, часы без цифр, записка и флаер без надписей); люди на фоне размыты и повёрнуты спиной; во всех клипах без текста сюжет передаётся голосом и субтитрами.

## Сводная таблица

| № | Дата | Day | Название | Формат | Хук | Сек | Клипы | Элементы |
|---|---|---|---|---|---|---|---|---|
| 1 | 23.10 (пт) | 14 254 | This Meeting Could Be an Email | Meeting Autopsy | #1 утверждение | 33 | 11+11+11 | Фраза (финал), Лампа |
| 2 | 24.10 (сб) | 14 255 | Touch Base | Jargon Translator | #4 буквализация | 30 | 10+10+10 | Скрепка |
| 3 | 25.10 (вс) | 14 256 | Form 27-B, Step 1: Find the Form | Day Off Quest | #3 визуальная странность | 30 | 10+10+10 | Форма, Скрепка |
| 4 | 26.10 (пн) | 14 257 | Why Does Priya Talk to a Rectangle? | Meeting Autopsy | #2 вопрос | 30 | 10+10+10 | Лампа |
| 5 | 27.10 (вт, тест 15:00 МСК) | 14 258 | The Printer Is Thinking | Ghost on Duty | #11 холодный старт | 30 | 10+10+10 | Скрепка |
| 6 | 28.10 (ср) | 14 259 | Halloween: 1987 vs Now | Then vs Now | #9 Then vs Now | 30 | 10+10+10 | нет |
| 7 | 29.10 (чт) | 14 260 | Form 27-B, Step 2: The Signature | Day Off Quest | #5 шёпот-признание | 30 | 10+10+10 | Форма |
| 8 | 30.10 (пт) | 14 261 | A Ghost Is Not a Bedsheet | Ghost on Duty | #8 «When…» | 30 | 10+10+10 | Лампа |
| 9 | 31.10 (сб) | 14 262 | Costume: A Man Who Went Home on Time | Day Off Quest | #7 POV | 40 | 10+10+10+10 | Форма |
| 10 | 01.11 (вс) | 14 263 | The Extra Hour | Ghost on Duty | #6 время как шутка | 30 | 10+10+10 | Лампа |

---

## Серия 1. This Meeting Could Be an Email

- **Дата / день записи:** 23.10 (пт), голосом: «Day fourteen thousand two hundred fifty-four»
- **Формат:** Meeting Autopsy. **Хук:** #1 утверждение. **Секунды:** 33 (11 + 11 + 11). **Сегмент ЦА:** A (основной), B. **Элементы:** Фраза (финал), Лампа.
- **Вчера → сегодня → завтра:** Вчера: пилот в старом виде, 2 клипа (ep-0001 переписывается). Сегодня: Walt находит в кладовке камеру 1987 года, снимает бессмысленную встречу и объявляет цель - оформить первый выходной. Завтра: нужна форма, а Priya сказала «let's touch base».

### Клип 1 (11 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt sits at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, mouth closed, deadpan weary stare, one stray strand of hair, warm lamp glow on his face; far behind him a glass meeting room with blurred figures. Even face lighting.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he stares straight into the lens, unblinking, mouth closed. 1-10s: he says in a low, dry, slightly hoarse American voice, slow and polite, with a short pause after the day number: "Day fourteen thousand two hundred fifty-four. I've been dead for thirty-nine years, and this meeting could still have been an email." 10-11s: a slow blink, the desk lamp hums. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: low office hum, distant keyboard clicks, desk lamp buzz. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred fifty-four. I've been dead for thirty-nine years, and this meeting could still have been an email."

**Слов / речь:** 21 слов / 10 с (макс. 25); 2.1 слова/с.

### Клип 2 (11 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt whispers to the lens, mouth closed, eyes wide and tired; behind him through a glass wall a meeting room with a long table, nine blurred people seen from behind, a big wall screen with a grid of tiny blurred faces. Cold fluorescent light.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he glances back at the glass room, then at the lens. 1-10s: he whispers in a hushed, dry, hoarse whisper, slow and polite: "Forty minutes. Nine people. One slide: we should schedule another meeting. I found this camera in the closet. Evidence." 10-11s: a small satisfied nod. Camera: handheld, slight shake, slow drift sideways along the glass wall. Audio: muffled droning voices through the glass, chair creak, one quiet notification ping. No music, no on-screen text.
```
**dialogue:** "Forty minutes. Nine people. One slide: we should schedule another meeting. I found this camera in the closet. Evidence."

**Слов / речь:** 19 слов / 10 с (макс. 25); 1.9 слова/с.

### Клип 3 (11 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; a small dusty cardboard box on the desk corner; lamp slightly dimmer than before; Walt's mouth closed, eyes tired, hands folded on the desk.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he exhales a long sigh, the desk lamp flickers once. 1-10s: he says in a low, dry, slightly hoarse American voice, slow and polite: "This is for whoever signs my day off. I need my day-off form. Priya wants to touch base. I'm still clocked in." 10-11s: a metallic punch-clock click on the last frame, lamp hum, the recording ends. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, lamp buzz, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "This is for whoever signs my day off. I need my day-off form. Priya wants to touch base. I'm still clocked in."

**Слов / речь:** 22 слов / 10 с (макс. 25); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt in the exact pose and framing of the first frame of clip 1, mouth closed, eyes on the lens, one hand rising toward the lens to switch the recording off; the lamp slightly dimmed. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Dead 39 years. Still in meetings. (слов: 6)  
**Номер дня в подписи ролика:** Day 14 254  
**Вопрос зрителю:** What's the longest meeting you've ever survived?

---

## Серия 2. Touch Base

- **Дата / день записи:** 24.10 (сб), голосом: «Day fourteen thousand two hundred fifty-five»
- **Формат:** Jargon Translator. **Хук:** #4 буквализация. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** C (основной), A. **Элементы:** Скрепка.
- **Вчера → сегодня → завтра:** Вчера: цель - оформить выходной, нужна форма, Priya хочет «touch base». Сегодня: Walt понимает жаргон буквально, трогает основания лампы, горшка, шкафа и принтера; под шкафом что-то пищит. Завтра: кто там?

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt stands slightly bent beside Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, one fingertip resting on the base of the warm desk lamp, mouth closed, deadpan eyes on the lens.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he looks into the lens, fingertip on the lamp base. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred fifty-five. Priya wants to touch base. Understood. I'm starting with the lamp." while tapping the lamp base twice with his finger. 9-10s: a slow blink. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, two soft taps on metal, distant keyboard clicks. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred fifty-five. Priya wants to touch base. Understood. I'm starting with the lamp."

**Слов / речь:** 17 слов / 9 с (макс. 22); 1.9 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt crouches in an office aisle beside a grey filing cabinet, mouth closed, glancing down; behind and below him the dark gap under the cabinet; blurred desks and a plant pot in the distance.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he walks along the aisle tapping the base of things with two fingers, then crouches by the cabinet. 1-9s: he says in a hushed, dry, hoarse whisper, slow and polite: "Plant, touched. Cabinet, touched. Printer, touched. Still no form. Wait. Something under the cabinet is chirping." 9-10s: a tiny blue light blinks in the dark gap behind him and a faint chirp sounds. Camera: handheld, slight shake, tilting down toward the gap at the end. Audio: office hum, soft taps on plastic and metal, a tiny electronic chirp from under the cabinet. No music, no on-screen text.
```
**dialogue:** "Plant, touched. Cabinet, touched. Printer, touched. Still no form. Wait. Something under the cabinet is chirping."

**Слов / речь:** 16 слов / 9 с (макс. 22); 1.8 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; Walt holds one silver paperclip between two fingers above the desk, mouth closed, tired eyes on the lens.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he turns to the lens. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Touch base, translated: let's postpone this politely. I touched six. Nothing touched back. Except whatever is chirping." and at "I touched six" sets the paperclip neatly on the desk. 9-10s: a tiny chirp from below the frame, he glances down; a metallic punch-clock click on the last frame. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, lamp buzz, a tiny chirp from below, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "Touch base, translated: let's postpone this politely. I touched six. Nothing touched back. Except whatever is chirping."

**Слов / речь:** 17 слов / 9 с (макс. 22); 1.9 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt at his desk glancing down-left toward the floor, one paperclip lying neatly on the desk, mouth closed, lamp lit. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Walt touches base. Literally. (слов: 4)  
**Номер дня в подписи ролика:** Day 14 255  
**Вопрос зрителю:** Which office phrase should Walt translate next?

---

## Серия 3. Form 27-B, Step 1: Find the Form

- **Дата / день записи:** 25.10 (вс), голосом: «Day fourteen thousand two hundred fifty-six»
- **Формат:** Day Off Quest. **Хук:** #3 визуальная странность. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** D (основной), A. **Элементы:** Форма, Скрепка.
- **Вчера → сегодня → завтра:** Вчера: писк под шкафом. Сегодня: это Dot, она вытащила форму выходного, пропавшую с 1991 года; в форме три графы (подпись, чернила, свидетель). Завтра: нужен Mr. Gable, а Priya шесть часов не отрывается от экрана.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt sits at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; about fifteen silver paperclips hover in the air around his head and shoulders, slowly orbiting; mouth closed, deadpan gaze at the lens; at the very bottom edge of the frame a tiny glowing blue light by the desk leg.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: the paperclips drift slowly around his head, he looks deadpan at the lens. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred fifty-six. Ignore the paperclips. They float when I'm hopeful. Look who came out." at "Look who came out." he glances down and a small blue light slides into the bottom of the frame. 9-10s: a slow blink. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, a soft glassy tinkle of paperclips, a faint wheel whir. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred fifty-six. Ignore the paperclips. They float when I'm hopeful. Look who came out."

**Слов / речь:** 18 слов / 9 с (макс. 22); 2.0 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt kneels on the carpet in an office aisle, mouth closed, quiet relief in his eyes; beside his knees Dot, a knee-high round charcoal-grey robot vacuum with one small glowing blue indicator light nudges a dusty folded pale-lemon sheet with a rust-red stripe out from under a grey filing cabinet; dust motes in the light.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: Dot's blue light blinks, she nudges the sheet out. 1-9s: Walt says in a low, dry, slightly hoarse American voice, slow and polite: "This is Dot. She vacuums, she chirps, and she found my form. Lost since nineteen ninety-one." and at "found my form" lifts the sheet. 9-10s: Dot chirps. Camera: handheld, slight shake, small tilt down toward Dot. Audio: office hum, a tiny wheel whir, cheerful electronic chirps, dust rustle. No music, no on-screen text.
```
**dialogue:** "This is Dot. She vacuums, she chirps, and she found my form. Lost since nineteen ninety-one."

**Слов / речь:** 16 слов / 9 с (макс. 22); 1.8 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; Walt holds up Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text in both hands and reads it, half-hopeful, mouth closed; at the floor below the desk the small blue light of Dot.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he lowers the sheet flat onto the desk. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Three boxes: a signature, the right ink, a witness. Simple. First, Mr. Gable. Priya won't look up for six hours." tapping the three boxes one by one with a finger at "signature", "ink", "witness". 9-10s: a long blink; a metallic punch-clock click on the last frame. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, finger taps on paper, lamp buzz, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "Three boxes: a signature, the right ink, a witness. Simple. First, Mr. Gable. Priya won't look up for six hours."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt at his desk, Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text lying flat in front of him with one fingertip on it, eyes toward the lens, mouth closed, three paperclips still hanging in the air near his shoulder. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Walt's paperclips float when he's hopeful. (слов: 6)  
**Номер дня в подписи ролика:** Day 14 256  
**Вопрос зрителю:** Would you sign Walt's form, no questions asked?

---

## Серия 4. Why Does Priya Talk to a Rectangle?

- **Дата / день записи:** 26.10 (пн), голосом: «Day fourteen thousand two hundred fifty-seven»
- **Формат:** Meeting Autopsy. **Хук:** #2 вопрос. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** B (основной), A. **Элементы:** Лампа.
- **Вчера → сегодня → завтра:** Вчера: форма найдена, нужен Mr. Gable, Priya занята. Сегодня: Walt разбирает видеозвонок Priya и читает её записку: Gable подписывает только в ночь Хэллоуина. Завтра: Priya печатает флаер, а принтер «думает».

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt sits at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, one open hand lifted slightly toward his left, mouth closed, an eyebrow raised at the lens; in the blurred background across the aisle Priya, a woman of about 30 with shoulder-length dark hair, an olive cardigan and a headset, blurred or seen from behind, her back to us, facing a monitor.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he looks into the lens and raises one eyebrow. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred fifty-seven. Why does Priya talk to a rectangle for six hours? Let me explain." and at "Let me explain" gestures with an open palm toward Priya. 9-10s: a slow blink. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, distant keyboard clicks, a muffled one-sided call far away. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred fifty-seven. Why does Priya talk to a rectangle for six hours? Let me explain."

**Слов / речь:** 19 слов / 9 с (макс. 22); 2.1 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt creeps behind Priya, a woman of about 30 with shoulder-length dark hair, an olive cardigan and a headset, blurred or seen from behind's chair, mouth closed, eyes wide; behind him Priya's back and headset, her monitor showing a grid of tiny blurred faces, a small blank yellow sticky note on the monitor's edge.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he creeps closer and glances at the screen. 1-9s: he whispers in a hushed, dry, hoarse whisper, slow and polite: "Nine faces. Nobody speaks. Everyone nods. The nodding is the work. Wait. What is that note?" and the camera drifts toward the sticky note at "that note". 9-10s: he leans in, squinting. Camera: handheld, slight shake, slow drift toward the sticky note. Audio: soft muffled call voices, a muffled "mm-hmm" from the headset, keyboard, office hum. No music, no on-screen text.
```
**dialogue:** "Nine faces. Nobody speaks. Everyone nods. The nodding is the work. Wait. What is that note?"

**Слов / речь:** 16 слов / 9 с (макс. 22); 1.8 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; Walt holds a tiny blank yellow sticky note between two fingers, mouth closed, brow furrowed; the lamp lit; Priya is a blurred figure far behind him.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he exhales a long sigh, the desk lamp flickers once. 1-9.5s: he says in a low, dry, slightly hoarse American voice, slow and polite: "The note says: Mr. Gable signs only on Halloween night. Saturday. Priya is printing a flyer. The printer is thinking." 9.5-10s: a printer starts a slow whir off-screen; a metallic punch-clock click on the last frame. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, lamp buzz, a faint printer whir, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "The note says: Mr. Gable signs only on Halloween night. Saturday. Priya is printing a flyer. The printer is thinking."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt at his desk, the sticky note stuck to the edge of his old beige monitor, eyes toward the lens, mouth closed, lamp slightly dimmed. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Why does Priya talk to a rectangle? (слов: 7)  
**Номер дня в подписи ролика:** Day 14 257  
**Вопрос зрителю:** How many hours a day do you talk to a rectangle?

---

## Серия 5. The Printer Is Thinking

- **Дата / день записи:** 27.10 (вт, тест 15:00 МСК), голосом: «Day fourteen thousand two hundred fifty-eight»
- **Формат:** Ghost on Duty. **Хук:** #11 холодный старт. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** A (основной), B. **Элементы:** Скрепка.
- **Вчера → сегодня → завтра:** Вчера: записка - Gable подписывает в ночь Хэллоуина, Priya печатает флаер. Сегодня: Walt придерживает «задумавшемуся» принтеру дверцу и хвалит его за одну страницу - это флаер офисной вечеринки в пятницу. Завтра: подготовка к вечеринке, шанс подойти к Gable.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium shot. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt stands beside a grey office printer holding its open front flap with one hand, the other finger raised to his lips, leaning toward the lens, mouth closed, eyes on the lens; his desk lamp glows behind.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-0.5s: a punch-clock click. 0.5-1s: he turns his head to the lens. 1-9s: he whispers in a hushed, dry, hoarse whisper, slow and polite: "Day fourteen thousand two hundred fifty-eight. Shh. He's thinking. Give him a minute. He's very sensitive." and at "Give him a minute" pats the printer lid. 9-10s: he stares, finger back at his lips. Camera: locked-off medium shot on a tripod, very slow push-in. Audio: a metallic punch-clock click on the last frame at the very start, slow grinding printer whir, distant keyboard clicks. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred fifty-eight. Shh. He's thinking. Give him a minute. He's very sensitive."

**Слов / речь:** 16 слов / 9 с (макс. 22); 1.8 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt crouches by the output tray of a grey office printer, a tender proud look, mouth closed; behind him a single sheet half out of the tray with a picture of an orange pumpkin and bats, the banner area blank, no text.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: the tray hums and the sheet slides out slowly. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "There it is. One page, eleven minutes. I'm so proud. It's a flyer: office Halloween party, Friday." and at "I'm so proud" places a silver paperclip on top of the printer as a tip. 9-10s: the printer clunks twice. Camera: handheld, slight shake, slow push toward the sheet. Audio: printer whir, a soft clunk, paper sliding, office hum. No music, no on-screen text.
```
**dialogue:** "There it is. One page, eleven minutes. I'm so proud. It's a flyer: office Halloween party, Friday."

**Слов / речь:** 17 слов / 9 с (макс. 22); 1.9 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. At Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, Walt holds a printed flyer (orange pumpkin and bats picture, blank banner, no text) up beside his face, an eyebrow raised, mouth closed.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he lowers the flyer a little and looks at the lens. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "A party. Mr. Gable is invited. Everyone is invited. Even the printer, if he finishes thinking. Tomorrow: decorations." and at "Even the printer" glances sideways. 9-10s: the printer gives a last whir and goes quiet. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, lamp buzz, a printer whirr that fades out, no click. No music, no on-screen text.
```
**dialogue:** "A party. Mr. Gable is invited. Everyone is invited. Even the printer, if he finishes thinking. Tomorrow: decorations."

**Слов / речь:** 18 слов / 9 с (макс. 22); 2.0 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt lowering the flyer, looking sideways toward the printer off-frame, mouth closed, lamp lit. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Shh. The printer is thinking. (слов: 5)  
**Номер дня в подписи ролика:** Day 14 258  
**Вопрос зрителю:** Does your office printer have a name?

---

## Серия 6. Halloween: 1987 vs Now

- **Дата / день записи:** 28.10 (ср), голосом: «Day fourteen thousand two hundred fifty-nine»
- **Формат:** Then vs Now. **Хук:** #9 Then vs Now. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** D (основной), A. **Элементы:** нет.
- **Вчера → сегодня → завтра:** Вчера: флаер вечеринки. Сегодня: в 1987-м - одна миска конфет, сегодня у конфет комитет; план Walt - ждать Gable у мисок. Завтра: подойти к двери Gable заранее.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt sits at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, holding a small glass bowl with a few wrapped candies in both hands, flat deadpan expression, mouth closed.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he stares at the lens holding the bowl. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred fifty-nine. Halloween, nineteen eighty-seven. One bowl of candy. Nobody asked who brought it." lifting the bowl slightly at "One bowl of candy" and lowering it at "Nobody asked". 9-10s: a slow blink. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, soft glass clink of the bowl, distant keyboard clicks. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred fifty-nine. Halloween, nineteen eighty-seven. One bowl of candy. Nobody asked who brought it."

**Слов / речь:** 18 слов / 9 с (макс. 22); 2.0 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt looks skeptical, mouth closed; behind him an office kitchen with a long table, eleven small bowls in neat rows, laptop screens, a huddle of blurred people around it, a plastic skeleton seated in a chair wearing a blank lanyard.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he turns the camera to the table. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Today the candy has a committee. Eleven bowls. One skeleton with a job title. Nobody has tasted anything yet." and at "job title" points at the skeleton. 9-10s: a slow blink. Camera: handheld, slight shake, slow drift along the table. Audio: murmuring blurred voices, rustling wrappers, a chair creak. No music, no on-screen text.
```
**dialogue:** "Today the candy has a committee. Eleven bowls. One skeleton with a job title. Nobody has tasted anything yet."

**Слов / речь:** 19 слов / 9 с (макс. 22); 2.1 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; Walt's hands folded on the desk, calm, mouth closed, eyes on the lens.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he looks at the lens. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "In eighty-seven, you took one candy and went home. My plan: wait by the bowls for Gable. Tomorrow, his door." 9-10s: he gives a single slow nod; a metallic punch-clock click on the last frame. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, lamp buzz, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "In eighty-seven, you took one candy and went home. My plan: wait by the bowls for Gable. Tomorrow, his door."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt in the pose of the first frame of this clip, hands folded, mouth closed, eyes on the lens, lamp steady. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Halloween 1987: one bowl of candy. (слов: 6)  
**Номер дня в подписи ролика:** Day 14 259  
**Вопрос зрителю:** Candy bowl or committee: what does your office have?

---

## Серия 7. Form 27-B, Step 2: The Signature

- **Дата / день записи:** 29.10 (чт), голосом: «Day fourteen thousand two hundred sixty»
- **Формат:** Day Off Quest. **Хук:** #5 шёпот-признание. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** A (основной), C. **Элементы:** Форма.
- **Вчера → сегодня → завтра:** Вчера: план ждать Gable на вечеринке. Сегодня: Walt шёпотом признаётся, что просунул форму под дверь Gable; она возвращается с красной тыквой: «в ночь Хэллоуина». Завтра: вечеринка, все в костюмах.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt very close to the lens, hunched forward at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, eyes cut sideways toward the aisle, mouth closed; far behind him in dim light a frosted-glass door.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he glances sideways, then at the lens. 1-9s: he whispers in a hushed, dry, hoarse whisper, slow and polite: "Day fourteen thousand two hundred sixty. Don't tell Mr. Gable. I slid the form under his door. Quietly." and at "under his door" mimes sliding paper with one hand. 9-10s: another glance sideways. Camera: locked-off close-up on a tripod, very slow push-in. Audio: low office hum, lamp buzz, distant keyboard. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred sixty. Don't tell Mr. Gable. I slid the form under his door. Quietly."

**Слов / речь:** 18 слов / 9 с (макс. 22); 2.0 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt crouches in a dim corridor by a frosted-glass door, whispering, mouth closed; behind frosted glass the faint dark smoke silhouette of Mr. Gable, a tall faceless silhouette of dark smoke with round glasses and a narrow dark tie; the floor gap under the door is empty.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he looks at the door. 1-9s: he whispers in a hushed, dry, hoarse whisper, slow and polite: "Ten minutes. A rustle. The form slides back with a red pumpkin. Not yes. Not no. Halloween night." and at "The form slides back" a pale-lemon sheet slides out from under the door with a small round red pumpkin stamp on it. 9-10s: he stares at the sheet. Camera: handheld, slight shake, small push toward the gap under the door. Audio: dim corridor hum, distant paper rustle, a soft slide, one heavy breath. No music, no on-screen text.
```
**dialogue:** "Ten minutes. A rustle. The form slides back with a red pumpkin. Not yes. Not no. Halloween night."

**Слов / речь:** 18 слов / 9 с (макс. 22); 2.0 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. At Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, Walt holds Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text in both hands, a small round red pumpkin stamp in its first box, eyes on the lens, mouth closed.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he lowers the form to the desk. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Thirty-nine years of silence, and now a pumpkin. Progress. Tomorrow everyone wears costumes. I wear the suit I died in." 9-10s: slow blink; a metallic punch-clock click on the last frame. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: office hum, paper rustle, lamp buzz, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "Thirty-nine years of silence, and now a pumpkin. Progress. Tomorrow everyone wears costumes. I wear the suit I died in."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt at his desk, Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text with the red pumpkin stamp lying in front of him, one hand flat on it, eyes on the lens, mouth closed. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Don't tell Mr. Gable. (слов: 4)  
**Номер дня в подписи ролика:** Day 14 260  
**Вопрос зрителю:** What would you wear to ask your boss for a day off?

---

## Серия 8. A Ghost Is Not a Bedsheet

- **Дата / день записи:** 30.10 (пт), голосом: «Day fourteen thousand two hundred sixty-one»
- **Формат:** Ghost on Duty. **Хук:** #8 «When…». **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** B (основной), C. **Элементы:** Лампа.
- **Вчера → сегодня → завтра:** Вчера: Gable ответил «в ночь Хэллоуина», сегодня вечеринка. Сегодня: коллега приходит «призраком» в простыне, Walt объясняет, что призрак - незакрытая бумага; приз получает простыня. Завтра: ему нужен свой костюм.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, mouth closed, a weary side-eye toward his left; in the blurred background a paper garland, orange party lights, and a blurred person in a plain white bedsheet with two eye holes walking past, back partly turned.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he watches sideways, then turns to the lens. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred sixty-one. When a coworker comes as a ghost. He thinks a ghost is a bedsheet." 9-10s: a slow blink. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: party chatter far away, office hum, a paper garland rustling. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred sixty-one. When a coworker comes as a ghost. He thinks a ghost is a bedsheet."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt looks patient and pained, mouth closed; right behind him a blurred person in a plain white bedsheet with two eye holes holds a paper cup under orange party lights.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he turns the camera on himself, the sheet person sips behind him. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "A ghost is not a sheet. A ghost is unfinished paperwork. With feelings. Mostly the paperwork." gesturing with one hand at "unfinished paperwork"; the sheet person tilts his head, unaware. 9-10s: a slow blink. Camera: handheld, slight shake, slow drift to the left. Audio: distant party chatter, a cup crinkle, office hum. No music, no on-screen text.
```
**dialogue:** "A ghost is not a sheet. A ghost is unfinished paperwork. With feelings. Mostly the paperwork."

**Слов / речь:** 16 слов / 9 с (макс. 22); 1.8 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; a small paper garland above the old monitor; Walt's mouth closed, tired eyes on the lens, lamp lit.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he exhales a long sigh, the desk lamp flickers once. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "He won the costume prize. For a bedsheet. Thirty-nine years in this suit, no prize. Tomorrow, I need a costume." 9-10s: slow blink; a metallic punch-clock click on the last frame. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: faint party chatter, lamp buzz, a metallic punch-clock click on the last frame. No music, no on-screen text.
```
**dialogue:** "He won the costume prize. For a bedsheet. Thirty-nine years in this suit, no prize. Tomorrow, I need a costume."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt at his desk in the pose of the first frame of this clip, eyes on the lens, mouth closed, lamp slightly dimmed. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** A ghost is not a bedsheet. (слов: 6)  
**Номер дня в подписи ролика:** Day 14 261  
**Вопрос зрителю:** What's the best office Halloween costume you've seen?

---

## Серия 9. Costume: A Man Who Went Home on Time

- **Дата / день записи:** 31.10 (сб), голосом: «Day fourteen thousand two hundred sixty-two»
- **Формат:** Day Off Quest. **Хук:** #7 POV. **Секунды:** 40 (10 + 10 + 10 + 10). **Сегмент ЦА:** A (основной), B. **Элементы:** Форма.
- **Вчера → сегодня → завтра:** Вчера: простыня получила приз, Walt нужен костюм. Сегодня (ключевая): в ночь Хэллоуина Walt в роли «человека, который ушёл домой вовремя» идёт к двери Gable; Gable ставит красный крест-штамп DENIED. Завтра: идём выше, а в офисе переводят часы.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium shot, dark empty open-space office at night, lit only by a warm desk lamp and monitor glow. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt stands upright by Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, same suit, with a folded coat over one arm and a small brown briefcase in his other hand, mouth closed, looking straight into the lens.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he stares at the lens. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred sixty-two. Halloween night. Last one here. My costume: a man who went home on time." and at "went home on time" lifts the briefcase slightly. 9-10s: a slow blink. Camera: locked-off medium shot on a tripod, slow push-in as if the viewer is walking up to him; the viewer is the only other person in the office. Audio: low empty-office hum, a distant fridge hum, lamp buzz. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred sixty-two. Halloween night. Last one here. My costume: a man who went home on time."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt in a dark office corridor at night, nervous, mouth closed, folded coat over his arm and a small brown briefcase; behind him a long dark corridor lit by faint monitor glow, at its far end a frosted-glass door with a thin line of light under it.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he walks forward, footsteps echoing. 1-9s: he whispers in a hushed, dry, hoarse whisper, slow and polite: "Saturday, midnight. The office is empty. Even the candy gave up. Mr. Gable's door. My costume has to work." 9-10s: he stops, swallows, and looks toward the door. Camera: handheld, slight shake, slow forward move down the corridor. Audio: soft footsteps, low empty-office hum, a far-off fridge hum. No music, no on-screen text.
```
**dialogue:** "Saturday, midnight. The office is empty. Even the candy gave up. Mr. Gable's door. My costume has to work."

**Слов / речь:** 19 слов / 9 с (макс. 22); 2.1 слова/с.

### Клип 3 (10 с, Штатив, общий)

**keyframe_prompt:**
```
Locked-off two-shot in a dark corridor. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt stands in three-quarter profile with face visible, holding out Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text in both hands, folded coat and small brown briefcase at his feet, mouth closed; across from him in an open doorway stands Mr. Gable, a tall faceless silhouette of dark smoke with round glasses and a narrow dark tie, holding a large rubber stamp at chest height.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: Walt holds the form out. 1-6s: he says softly in a low, dry, slightly hoarse American voice, slow and polite: "Mr. Gable. I went home on time. Once. Look at me. One signature." 6-8s: Gable says nothing, slowly lifts the stamp, paper rustles. 8-9s: the stamp slams down onto the form, a big rust-red X mark appears, a heavy thud. 9-10s: silence. Camera: locked-off medium two-shot, no movement. Audio: corridor hum, paper rustle, a heavy stamp thud at 8 seconds. No music, no on-screen text.
```
**dialogue:** "Mr. Gable. I went home on time. Once. Look at me. One signature."

**Слов / речь:** 13 слов / 9 с (макс. 22); 1.4 слова/с.

### Клип 4 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Back at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions; Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text with a big rust-red X mark lying flat in front of him, the folded coat on his chair, mouth closed, tired eyes on the lens, lamp lit.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: a slow blink. 1-8s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Denied. Thirty-nine years, and the answer is still a stamp. Fine. Then I'll go over his head." and at "over his head" slowly looks up at the ceiling. 8-10s: he holds his gaze upward; a heavy stamp thud echoes and the lamp hum cuts off. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: lamp buzz, a single heavy stamp thud with an echo at the end instead of a click. No music, no on-screen text.
```
**dialogue:** "Denied. Thirty-nine years, and the answer is still a stamp. Fine. Then I'll go over his head."

**Слов / речь:** 17 слов / 9 с (макс. 22); 1.9 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt looking up at the ceiling, mouth closed, Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text with the red X lying on the desk beneath him, lamp lit. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Walt's costume: went home on time. (слов: 6)  
**Номер дня в подписи ролика:** Day 14 262  
**Вопрос зрителю:** Where does Walt go next: up to the boss's boss, or down to HR?

---

## Серия 10. The Extra Hour

- **Дата / день записи:** 01.11 (вс), голосом: «Day fourteen thousand two hundred sixty-three»
- **Формат:** Ghost on Duty. **Хук:** #6 время как шутка. **Секунды:** 30 (10 + 10 + 10). **Сегмент ЦА:** A (основной), D. **Элементы:** Лампа.
- **Вчера → сегодня → завтра:** Вчера: DENIED, «идём выше». Сегодня: часы переведены назад; Walt проводит лишний час за мелким шрифтом на обороте формы и находит слово «appeal». Завтра: ждёт письменного ответа.

### Клип 1 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt at Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, deadpan stare, mouth closed; behind his shoulder a round wall clock with plain tick marks and no numerals.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he stares at the lens, a slow tick of the clock. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Day fourteen thousand two hundred sixty-three. You got an extra hour today. I get one every day. It's called overtime." 9-10s: a slow blink at "overtime". Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: slow wall-clock ticking, office hum, distant keyboard. No music, no on-screen text.
```
**dialogue:** "Day fourteen thousand two hundred sixty-three. You got an extra hour today. I get one every day. It's called overtime."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

### Клип 2 (10 с, Ручная, селфи)

**keyframe_prompt:**
```
Handheld arm's-length selfie framing, slightly wide lens: Walt's face and shoulders large in the foreground, the place behind him. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. Walt at his desk, his face on the left, mouth closed, peering sideways at Form 27-B, a pale lemon-yellow sheet with a rust-red stripe across the top, three empty rectangular boxes at the bottom, no printed text with a big rust-red X, held up in his hand on the right with a round black-handled magnifying glass over its back, covered in tiny unreadable squiggly lines.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he peers through the magnifying glass. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "Fine print on the back. Smaller than my hopes. Wait. There is a word here. Appeal." freezing at "Wait" and at "Appeal" his eyes widen slightly, still deadpan. 9-10s: a slow blink. Camera: handheld, slight shake, slow push toward the sheet. Audio: paper rustle, slow clock ticking, office hum. No music, no on-screen text.
```
**dialogue:** "Fine print on the back. Smaller than my hopes. Wait. There is a word here. Appeal."

**Слов / речь:** 16 слов / 9 с (макс. 22); 1.8 слова/с.

### Клип 3 (10 с, Штатив)

**keyframe_prompt:**
```
Tripod framing, medium close-up, Walt at eye level looking straight into the lens. The same man from the reference image (Walt, ghost clerk): semi-transparent with a soft cyan glow, mustard-brown polyester suit, rust tie with paperclips, small name badge with unreadable text. At Walt's corner desk: beige 1987 computer, warm yellow desk lamp, stack of papers, small pot with a dry plant, grey office partitions, hands folded, the form with the red X in front of him, the wall clock behind him, lamp lit, mouth closed.
```
**motion_prompt:**
```
The same ghost man from the image (toothbrush moustache, taped glasses, rust paperclip tie, faint cyan glow). Warm grainy 1987 camcorder footage. 0-1s: he exhales a long sigh, the desk lamp flickers once. 1-9s: he says in a low, dry, slightly hoarse American voice, slow and polite: "An appeal means he has to answer in writing. I wait. Tomorrow, the letter. Best extra hour of my afterlife." folding his hands at "I wait". 9-10s: a slow blink while the clock ticks loudly. Camera: locked-off medium close-up on a tripod, very slow push-in. Audio: lamp buzz, loud slow wall-clock ticking at the end instead of a click. No music, no on-screen text.
```
**dialogue:** "An appeal means he has to answer in writing. I wait. Tomorrow, the letter. Best extra hour of my afterlife."

**Слов / речь:** 20 слов / 9 с (макс. 22); 2.2 слова/с.

**End-frame для петли (`--end-image`, последний клип):** Walt in the pose of the first frame of clip 1, hands folded, eyes on the lens, mouth closed, the plain wall clock behind him, lamp steady. Vertical 9:16, warm grainy 1987 camcorder look, soft focus at the edges, gentle color bleed, warm yellow cast over cold fluorescent light, no text, no numbers, no logos in frame, people in the background are blurred and turned away.

**Подпись / обложка (≤7 слов):** Your extra hour: Walt's overtime. (слов: 5)  
**Номер дня в подписи ролика:** Day 14 263  
**Вопрос зрителю:** What did you do with your extra hour?

