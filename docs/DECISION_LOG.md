# ColorHugs — Decision Log

Canonical version: **v1.1** (Permanent AI & Development Instructions)
Phase: **1 — Website / Web App Foundation**
Date: 2026-08-14

Status vocabulary: `[DEFINED]` approved · `[IMPLEMENTATION]` approved feature
being built · `[PROPOSAL]` awaiting approval · `[OPEN QUESTION]` needs a
decision from you.

---

## Implemented in this phase

### D-001 `[IMPLEMENTATION]` Stack
Next.js 14 (App Router), React 18, TypeScript strict, Tailwind CSS. No other
runtime dependency except `clsx`. **Impact:** deployable to Vercel, Netlify or
GitHub Pages; 42 pages prerender statically. **Reason:** matches the brief and
keeps the surface small enough to maintain.

### D-002 `[IMPLEMENTATION]` Content is data, not markup
`src/data/sections.ts` is the single source of truth for sections, activities,
artwork, plan level and build status. One section template and one activity
template render everything. **Impact:** a new activity is a data object plus a
sticker — no new component, route or layout work.

### D-003 `[IMPLEMENTATION]` Artwork prepared, never redrawn
Supplied files were flat RGB on white or black studio backgrounds. Backgrounds
were cut out programmatically, the white die-cut rim rebuilt, artwork trimmed
and converted to WebP. See `docs/ASSET_MAP.md`. **Reason:** sticker UI needs
transparency; the alternative was recreating the assets, which is forbidden.
**Reversible:** re-run `scripts/prepare-assets.py` from the originals.

### D-004 `[IMPLEMENTATION]` Missing artwork is flagged, never invented
`sticker.src: null` renders a dashed "Artwork pending" tile. **Reason:** rule
6 — approved assets are brand assets, and a substitute graphic would quietly
become one.

### D-005 `[IMPLEMENTATION]` Text always accompanies artwork
Every sticker button carries a real text label and caption; the illustration is
marked decorative so screen readers hear the label once. Status is signalled by
icon *and* word, never colour alone. **Reason:** accessibility, plus children
who are still learning to read benefit from consistent pairing.

### D-006 `[IMPLEMENTATION]` Navigation is flat and explicit
No hamburger, no dropdown, no hidden gesture. The homepage grid *is* the
navigation. Every page below the homepage carries a Back control pointing at a
fixed destination (not browser history) and a Home control.

### D-007 `[IMPLEMENTATION]` The adult area looks different on purpose
`/parents` uses its own shell: calmer palette, denser type, no sticker chrome.
**Reason:** a child should never be confused about which side of the product
they are on — and neither should a parent.

### D-008 `[IMPLEMENTATION]` Motion is feedback, not decoration
Hover lift, press-down, one entrance pop. No looping animation on interactive
elements. `prefers-reduced-motion` disables all of it.

### D-009 `[IMPLEMENTATION]` No third-party requests
No analytics, no ad technology, no tracking, no font CDN, no external scripts.
**Reason:** rule 11 of the phase brief plus data minimisation. Fonts resolve
from a rounded system stack until licensed faces are self-hosted.

### D-010 `[IMPLEMENTATION]` Honest build status
Activities are marked `planned` and their pages say so. **Reason:** rule 48 —
nothing should imply a feature exists before it does.

---

## Routine decisions taken without approval (rule 47)

- **D-011** Routes use full section slugs: `/learning-hub`, `/brain-gym`,
  `/my-inner-world`, `/kids-draw`, `/color-and-create`, `/my-colorhugs`,
  `/community`, `/parents`. The brief sketched `/learning`; the longer form
  matches the section name and reads better in a shared URL.
- **D-012** `images.unoptimized` is on, because assets are already sized and
  converted. Keeps static export working on any host.
- **D-013** Minimum tap target 64px, above the 44px accessibility floor, for
  smaller hands.
- **D-014** Section colour themes are CSS custom properties (`--sec-*`) set by
  one class per section, so a section's palette is a single edit.

---

## Needs your decision

### Q-001 `[OPEN QUESTION]` Is Color & Create a main section?
The Phase 1 brief lists seven sections and omits Color & Create. The permanent
instructions list it as an approved universe (rule 5) and place Imagine &
Create inside it (rule 23), and both the section sticker and banner exist.
**Currently built as a seventh child section.** Confirm, or tell me where else
it belongs.

