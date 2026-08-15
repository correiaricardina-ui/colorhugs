# ColorHugs — Avatar Generation Prompts

Twelve avatars, six animals and six non-animals, each with the **same seven
paintable zones**. Generate one at a time, using the shared block below plus one
variant line.

---

## Why the rules are what they are

The avatar is coloured **by code**, not by the image generator. Each zone is
filled when the child visits the matching area, so the artwork must arrive as
clean outlines with fully enclosed regions.

Three consequences, and none of them is optional:

- **No fill, no shading, no gradients.** A shadow inside a zone stops the colour
  filling cleanly and shows up as a dirty patch.
- **Every zone fully enclosed by an unbroken black line.** A gap anywhere lets
  colour leak into the neighbouring zone.
- **Every avatar has all seven zones.** If one has five and another has eight,
  a child who chose the wrong one gets less colour than her friend for the same
  work.

---

## The seven zones, and which area paints each

Fixed across all twelve. The mapping never changes.

| Zone | ColorHugs area |
| --- | --- |
| 1 — Head / face | Learning Hub |
| 2 — Head-top feature (ears, antenna, horns, tuft) | Brain Gym |
| 3 — Chest patch | My Inner World |
| 4 — Arms / front limbs | Kids Draw for Kids |
| 5 — Body / torso | Color & Create |
| 6 — Back feature (tail, cape, wings, shell) | My ColorHugs |
| 7 — Legs / feet | Community |

**Chest for My Inner World** is deliberate — it is where a child points when
asked where a feeling lives.

---

## Shared prompt block

Paste this before every variant line.

```
A cute cartoon character for a children's app, drawn as clean line art only.

STYLE
Bold, even black outlines of uniform weight. Rounded, friendly, chunky shapes.
Simple kawaii face with large eyes and a small smile. Sticker-illustration style.

CRITICAL — LINE ART ONLY
No colour. No fill. No shading. No gradients. No texture. No hatching.
Pure white inside every shape. Plain white background.
The image must look like a colouring-book page.

CRITICAL — ENCLOSED REGIONS
Every body part must be a fully closed shape, sealed by an unbroken black line,
so it can be filled with colour separately. No gaps in any outline. Do not let
body parts merge into one another.

COMPOSITION
Front-facing, symmetrical, standing, whole body visible from head to feet.
Centred, with even margin on all sides. No background elements, no props,
no accessories, no text, no shadow beneath the character.

SEVEN SEPARATE REGIONS, ALL CLEARLY DIVIDED BY OUTLINES
1. head and face
2. the feature on top of the head
3. an oval patch on the chest
4. arms
5. body and torso
6. the feature on the back
7. legs and feet
```

## The twelve variants

Add one of these lines to the end of the block.

### Animals

1. `The character is a friendly cat, with pointed ears on top and a curled tail behind.`
2. `The character is a friendly rabbit, with long upright ears and a round fluffy tail behind.`
3. `The character is a friendly bear, with small round ears on top and a short round tail behind.`
4. `The character is a friendly fox, with pointed ears on top and a large bushy tail behind.`
5. `The character is a friendly penguin, with a small tuft of feathers on top and small wings at the back.`
6. `The character is a friendly dinosaur, with two small horns on top and a thick tail behind.`

### Non-animals

7. `The character is a friendly robot, with a single antenna on top and a small square backpack on its back.`
8. `The character is a friendly astronaut in a rounded suit, with a small fin on top of the helmet and an oxygen pack on its back.`
9. `The character is a friendly star-shaped character with arms and legs, with a small tuft on top and a small cape behind.`
10. `The character is a friendly monster, with two rounded horns on top and a curly tail behind.`
11. `The character is a friendly cloud-shaped character with arms and legs, with a small tuft on top and small wings at the back.`
12. `The character is a friendly rocket-shaped character with arms and legs, with a pointed cone on top and a small fin at the back.`

---

## What to check before accepting one

