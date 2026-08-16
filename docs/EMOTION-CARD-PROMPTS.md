# ColorHugs — Emotion Cards

> **Style is governed by [`ART-DIRECTION.md`](ART-DIRECTION.md)** — kawaii,
> Jellycat soft toy, cozy, with a thick bold outline. Where this document and
> that one disagree, that one wins.
The content of *How Do I Feel?*, the first printable deck, and the first
professional material. One set of artwork, three destinations.

Status: `[DEFINED]` for the seven families — all seven generated, checked and
accepted (D-092, D-093). The fine words are `[DEFINED]` for PT-PT only (D-102).

Original guidance, kept because it held: **generate the seven families first**, check them, and
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
| 7 | Bored | muted olive-khaki `#A89B5C` | slumped, chin propped on one hand, eyelids low |

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

5  The heart character is soft pink, body turned three-quarters away from the
   viewer, head tilted down, eyes open but looking down and off to the side,
   one hand raised to shield the side of its face, the other arm hanging down,
   small closed mouth, cheeks strongly blushed. No tears and no crying. Both
   hands must NOT be at the eyes; it must NOT be rubbing its eyes; it must NOT
   face the viewer straight on.

6  The heart character is mint green, standing relaxed with arms loose at its
   sides, eyes gently closed as two curved lines, small content smile.

7  The heart character is a muted olive-khaki colour, roughly #A89B5C — clearly
   a real colour, definitely not grey and not beige. It slumps sideways, chin
   propped on one hand, eyelids low and heavy over open eyes, looking sideways
   into the distance, mouth a small flat line. It must NOT be grey, beige,
   brown or desaturated.
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
- [ ] **Only sad carries a tear.** It is that card's strongest signal and it
      works only while it is unique to it. A second crying card leaves a child
      with two she cannot choose between.
- [ ] **Real colour, measured.** Coloured pixels should fall in the 25–36% band
      of the accepted set. The first bored card came in at 0.9% and would have
      read as *disabled* rather than as a feeling.
- [ ] Readable at 120px.

Generate all seven in one session, and generate happy first — it sets the
character that the other six have to match.

---

## The fine words

Each family opens into three or four finer words, drawn as the same character
in the same family colour with a smaller change of expression.

**The count is per language, not global** (D-101). PT-PT came to twenty-three,
not the twenty-eight estimated in English. A family may hold four words in one
language and three in another; that is the language, not an error. The data
model must allow different counts per family per locale.

The vocabulary is **written in each language, not translated**. *Ashamed* and
*embarrassed* are two words in English and one in Portuguese; *com saudades*
has no equivalent in six of the seven locales. The art is unaffected, because
no card carries text (D-081) — the same drawing serves different words in
different languages, which is where that rule pays for itself.

**Criterion for admitting a word:** the child must already have heard it, even
if she does not use it. The layer names what she already feels; it does not
teach vocabulary. An unknown word means she picks by the drawing.

**Excluded on principle:** words that are only *more* of the same — terrified,
petrified. That is intensity, and intensity is out (D-096).

### PT-PT, first pass (D-102)

| Family | PT-PT label | Fine words |
| --- | --- | --- |
| Happy | Feliz | contente · entusiasmado · orgulhoso · aliviado |
| Sad | Triste | desiludido · sozinho · com saudades · magoado |
| Angry | Zangado | chateado · irritado · furioso |
| Scared | Assustado | nervoso · preocupado · tímido |
| Ashamed | Envergonhado | culpado · arrependido · embaraçado |
| Calm | Calmo | tranquilo · descansado · seguro |
| Bored | **Tédio** | aborrecido · farto · impaciente · sem vontade |

**Note on the seventh, and do not undo it.** The canonical deck name stays
*Bored*. The PT-PT documentation label is **Tédio**, because *aborrecido* in
European Portuguese means both *nothing to do* and *cross with someone*, and
the ambiguity costs in the notes and the materials. The **child-facing label**
under the card is **Aborrecido**, the word a child actually says — the drawing
beside it removes the ambiguity. This is a PT-PT correction only; *boredom*,
*ennui* and *aburrimiento* do not carry it.

Three words unresolved (Q-027): which family *chateado* belongs to,
the weakness of *embaraçado*, and the absence of a childlike Portuguese word
for the feeling of injustice.

---

## Card order (D-104)

**Feliz · Calmo · Triste · Assustado · Zangado · Envergonhado · Tédio**

Fixed, never shuffled — a five-year-old learns where her card is. Not grouped
by valence, which would teach that feelings divide into good and bad. Three
columns, last row centred, label always beneath the card and never inside it.