### Q-002 `[OPEN QUESTION]` Kids Draw for Kids structure
The brief lists five items; the artwork supports eleven. I grouped them:
*Start Drawing* (Draw Your Own Idea, Drawing Missions) → *Drawing Missions*
(the six approved levels, fun-first, plus Surprise Mission) → *Kids' Gallery*
(See Kids' Drawings, Submit My Drawing). This preserves rules 15–17. Confirm
the grouping and the group names.

### Q-003 `[OPEN QUESTION]` What is `kidsdraws_surprise.png`?
Mapped provisionally to a "Surprise Mission" — the system picks a mission for
the child. It does not appear in any canonical list. Confirm the name and
whether it is its own activity or an entry point inside Drawing Missions.

### Q-004 `[PROPOSAL]` Free / Premium split
Placeholder assignment: roughly the first two activities of each area are Free,
the rest Premium; Imagine & Create is Premium (rule 23); everything in My
ColorHugs is Free, since progress should never be paywalled. This is a
planning placeholder only (rules 35–36) and sets no price or limit.

### Q-005 `[OPEN QUESTION]` Which "How Do I Feel?" master is approved?
Two near-identical files were supplied. The black-background version was used.

### Q-006 `[OPEN QUESTION]` Section taglines
Learning Hub's ("Read • Count • Discover") comes from its artwork. The other
six I wrote in the same rhythm as placeholders. They are child-facing copy and
should be approved rather than inherited from me.

---

## Deferred to later phases

- Authentication, adult account model, child profiles, consent capture.
  **Must be legally validated per jurisdiction before launch (rule 9).**
- Moderation pipeline for Kids Draw submissions, including human review.
- Imagine & Create: input moderation, output moderation, controlled prompting.
- Drawing Mission generation with an approved concept library and safety checks.
- Internationalisation (EN, FR, ES, PT-PT, PT-BR, ZH, HI) — the interface is
  ready for it; no strings are extracted yet.
- Progress, rewards and sticker book persistence.
- Advertising, if it survives child-safety validation (rule 37).
- Legal pages: privacy policy, terms, cookie posture.

---

# Increment 2 — Deployment readiness (2026-08-14)

Closes the last outstanding item of the Phase 1 brief: *deployment-ready
structure*, plus responsive verification.

### D-015 `[PROPOSAL]` App mark for small sizes
The full ColorHugs lockup is illegible below about 48px — at 16px it is a
coloured smudge. The favicon, app icon and PWA icons therefore use the yellow
smiley face **cropped from the approved logo** (`branding/colorhugs-mark.png`),
which reads cleanly at 16px. This is a crop and a circular mask, not a redraw,
but it does introduce a standalone mark, so it needs your approval. The full
lockup is still used everywhere it has room. **Alternative:** commission a
dedicated small-size mark.

### D-016 `[IMPLEMENTATION]` Social share image
`public/og.png` (1200×630) is a centre crop of the approved home banner. No
new artwork.

### D-017 `[IMPLEMENTATION]` Two deployment modes, one codebase
`npm run build` produces a normal server build; `npm run build:export` produces
a static `out/` for GitHub Pages (`BASE_PATH` handles project subpaths). The
mode is a build-time environment switch, so the choice stays reversible and
nothing is duplicated.

### D-018 `[IMPLEMENTATION]` GitHub workflow
`ci.yml` runs typecheck, lint and build on `main` and `develop` and on every
pull request. `deploy-pages.yml` publishes only from `main`, so the live site
always reflects an approved state. Site URL and base path come from repository
variables, never from committed values.

### D-019 `[IMPLEMENTATION]` Baseline security headers
`nosniff`, `strict-origin-when-cross-origin`, `SAMEORIGIN`, and a
Permissions-Policy denying camera, microphone, geolocation and interest-cohort.
**A Content-Security-Policy is still missing** and should be added alongside
the privacy work, before launch.

### D-020 `[IMPLEMENTATION]` Manifest stays in browser mode
`display: "browser"`, not `standalone`. An installed chrome-less app removes
the browser's own back button, and the child navigation model has not been
tested without it. Revisit when a native-feeling app is actually wanted.

### D-021 `[IMPLEMENTATION]` Robots and sitemap
Public pages are indexable. `/api/`, `/account/` and `/profile/` are disallowed
in advance, so the authenticated surfaces added in later phases are excluded
from day one rather than retrofitted.

### D-022 `[IMPLEMENTATION]` Responsive behaviour verified
Mobile 390px → 2 columns; tablet 820px → 3; desktop → 4. Section labels fit
without truncation at every width, including "Kids Draw for Kids", the longest.
Tap targets stay well above the 64px floor on the narrowest supported screen.

---

### Q-007 `[OPEN QUESTION]` Do you approve the smiley as the app mark?
See D-015. If not, the favicon needs its own commissioned artwork before
launch — the full lockup cannot do the job.

---

# Increment 3 — Community artwork (2026-08-14)

### D-023 `[IMPLEMENTATION]` Community section sticker integrated
Supplied artwork processed through the same pipeline as everything else
(background cut, rim rebuilt, trimmed, WebP). The `MissingArtwork` placeholder
is gone from the homepage. **Four missing assets remain:** Brain Gym / Memory
Challenge, My ColorHugs / My Progress, the Community banner, and the
Parents & Safety banner.

### D-024 `[DEFINED]` Community tagline comes from the artwork
"Together we share, together we grow" is on the ribbon in the supplied
sticker, so it replaces the placeholder I had written. It reads longer than the
other taglines, which is fine — it is the approved line, not interface copy.
This closes part of Q-006; the remaining five taglines are still mine and still
need your approval.

### D-025 `[IMPLEMENTATION]` Community sticker declared as `square`
The artwork is landscape (1000×783) while the other six section stickers are
square. Declaring it `wide` would give it a shorter tile and leave the
homepage row visibly ragged. It is declared `square` instead: `object-contain`
letterboxes it inside the standard tile, so all seven tiles match and nothing
is cropped or stretched. The trade-off is that the Community illustration
renders about 20% smaller than its neighbours. **If that bothers you, the fix
is a square-format export of this artwork — not a crop in code.**

---

# Increment 4 — Remaining artwork (2026-08-14)

All four outstanding assets supplied and integrated. **No `MissingArtwork`
placeholder appears anywhere in a build.** The fallback stays in the components
on purpose, so any future gap is still signposted honestly.

### D-026 `[IMPLEMENTATION]` Memory Challenge and My Progress integrated
Both processed through the standard pipeline. `Kidsdraw_memory.png` was never
reused for Brain Gym — it belongs to the Kids Draw *Memory Mission*, a
different activity in a different universe, and reusing it would have blurred
two content origins.

### D-027 `[IMPLEMENTATION]` Two new banners are padded, not cropped
`Faixa_community.png` (2.35:1) and `Faixa_parents.png` (2.50:1) are die-cut
compositions on white, unlike the six existing full-bleed banners. The banner
slot renders at 2.435:1 with `object-cover`, which would have clipped the star
at the far left of the Parents artwork. They are therefore padded with their
own background colour to the exact slot aspect before export — padding adds
nothing and removes nothing. Implemented as `PAD_TO_BANNER_ASPECT` in
`scripts/prepare-assets.py`, so the rule is visible rather than hidden in a
one-off edit.

### D-028 `[IMPLEMENTATION]` Parents & Safety banner used on the adult page
The adult area now opens with its approved banner, capped in width and sitting
above the same quiet, dense type as before. The adult area borrows the brand
mark, not the child interface — it must still be obvious at a glance which side
of the product you are on.

### D-029 `[IMPLEMENTATION]` Asset pipeline source is configurable
`scripts/prepare-assets.py` reads `COLORHUGS_SOURCE_DIR`, defaulting to the
original folder. New artwork can be processed from anywhere without editing the
script, and the mapping stays in one auditable place.

### Note on Q-006
The Community tagline came from its artwork (D-024). The remaining five
section taglines are still mine and still need your approval.

---

# Increment 5 — Open questions resolved (2026-08-14)

### D-030 `[DEFINED]` Color & Create is a main section — closes Q-001
Confirmed. Seven child-facing sections, Color & Create among them, and
Imagine & Create lives inside it.

### D-031 `[DEFINED]` Kids Draw for Kids structure — closes Q-002
Confirmed: *Start Drawing* → *Drawing Missions* → *Kids' Gallery*.

### D-032 `[DEFINED]` Surprise Mission — closes Q-003
Confirmed. `kidsdraws_surprise.png` is the Surprise Mission: the system picks
a mission for the child.

### D-033 `[DEFINED]` How Do I Feel? master — closes Q-005
The black-background 1536×1024 version is the master. Re-exported from the
supplied file; the white-background duplicate is retired.

### D-034 `[DEFINED]` Free / Premium — closes Q-004
Approved rule:

- **Free** — the entire Color & Create colouring library (all folders, not a
  sample), plus two or three activities in every other area.
- **Premium** — everything, sold weekly, monthly or yearly.

Applied as: two Free activities each in Learning Hub, Brain Gym and My Inner
World; Explore & Color entirely Free; Community Favorite Free.

Two consequences worth your attention, both decided in the spirit of the rule
rather than mechanically:

1. **Kids Draw for Kids — Free covers Draw Your Own Idea, See Kids' Drawings
   and Submit My Drawing.** All six mission levels and Surprise Mission are
   Premium. Making submission Premium would have starved the gallery: the
   artwork children see is contributed by children, so paywalling contribution
   shrinks the very thing that makes the section work. Creating and sharing
   stay open; the structured progression is the paid value.
2. **My ColorHugs is entirely Free.** Progress, stickers and trophies are a
   record of what a child did, not content to sell back to them. Locking them
   behind a lapsed subscription would mean a child loses sight of achievements
   they earned, which contradicts the rule that no achievement is ever taken
   away.

### D-035 `[DEFINED]` Section taglines come from the artwork — closes Q-006
My question was badly put, and the answer was in the assets all along. Every
section sticker carries its tagline on its own ribbon, so all six invented
lines are replaced with transcriptions:

| Section | Tagline | Source |
| --- | --- | --- |
| Learning Hub | Read • Count • Discover | ribbon |
| Brain Gym | Focus • Think • Solve | ribbon (my line said "Remember") |
| My Inner World | Discover • Grow • Shine | ribbon |
| Kids Draw for Kids | Drawn by Kids • Colored by Kids | ribbon |
| Color & Create | Draw • Color • Imagine | ribbon |
| My ColorHugs | Small Steps, Big Achievements! | ribbon |
| Community | Together we share, together we grow | ribbon |

No interface copy is invented at section level any more.

---

## New questions

### Q-008 `[OPEN QUESTION]` "Two or three examples" — activities, or items inside them?
Two readings, materially different for a child:

- **A — two or three whole activities per area are Free, the rest are locked.**
  This is what is currently built. Simple to explain and to bill.
- **B — every activity opens, but each holds only two or three Free items.**
  A child sees Story Time, Think & Solve and My Worries, and plays a couple of
  rounds of each.

**I recommend B.** A child on Free meets no locked doors, discovers the whole
shape of ColorHugs, and a parent sees exactly what they would be buying rather
than a wall. It is also gentler: locked tiles read to a young child as
"you can't", not "your grown-up hasn't bought this". The cost is a more
involved content model, since the gate moves inside each activity. If you pick
B, the change is small now and awkward later, so it is worth deciding before
activities are built.

### Q-009 `[OPEN QUESTION]` Weekly billing
Weekly plans usually cost two to three times more per year than yearly ones.
That is fine as an option, but if weekly is shown first it tends to read as a
trap to parents and undermines the trust the rest of the product is built on.
**I recommend** showing monthly and yearly by default, offering weekly as a
third choice, and displaying a per-month equivalent beside every price. Prices
themselves remain undecided.

---

# Increment 6 — Adult entry point (2026-08-14)

### D-036 `[DEFINED]` Parents & Safety lives at the foot of the page only
The link was duplicated: a button in the top bar and the "For grown-ups" strip
at the bottom. The top-bar button is removed, on every page, not just the
homepage — an inconsistent top bar would be worse than a duplicated one.

Beyond removing the duplication, this is the better place for it. A button in
the child's top bar invites taps that lead somewhere a child has no use for,
and the top bar is the one piece of chrome that follows them everywhere. The
adult door now sits where adults look for it, at the foot of the page.

**Parents still reach the area from anywhere:** the footer carries a
Parents & Safety link on every page, and `/parents` remains a direct URL. The
top bar is now the logo alone, which doubles as the route home.

---

# Increment 7 — The Free gate moves inside the activities (2026-08-14)

### D-037 `[DEFINED]` Sampling is per item, not per activity — closes Q-008
Every activity opens on Free. Most hold their first three items free; the rest
need Premium. A child never meets a locked tile, only a limit reached after
playing.

The data model changed to match. `plan: "free" | "premium"` on an activity was
the wrong shape — it described a door, and there are no doors any more. It is
replaced by `access`:

| Shape | Meaning | Where it applies |
| --- | --- | --- |
| `{ kind: "free" }` | no limit at all | Explore & Color, all of My ColorHugs, Draw Your Own Idea, See Kids' Drawings, Submit My Drawing, Community Favorite |
| `{ kind: "sample", freeItems: 3 }` | opens; first three items free | every activity in Learning Hub, Brain Gym, My Inner World, and all Drawing Missions |
| `{ kind: "premium", reason }` | cannot be sampled, and must say why | Imagine & Create only |

**Three is used everywhere rather than varying between two and three.** A rule a
parent can hold in their head — "the first three of most things are free" — is
worth more than a per-activity optimisation, and the number is one edit away if
testing says otherwise.

**Imagine & Create is the single exception, and it is a real one.** Every use
costs money and must pass input and output moderation, so a free sample is not
the same low-risk offer as three fixed items from a library — it is an open
tap on cost and on the safety pipeline. It carries the Premium badge and a
stated reason in the data, so the exception cannot quietly spread.

### D-038 `[DEFINED]` Premium badges disappear from sampled activities
A sampled activity now looks exactly like a free one, because to a child it
behaves exactly like one: it opens, and it plays. Only Imagine & Create carries
a badge.

### D-039 `[DEFINED]` The upgrade prompt addresses the grown-up, not the child
No child-facing screen shows a price or a payment button, anywhere. The one
plan message a child can see reads "Ask a grown-up to unlock this one", and
purchase lives entirely in the parent area. When a sampled set runs out, the
child is told the set is finished and pointed at their grown-up — never sold
to. **This is a standing constraint on every activity built from here on.**

### D-040 `[DEFINED]` Billing presentation — closes Q-009
Monthly and yearly shown by default, weekly offered as a third choice, and a
per-month equivalent displayed beside every price. Prices remain undecided.

---

## Open questions

None. Every question raised in this phase has been answered.

---

# Increment 8 — GitHub Pages deployment (2026-08-14)

### D-041 `[IMPLEMENTATION]` Artwork paths go through a base-path helper
A latent bug, found by building exactly as GitHub Pages will. Next applies
`basePath` to `<Link>` automatically, but **not** to `<Image>` when
`images.unoptimized` is on — the default loader returns the src untouched. On
a project page at `/colorhugs`, every sticker and banner would have 404'd while
the pages themselves loaded fine: a site that looks broken rather than one that
fails loudly.

All artwork now resolves through `asset()` in `src/lib/site.ts`, driven by
`NEXT_PUBLIC_BASE_PATH`. Manifest icon paths and `start_url` go through the
same helper. Verified against a real export: images, preload hints, routes and
manifest all carry the prefix, and the plain server build is unchanged.

**Repository:** `correiaricardina-ui/colorhugs` (public — it holds no secrets,
and `.gitignore` plus `.env.example` keep it that way).
**Published at:** `https://correiaricardina-ui.github.io/colorhugs/`

---

# Increment 9 — Pre-launch holding page (2026-08-14)

### D-042 `[DEFINED]` The domain shows a holding page until launch
`colorhugs.pt` serves a holding page; the real site is built under `/preview`,
unlinked from anywhere. Controlled by a repository variable, `SITE_MODE`:

| `SITE_MODE` | Result |
| --- | --- |
| `holding` | holding page at `/`, real site at `/preview/`, nothing indexable |
| *(cleared)* | the real site at `/`, indexable |

Chosen over unpublishing the site, which would have left a bought domain
returning GitHub's generic error page — a site that looks broken rather than
one that looks unfinished on purpose.

**One build, one deployment, one source of truth.** `scripts/assemble-holding.sh`
moves the export under `/preview` and drops the holding page at the root. There
is no second repository to keep in sync and nothing to undo by hand at launch:
clearing the variable and re-running the workflow is the whole switch.

### D-043 `[IMPLEMENTATION]` Nothing is indexable before launch
Two independent measures, because either alone has a gap. A root `robots.txt`
disallows all crawling, and every page in the preview build carries
`noindex, nofollow` — so a search engine that reaches `/preview` through a link
rather than a crawl still refuses to list it. Without this, Google would have
banked dozens of "Coming soon" pages before launch.

### D-044 `[DEFINED]` GitHub Pages cannot keep anything private
Stated plainly because it constrains every future decision: Pages is static
hosting with no server, so there is no password protection worth the name — any
gate would be client-side JavaScript with the content shipped alongside it.
`/preview` is unlisted and uncrawled, not secret, and the repository is public
regardless. **A genuinely private review environment would need different
hosting**, and that decision belongs with the authentication work, not before it.

---

# Increment 10 — Authorship and clinical credit (2026-08-14)

### D-045 `[DEFINED]` The credit appears in three places, at three weights
Ricardina Correia is credited as creator and clinical reviewer, linked to
`ricardinacorreia.pt`:

| Where | Form |
| --- | --- |
| Parents & Safety | full section with logo, placed **above** the safety commitments |
| Footer, every page | one quiet line with the link |
| Holding page | one line |

**Deliberately not on child-facing screens above the footer.** A child has no
use for an authorship credit, and anything extra on their screen is noise.

The credit sits first on the Parents page rather than last because a parent
deciding whether to trust the product looks for the person behind it before
reading the promises — the credential is what makes the commitments below it
credible. On a platform that calls itself psychology-informed, naming the
paediatric psychologist responsible is a trust signal, not a byline.

### D-046 `[DEFINED]` The credit states the work, not a clinical service
Wording: *"created and clinically reviewed by"*. The boundary is restated
immediately beneath it — psychoeducational tools, no diagnosis, no assessment,
no replacement for psychological care. **Claiming the credential is exactly the
moment the boundary is most at risk of blurring**, so the two travel together
and neither appears without the other.

All wording lives in `src/data/credits.ts`, so it reads identically everywhere
and changes in one place.

### D-047 `[IMPLEMENTATION]` Logo processed like every other brand asset
`Logo_RC.png` had a white background and heavy margins. Background flood-filled
to transparency and trimmed — no die-cut rim rebuilt, since this is a fine-line
mark rather than a sticker. The artwork itself is untouched.

External links open in a new tab with `rel="noopener noreferrer"`, and screen
readers are told so.

---

# Increment 11 — Account screens, designed not built (2026-08-14)

### D-048 `[DEFINED]` The gate sits on the action, not on the door
*(Supersedes the separate landing page and the `/play` move, both reversed.)*

The sticker grid is the root again, and a visitor browses it and every activity
page without an account. The account is required to **do** something — start an
activity, download, submit a drawing.

Three reasons this beats a login wall:

1. **It persuades better.** Seeing an activity convinces a parent far more than
   a form does. A wall means nobody can see what they would be buying.
2. **A child meets one door, not seven.** With a wall at the entrance, every
   sticker is a locked door. With the gate on the action, the child reaches the
   activity and meets a single, explained stop.
3. Rule 7 already drew this line: informational pages stay open, *interactive
   child use* requires an authorised profile. Browsing is not use.

Route map: `/` child universe (open to browse) · `/sign-in` · `/sign-up` ·
`/profiles` · `/[section]/[activity]` (open to read, gated to do) · `/parents`.

### D-049 `[DEFINED]` The signed-out band carries the parent's case
The grid alone shows *what* exists but not who made it, what it costs, or why
it is safe — the things that actually decide a parent. `SignedOutBand` sits
below the grid with the psychologist credit, three claims (no ads, no tracking,
no child chat), and the call to action.

**It renders only while nobody is signed in.** Once a child's profile is open
it disappears, along with the sign-in controls in the top bar, and the page is
the child's universe and nothing else. No selling, no credentials and no adult
controls follow a child around the product.

### D-050 `[DEFINED]` The flow has four steps, not two
The question assumed "user signs in". The approved account model makes it:

public page → sign in or create account → **adult account** → **choose child
profile** → child universe.

The profile picker is the piece the split-screen question left out, and it is
the most important one: it is where the adult hands over and steps back. It is
the only screen both of them look at together, so it is warm enough for a child
and clear enough for a parent.

### D-051 `[IMPLEMENTATION]` Split screen, with the product on the right
Form left; right carries the main banner, what ColorHugs is, who created it,
**all seven sections**, and three claims a parent rarely gets to read — no ads,
no tracking, no child chat. Real artwork throughout, not a decorative photo, so
the panel sells the product instead of filling space. Below `lg` it is dropped
rather than stacked: on a phone a parent wants the form, not to scroll past
decoration to reach it.

The count is read from the data rather than written by hand. A first pass
showed six sections under a heading promising seven — a small lie, on the one
screen where a parent is deciding whether to trust us.

### D-052 `[IMPLEMENTATION]` Nothing pretends to work
Every field is disabled and every screen carries a visible "Design preview"
notice. **A form that looks live but quietly does nothing is worse than no form
at all** — especially one asking a parent for an email address.

### D-053 `[IMPLEMENTATION]` Consent is marked, not implemented
The sign-up screen shows where verified parental consent goes and states that a
tick box is not enough and that the method depends on jurisdiction. Rule 9.
**Must be validated legally before launch.**

---

## Open questions

### Q-010 `[OPEN QUESTION]` Where the account system lives
Nothing on this page works until this is answered — see the conversation. It
also decides where the download limit is counted, and a limit counted in the
browser is a limit that can be erased by the child.

### Q-011 `[OPEN QUESTION]` Landing-page copy
The marketing wording on `/` is a first draft, written so the page can be
reviewed. It is adult-facing sales copy and needs approval, like the section
taglines did.

### Q-012 `[OPEN QUESTION]` Child avatars
The profile picker uses coloured circles with an initial. No avatar artwork
exists, and inventing a set would create brand assets by the back door.

---

# Increment 12 — Account screens rolled back (2026-08-14)

### D-054 `[DEFINED]` The account work is deferred; the design is kept
The sign-in, sign-up and profile screens, the action gate and the signed-out
band are **removed from the build**. So is any notion of counting downloads.
The site returns to what it was: the child universe at the root, the quiet
adult strip at the foot of it, and `/parents`.

**Removed rather than left dormant.** Disabled forms sitting in production age
badly — sooner or later someone finds them, and a form that asks a parent for
an email and does nothing is worse than no form. Nothing half-built stays
deployed.

**The design decisions stand.** D-048 to D-053 remain the agreed specification
for when accounts are built: gate on the action rather than the door, the
four-step flow through the profile picker, the split screen with the product on
the right, verified consent rather than a tick box, and no price or purchase
button on any child-facing screen. Rebuilding from that spec is a small job;
what took the thinking is written down.

Route map is back to: `/` child universe · `/[section]` · `/[section]/[activity]`
· `/parents`.

### Still open, unchanged
Q-010 where the account system lives · Q-011 landing copy (now moot until the
public page returns) · Q-012 child avatars.

---

# Increment 13 — Content design proposals (2026-08-15)

### D-055 `[PROPOSAL]` Content concepts for all seven universes
See `docs/CONTENT-DESIGN.md`. Every concept is written with the mechanism it
rests on and an honest evidence grade — established, reasonable, or practice.
Nothing is claimed more strongly than its support, because a psychology-informed
platform that overstates its science is worth less than one that has none.

Three flags raised there need decisions and are repeated here:

- **Q-013 `[OPEN QUESTION]` The "Brain Gym" name.** Brain Gym® is a trademarked
  educational programme and one of the most cited examples of pseudoscience in
  education. The audience most likely to recognise it — psychologists, teachers,
  SEN staff — is the audience whose trust the product most needs. Credibility
  and trademark issue both. Cheaper to change now than after launch.
- **Q-014 `[OPEN QUESTION]` Which languages get literacy content at launch.**
  Phonics cannot be translated; Word Explorer in seven locales is seven designs.
- **Q-015 `[OPEN QUESTION]` What happens when a child repeatedly reports intense
  distress in My Inner World.** Requires clinical and legal input before any of
  that section is built. No automatic alerting, no diagnosis.
- **Q-016 `[OPEN QUESTION]` Can a child's drawing become a colouring page for
  other children?** Strongest single idea in the proposals; IP and consent
  position needs legal advice.
- **Q-017 `[OPEN QUESTION]` Is any of My Inner World visible to a parent?**
  Argued no. A clinical judgement, not a product one.

### D-056 `[PROPOSAL]` Build Calm My Body first
Smallest activity with no AI, no moderation, no content library and no
child-authored input — the fastest route to one finished end-to-end activity.
One finished teaches more about the other thirty than thirty sketches.

---

# Increment 14 — Commercial model (2026-08-15)

### D-057 `[DEFINED]` Three revenue lines: printables, professional licences, family subscription
All three, in that order. See `docs/COMMERCIAL-MODEL.md`.

They are not three products competing for the same hours. **It is one content
library packaged three ways** — a deck of emotion cards authored once becomes
the content of an activity, a printable pack, and a session-ready professional
material. Each phase funds the next and none is thrown away when the next
begins.

### D-058 `[DEFINED]` Printables are a first-class format
No longer an extra at the end of an activity. Every activity designed from here
specifies its printable alongside its interaction.

### D-059 `[DEFINED]` Every piece of content is authored three ways at once
Interactive content, printable, and professional application note — written
together, not retrofitted. **This is the most important change to how the
design work is done from here**, and it applies to every area discussion that
follows.

### D-060 `[PROPOSAL]` An eighth area: the professional library
Adult-facing, separately licensed, with application notes on each material.
Does not exist in the current design. Required by Line B.

### D-061 `[DEFINED]` Licence tiers are settled before the first sale
Personal, professional, institutional — scoped as written in the commercial
model. Terms cannot be tightened retroactively once material is out.

### D-062 `[DEFINED]` The production constraint is authoring, not engineering
The engines are finite; the content is not. Anything that reduces authoring
time per piece is worth more than any feature.

---

## New open questions

- **Q-018** VAT and invoicing on EU digital sales — needs an accountant before
  the first sale, not after.
- **Q-019** Prices. Every figure is a reasoned starting point, not research.
  Ask five colleagues what they would pay for the professional tier.
- **Q-020** Where printables are sold: own site, marketplace, or both.
- **Q-021** Does the professional line share the ColorHugs brand, or sit under
  your own name — which already carries the credential the buyer is buying.

---

# Increment 15 — Endorsed brand lockup (2026-08-15)

### D-063 `[DEFINED]` ColorHugs by Ricardina Correia — endorsed branding
One brand, endorsed by the practitioner, rather than two brands competing.
Closes Q-021.

- **Child-facing screens: ColorHugs alone.** A child has nothing to do with who
  made it.
- **Adult-facing surfaces carry the endorsement**: parents area, printables,
  professional library, holding page, sales material.
- **The emphasis flips with the audience.** For a parent, ColorHugs leads and
  the credential reassures. For a psychologist it is nearly the reverse — the
  name is what gets the email opened, and ColorHugs is what it contains. Same
  block, different visual weight.
- **The two logos are never set side by side.** One is fine-line slate, the
  other is rainbow and rounded; adjacent they fight. The endorsed lockup, or
  the practitioner's own logo where she is the subject — never both at once.

### D-064 `[IMPLEMENTATION]` The endorsed lockup has a minimum size
Supplied lockup processed like every other asset and stored as
`colorhugs-parents.webp`. **Usable at 110px tall and above only.**
Rendered at the sizes the interface actually uses, the script line becomes an
unreadable smudge below that — noise without meaning. Navigation renders at
44–56px and keeps the plain lockup.

### Q-022 `[OPEN QUESTION]` A typeset variant for professional materials
The handwritten script reads warm, which suits families. On a licence sold to
psychologists it reads whimsical where it needs to read credentialed, and the
pale script sits close to the contrast floor for adult body text. Worth a
second variant with the endorsement typeset rather than handwritten, for the
professional line only.

### D-065 `[DEFINED]` Two endorsed lockups, one per audience — closes Q-022
The typeset version supplied on 2026-08-15 solves the professional-register
problem raised in Q-022, and it does something better than replacing the script
version: **the two of them are the audience flip in D-063, made concrete.**

- **Script lockup — families.** ColorHugs clearly dominant, the endorsement warm
  and secondary. Parents area, family printables, sales pages.
- **Typeset lockup — professionals.** The practitioner's name at near-equal
  weight to the brand, set bold in the brand navy. Reads credentialed rather
  than whimsical. Licensed materials, application notes, anything sold to
  practitioners.

Neither is a downgrade of the other; they are the same idea weighted for who is
looking. Navigation keeps the plain lockup at both.

Stored as `colorhugs-parents.webp` and `colorhugs-professional.webp` — named
for the audience rather than for the typography, so that in six months nobody
has to work out which is which.

---

# Increment 16 — How the colour works (2026-08-15)

### D-066 `[DEFINED]` The colour lives on the child's avatar, not on the screens
Earlier framing — every screen starting muted and gaining colour as the child
acts — was right in spirit and wrong in practice. Two objections, both correct:

- **Color & Create is exempt.** There the child is already colouring for real.
  A layer of symbolic colour on top of actual colour is redundant and confusing.
- **Everywhere else the colour has to mean something.** In a drawing mission it
  does. In a breathing exercise or an emotion choice, tinting objects at random
  is decoration pretending to be feedback.

**One constant place instead.** The child's avatar sits at the top of the
interface and gains colour as they use ColorHugs. One piece solves what a
per-screen rule could not, and it never has to be forced onto an activity where
it makes no sense.

### D-067 `[DEFINED]` Colour is earned by *having been*, never by how much
The avatar gains the day's colour for showing up and doing something —
**one activity or six, the same colour.**

Colour by quantity would have been scoring in disguise: a child who did one
thing and stopped would see a paler avatar than a child who did five, and
productivity would have re-entered through the side door after being kept out
of everything else.

What accumulates over time is **variety, not intensity** — different colours
from different areas, so a child who has wandered widely ends up painted in
many colours. It rewards exploring, which is what the product wants, and it
cannot be compared as a score.

In My Inner World the existing rule holds: the avatar gains colour for having
named a feeling, whichever feeling it was. "Furious" paints exactly as much as
"calm".

### D-068 `[DEFINED]` Art is produced flat, not in layers
Direct consequence of D-066. With the colour carried by one avatar rather than
by every illustration, no artwork needs a muted twin or separately paintable
parts. **Illustrations continue to be produced as single flat images**, as all
existing assets already are.

The avatar itself is the exception, and the only asset that needs to exist in
progressive colour states.

### Q-023 `[OPEN QUESTION]` What the avatar is
It is now the most-seen element in the product and the carrier of the whole
colour idea, so it is worth more thought than a placeholder circle. Options
range from a fixed ColorHugs character that every child shares, to a small set
the child picks from, to something the child assembles. Also open: whether it
is the same artwork as the profile picker avatars left open in Q-012.

### D-069 `[DEFINED]` Twelve avatars, seven zones each — closes Q-023 and Q-012
Six animals and six non-animals, all in the existing ColorHugs drawing style.
The child picks one; it is theirs, and it carries the colour.

**Seven paintable zones, identical on all twelve**, one per area:
head → Learning Hub · head-top feature → Brain Gym · chest patch → My Inner
World · arms → Kids Draw · torso → Color & Create · back feature → My ColorHugs
· legs → Community.

Identical zones are not a stylistic preference. **If one avatar had five zones
and another eight, a child who picked the wrong one would receive less colour
than her friend for the same work** — and the choice of avatar would quietly
become a choice about reward.

Chest for My Inner World is deliberate: it is where a child points when asked
where a feeling lives.

### D-070 `[IMPLEMENTATION]` Avatars are produced as line art and coloured by code
Supplied as outlines only — no fill, no shading, every region sealed by an
unbroken line. Colour is applied per zone at runtime.

**One file per avatar covers every possible state**: grey, one colour, seven
colours, any combination. The alternative — a generated image per state — would
have been well over a hundred files for twelve characters, and impossible to
keep consistent.

Prompts and acceptance checks: `docs/AVATAR-PROMPTS.md`.

### D-071 `[DEFINED]` No gendered avatars and no human skin tones
Hence animals, robots and creatures rather than boys and girls. It avoids
having to represent the whole range of human appearance in twelve characters,
and avoids doing it badly — while making sure no child looks at the picker and
finds nothing meant for them.

---

# Increment 17 — Twelve avatars supplied and tested (2026-08-15)

### D-072 `[IMPLEMENTATION]` All twelve pass the sealing test
Each drawing was analysed for enclosed regions — white areas sealed on every
side by black line, and therefore fillable by code. **No leaks in any of the
twelve.** Region counts run from 7 (penguin) to 24 (robot).

This was the failure most likely to appear and the hardest to see by eye: a
single gap in an outline lets colour flood into the neighbouring part, and it
only shows once the colour is applied.

### D-073 `[DEFINED]` Seven *chosen* regions per avatar, not seven identical anatomical zones
The original rule — head, ears, chest, arms, torso, back, legs, the same on all
twelve — does not survive contact with the artwork, and it should not. Five of
the supplied characters are objects: a house has no arms, a kite has no legs.

The rule that actually matters is the fairness one: **every avatar exposes
exactly seven paintable regions, one per area, of broadly comparable visual
weight.** Which seven differ per character, chosen from what that character has.
The anatomy was a convenience; the count is the constraint.

Where a character has more than seven sealed regions, the surplus small ones
are simply never painted — they stay white, like a highlight.

### D-074 `[OPEN QUESTION → resolved by artwork]` Consistency
Line weight and style are consistent across all twelve. Canvas sizes differ
(1254×1254 for the animals, 1086×1448 for the taller objects) and framing
differs slightly; both are normalised in processing, not in the artwork.

### Q-024 `[OPEN QUESTION]` Which seven regions on each avatar
Needs one pass through the twelve, deciding what gets which area. The chest is
the natural home of My Inner World on any character that has one; the objects
need a judgement each.

### D-075 `[DEFINED]` Every region is grouped; nothing is left permanently white
Choosing seven regions and abandoning the rest would have left the robot with
seventeen white parts for ever, looking unfinished even after the child had
done everything. Instead **all regions are grouped into seven**, so a child who
has visited all seven areas ends with a fully painted avatar.

Mapping: `scripts/mapping.py`. Ten of the twelve map cleanly to
head → Learning Hub · head-top → Brain Gym · chest → My Inner World ·
arms → Kids Draw · torso → Color & Create · back feature → My ColorHugs ·
legs → Community. The objects use their own equivalents — the car's windscreen
is its face, the house's door is its face, the rocket's fins are its arms.

### D-076 `[IMPLEMENTATION]` Assets exported as transparent line art plus fill points
Each avatar is stored once, as trimmed transparent outlines, with
`manifest.json` giving the points where each of the seven areas is filled.
**One file per avatar covers every possible colour state.**

### Q-025 `[OPEN QUESTION]` Two avatars need a small correction
- **Penguin — only six groups.** Its wings are part of the same sealed region
  as its head and back, so Learning Hub and Kids Draw cannot be separated, and
  it has no distinct head-top. It needs regenerating with the wings outlined
  separately from the body and a small tuft on the head.
- **Kite — seven groups, but two are arbitrary.** It has no back feature, so
  the tail bows were split between My ColorHugs and Community for want of
  anywhere better. It works, but the division means nothing.

Neither is urgent. Ten avatars are enough to build with.

### D-077 `[DEFINED]` Avatars are stickers without the white rim
Exported as transparent line art, so they sit on any background like the rest
of the ColorHugs vocabulary — but **without the white die-cut rim** the section
stickers carry.

The rim marks something as cut out and collectable. **An avatar is not
collected; it is the child on the screen.** Leaving it off keeps that
distinction readable without anyone having to explain it, and it matches the
artwork as supplied.

### D-078 `[DEFINED]` Where the avatar sits
Large on the home page, small on every other page. New colour appears on the
home page, when the child comes back from an activity — so returning home is
where the reward lands, which also gives a reason to go back there.

At 44px in a top bar, seven colours are indistinguishable; at home-page size
they read clearly. The mixture gets both: constant presence, and one place
where it is actually legible.

### D-079 `[DEFINED]` Penguin and kite withdrawn — ten avatars
Both are removed rather than patched. The penguin's wings share a single sealed
region with its head and back, so Learning Hub and Kids Draw could never be
told apart on it; the kite has nothing at the back, so two of its seven groups
were arbitrary.

**Ten avatars is a real choice for a child and a clean system.** A tenth of the
set carrying an invented rule would have cost more than it was worth.

Remaining: gato · coelho · urso · raposa · dino · robot · borboleta · carro ·
casa · foguetao — six creatures and four objects.

### D-080 `[PROPOSAL]` Twenty-four collectible stickers for launch
See `docs/STICKER-PROMPTS.md`. Grouped as: first visit to each area (7), tried
everything in an area (7), exploring (3), making (4), feelings (3).

### D-081 `[DEFINED]` No text on any sticker
The moment a sticker reads "Explorer" it needs seven translations and seven
regenerations, for ever. **Names are rendered by the app underneath the
sticker**, from the language file; the artwork stays language-free and is drawn
once.

This is the most expensive mistake available in this piece of work, and it is
invisible until the second language.

### D-082 `[DEFINED]` Nothing counted for a sticker can be lost
The return stickers count days the child came back — cumulatively, with no
penalty for gaps. **A streak that breaks is a punishment**, and rule 38 rules
those out. Everything else is participation and variety, so a child with
learning difficulties collects as many as the quickest child in her class.

### D-083 `[DEFINED]` Stickers keep the white rim; avatars do not
The rim means *cut out and collectable*. Stickers are exactly that; an avatar
is the child on the screen. The two families stay visually distinct without
anyone having to explain the difference.

---

# Increment 18 — Certifications and seals (2026-08-15)

### D-084 `[DEFINED]` Certification is a pre-launch goal
Recorded so it is not forgotten. See `docs/CERTIFICATIONS.md`.

**Two of the three suggested seals do not apply, and one no longer exists.**
Checked rather than assumed:

- **Selo de Segurança Digital / eSafety Label** certifies *schools*, not
  websites or companies. ColorHugs cannot apply.
- **Selo Protetor (CNPDPCJ)** is awarded to *entities* with competence in child
  and youth matters — so the candidate is Ricardina Correia's practice, not
  colorhugs.pt. Still worth having: it attaches to the name that endorses the
  platform. Next window likely early 2027.
- **Great Websites for Kids (ALSC/ALA)** was retired and folded into Notable
  Children's Digital Media.

Realistic targets instead: **kidSAFE Seal Program** (designed for children's
websites and apps, with an FTC-approved COPPA tier and an AI seal), and
inclusion in ALSC's Notable Children's Digital Media.

### D-085 `[DEFINED]` Design to the criteria now, certify later
Almost everything these programmes require, ColorHugs has already decided to do
— verifiable consent, no behavioural advertising, no third-party trackers, data
minimisation, no child-to-child contact, human review before publication.

**That only stays cheap if it is designed in.** Retrofitting consent flows and
data practices to pass an audit is where certification becomes expensive. The
kidSAFE AI seal is worth keeping in view while Imagine & Create is designed,
for the same reason.

### D-086 `[DEFINED]` Never display an unearned seal
No badge, and no phrasing implying assessment that did not happen. On a product
for children sold on trust, a false mark is not a shortcut — it ends the
proposition.
