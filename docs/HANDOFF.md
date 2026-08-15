# ColorHugs — Handoff

Paste this as the first message of a new conversation, and upload
`colorhugs-phase1.zip` with it.

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

**Live.** `colorhugs.pt`, hosted on GitHub Pages from the repository
`correiaricardina-ui/colorhugs`, deployed by a GitHub Actions workflow. I
manage commits through GitHub Desktop.

**In holding mode.** The repository variable `SITE_MODE` is set to `holding`,
so the domain shows a "coming soon" page and the real site is built at
`colorhugs.pt/preview/`, unlinked and not indexed. Clearing that variable and
re-running the workflow puts the site live.

**Built:** Next.js 14, TypeScript, Tailwind. The homepage, seven section pages,
thirty-one activity placeholder pages, and the Parents & Safety area. All
artwork processed and wired. Nothing is faked — placeholder activities say so.

**Not built:** any actual activity, accounts, payments, moderation, and
internationalisation.

---

## The rules that keep applying

These recur constantly. Apply them without being reminded.

**Child safety over everything.** No advertising, no behavioural tracking, no
third-party scripts, no child-to-child messaging, no publication without human
review, no diagnosis or assessment ever.

**No price and no purchase button on any child-facing screen.** When a free set
runs out the child is told the set is finished and pointed at a grown-up.

**Nothing is scored, ranked or taken away.** Rewards are for participation and
variety, never performance. No streaks that can break — a streak that breaks is
a punishment.

**No text inside artwork.** Names come from the language file. A sticker that
reads "Explorer" needs seven translations and seven regenerations, for ever.

**Evidence is graded honestly** — established, reasonable, or practice. Never
claim more than the support. A psychology-informed platform that overstates its
science is worth less than one that has none.

**Never display a certification seal that has not been earned.**

**Approved artwork is never redrawn or replaced.** It can be processed —
background removal, trimming, format conversion — but not reinvented. If
artwork is missing, say so and show an honest placeholder.

---

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

**Immediately, in My Inner World** — this is where we were working:

1. Can a child see what she felt before? (We decided the parent cannot.)
2. The remaining emotion cards: seven families are specified, the ~28 finer
   words are not.
3. The printable and the professional note for *How Do I Feel?*, designed
   alongside the activity rather than after it.

**Artwork still to generate:** eight stickers — six rosettes and numbers 15 and
16 — using `docs/STICKER-PROMPTS.md`. Then the seven emotion family cards using
`docs/EMOTION-CARD-PROMPTS.md`.

**Bigger questions, recorded in the decision log:**

- **Q-013 The "Brain Gym" name.** Brain Gym® is a trademarked programme widely
  cited as pseudoscience in education. The audience most likely to recognise it
  is the one whose trust this product most needs. Needs deciding.
- **Q-010 Where the account system lives.** Nothing about logins or download
  limits can work until this is answered.
- **Q-015 What happens when a child repeatedly reports intense distress.**
  Needs clinical and legal input before My Inner World is built.
- **Q-016 Can a child's drawing become a colouring page for other children?**
  The strongest idea in the content design; needs a legal position on consent.
- **Q-018 VAT on EU digital sales.** Needs an accountant before the first sale.

---

## What I would like you to do first

Read the decision log. Then tell me, in a few lines, what you understand the
state of the project to be — so I can check you have it right before we carry
on.

Do not start building anything until we have agreed what.
