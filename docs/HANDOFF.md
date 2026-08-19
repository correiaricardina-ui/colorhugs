# ColorHugs — Handoff

Paste this as the first message of a new conversation, and upload
`colorhugs.zip` with it.

---

## Start here

I am Ricardina Correia, a paediatric psychologist. I am building **ColorHugs**
(colorhugs.pt), a psychology-informed platform where children learn, create and
grow, with families in control. You are helping me design and build it.

**Read `docs/DECISION_LOG.md` in the attached project before answering
anything.** It holds every decision made so far, numbered D-001 onwards, with
the reasoning. It is the source of truth. If something here and something there
disagree, the decision log wins. **It now runs to D-347.**

The other documents in `docs/`:

| File | What it holds |
| --- | --- |
| `DECISION_LOG.md` | every decision, in order, with reasons |
| `CONTENT-DESIGN.md` | activity concepts for all seven areas, with honest evidence grading |
| `COMMERCIAL-MODEL.md` | three revenue lines and their sequence |
| `ASSET_MAP.md` | every artwork file and where it goes |
| `CERTIFICATIONS.md` | seals worth pursuing, and two that turned out not to apply |
| `QA-CHECKLIST.md` | pre-launch checks, with blockers |
| `AVATAR-PROMPTS.md`, `STICKER-PROMPTS.md`, `EMOTION-CARD-PROMPTS.md` | image generation specs |
| `COLOURING-PROMPTS.md` | every colouring page prompt, with the failures named |
| `WORKBOOK-RECIPE.md` | how a family workbook is built, section by section |
| `materials/livro-historia.md` | *Quem És Tu?*, the children's story, sixteen scenes |
| `materials/livro-paratexto.md` | the book's cover, imprint, cast page and back cover |
| `materials/livro-personagens.md` | the cast sheet and the consistency rules |
| `materials/livro-prompts.md` | the scene prompts, and the cover prompt |
| `materials/livro-pais.md` | *Antes de Precisar*, the parents' book |

---

## How I like to work

- **One question at a time.** If you stack three decisions into one message I
  lose the thread. Ask one, wait, then ask the next.
- **Tell me when I am wrong.** I would rather be corrected than agreed with.
  Several of the best decisions in this project came from you pushing back.
- **Verify before recording.** Do not write facts into the project without
  checking them.
- **Write decisions down.** Every material decision goes into
  `docs/DECISION_LOG.md` with its reasoning, so the *why* survives.
- I communicate by voice message and screenshot. Sometimes the transcription
  garbles a word — ask rather than guess.

---

## Where the project is