- [ ] Nothing is filled or shaded — pure white inside every shape.
- [ ] Every one of the seven regions exists and is separately outlined.
- [ ] No gaps in any outline. Follow each region round with your eye.
- [ ] Front-facing, whole body, same framing as the others.
- [ ] Line weight matches the others — this is the one that most often drifts.
- [ ] No accessories, props, background or ground shadow.
- [ ] Nothing gendered, and no human skin tone.

**Expect to regenerate.** Line weight and framing drift between generations more
than anything else. Generating all twelve in one session, with the same tool and
the same block, keeps them closer than doing them across several days.

---

## What happens after

Supply them at any size, on white. Processing does the rest:

1. Background cut to transparency and artwork trimmed, as with every other asset.
2. Each of the seven regions identified and given a fill point, so code can
   colour it.
3. Line weight and canvas normalised across all twelve so they sit evenly
   together on the picker.

If a region turns out not to be sealed, it shows up immediately at that stage —
colour floods where it should not — and that avatar goes back for regeneration.

---

# Body map figure

Not an avatar. It is the figure in *How Do I Feel?* on which a child points to
where in her body she feels something (D-105, D-106). **No white die-cut rim** —
it is interface, not a collectable (D-083). Sealed line art coloured by code, as
the avatars are (D-070).

Five zones: **head · chest · stomach · arms and hands · legs and feet.**
The throat is deliberately excluded: the lump in the throat is one of the most
recognisable signals, but at phone size a neck zone is too small for a child's
finger, and a zone that misses reads as the app not listening.

The neck sliver between the chin line and the shoulder line is grouped with the
head in processing, so nothing is left permanently white (D-075).

```
A simple outline figure for a children's app.

THE FIGURE
A single standing human figure seen from the front, arms held away from the
body with a clear gap at each armpit, legs slightly apart. Simple, rounded,
friendly proportions with a slightly large head.

NO FACE AND NO IDENTITY
The head is completely blank — no eyes, no mouth, no nose, no ears, no hair.
No clothing, no shoes, no accessories. No gender. No fill of any kind.

STYLE
Black outline only, on a plain white background. THICK, BOLD lines of even
weight, the same heavy weight throughout, like a children's colouring book.
No colour, no fill, no shading, no gradient, no drop shadow.

FIVE CLOSED COMPARTMENTS — THE MOST IMPORTANT REQUIREMENT
The figure must be divided by internal lines into exactly five separate
compartments: head, chest, stomach, arms with hands, legs with feet.

EVERY internal dividing line must start ON the outer outline and end ON the
outer outline, touching it at both ends, so that each compartment is a
completely closed shape. A dividing line that stops in the middle of the body
without reaching the outline is wrong.

The required dividing lines are:
- a line across the neck, separating the head from the chest;
- a line across the waist, separating the chest from the stomach;
- a line across each shoulder, separating each arm from the body;
- a line across each hip, separating each leg from the stomach.

Imagine pouring paint into the head: it must not be able to reach the chest.
Pour paint into the stomach: it must not reach the legs or the arms.

COMPOSITION
Square image. The whole figure centred, even margin on all sides.

DO NOT INCLUDE
No text, no numbers. No background scenery. No other figures. No white
die-cut border. No face of any kind. No internal line that fails to touch the
outline at both ends.
```

## Why this prompt is longer than it looks

The first attempt produced **one** fillable region instead of five. Its internal
lines floated — they never met the outer outline at either end — and there was
no line at the neck or the waist at all. Paint poured into the chest reached the
head, both arms, both hands, both legs and both feet.

**The sentence that fixed it is the one requiring every internal line to touch
the outline at both ends.** It belongs in every line-art prompt from here on.

Black ink was also 2.41% of the image against 5.2–6.1% on the avatars, so the
line was too fine for the family. The second version came in at 5.76%.

## Acceptance check

- [ ] Count the sealed white regions. Group them: head, chest, stomach, two
      arms, two legs. Anything that does not group into the five zones is a
      defect.
- [ ] Flood-fill each region a different colour and look. **No colour may cross
      into a neighbour.** This is the failure that is invisible by eye and
      obvious the moment colour is applied (D-072).
- [ ] Black ink between 5% and 6.5% of the image, or the line does not belong
      to the ColorHugs family.
- [ ] No face, no hair, no clothing, no rim.
