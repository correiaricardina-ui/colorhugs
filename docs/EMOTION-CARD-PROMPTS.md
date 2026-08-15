# ColorHugs — Emotion Cards

The content of *How Do I Feel?*, the first printable deck, and the first
professional material. One set of artwork, three destinations.

Status: `[PROPOSAL]`. **Generate the seven families first**, check them, and
only then the finer words. Thirty-five images in a style that turns out wrong
is thirty-five images wasted.

---

## Two decisions built into the prompt

### The same character every time

Every card shows **the same creature**, changing only its expression and
posture. If each emotion were a different animal, a child would be comparing
animals. With one character, the only thing that changes is the feeling — which
is the entire point.

The character is **a heart with a face**, which the My Inner World sticker
already establishes as the face of this section. It ties the deck to the area a
child arrived from.

### Posture, not just face

A face alone cannot carry shame or boredom. Shame is looking down and turning
away; boredom is slumping. So the character has **arms and a body**, and the
prompts describe what it is doing as much as how it looks.

This also makes the cards work for a child who cannot yet read a subtle
expression — the whole body says it.

### And, as with the stickers: no text

Names come from the language file. Seven families in seven locales is seven
translations of a word, not seven regenerations of a drawing.

---

## The seven families

| # | Family | Colour | What the child sees |
| --- | --- | --- | --- |
| 1 | Happy | sunny yellow | arms up, wide open smile |
| 2 | Sad | soft blue | drooping, one tear, mouth turned down |
| 3 | Angry | warm red | fists clenched, frowning, small puff of steam |
| 4 | Scared | pale purple | wide eyes, hands drawn up to the chest |
| 5 | Ashamed | soft pink | looking down and away, hands half covering the face |
| 6 | Calm | mint green | eyes gently closed, small content smile, relaxed |
| 7 | Bored | warm grey-beige | slumped, chin propped on one hand, eyelids low |

Colour here is a recognition aid, not a meaning. **The face and the posture do
the work** — a child who cannot distinguish the colours can still read every
card, and nothing depends on knowing that blue means sad.

*Note: this colour set is unrelated to the seven area colours used on the
avatar. Different context, no overlap in use.*

---

## Shared prompt block

Paste this before every variant line.

```
A cute cartoon character card for a children's app.

THE CHARACTER
A single rounded heart-shaped character with a simple face, two small arms and
two small legs. Big expressive eyes, simple mouth, rosy cheeks. Kawaii sticker
style. The same character in every image — only its expression, posture and
colour change.

STYLE
Bold black outline of even weight. Flat colour, no gradients, no shading, no
texture. Rounded, chunky, friendly shapes.

DIE-CUT STICKER
The character sits on a thick white border that follows its outline, like a
cut-out sticker. Plain white background outside that border.

COMPOSITION
Square image. The character centred, filling most of the frame, whole body
visible. Even margin on all sides.

DO NOT INCLUDE
No text, no letters, no numbers. No background scenery. No other characters.
No props except where the variant line asks for one. No drop shadow.
```

## The seven variant lines

```
1  The heart character is sunny yellow, standing with both arms raised high,
   eyes happy curves, wide open smile. It looks delighted.

2  The heart character is soft blue, drooping downward, arms hanging limp, eyes
   looking down with one single tear on its cheek, mouth turned down.

3  The heart character is warm red, both fists clenched by its sides, eyebrows
   pulled down in a frown, mouth a small tight line, one small puff of steam
   above its head.

4  The heart character is pale purple, eyes very wide and round, both hands
   drawn up close to its chest, small open mouth, leaning slightly backward.

5  The heart character is soft pink, head lowered and turned slightly away,
   both hands half covering its face, eyes looking downward, small closed
   mouth.

6  The heart character is mint green, standing relaxed with arms loose at its
   sides, eyes gently closed as two curved lines, small content smile.

7  The heart character is warm grey-beige, slumped sideways, chin propped on
   one hand, eyelids low and heavy, mouth a small flat line.
```

---

## Check before accepting one

- [ ] **The same character** as the others — shape, proportions and face style
      must match. This is the one that drifts most across generations.
- [ ] No text anywhere.
- [ ] Whole body visible, centred, square, even margins.
- [ ] Flat colour, no gradient.
- [ ] The feeling is readable **with the colour removed**. Look at it in
      greyscale; if it becomes ambiguous, the posture is not doing enough.
- [ ] Nothing that reads as punishment. Ashamed in particular must look like a
      child who feels small, never a child being told off.
- [ ] Readable at 120px.

Generate all seven in one session, and generate happy first — it sets the
character that the other six have to match.

---

## After the seven are approved

Each family opens into three or four finer words, drawn as the same character
in the same family colour with a smaller change of expression. Roughly
twenty-eight more cards. **Those prompts are written once the seven are
settled**, because they inherit everything from them.
