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
disagree, the decision log wins.

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
| `materials/livro-historia.md` | the children's story, sixteen scenes |
| `materials/livro-personagens.md` | the cast sheet and the consistency rules |
| `materials/livro-prompts.md` | the scene prompts for the story |

---

## How I like to work

- **One question at a time.** If you stack three decisions into one message I
  lose the thread. Ask one, wait, then ask the next.
- **Tell me when I am wrong.** I would rather be corrected than agreed with.
  Several of the best decisions in this project came from you pushing back.
- **Verify before recording.** Do not write facts into the project without
  checking them. Two of three certification seals I asked for turned out not to
  apply, and finding that out early saved real work.
- **Write decisions down.** Every material decision goes into
  `docs/DECISION_LOG.md` with its reasoning, so the *why* survives.
- I communicate by voice message and screenshot. Sometimes the transcription
  garbles a word — ask rather than guess.

---

## Where the project is

**Seven families closed.** Zangado, Triste, Assustado, Envergonhado, Aborrecido,
Calmo, Feliz. Each has three PDFs — `caderno` (clinician, 25 to 29 pages),
`exploracao` (the child's sheets, 12 to 14 pages) and `pais` (one page) — built
from `<família>-caderno.md` plus `<família>-fichas.html` by
`scripts/build-workbook-pdf.py <family>`. **Twenty-one documents.**

**Teacher line complete.** `professores-sala.pdf` (seven classroom pages plus the
disclosure page), `professores-vocabulario.pdf` (eleven pages), the A3 poster and
six A5 schema cards. Built by `build-teacher-pages.py` and
`build-teacher-extras.py`.

**The children's story is written and illustrated.** *Quem És Tu?* — sixteen
scenes, about five hundred words, in `livro-historia.md`, with all sixteen
illustrations in `artwork/livro/`.

**Interactive:** all seven families live on screen, each with its own question.
The bored family waits to be asked before it offers anything (D-262).

---

## What is being worked on, and what is not started

**Three commercial lines** (D-288): **Professores** — complete. **Pais** — in
progress. **Psicólogos** — not started.

**Next in the parents' line:**

- **The parents' book** — the seven families as a narrative read by the adult
  alone, beginning with calm and happy. Not written.
- **The seven letters rewritten** so they close without a session (D-298). As
  they stand they say *combinámos experimentar isto esta semana*, which has no
  referent outside a consultation.
- ***Quem És Tu?*** needs laying out. **One job left on the art:** scenes 9, 11,
  12 and 14 sit 34 to 60 units from the book's median floor colour. No drawing is
  wrong — it is a levelling pass at layout, one colour adjustment per image.

**The psychologists' line, not started** (D-288): body map on paper, record pad,
accommodation grid, ladder log, eight-session plan, school feedback sheet,
framing and consent, A3 store map.

## The rules that keep applying

These recur constantly. Apply them without being reminded.

**Child safety over everything.** No advertising, no behavioural tracking, no
third-party scripts, no child-to-child messaging, no publication without human
review, no diagnosis or assessment ever.

**No price and no purchase button on any child-facing screen.** When a free set
runs out the child is told the set is finished and pointed at a grown-up.

**A material a child uses alone must close itself.** Naming can stand alone;
exploring cannot. No "why", no free-text box, no interpretation, no intensity.
Only material licensed to practitioners may open something and leave it open —
because there is a person there to pick it up. Family printables follow the
child-alone rules, because a printed sheet does not choose who is in the room.

**Nothing is scored, ranked or taken away.** Rewards are for participation and
variety, never performance. No streaks that can break — a streak that breaks is
a punishment.

**Six families are closed** — angry, sad, scared, ashamed, bored and calm — each in three PDFs plus
the shared deck. **A family workbook is built to a fixed recipe** — three PDFs from one source,
for the clinician, the child and the parents. `docs/WORKBOOK-RECIPE.md` holds
the section order, the sheet menu, the non-negotiable rules (boxes not lines,
nothing printed inside a box, the child's page speaks to her not about her) and
the list of faults that were invisible in the file and obvious on the printed
page. Angry is the worked example.

**The house style is kawaii, Jellycat soft toy, cozy** — fat squashy shapes,
thick bold outline, nothing rigid or elegant. It governs **every** image in the
project, colouring pages included, and lives in `docs/ART-DIRECTION.md`, which
also holds the prompting lessons and the rule to verify by measuring rather
than by looking.

**No text inside artwork.** Names come from the language file. A sticker that
reads "Explorer" needs seven translations and seven regenerations, for ever.
The existing activity artwork predates this rule and carries English text baked
in; it is regenerated text-free as each activity is built (D-110). Section
names are the exception — they work as wordmarks and are not translated.

**Evidence is graded honestly** — established, reasonable, or practice. Never
claim more than the support. A psychology-informed platform that overstates its
science is worth less than one that has none.

**Never display a certification seal that has not been earned.**

**Approved artwork is never redrawn or replaced.** It can be processed —
background removal, trimming, format conversion — but not reinvented. If
artwork is missing, say so and show an honest placeholder.

---


### Added in the session that closed the seven families

**Register — applies to everything written** (D-293). Technically careful and
professionally serious. No colloquial phrasing, no chatty asides, no jokey tone.
Named constructs, stated evidence level, explicit limits. **Warmth belongs in the
parents' letters and the child's sheets and nowhere else**, and never at the cost
of accuracy.

**Evidence is never described by metaphor** (D-294, D-295). The three levels —
**estabelecido / razoável / prática** — are defined in a table at the top of
section 3 of every workbook, and every claim uses them or says concretely what is
replicated and where. *Terreno firme*, *a literatura é fina* and *apoio
indirecto* were removed nineteen times.

**No gender in anything the child or family takes home** (D-287). Double forms
where the word *is* the feeling — *nervoso ou nervosa* — and rewriting where the
agreement was incidental. **Age ranges live in the workbook and never on the
child's sheet** (D-247).

**Each family adds one rule to its artwork.** Nobody is sad in the sad pages;
nobody is frightened in the scared pages; nobody is being looked at in the
ashamed pages; nobody is bored in the bored pages, **and there are no screens in
them**.

**For image prompts: describe the picture, not the measurement.** Asking for
*three times taller* failed twice; describing the frame worked at once. The same
held for the ground line, the sealed thumb and the unrecognisable object — **four
times out of four** (D-307).

**Generate in batches with one already-accepted image as an anchor**, or the
whole batch drifts together and the drift is invisible until they are laid side
by side (D-310).

## Recent decisions worth knowing

**The child brings the colour.** The child picks one of ten avatars, supplied as
line art. It gains colour as she uses ColorHugs — **for having been there, not
for how much she did.** One activity or six, the same colour. What accumulates
over time is variety, not intensity. Large on the home page, small elsewhere.

**Seven areas, seven avatar zones**, one per area: head → Learning Hub,
head-top → Brain Gym, chest → My Inner World, arms → Kids Draw, torso → Color &
Create, back → My ColorHugs, legs → Community.

**Stickers are separate from avatars.** Avatars are the child on the screen and
have no white rim; stickers are collectible, arrive already coloured, and keep
the rim. Twenty-four planned; sixteen made.

**Commercial model: three lines, in order** — printables first, professional
licences second, family subscription third. It is one content library packaged
three ways, so **every piece of content is authored three ways at once**:
interactive, printable, and professional application note.

**Branding is endorsed**: ColorHugs by Ricardina Correia. Three lockups —
plain for children, `colorhugs-parents.webp` for families,
`colorhugs-professional.webp` for practitioners. No endorsement on child
screens.

---

## What is open right now

**My Inner World / How Do I Feel? is designed** — increment 20 of the decision
log holds it, and the rules there apply to every activity built after it. The
three expressions exist: the activity spec, the printable (a seven-card deck),
and the professional note at
`docs/materials/como-me-sinto-nota-aplicacao.md`.

**What that activity still needs before it can be built:** the artwork
regenerated without text (D-110). The account question is answered (D-202) and
the short trail now has somewhere to live — the device.

**Artwork:** all twenty-four stickers and all seven emotion cards are done. The
body map figure is done and passed the sealing test. Two avatars — penguin and
kite — remain withdrawn (D-079).

**Bigger questions, recorded in the decision log:**

- ~~**Q-010 Where the account system lives.**~~ **Closed by D-202:** commercial
  state on a server, the child's trail on the device and never synced. The short
  trail is unblocked; the Free boundary stays declared and not enforced until a
  backend exists.
- **Q-013 The "Brain Gym" name.** Brain Gym is a trademarked programme widely
  cited as pseudoscience in education. The audience most likely to recognise it
  is the one whose trust this product most needs.
- **Q-015 What happens when a child repeatedly reports distress.** Narrower
  now: with no intensity recorded, the question is about repetition, not
  severity. Still needs clinical and legal input.
- **Q-016 Can a child's drawing become a colouring page for other children?**
  Needs a legal position on consent.
- **Q-018 VAT on EU digital sales.** Needs an accountant before the first sale.
- **Q-026, Q-027, Q-028** — small and carried: the ashamed card's raised hand,
  three unresolved PT-PT words, and whether language is detected or asked.

## What I would like you to do first

Read the decision log — it now runs to **D-313**. Then tell me, in a few lines,
what you understand the state of the project to be, so I can check you have it
right before we carry on.

**Do not start building anything until we have agreed what.**

The next piece is the parents' book, unless I say otherwise.