**Seven families closed.** Zangado, Triste, Assustado, Envergonhado, Aborrecido,
Calmo, Feliz. Each now has **four** PDFs — `caderno` (clinician), `exploracao`
(the child's sheets), `pais` (the letter as handed over in session) and
`pais-familia` (the same letter for a family that downloaded it, closing on
itself). Built by `scripts/build-workbook-pdf.py <family>`. **Twenty-eight
documents.**

**Teacher line complete.** `professores-sala.pdf`, `professores-vocabulario.pdf`,
the A3 poster and six A5 schema cards.

**Parents' line complete.**

- ***Quem És Tu?*** — the illustrated story, in **three expressions from one
  source**: `quem-es-tu-leitura.pdf` (twenty A5 pages in reading order),
  `quem-es-tu-impressao.pdf` (instruction sheet plus five imposed A4 sheets for
  a home-printed, folded and stapled booklet), and `docs/materials/livro-ecra/`
  (open `index.html` — nineteen screens, no server, no network, no storage).
  Built by `scripts/build-book-pdf.py` and `scripts/build-book-web.py`.
- ***Antes de Precisar*** — the parents' book, read alone by the adult. Seven
  chapters and a closing, about five thousand words, twenty-four A5 pages.
  Built by `scripts/build-parents-book-pdf.py`.
- **The seven letters**, in the two settings described above.

**Psychologists' line, in progress.** Its governing distinction is D-327: **these
are therapeutic pieces, selected and applied by the clinician according to her
clinical judgement, and adjusted to the case in front of her.** No piece
presupposes another and nothing is a programme. **Eight of nine pieces are
built:**

- **Bonecos de tamanhos** — seven A4 sheets, one per family, the figure at three
  sizes to cut out. `build-size-figures.py`.
- **Baralho terapêutico** — fifty-nine cards in four naipes: *fizeste, não és* ·
  *reparação* · *quase* · *conversa*. Naipes, not levels. `build-therapy-deck.py`.
- **Peças de sessão** — eleven pages gathered in `pecas-de-sessao.pdf`, and every
  piece also prints alone: *Quem vive nesta casa*, *Antes durante depois*, *Duas
  listas*, the **dice for Zangado and Triste**, and the two games **Outra vez**
  (losing) and **A vez** (waiting). `build-session-sheets.py`,
  `build-strategy-die.py`, `build-session-games.py`.

Each piece has an application note with the evidence graded honestly. **Still to
build: O Depósito**, the cooperative board game — the only physical expression of
the store the whole product assumes, and the most expensive piece.

**A rule this line added** (D-328): *nothing is scored or ranked* applies to the
autonomous product, **not to the consulting room**. With a clinician present,
competition, losing and waiting are legitimate and are frequently the point.

---

## The rules that keep applying

These recur constantly. Apply them without being reminded.

**Child safety over everything.** No advertising, no behavioural tracking, no
third-party scripts, no child-to-child messaging, no publication without human
review, no diagnosis or assessment ever.

**No price and no purchase button on any child-facing screen.**

**A material a child uses alone must close itself.** Only material licensed to
practitioners may open something and leave it open — because there is a person
there to pick it up. **Family printables follow the child-alone rules**, and this
is why the letters exist in two settings (D-322).

**Nothing is scored, ranked or taken away.** Rewards are for participation and
variety, never performance.

**Address forms** (D-319, D-320). **No *vós* and no *você*** — the verb carries
the address. The letters and anything addressed to the parents use the third
person plural (*cuidem*, *digam*, *a vossa filha*); anything addressed to one
adult at a time, like a printing instruction, uses the singular (*imprima*,
*pode*). ***Sua* is avoided**, because in European Portuguese it is ambiguous.

**The house style is kawaii, Jellycat soft toy, cozy** — fat squashy shapes,
thick bold outline, nothing rigid or elegant. It governs **every** image in the
project and lives in `docs/ART-DIRECTION.md`.

**No text inside artwork.** Names come from the language file.

**Evidence is graded honestly** — established, reasonable, or practice. Never
claim more than the support.

**Never display a certification seal that has not been earned.**

**Approved artwork is never redrawn or replaced.** It can be processed —
background removal, trimming, colour levelling, format conversion — but not
reinvented.

**Register** (D-293). Technically careful and professionally serious. Warmth
belongs in the parents' letters, the child's sheets and the parents' book, and
never at the cost of accuracy.

**For image prompts: describe the picture, not the measurement** (D-307), and
**generate in batches with an already-accepted image as an anchor** (D-310).

---

## What the last session did, and what is worth knowing about it

**The illustrated book was finished.** A cover was generated — right on the first
attempt, the only time in this book that has happened. The palette of scenes 9,
11, 12 and 14 was levelled onto the book's median by
`scripts/level-book-palette.py`, closing the spread from 58.5 to 29.7. Scene 11
was trimmed 6.2% to match the 5:4 format; **scene 4 was deliberately left
portrait** and given a narrower placement on its page, because cropping it would
cost 36% of the height and regenerating it would risk the most expensive image in
the book (D-317).

**Three lessons from that session that generalise:**

- **Measure before believing a fault.** Three faults suspected on the cover by
  looking — a cast shadow, separate fingers, a tongue — were all disproved on
  measuring, and two of them turned out to be **rules the project had written for
  itself that contradicted its own canonical artwork** (D-315).
- **A test can be wrong as easily as an image.** Twice a measurement accused a
  correct file, once because a colour mask was sweeping in scenery (D-316).
- **Render it, do not read it.** Every layout fault that session — a literal `#`
  on a cover, a mark printed over the characters, a footer telling a family they
  held licensed professional material, a doubled percent sign that printed
  `colorhugs.pt3` as one word — was invisible in the source and obvious on the
  page.

**Fonts now live in the repository.** `assets/fonts/` holds Nunito and Baloo 2,
both SIL Open Font License, with the licences beside them, plus the three static
instances generated by `scripts/make-book-fonts.py`. **Static instances and not
the variable files** — Chromium embeds a variable font as Type 3, which is worse
in every way.

**The PSD is not the master and cannot be** (D-318). No library that writes PSD
writes live text, so a generated PSD would carry the text rasterised, destroying
the one reason to want it. **The master is the markdown plus the build script.**

---

## What is open right now

- **`[mês e ano]`** in the book's imprint is the only placeholder left in it.
- **Q-013 The "Brain Gym" name.** Trademarked programme, widely cited as
  pseudoscience. The audience most likely to recognise it is the one whose trust
  this product most needs.
- **Q-015 What happens when a child repeatedly reports distress.** Needs clinical
  and legal input.
- **Q-016 Can a child's drawing become a colouring page for other children?**
  Needs a legal position on consent.
- **Q-018 VAT on EU digital sales.** Needs an accountant before the first sale.
- **Q-026, Q-027, Q-028** — the ashamed card's raised hand, three unresolved
  PT-PT words, and whether language is detected or asked.

---

## What I would like you to do first

Read the decision log — **D-325**. Then tell me, in a few lines, what you
understand the state of the project to be, so I can check you have it right
before we carry on.

**Do not start building anything until we have agreed what.**

The next piece is the psychologists' line, unless I say otherwise.
