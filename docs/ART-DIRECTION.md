# Art direction

**Status: `[DEFINED]` (D-149).** The single source for how ColorHugs artwork
looks. Every prompt document — `STICKER-PROMPTS.md`, `EMOTION-CARD-PROMPTS.md`,
`AVATAR-PROMPTS.md`, and the colouring-page prompts — inherits from here. Where
one of them disagrees with this file, this file wins and the other is corrected.

---

## The house style

**Kawaii · Jellycat soft toy · cozy.**

Everything is drawn as if it were a **soft plush toy**: shapes fat, full and
squashy, slightly lumpy and imperfect rather than neat and symmetrical, as
though sewn by hand and lightly overstuffed. Short chubby limbs, large rounded
heads. No sharp points, no straight edges, no thin spikes — **even a leaf or a
feather is plump and soft**.

**Cozy in feeling:** calm, gentle, huggable. Never bright, spiky or loud.

**Thick, bold black outline of even weight**, the confident chunky outline of a
sticker, with a slight hand-drawn wobble rather than a perfect line.

### What is wrong

- A thin, delicate or varying line.
- A neat, technical or generic colouring-book line.
- Anything rigid, geometric, symmetrical or mechanically neat.
- Realistic proportions.

**This applies to every image in the project, colouring pages included.** The
rule was previously assumed to govern stickers only, and it produced seven
colouring pages of which three were generic line art — the feather, the hand and
the cushions. Measurably so — though **by the wrong measure**: ink share was read as line
weight, when a simple drawing has little ink even with a fat stroke. Stroke
width is the right number, and `prepare-colouring.py` now reports it, flagging
anything under 7px.

---

## Faces

**Kawaii in the shapes is always. Kawaii with a face is case by case.**

| | Face |
| --- | --- |
| Emotion cards, stickers, avatars | yes, by design |
| An object standing alone as a subject — a feather, a cloud | yes |
| **The child's own hand** | **no.** A hand with eyes stops being hers |
| Body map figure | **no** (D-106) — it is interface, and facelessness is what lets it stand for any child |
| A set of identical objects — four cushions | no. Four identical faces turn a quiet corner into a crowd staring back |

---

## What the soft-toy reference must not bring with it

**No stitching, no seams, no sewn lines, no fabric tags or labels.** They would
look right on a plush toy and they break the rule that matters more: on a
colouring page they are fine lines a child cannot colour, and they undo the
requirement for large fillable areas.

**The plush toy is the feeling, not the subject.**

---

## The block to paste

Into any image prompt, before the scene:

```
STYLE — KAWAII, JELLYCAT SOFT-TOY, COZY
Everything is drawn as if it were a soft plush toy: shapes are fat, full and
squashy, slightly lumpy and imperfect rather than neat and symmetrical, as
though sewn by hand and lightly overstuffed. Short, chubby limbs. Large rounded
heads. No sharp points, no straight edges, no thin spikes — even a leaf or a
feather is plump and soft.

Warm and cozy in feeling: calm, gentle and huggable, never bright, spiky or
loud.

THICK, BOLD black outline of even weight throughout, the confident chunky
outline of a sticker, with a slight hand-drawn wobble rather than a perfect
line. A thin, delicate or varying line is WRONG. A neat, technical or generic
colouring-book line is WRONG.

Nothing rigid, geometric, symmetrical or mechanically neat. No realistic
proportions. No fine or elegant lines.

No stitching, no seams, no sewn lines, no fabric tags or labels — a soft toy is
the feeling, not the subject.
```

---

## Rules that hold across all artwork

**No text inside artwork** (D-081, D-110). No words, letters, numbers or
numerals, in any image, ever. Names come from the language file. A sticker
reading "Explorer" needs seven translations and seven regenerations, for ever —
and numerals are not exempt: two of the seven priority locales do not always
write them the same way.

**Approved artwork is never redrawn or replaced** (rule 6, D-003). It may be
processed — background removal, trimming, format conversion — but not
reinvented.

**The white die-cut rim means collectable** (D-083). Stickers and emotion cards
keep it. Avatars, the body map figure and colouring pages have none: they are
not collectables.

**Line art that will be coloured by code must be sealed** (D-070, D-129). Every
internal dividing line starts on another line and ends on another line. An
unclosed line is not a wall, and the colour runs across the whole page.

**Six fillable areas minimum** in any official-library colouring page (D-129),
each at least 0.5% of the image. Checked by `scripts/prepare-colouring.py`,
which refuses to export a page that fails.

---

## Prompting, learned the hard way

Recorded because each one cost regenerations (D-132, D-140).

**State what MUST exist rather than describing it.** *"Every figure must have
hair, bald is wrong"* works where *"simple hair"* fails.

**List forbidden details one by one.** *"Simple face"* returned eyebrows, ears
and a nose.

**Phrase a critical instruction three ways** — the rule, the failure it must
avoid, and a picture of it. The ground line needed all three: it spans edge to
edge · it must not stop short · think of it as the horizon.

**Start a fresh conversation** when an earlier instruction keeps being carried
forward. *"No hair"* survived two rewrites of the prompt asking for hair.

**Ask for more than the minimum.** The floor is six fillable areas; prompts ask
for eight, because asking for the minimum reliably returns less.

**Generate a series in one conversation.** The first set of five pages came from
two different sessions and arrived in two different styles.

---

## Verify by measuring, not by looking

Almost every fault found so far was invisible in a screenshot and obvious in a
measurement:

- a hand that was one open region, not six
- the bored card with 0.9% coloured pixels, which would have read as *disabled*
- an outline exported opaque, hiding every zone beneath it
- a PDF the size of a postage stamp on A4
- legs classified as arms by a threshold meant for both
- a six-area check passed by counting five hollow numerals
- line weight judged by ink share, which measures how much there is to draw

Count the sealed regions. Flood-fill each one and look for leaks. Measure the
black ink and compare it with artwork already accepted. Then look.
