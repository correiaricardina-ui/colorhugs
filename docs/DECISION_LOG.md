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

---

# Increment 19 — Emotion families (2026-08-15)

### D-087 `[DEFINED]` Seven emotion families
Happy · Sad · Angry · Scared · Ashamed · Calm · Bored.

Proposed six, requested ten. Seven is the resolution, and the reasoning
matters: **three of the four requested additions are not families, they are
words inside one.** Anxious and shy live inside *scared* — same family, finer
word, which is exactly the granularity the activity is built on. Excited lives
inside *happy*. Disgusted lives inside *angry* or *scared* depending on context.

Two are genuinely their own: **ashamed**, which is not fear and is the emotion
most often arriving disguised as something else; and **bored**, which fits
nowhere and appears constantly with nowhere to go.

Seven is also the ceiling for a choice screen used by a four-year-old who
cannot read. More than that and a child picks the first icon or the one she
recognises, rather than searching for the one that matches — which defeats the
activity. It coincides with the seven areas, which gives the product one number
instead of two.

*Calm is deliberately included although it is a state rather than an emotion: a
child needs to be able to say she is fine without having to be happy, and it is
where Calm My Body leads.*

### D-088 `[DEFINED]` One character, changing only expression and posture
Every card is the same heart character — the face the My Inner World sticker
already establishes. **If each emotion were a different animal, the child would
be comparing animals.** With one character the only variable is the feeling.

It has arms and legs because a face alone cannot carry shame or boredom: shame
is looking down and turning away, boredom is slumping.

### D-089 `[DEFINED]` The feeling must survive greyscale
Colour on these cards is a recognition aid, never the meaning. Every card is
checked with the colour removed — if the feeling becomes ambiguous, the posture
is not doing enough. A child who cannot distinguish the colours reads every
card, and nothing depends on knowing that blue means sad.

Prompts: `docs/EMOTION-CARD-PROMPTS.md`. Seven families first; the ~28 finer
words inherit from them and are written once these are settled.

### D-090 `[IMPLEMENTATION]` Sixteen collectible stickers accepted, seven rejected
Accepted and stored in `public/assets/stickers/collectible/`: all seven
first-visit stickers, the Learning Hub rosette, and numbers 17–24.

Rejected, with reasons:
- **Target, speech bubbles, folder, clipboard** — outlines are navy, not black.
  Measured: the accepted sixteen return RGB 0,0,0; these return 13–23 on the
  blue channel. Side by side at small size they read as a different family.
- **Magnifying glass and alarm clock** — correct style, but not on the list, and
  the clock face carries numbers that are illegible at 100px.
- **Trophy** — correct style, but carries a blank ribbon banner. A blank banner
  is an invitation to write in it, and sooner or later someone does. The prompt
  block now forbids them explicitly.

Brain Gym arrived as a brain with a lightbulb rather than a sweatband, and
without a face. Accepted: it reads clearly and is distinct from the others.

Community shows three hands in different skin tones. This does not conflict
with the no-skin-tone rule for avatars — that rule exists so twelve characters
do not have to represent the whole range of human appearance. Here the
diversity is the content.

Still to generate: six rosettes and numbers 15 and 16.

### D-091 `[DEFINED]` Handoff document
`docs/HANDOFF.md` briefs a new conversation on the project state, the standing
rules, and what is open. Written so the reasoning survives a change of context,
not just the conclusions.

---

# Increment 20 — My Inner World: How Do I Feel? (2026-08-15)

The first activity designed all three ways at once, as D-059 requires.

## Artwork closed

### D-092 `[IMPLEMENTATION]` The twenty-four stickers are complete
The eight outstanding pieces arrived: numbers 15 (compass) and 16 (footprints),
and the six remaining rosettes. With the Learning Hub rosette already accepted,
all seven are in.

**One spec correction, not an art correction.** The prompt for #13 asked for a
rosette with a star at its centre; the artwork came with the sticker album. The
artwork is right and the prompt was wrong — the block rule says each rosette
carries the same motif as its first-visit pair, and #6 is an open album. A star
would have broken the only rule that makes the rosettes read as the older
siblings of the first-visit set. `STICKER-PROMPTS.md` is corrected.

### D-093 `[DEFINED]` Ashamed and bored regenerated; only sad carries a tear
Both failed review and both were regenerated. Measured, not judged by eye.

- **Bored** carried almost no colour: 0.9% of pixels had real hue, against
  25–36% across the accepted five. Next to six bright cards it would have read
  as *disabled*, not as a feeling — the one card a child might not touch
  because she thinks she cannot. The specified colour changes from
  *warm grey-beige* to a **muted olive-khaki, `#A89B5C`**. Not a mustard:
  beside the happy yellow a dull mustard reads as a dirty version of it.
  After regeneration: 35.9% coloured pixels, mean luminance 141 — the second
  darkest card after angry, which helps it in greyscale.
- **Ashamed** was drawn facing forward, rubbing its eyes: a second *sad*.
  D-088 specified looking down and turning away. Shame is the emotion D-087
  added precisely because it arrives disguised as something else, so drawing it
  as crying returns it to the disguise, and a child would have faced two crying
  hearts with no way to choose. Regenerated with the gaze averted, one hand
  shielding the side of the face, and no tear.

**New acceptance rule: only sad carries a tear.** It is that card's strongest
signal and it only works while it is unique to it.

Both new cards were measured for flatness as well: luminance spread within the
body is 11.2 and 9.4, against 11.3–14.4 across the accepted five. They are as
flat or flatter, contrary to first impression. Canvas is 1254×1254 against
1092×1092, normalised in processing as with the avatars (D-074).

### Q-026 `[OPEN QUESTION]` The ashamed hand may read as a wave
Open palm, fingers spread, at head height. With the averted eyes and the down-
turned mouth it probably holds, but only a four-year-old settles this. If it
reads as a greeting in testing, the fix is small: turn the palm inward against
the cheek. Not worth regenerating for now.

---

## The principle underneath the section

### D-094 `[DEFINED]` A material for a child alone must close itself
The standard is not *infallible* — no activity is, on paper or on screen. The
standard is that **when it fails, it fails safe**: a child who abandons it,
picks at random, or does not understand it ends up no worse off than she
started.

From that, the distinction that actually separates the child version from the
professional one is **not depth**. It is whether the material closes itself or
opens deliberately. A material for a child alone has to end. A consultation
material does the opposite on purpose — it opens something and leaves it on the
table, because there is a person there whose job is to pick it up. **It is the
clinical relationship that closes, not the material.**

Practical rule: **naming can stand alone; exploring cannot.** "What are you
feeling?" closes. "Why do you feel that?" does not — it needs a listener, and
without one it is a child who has opened something in front of a screen.

Four tests for anything built for a child on her own:

1. If she leaves halfway and never comes back, is anything left open?
2. Does it ask *why*, or ask for an account of what happened? A free-text box
   is the most likely way this enters without anyone noticing — a child writing
   what happened at home is telling nobody.
3. Does it **interpret**? Naming is description. Telling a child what it means,
   or what to do next, is a person's work.
4. Does it ask for **intensity**?

### D-095 `[DEFINED]` Family printables follow the child-alone rules
The tempting arrangement is three degrees of mediation: interactive for the
child alone, print for the family, notes for the psychologist. It is wrong.
**A printable, once downloaded, does not choose who is in the room.** A sheet
sold to families can end up with a child alone at the kitchen table and the
adult next door.

So family printables obey the child-alone rules. **Only material licensed to
practitioners may open.**

### D-096 `[DEFINED]` No intensity in the child-alone version
Closes test 4 above. No scales, no 1-to-5, no "how big", no heart sizes. The
child names; she does not grade. Grading may live in licensed material, where
someone reads it.

**This narrows Q-015.** Without intensity the product has no signal of what
counts as "intense distress" — it knows only which family was chosen and how
often. That is the right information not to have: a system that can measure
emotional intensity in a child is one that sooner or later someone wants to
fire an alert, which is automatic assessment and forbidden by rule 12. Q-015
becomes a question about repetition, not about severity.

### D-097 `[DEFINED]` A short trail, never an aggregate
The child can see the last few cards she chose — the same cards, in order, and
nothing else. No counts, no percentages, no charts, no "your most frequent
feeling", no monthly view, no week-on-week comparison.

**The line that matters is not between storing and not storing; it is between
trail and aggregate.** A trail says "these were the days". An aggregate
produces a sentence about who the child is, and *"you felt sad 12 times this
month"* has the shape of a diagnosis. The line is easy to hold now and almost
impossible to walk back once someone asks for a nice chart.

Arguing for the trail: a child who sees she was angry on Monday and is calm
today learns that feelings pass, which is one of the few genuinely useful
things psychoeducation can give a small child. Arguing against: rumination,
self-labelling, and performance if she knows it is recorded. The short trail
without aggregation is the version that keeps the first and avoids the second.

**Evidence: practice.** That naming feelings helps is well supported; that
*reviewing one's own record* helps a child is practice, not established
evidence, and the professional note says so.

### D-098 `[DEFINED]` Nothing in My Inner World is visible to the parent — closes Q-017
Confirmed as a clinical judgement.

**The parents page must say so out loud.** A parent who looks for the record
and finds nothing assumes it is broken. Stated plainly it stops being a gap and
becomes a promise — and it is the sentence that makes the decision hard to
reverse by accident when someone proposes a weekly summary next year. Wording
in `docs/materials/parents-my-inner-world.md`.

The printable does not contradict this. If the child fills in the sheet and the
parent sees it, she showed him. **The product does not report; the child is not
required to hide.**

---

## The activity

### D-099 `[DEFINED]` How Do I Feel? is free with no limit
`{ kind: "free" }`, replacing `{ kind: "sample", freeItems: 3 }`.

Under the sample rule, the fourth time a child wanted to say how she felt the
product would have told her the set was finished and to ask a grown-up. **An
activity that exists so a child can name what she feels cannot have a limit on
how many times she may feel.** And the message would arrive precisely to the
child who came back most often.

The three-item rule works when the item is a piece of a library — three
stories, three challenges, three missions. It fails when the "item" is an act
of the child rather than content of ours. What sells in My Inner World is the
library: the fine words, the breathing exercises, the materials.

### D-100 `[DEFINED]` The activity closes after the family; the fine layer is optional
The seven families work for a four-year-old because they are drawings. The fine
words are words — *frustrated*, *disappointed*, *nervous* do not differ by
posture, they differ by meaning. **So the fine layer is for a child who reads,
and we ask nobody's age.**

Chosen: the activity closes after the family choice. A child who wants more
taps again. A child who does not read never reaches it and loses nothing,
because the activity has already closed.

Rejected: unlocking by declared age (collects more personal data than needed,
and reading does not track age — there are six-year-olds who read and
nine-year-olds who do not). Deferred: audio carrying the fine words, which
solves reading but costs seven recordings per word for ever (rule 19).

The reason is not technical. **If the activity only closed after the fine word,
the child who cannot read would be left with an unfinished activity** — the
child with the most difficulty getting the worst version. This way everyone
ends in the same place.

It also makes the fine layer exactly what is sold in My Inner World, without
any child meeting a wall: she has already named what she feels and already been
met before the layer exists for her.

### D-101 `[DEFINED]` The fine vocabulary is written per language, not translated
It became visible only at this layer, because the seven families are universal
and are drawings.

English *ashamed* and *embarrassed* are two useful things; Portuguese
*envergonhado* carries both. Portuguese separates *chateado* from *zangado*
where English has no single word. *Com saudades* has no equivalent in six of
the seven planned locales and is one of the most useful words a Portuguese
child has.

Consequences:

- **The art holds**, because no card carries text (D-081). This is where that
  rule pays for itself.
- **~28 is a number per locale, not a global one.** A family may have four
  words in Portuguese and three in English. The data model must allow different
  counts per family and per language from the start; assuming four fixed breaks
  silently on the second language, with someone force-translating a word no
  child says.
- It is closer to **pedagogical adaptation than translation**, in the rule 10
  sense. That is authoring work, which is the real constraint (D-062), and
  worth knowing before promising seven locales.

Criterion for admitting a word: **the child must already have heard it**, even
if she does not use it. The layer names what she already feels; it does not
teach new vocabulary. An unknown word means she picks by the drawing, and the
data is lost.

### D-102 `[DEFINED]` PT-PT vocabulary, first pass — 23 words
Written in PT-PT first, because that is where the ear for what a Portuguese
child actually says is finest, and it is the one thing here that cannot be
verified from outside. English is written later as its own set, not as a
translation of this.

| Family | PT-PT fine words |
| --- | --- |
| Feliz | contente · entusiasmado · orgulhoso · aliviado |
| Triste | desiludido · sozinho · com saudades · magoado |
| Zangado | chateado · irritado · furioso |
| Assustado | nervoso · preocupado · tímido |
| Envergonhado | culpado · arrependido · embaraçado |
| Calmo | tranquilo · descansado · seguro |
| Tédio | aborrecido · farto · impaciente · sem vontade |

Twenty-three, not twenty-eight. The estimate was made in English; the count is
per language, which is the point.

**Deliberately excluded:** words that are only *more* of the same — terrified,
petrified, furious-beyond-furious. That is intensity, and intensity is out
(D-096). Admitting them through the fine layer would let back in by the side
door what was kept out at the front.

### D-103 `[DEFINED]` Tédio is the PT-PT family label; Bored stays canonical
*Aborrecido* in European Portuguese means both *having nothing to do* and
*cross with someone*. A child tapping the khaki heart could mean either.

*Tédio* is unambiguous but adult — no seven-year-old says it. That is fine,
because **the child never reads the family name; she sees the card.** The label
is read by the author, by colleagues, and by whoever writes the material, and
those are exactly the places where the ambiguity costs.

So: **Tédio** as the PT-PT label, *aborrecido* moves inside the family as a
fine word, where it is the word a child actually says. The child-facing label
under the card stays **Aborrecido**, because the drawing beside it removes the
ambiguity.

**This is a PT-PT correction only.** *Boredom*, *ennui*, *aburrimiento* do not
carry it. The canonical deck name stays *Bored* — written down so that nobody
translates *Tédio* back in six months and reintroduces the problem.

### D-104 `[DEFINED]` Card order is fixed
Feliz · Calmo · Triste · Assustado · Zangado · Envergonhado · Tédio

**Fixed, not shuffled.** A five-year-old learns where her card is and goes
straight there; shuffling to "avoid priming" would take away the only advantage
she has. It also makes the printed deck and the screen the same object, which
is half the value of the bridge to consultation.

**Not grouped by valence.** Pleasant on one side and unpleasant on the other is
tidy and teaches the wrong thing — that feelings divide into good and bad. The
reward system already paints the avatar identically for *furious* and for
*calm* (D-067); the grid cannot say the opposite.

Happy first because it is easiest and teaches the gesture. Calm immediately
after, so a child who is fine without being cheerful finds her card at once
instead of defaulting to happy. Sad, scared and angry in the order a small
child recognises them. Ashamed after angry, because it arrives later
developmentally and most often hides behind the one before it. Tédio last
because it belongs nowhere, and with no neighbour to be confused with.

**Layout:** three columns with the last row centred, label always beneath the
card, never inside it. Seven in a grid otherwise leaves one card alone with an
emphasis it has not earned.

### Q-027 `[OPEN QUESTION]` Three words unresolved
- **Which family *chateado* belongs to.** The most used word a Portuguese child
  has and the most ambiguous: it serves for mild anger, for sadness and for
  boredom. Placed in *zangado*. It may belong in *Tédio* instead, or be useful
  enough to sit in two families — which sets a precedent we may not want.
- **_Embaraçado_ is the weakest word on the list.** A seven-year-old rarely
  hears it. It is there because English separates *ashamed* from *embarrassed*
  and Portuguese does not, and without it the family has two words. Flagged
  rather than replaced with something invented.
- **No child's word for injustice.** "Não é justo" is the most common cause of
  a child's anger and Portuguese has no single childlike word for it;
  *injustiçado* and *revoltado* are adult. Either the family lacks its most
  frequent trigger, or one card becomes a short phrase instead of a word — not
  serious, since no card carries text and the length is only a label question.

---

## The body map

### D-105 `[DEFINED]` The body map is in; the location is not stored
The child may point to where in her body she feels it. It survives the four
tests of D-094: pointing is descriptive, not interpretive.

**It does not enter the short trail.** The trail holds the cards, in order, and
nothing else. Storing location as well would give a record with two
dimensions — emotion and place — which is the shape of a clinical instrument,
and from there the distance to someone asking for a pattern is short.
**The map is the moment; the card is the record.**

### D-106 `[DEFINED]` A neutral outline figure, five zones
Not the avatar: ten avatars, five of them objects, and a house has no chest —
the child who picked it would get a different activity from her friend. Not the
heart character either: it *is* the emotion, and pointing to where the emotion
lives inside the emotion does not read.

A **neutral outline figure**: no face, no hair, no clothing, no gender, no skin
tone. The same solution D-071 found for the avatars, applied here — a figure
that represents nobody in particular is the only one that leaves no child out.
Without a face it also does not compete with the card.

Five zones: **head · chest · stomach · arms and hands · legs and feet.** The
child touches where she feels it and the zone lights in the colour of the card
she chose.

**Throat deliberately excluded.** The lump in the throat is one of the most
recognisable signals, but at phone size a neck zone is too small for a child's
finger, and a zone that misses reads as the app not listening.

No white die-cut rim (D-083 — this is interface, not a collectable). Sealed
line art coloured by code (D-070), so one file covers every state.

### D-107 `[IMPLEMENTATION]` The figure passes the sealing test at the second attempt
**First version: one fillable region, not five.** Paint poured into the chest
reached the head, both arms, both hands, both legs and both feet. The internal
lines were floating — they never met the outer outline at either end — and
there was no line at the neck or the waist at all. Black ink was 2.41% of the
image against 5.2–6.1% on the avatars, so the line was also too fine for the
family.

This is the D-072 failure again: it looks right until the colour goes in.

**Second version passes.** Eight sealed regions inside the figure, grouping to
the five zones — head, chest, stomach, arms (two), legs (two). No colour
crossed between them. Black ink 5.76%, in family.

A ninth region exists: a **sliver of neck** between the chin line and the
shoulder line, 0.18% of the area. Sealed, so not a defect — but an orphan, and
D-075 already settled this for avatars: nothing is left permanently white, or
the figure looks unfinished even after the child has done everything. **Grouped
with the head in processing**, its adjacent larger zone. No regeneration
needed.

The corrected prompt is in `docs/AVATAR-PROMPTS.md` under *Body map figure* —
its instruction that every internal line must touch the outer outline at both
ends is what fixed it, and it belongs in every future line-art prompt.

---

## The other two expressions

### D-108 `[DEFINED]` The printable is a seven-card deck, with the weekly sheet secondary
Chosen over the fill-in weekly sheet as the core.

The deck closes itself, asks no why, interprets nothing, and a child alone at
the kitchen table is not worse off for it — which is the D-095 requirement. The
weekly sheet needs marking and probably writing, and so brings an adult into
something that had to work without one. It stays in the pack, but it cannot be
what the pack *is*: a pack whose core needs an adult fails exactly when the
adult is absent.

**And the deck survives the seventh language.** No card carries text, so it
prints identically in every locale — one PDF, two language files, seven cards
drawn once. The weekly sheet is headers, weekdays and instructions, all of it
text. The piece that survives translation is the one without words, which is
the D-081 economy appearing again somewhere else.

Printed in black and white the card is also a colouring page: the child colours
the heart whatever colour she likes rather than the one we gave her. Not
decided, but it costs nothing.

### D-109 `[DEFINED]` The professional note is a material note with a separated practice section
Not a protocol. The buyer is a psychologist: she knows how to run a session;
what she does not know is whether this material is any good and what it can be
claimed to do. Selling her a script sells her the thing she is better at than
we are. A protocol also runs close to rule 12 — a note advising what to do when
a child repeatedly picks the blue heart is one step from saying what that means.

What makes it valuable is the honest grading, not the volume.

**The boundary, since some usage suggestions are included:** the note may
**suggest uses, never interpret responses**. "Some colleagues leave the deck on
the table with no instruction" is use. "If the child repeatedly picks the same
card, consider X" is interpretation and stays out. The test: does the
suggestion describe what the psychologist does, or what the child revealed?

Suggestions sit in their own visibly separated section, labelled **practice**.
Interleaved with the rest, the reader gives everything the same weight and the
honest grading — which is the value — is lost.

Written in PT-PT rather than English, unlike the documentation: it is licensed
material, not documentation, and the first buyers are Portuguese colleagues.

`docs/materials/como-me-sinto-nota-aplicacao.md`. **References are not yet
cited by name.** The note describes the state of the evidence and carries a
notice that citations must be verified before licensing — a reference nobody
checked, in a document carrying a clinician's signature and claiming what the
science supports, is exactly the error that ends the proposition.

---

## Language and artwork

### D-110 `[DEFINED]` Activity artwork is regenerated text-free, once
The section stickers, activity stickers and banners carry English text baked
into the illustration — relief, double outline, shadow, one colour per letter.
It is paint, not a text layer. Replacing it is redrawing approved artwork,
which rule 6 and D-003 forbid, and any automated attempt would look nearly
right, which is worse.

**Nor is the answer a Portuguese set of the same artwork.** Seven section
stickers, thirty-one activity stickers and eleven banners is 49 pieces: 98 in
two languages, 343 in the seven priority locales, and every new activity would
cost seven generations instead of one, for ever, with style consistency
degrading each time. This is the D-081 mistake at full scale; the artwork
predates that decision.

**Half of it is saved by a distinction.** The seven section names work as
**wordmarks**, not as translatable copy — "My Inner World" behaves like
"ColorHugs": it is not translated, it is recognised. The app writes *O Meu
Mundo Interior* beneath the tile from the language file and the artwork is
untouched.

The thirty-one activity stickers do not survive that argument. "HOW DO I FEEL?"
is a question put to a child, not a mark, and it fills half the tile. **These
are regenerated without text, once**, then serve all seven languages with the
label drawn by the app. Not urgent — all are activities still to be built — so
each is regenerated as its activity is built, starting with this one.

### D-111 `[DEFINED]` The language switcher lives in the footer, not the child's top bar
A child taps the control, the product changes to a language she cannot read,
and the way back is now in that language. A five-year-old does not undo this;
an adult does, in ten seconds — but the adult is not there, which is the
premise of this whole section. The top bar is also the one piece of chrome that
follows her everywhere, and D-036 already removed the parents button from it
for the same reason.

**Language is a household setting, not a session choice.** A child does not
change language mid-afternoon; the family configures it once. So it sits in the
footer and in `/parents`, where D-036 already put the adult door, reachable
from any page and in nobody's way.

Two safeguards: the control names languages **in their own names** —
*Português*, *English* — never translated and never by flag alone. Flags are
the usual choice and are wrong: PT-PT and PT-BR share a language and not a
flag, and a flag names a country, not a language. And **changing language
changes nothing the child made** — not the avatar, not the stickers, not the
trail. Worst case is a strange page for a minute, not a loss.

### Q-028 `[OPEN QUESTION]` Detected or asked on first visit
Detecting from the browser is smoother and is almost always right; asking is
explicit but puts a chooser in front of someone who only wanted to see the
site. Blocks nothing.

---

## Still open, carried forward

Q-010 where the account system lives · Q-013 the Brain Gym name · Q-014 which
languages get literacy content · Q-015 repeated distress, now narrowed to
repetition rather than severity · Q-016 a child's drawing as a colouring page ·
Q-018 EU VAT · Q-019 prices · Q-020 where printables are sold · Q-025 penguin
and kite corrections · Q-026 the ashamed hand · Q-027 three PT-PT words ·
Q-028 language detected or asked.

---

# Increment 21 — How Do I Feel? built (2026-08-15)

The first activity in the product that is not a placeholder.

### D-112 `[IMPLEMENTATION]` Built without the trail
The short trail (D-097) is not implemented. It waits on Q-010, because a trail
kept in the browser vanishes when someone clears history — **the child comes
back and the product has forgotten her**, which is worse than never having
offered it.

So this version stores nothing at all. The child picks a card, points if she
wants, is thanked, and it closes. Everything else in the design holds: no
intensity, no why, nowhere to write, no correct answer, no interpretation, and
the body location is never a record (D-105).

It is honest as it stands rather than half-finished: nothing on screen implies
a memory that does not exist. What it cannot yet teach is the thing the trail
was for — that feelings pass.

### D-113 `[IMPLEMENTATION]` Activities are a registry, not a route
`src/components/activities/registry.ts` maps `section/activity` to a component.
Anything absent renders the honest `ComingSoon` placeholder. Adding a built
activity is one line plus its component, which keeps D-002's discipline: the
route, the chrome and the way back are written once.

### D-114 `[IMPLEMENTATION]` The language file exists — `src/i18n/`
Title, tagline and every child-facing word for this activity now come from
`src/i18n/strings.ts` in EN and PT-PT, with English as the fallback while a
locale is unwritten. An untranslated line is honest; an empty one is a bug.

Locale is React context plus one stored key, read after mount so the
prerendered HTML is not contradicted. **Changing language touches nothing the
child made.**

The switcher sits in the footer, names each language in its own language, and
uses no flags (D-111).

**Not yet localised:** the navigation, the footer and the section pages. Those
strings are still written into components, and the screenshots show it — the
Portuguese activity sits under an English "Back to My Inner World". Recorded
rather than hidden.

### D-115 `[IMPLEMENTATION]` The body figure colours by stacked shapes, not canvas
Five zone silhouettes are exported alongside the outline and tinted with CSS
beneath it. One outline and five shapes cover every state, with no canvas and
no script — it works on static hosting.

**A trap worth recording.** Cutting the white background is not enough for this
figure. The white *inside* it is sealed, so it is not connected to the border
and survives the cut as opaque white — which would sit on top of every coloured
zone and hide all of them. The outline is therefore exported as **line only**,
with alpha taken from darkness so the anti-aliased edge survives. First
composite check came back blank, which is how this was found.

`scripts/prepare-emotions.py` runs the sealing test on every build of the
artwork and **refuses to export** if a zone is missing or if arms or legs
resolve to one region instead of two — a merged pair being exactly the leak the
test exists to catch.

### D-116 `[DEFINED]` The primary button names what it does
Before a zone is chosen it reads *I would rather not say*, because a child never
has to point at her body. Once she has chosen, it becomes *Done*.

The first build offered the skip as the only way forward, so a child who had
answered was still being asked to give up. A control should say exactly what
happens when it is used.

### Q-029 `[OPEN QUESTION]` The section banner still says HOW DO I FEEL?
The English wordmark now sits directly above the Portuguese title, which is
D-110 made visible. This activity's artwork is the first that should be
regenerated text-free.

---

# Increment 22 — How Do I Feel? gains substance (2026-08-15)

The built activity lasted twenty seconds and gave nothing back. It kept every
rule and kept them by being thin, and a product a child uses once protects
nobody.

### D-117 `[DEFINED]` Three paths, because the feelings are not the same kind of thing
- **Difficult** — sad, scared, angry, ashamed → a **strategy**, offered as a
  choice: *which would you like to try?*
- **Good** — happy, calm → **moments when I feel like this**, choosing the one
  that matters most.
- **Boredom** — its own path, **what I could do now**.

All three end in a colouring page, on screen or downloaded.

**Why not strategies everywhere.** Strategies only on the unpleasant feelings
would teach that some feelings need fixing and others do not — valence
returning by the side door, after D-104 refused it in the grid and D-067
refused it in the avatar. A child who says *angry* and gets three things to do,
and says *happy* and gets nothing, learns which one the product prefers.

The moments path is not a consolation prize: choosing when I feel like this is
savouring, which has a literature of its own.

Boredom is neither difficult nor good, and it is the **only** feeling where the
answer may be another part of ColorHugs. A bored child with nothing to do is
well served by "draw something silly"; a sad child must not be redirected into
an activity, and a happy one does not need distracting.

Boredom is also rarely a lack of stimulation — more often a lack of meaning or
of choice, a child with things to do and none that interest her. That argues
against a list of ready suggestions, which is the obvious answer, and in favour
of a real choice between a few genuinely different options. Mostly adult
research: **reasonable**, not established.

### D-118 `[DEFINED]` Offer, not instruction; literacy about the feeling, never about the child
*Which would you like to try?* closes and leaves the choice with her. *Do this*
decides for her, and deciding what a child should do next is a person's work
(D-094, test 3).

The literacy line is about the feeling in general. "Sometimes people feel angry
when something seems unfair" is description. "You are angry because…" is
interpretation, and it is where this breaks.

### D-119 `[DEFINED]` The pages live in Explore & Color and are visible there
Not a new activity: a group inside Explore & Color, which already exists, is
already free in full, and whose `group` field the model already has.

**Visible, not unlocked.** Hidden, the choice inside the activity becomes a
reward, and a child starts choosing the feeling that yields the drawing she
wants — destroying the only honest thing the activity records. Visible,
choosing in the activity stays a choice about what helps.

### D-120 `[DEFINED]` Pages are named for what they show, never for the feeling
A page called *When I am angry*, or a folder called `angry/`, makes the
downloaded file report what the child chose. No screen would say it, but a
parent finding that PDF knows — and D-098 promised the product does not report.
The child showing her drawing is one thing; the file announcing itself is
another.

A drawing of slow breathing is a drawing of breathing. **The link between
feeling and page lives in data** — `src/data/colouring.ts` — never in the
filename, the folder, or the page.

It also lets one page serve several families: slow breathing belongs to angry,
scared and sad. One strategy, one drawing, three links.

### D-121 `[DEFINED]` Evidence decides the number of strategies, not symmetry
Integrity over economy, explicitly: more drawings and more links are acceptable
if that is what the literature supports.

**The families will not have equal numbers of strategies, and must not be made
to.** Four for angry and one for ashamed is a legitimate outcome. A symmetrical
grid would look tidy and would be a lie.

An honest caution about the literature: most research on children's emotion
regulation compares **strategies** — distraction, reappraisal, suppression —
rather than establishing which strategy suits which emotion. The
emotion→strategy map is largely clinical extrapolation, so many cells will
grade as *practice*, and the professional note must say so.

Two exclusions, recorded now so they do not creep back in later:

- **Discharging anger by hitting something.** The catharsis idea is the first
  thing most children's apps reach for, and the literature points the other
  way: it raises arousal rather than lowering it. Unwritten, it returns on its
  own, because it is the picture everyone has of "dealing with anger".
- **Cognitive reappraisal as a young child's strategy.** Among the most studied
  in adults and developmentally out of reach at five.

And one distinction to hold: **shame is not guilt.** Guilt moves a child to
repair, shame moves her to hide, and a strategy built for one can make the
other worse.

### D-122 `[IMPLEMENTATION]` Emotion card scale is normalised by character mass
The seven cards were trimmed to their own bounding boxes — right for section
stickers, which are seven different subjects, wrong here. These are the same
character seven times, compared side by side: if happy renders smaller than
bored, the child reads a size difference that means nothing.

Keeping the original canvases does not fix it either; they were generated at
two sizes and framed from 0.64 to 0.85 of frame height.

Normalised by **ink area** — the character's mass — because raised arms make
happy wide and short while bored slumps narrow and tall, and area is the only
measure that means the same across all seven poses. One shared fit factor
brings the largest inside the canvas; shrinking only the overflowing ones would
undo the normalisation. All seven now sit at 50.0% ink on an identical square.

### Q-030 `[OPEN QUESTION]` The printable needs revisiting
The seven-card deck (D-108) was the right core for a twenty-second activity. It
is too small for what this has become. Recorded now rather than discovered
later.

---

# Increment 23 — Anger, and audio (2026-08-15)

### D-123 `[DEFINED]` Angry — the first family authored
**Literacy line, about the feeling and never about the child:**

> Anger usually turns up when something seems unfair, or when we wanted
> something badly and could not have it. It arrives fast and takes longer to
> leave than it took to come.

The second sentence earns its place: arousal rises quickly and falls slowly,
and a child who knows that does not conclude a strategy failed because it did
not work in five seconds.

**Strategies, each with what actually supports it:**

| Strategy | Support |
| --- | --- |
| Go and tell someone | Base **established** — young children regulate *with* an adult, not alone. This gesture helping in the moment: **reasonable** |
| Move away from it | **Reasonable** — changing the situation rather than enduring inside it |
| Look at something else, count slowly | **Reasonable**, and probably the strongest here for four- and five-year-olds; attentional deployment is the mechanism in the classic delay research |
| Slow breathing, longer out than in | **Reasonable in adults, practice in children.** The most popular strategy in children's products and the evidence is thinner than the popularity implies |
| Move the body — run, jump, climb | **Practice.** Ships with the distinction written down: moving is not hitting |

**Excluded: hitting a pillow or anything else.** The catharsis literature points
the other way — discharging like that raises arousal rather than lowering it.

Five drawings, named for what they show: two people sitting and talking · a
quiet corner with cushions · fingers counting · a feather falling slowly · a
child jumping.

**What authoring one family revealed, and it is uncomfortable.** No cell
reaches *established*. One base does; no application does. And the only
well-supported thing is that **a small angry child regulates with another
person** — the best evidence points off the screen.

### D-124 `[DEFINED]` "Go and tell someone" stays, and the reason reframes it
Argued against on the grounds that the product cannot guarantee anyone is
there, and a suggestion that fails is worse than none.

Overruled, correctly: **the strategy teaches that there is always someone to
go to** — at home, at school — and that holds even in a minute when the room is
empty. The drawing follows the reframing: not two particular people, but the
idea that someone exists. It likely needs a second adult who is not a parent,
since school is half the argument.

### D-125 `[DEFINED]` Everything written can be heard
No longer a comfort feature. The fine vocabulary and the literacy line were
written for a child who reads, and **we ask nobody's age** (D-100). Without
audio, the child who cannot read gets the smaller version of the activity, and
she is the one who needs it most.

**Chosen: files generated at build time.** Rejected: the browser's own voice —
free and file-free, but on several systems synthesis happens on a server, which
means a child's text leaving her device, and D-009 says her browser talks to
nobody. Quality would also vary by device with no control.

**Recorded human voice supersedes it, one line at a time.** Files are named
from the string key — `feelings.families.angry` →
`/assets/audio/pt-PT/feelings.families.angry.mp3` — so a real recording at that
path replaces the generated file with **no code change**. Ricardina's own voice
can arrive piece by piece, starting with whatever matters most.

**Two rules, fixed now because they erode later:**
- **Nothing plays by itself.** A child presses to hear. Sound that starts on
  its own startles, and starting it for her decides what she needs.
- **The button appears wherever there is text**, not only where we judge it
  necessary — otherwise we are deciding which children can read.

Where no recording exists the button is **absent, not broken**. A control that
fails when pressed teaches a child not to press anything.

**No placeholder voice is bundled.** A robotic stand-in would be worse than
silence: it looks finished, so nobody replaces it. `scripts/prepare-audio.py`
takes the engine as configuration and reports what is missing.

### D-126 `[IMPLEMENTATION]` The language file is JSON
`src/i18n/en.json` and `pt-PT.json`, with `strings.ts` reduced to types and
loading. A translator edits JSON and never opens a TypeScript file — and the
audio script reads the same source the screen reads, so the spoken and written
lines cannot drift apart.

### Q-031 `[OPEN QUESTION]` Which lines get the real voice first
Not everything needs recording at once. The seven family names and the literacy
lines are the strongest candidates; the interface furniture matters least.

### D-127 `[DEFINED]` Piper generates the audio, locally
Chosen over a cloud service (ElevenLabs, Google, Azure). Those sound better —
some pass for human — but they cost money, need a key that cannot live in the
repository (rule 44), and add a vendor and an account to maintain.

Piper runs locally, needs no account, and nothing leaves the machine, which
keeps D-009 true behind the scenes as well as in the browser.

**The deciding argument was not quality.** The generated audio is a bridge
until a recorded voice exists, and a bridge does not justify a vendor, a key
and an invoice. With a paid service every correction to a word costs something,
and people start avoiding edits to the copy — the opposite of what is wanted
while the content is still being written. With Piper, changing a word
regenerates the line for free.

**A recorded voice remains the destination, without blocking anything.** It is
now explicitly a later project: files are named from the string key, so a real
recording dropped at that path replaces the generated one with no code change,
one line at a time, in whatever format it was recorded.

**Implementation notes.** Piper writes WAV; the script converts to MP3 when
ffmpeg is present and keeps WAV otherwise. The manifest records the real
filename including extension, so any format drops in. Existing files are never
overwritten — a real recording already sitting there is the whole point.

Pick a **pt_PT** voice, not pt_BR. They are different localisations (D-101),
and the accent is the one difference a child notices immediately.

**Not verified here:** the model host is unreachable from this environment, so
the Piper command flags were checked against the installed CLI but no voice was
downloaded and no line was generated. The first real run needs watching.

---

# Increment 24 — Colouring pages: two routes and a floor (2026-08-16)

### D-128 `[DEFINED]` Angry's five drawings, and the sealing test applied to pages
Named for what they show, never for the feeling (D-120): `talking-together` ·
`quiet-corner` · `counting-fingers` · `floating-feather` · `jumping`.

No white rim — these are pages, not collectables — and every region must be
sealed, because a child colours them on screen and colour leaks through any
line that fails to meet another.

Four passed the leak test at the first attempt. **The hand failed completely**:
the two wrist lines ended in mid-air, so the hand was one open shape continuous
with the background — tap the palm and the whole page fills. The same failure as
the body figure, in the most obvious place a hand can have one.

The regenerated hand closed the wrist and **arrived with the numerals 1–5 drawn
beside the fingers**. Removed, for two reasons. It is text inside artwork, which
is the rule that cost thirty-one regenerations (D-110) — and numerals do not
survive translation either, since two of the seven priority locales do not
always write them this way. More importantly it changes what the page is: the
strategy is *look at something else and count slowly*, where counting is
somewhere to put attention, not an exercise. With numbers the page teaches
counting to five, and the child who cannot count yet gets a task instead of a
rest. That is Learning Hub entering My Inner World by the side door.

### D-129 `[DEFINED]` Six fillable areas, official library only
Tap-and-fill gives a child exactly as many colours as the drawing has sealed
regions. Measured across the five: hand 1, conversation 4, corner 9, jumping
15, feather 19. **The hand gave one colour and nothing else to do.**

So: **at least six fillable areas** in any page published in the official
ColorHugs library, with every internal dividing line touching the outer outline
at both ends.

**Scope, decided deliberately.** The official library only. Imagine & Create
cannot guarantee it — no model does — and enforcing it there would mean
re-generating on failure, at real cost, in the most expensive feature we have.
A child's own drawing in Kids Draw for Kids almost never has six sealed
regions and often has none. **Those two depend on the brush instead, and
downloading is offered prominently, because paper is where they work best.**

**On paper the rule does not apply.** With crayons, a one-region hand is a whole
hand to colour however you like. The limit belongs to the screen, and rejecting
good art because of it would be a mistake.

`scripts/prepare-colouring.py` **refuses to export** a page below six. A rule
nobody checks is not a rule.

**A floor on the areas, learned the hard way.** The first version of the checker
passed the numbered hand — the five hollow digits counted as five areas, so
1 + 5 = 6. The hand was still one region and still gave one colour. A fillable
area must now be at least 0.5% of the image to count. Without a floor the rule
is trivially gamed, and the thing that gamed it was not a person.

### D-130 `[DEFINED]` The brush is no longer optional
Not as the first mode: tap-and-fill stays the accessible one, because a
four-year-old does not have the finger control for a brush and going outside
the line twenty times is defeating. But the brush is what makes it possible to
colour a drawing that cannot obey the six-region rule — which is every
AI-generated page and every child's drawing. Without it, D-129's scope decision
leaves those two with nothing.

### D-131 `[DEFINED]` Every published page has both routes
**Colour it on screen, or download the PDF.** Neither is a fallback for the
other: some children have a printer and crayons and no patience for a screen,
and some have the opposite.

PDFs are generated at build time from the same line art — A4, centred, 300 dpi,
static files needing no server and no JavaScript. For Imagine & Create and Kids
Draw the download is not merely available but **encouraged**, since those are
the pages the brush serves and paper serves better.

**No title and no feeling name on the page.** By D-120 the file must not report
what the child chose. Only the quiet ColorHugs mark belongs there.

### Q-032 `[OPEN QUESTION]` Encouraging download of another child's drawing
D-131 encourages downloading in Kids Draw for Kids — which means one child's
artwork travelling to strangers' devices as a file, beyond any later
withdrawal. Q-016 already needs a legal position on consent for reuse; this
raises the same question with the added fact that a downloaded file cannot be
taken back. **The encouragement should not ship for Kids Draw until Q-016 is
answered.** It is uncontroversial for Imagine & Create, where the child
downloads her own page.

### D-132 `[IMPLEMENTATION]` Angry's five pages, at the fourth attempt
Passed: hand 7 areas, feather 11, corner 11, jumping 13, conversation 21. Ink
5.3%–8.6%, one family, no leaks. Each exported as a WebP for the screen and an
A4 PDF for printing.

**What the three failed attempts taught, and it is mostly about prompting.**

*Round one* — the hand was one open shape: the wrist lines stopped in mid-air
and colour poured out to the whole page.

*Round two* — the closed hand arrived with the numerals 1–5 beside the fingers.
Text inside artwork (D-110), and it changed what the page taught: counting is
somewhere to put attention, not an exercise.

*Round three* — the two people pages came back gendered, both reading as boys,
one as a boy with his dad. **Instructive tension:** dividing a person into
colourable areas nearly forces clothing, because an unclothed outline body has
few natural divisions. Clothing stays; hair was the gender signal — and hair is
itself a colourable area, which helps reach eight.

*The bald detour was my error.* The plain round head is right for the body map,
where it is interface a child sees for a second, and wrong for a page she sits
with for ten minutes: there it reads not as *any child* but as *no child*. And
I had taken the thin object pages as the style reference and told the people
pages to slim down — backwards. The reference is the ColorHugs stickers and
logo: thick, even, rounded. The people pages were closer to right than the ones
I was matching them to.

*Round four* also needed **a fresh conversation.** "No hair" from an earlier
turn kept being carried forward despite the new prompt asking for hair. Two
prompting lessons worth keeping: state what **must** exist rather than
describing how it should look — "every figure must have hair, bald is wrong"
works where "simple hair" does not; and list forbidden details one by one,
since "simple face" returned eyebrows, ears and a nose.

**Minor, not blocking:** the jumping page's ground line stops short of the left
edge, and in the quiet corner the cushions cross the wall/floor line so wall
and floor read as one area.

### D-133 `[IMPLEMENTATION]` A general library folder in Color & Create
`artwork/colouring/library/` → `public/assets/colouring/library/`, for pages
that answer to no activity and are simply good pages to colour. First two:
`elephant` (12 areas) and `playing-football` (12 areas), both passing the
six-area rule.

Kept separate from `strategies/`, `moments/` and `now/` so that a page which
belongs to no strategy cannot drift into looking like one. A page filed under a
strategy but answering to none would be unreachable from the activity and
misleading in the data.

---

# Increment 25 — The strategy step, and the colouring canvas (2026-08-16)

### D-134 `[IMPLEMENTATION]` Angry's path is built end to end
Card → body map → literacy line → choose a strategy → colour the page, on
screen or on paper. The other six families still close after the body map,
because they have no pages yet — which is honest: nothing on screen implies
more exists.

The literacy line is general, never about this child (D-118), and the
strategies are offered — *which would you like to try?* — never instructed.

### D-135 `[IMPLEMENTATION]` The colouring canvas
Two layers: a paint canvas beneath, the line art as a plain image on top. The
line art is never painted over, which keeps flood fill simple and undo cheap.

**Fill is bounded by the line art, not by the paint.** A pixel is a wall where
the drawing is dark. This is exactly why D-129 exists: an unsealed line is not
a wall, and the colour runs across the whole page.

Both modes on every page (D-130). **Undo, and a limit of twelve steps** — with
fill a wrong tap is fixed by another tap, but a wrong brush stroke crosses the
drawing, and a child who ruins her page after ten minutes does not come back.

**Nothing is saved.** Same reason as the short trail: nowhere to put it until
Q-010, and work that vanishes when someone clears history is worse than work
never promised. What she makes can be downloaded.

Twelve colours, chosen to include a brown and a dark grey so that skin and hair
can be coloured plausibly by more children than a primary-colour set allows.

### D-136 `[DEFINED]` The colouring is not kept — closes Q-033
Raised as a gap: the child paints, leaves, and it is gone; the PDF downloads
blank rather than as she coloured it. **It is not a gap.**

The download exists so she can colour *by hand, on paper* — not so a record of
what she coloured on screen follows her home. The blank PDF is not an
incomplete version of her painting; it is a different thing, for a different
place, with crayons and a table.

This is the same decision as the activity itself (D-112), applied to the
drawing: **it happens in the moment and does not stay.** And it extends the
division already drawn between screen and paper — paper carries what lasts, the
screen carries the moment. That split now earns its keep twice.

It also removes a whole class of problem rather than deferring it. Nothing to
moderate, nothing to delete, nothing a parent finds. A child who paints the
whole page black leaves no trace: she painted, she left, it is done.

**It does not wait on Q-010** — this is not "nowhere to store it yet", it is
nothing to store.

**One thing to keep in view, without adding a dialog.** Ten minutes of painting
is lost by an accidental tap on *Start again*, and no warning is given.
Confirmation boxes are tedious and teach children to press *yes* without
reading. Undo already covers *Start again* exactly as it covers any stroke —
it is built that way, and that is the safeguard. Do not let a later change
break it.

### D-137 `[IMPLEMENTATION]` The PDF fills the sheet, and carries the mark
Two faults found by printing one.

**The drawing was a stamp in the middle of the page.** `Image.thumbnail` only
ever shrinks; the sources are around 1250px and the printable area is over
2000, so it left them at original size on an A4 sheet. Replaced with a fit that
scales up as well as down. A child colours with a crayon, not a needle.

**No mark and no small print.** The page now carries the ColorHugs logo and one
line beneath it, with a footer band reserved so nothing crowds the art.

**The line is deliberately language-neutral** — `colorhugs.pt · © year
ColorHugs`. A translatable sentence in the footer would mean seven versions of
every PDF, for ever: the D-081 trap in another form. And by D-120 nothing on
the page may name the feeling the child chose, so a parent who finds this file
learns nothing about her.

### D-138 `[DEFINED]` A wordless colour band heads the page
Two layouts were printed and compared: a band of the seven section accents at
the head with the mark at the foot, against the mark at the head with only the
small line at the foot.

**The band wins, and one reason only showed up on paper: the drawing comes out
measurably larger.** With the mark already at the foot, the head needs only a
thin band; putting the mark at the top costs space at both ends and shrinks the
art. On a sheet that exists to be painted, that decides it.

It also frames the page — without it the drawing floats — and it is the only
colour on the sheet, which suits the object: the paper starts with a little
colour and the child adds the rest.

**No title, in any variant.** *Go and tell someone* printed across the top would
tell anyone holding the sheet that the child chose angry. Same reason the pages
are named for what they show. And a wordless band costs no translation, where a
heading would mean a PDF per page *per locale*.

### D-139 `[IMPLEMENTATION]` Explore & Color is built, and holds every page
The whole library, free in full. Seven pages: the two general ones and the five
that a strategy leads to.

**The strategy pages appear here too** (D-119). Hidden, the choice inside How Do
I Feel? would become a reward to unlock, and a child would start choosing the
feeling that gives the drawing she wants.

**Named for the picture, never for the strategy.** The bench page is *On the
bench* here, not *Go and tell someone*; the feather is *Feather*, not *Breathe
slowly*. A child browsing the library has no reason to meet a feeling she did
not choose, and a name that carried its strategy would carry the feeling with
it (D-120). The same drawing therefore has two labels — its strategy name
inside the activity, its plain name in the library — and both live in the
language file, not in the artwork.

The canvas is the same component in both places, so a page gains fill, brush,
undo and the printable PDF by existing, with no per-page work.

### D-140 `[IMPLEMENTATION]` Jumping regenerated, and PDFs trim before scaling
The ground line now runs the full width — verified, not judged by eye: it
covers 100% of the image width and reaches both edges. Twelve fillable areas,
ink 5.3%, in family with the other four.

**Three phrasings of the same instruction were needed** to get it: state the
line spans edge to edge, state it must not stop short, and give the picture —
*think of it as the horizon*. One phrasing had failed twice.

**A second fault showed up only in print.** The child sat in the upper two
thirds of its square, so on A4 it printed noticeably smaller than the elephant,
which filled its own. How much of the sheet a drawing covered depended on how
the generator happened to frame it, not on the drawing.

The PDF step now trims the empty margin before scaling, with a small pad. Same
reasoning as normalising the emotion cards by mass (D-122): remove the
accident of framing so the comparison is between drawings.

**PDF only.** The WebP stays square, because the colouring canvas takes its
size from the image and assumes a square frame. Changing that would need the
canvas changed with it, and the print fault did not warrant the risk.

### D-141 `[DEFINED]` Twenty-four colours, in composed rows
Twelve was too few, and the elephant showed why: a child who wants to colour an
elephant reaches for a grey, finds none, uses whatever is nearest, and the page
quietly becomes a colour-matching exercise instead of hers.

**More colours cost nothing in tap-target size.** The grid stays six wide, so
swatches keep their width and only the panel grows taller. Swatch height went
from 48 to 56px at the same time.

The rows are composed rather than gathered:

1. **warm** — reds, oranges, yellows
2. **cool** — greens, blues, purples
3. **skin** — four tones, so a child can colour a person to look like someone
   she knows. Four is the least that is honest: a single "flesh" colour tells
   most of the world the product is not for them.
4. **hair, earth and neutrals**, ending in white — which doubles as an eraser,
   since the paint layer sits on white.

Row three matters more than the count. The neutral outline figure (D-106) has
no skin tone precisely so that no child is left out; a palette with one skin
colour would put that back the moment she starts painting.

---

# Increment 26 — What is sold, and the practitioner note (2026-08-16)

### D-142 `[DEFINED]` The essential of each feeling is free; depth is what sells
Proposed: a premium version of the angry activity. **Rejected as proposed**, for
two reasons.

**Incoherent.** The five strategy pages are already free in Explore & Color,
which is free in full (D-139). Gating them inside My Inner World would make the
same image paid in one place and open two taps away.

**And worse than incoherent.** A strategy for handling anger is help, not
content. Gating it means the child whose family does not pay goes without —
and she is very likely the child it is least defensible to take anything from.
A product that sells emotional help to children loses the thing that
distinguishes it.

**Never premium, written down now, before commercial pressure arrives:**
- **Naming what you feel** (already D-099).
- **The audio.** Gating it charges precisely the child who cannot yet read.
- **The first strategies of any feeling.**

**Premium is:**
- **The fine vocabulary** — the ~23 words inside the seven families. It fits
  exactly: the activity already closes before that layer (D-100), so no child
  meets a wall; it is real authoring work, which is where the cost is; and it
  is enrichment, not rescue. A child who says *zangado* has been helped; a
  child who wants *chateado* or *furioso* is going deeper.
- **Additional strategies beyond the first five** — the fifth, sixth and
  seventh way of handling anger is enrichment; the first ones are the essential.

The rule generalises to the six remaining families and to the rest of the
product: **the essential of each feeling is free; depth is what sells.**
Defensible to a parent, to a colleague, and to ourselves in two years.

### D-143 `[DEFINED]` The angry practitioner note, and the shape the other six follow
`docs/materials/zangado-nota-aplicacao.md`, in PT-PT, following D-109: a
material note with a visibly separated practice section, never a protocol.

**The skeleton every family reuses:**

1. *What the child meets* — the flow, and the literacy line quoted in full, so
   a practitioner knows exactly what was said to the child.
2. *The strategies, each with what actually supports it* — graded one by one,
   not as a block.
3. *What this material does not do* — no assessment, no scale, nothing kept,
   nothing visible to a parent.
4. *Limits* — including what is missing and what is weakest.
5. *Suggestions for use*, labelled practice, describing what the clinician
   does, never what the child's choice means.
6. *Misuse*, and the standing disclaimer.

**Section four is the one that must not be softened per family.** For angry it
says plainly that no cell reaches *established*, that the best-supported thing
in the set points off the screen, and that Portuguese lacks a child's word for
the feeling of injustice — leaving this family's vocabulary incomplete at the
point that matters most. A note that lists only strengths is worth less than no
note, because a practitioner who finds one overstatement discounts the rest.

Citations are still to be verified before licensing, as in the *Como Me Sinto?*
note. Recorded rather than filled in from memory.

### D-144 `[DEFINED]` The practitioner material is a workbook, not a note
Chosen over a short note with separate annexes. Two reasons: a colleague buying
this wants one file, not seven; and **we need to know what a whole family
actually costs**, which loose annexes hide. If angry comes to twelve pages,
that number times seven changes the plan, and it is better known now than at
the fourth family.

`docs/materials/zangado-caderno.md` replaces the shorter note. Eight sections,
in the order a session happens: what the child meets · the strategies with what
supports each · the arousal schema · exploratory questions · dynamics · a
clinician's sheet · limits · what the material does not do. Plus the five pages
as an annex.

**Exploratory questions were the hard case.** D-094 says exploring cannot stand
alone — but that governs material a child uses by herself. In a session there
is someone to receive it. The line that still holds: the workbook may suggest
**what to ask**, never **what the answer means**. "Ask her who she would go to"
is a question; "if she cannot name anyone, consider…" is a reading, and that is
the clinician's.

The questions are grouped by the strategy that prompts them rather than listed
loose, so they attach to what the child just chose.

**The clinician's sheet is for their notes, not a score.** It records what she
chose and said, never a rating, and is explicitly not to be filled in with the
child watching as though it were a test.

### D-145 `[IMPLEMENTATION]` The arousal schema is drawn in code, not generated
An image generator is the wrong tool: exact curves and clean type are what they
do worst, and this carries a clinician's signature. Drawn with a script —
`scripts/figure-arousal-curve.py` — so it regenerates when a word changes.

**No numbers and no tick marks on either axis**, with *esquema ilustrativo, não
representa medições* printed beneath. A graph with a scale looks like data, and
there is no data behind this shape. It is the visual form of the same trap the
evidence grading exists to avoid: better it look plain than look measured.

It carries one claim not in the child's literacy line — *aqui a estratégia ainda
está a agir, mesmo que ela ache que não* — which is the clinical reason to show
the schema at all, and which needs Ricardina's confirmation before licensing.

### D-146 `[DEFINED]` The workbook opens with a framing section, and no references
Written as synthesis, not review, with a notice that no reference is treated as
verified until it is. **References are not written from memory.** In a field
where error propagates easily, and in a document carrying a clinician's
signature, one invented citation destroys everything around it, including what
is correct — the same discipline as never displaying an unearned seal (D-086).

The framing states four things: anger is normal, early and functional, and the
aim is not to reduce it; **anger is not aggression**, which is the distinction
the whole workbook rests on; regulation begins as a two-person process, which
is why *go and tell someone* has the best base and why a digital material alone
has a ceiling worth admitting; and the five strategies map onto recognised
families of emotion regulation rather than being a list.

**That mapping revealed something useful.** Situation selection and
modification, attentional deployment and response modulation are all covered;
**cognitive change is absent** — reappraisal, developmentally out of reach for a
small child. The gap is a choice rather than an oversight, and it marks where
the material could grow for older children.

### D-147 `[DEFINED]` The workbook carries the fine words; the child's app gates them
Section 8 holds *chateado · irritado · furioso* in full. In the app the layer is
premium and optional (D-142); in the practitioner material it is included
entirely, because whoever applies it needs the whole vocabulary even when the
child meets only part.

**A tension the workbook now states out loud.** Those three words differ largely
by intensity, and intensity was deliberately excluded (D-096) — no *my anger is
a 5*. The defence is that the child **names** rather than **grades**: she picks
a word that already exists in her language, not a point on a scale. The
practical effect is close, and the workbook says so rather than hiding it.

Also recorded there: *chateado* serves for mild anger, sadness and boredom
alike, so a child saying it may be in any of the three (Q-027 remains open).

### D-148 `[IMPLEMENTATION]` The workbook cover, drawn in code
`scripts/figure-workbook-cover.py`, one command per family.

**Drawn, not generated**, for the same reason as the schema: a cover is
typography, and type is what image generators do worst. Garbled Portuguese on a
document carrying a clinician's signature is not a risk worth taking, and a
drawn cover regenerates when a word changes.

The illustration is the family's **own emotion card**, on a soft disc of its
colour — so the workbook is recognisable from across a desk and matches exactly
what the child sees on screen. That link is the point: the practitioner and the
child are looking at the same object.

**The endorsed professional lockup**, never the plain child-facing one
(D-063, D-065). The header band is the same seven accents as the colouring
pages, so every printed ColorHugs sheet reads as one family of objects.

**Positions are fixed rather than flowed.** Tested with *Envergonhado*, the
longest family name: flowed, a long title pushed the lockup into the text
beneath it. The first version had exactly that fault.

The script refuses to build a cover for a family whose workbook is not written,
unless forced. A finished-looking cover in front of a colleague, with nothing
behind it, is the kind of thing that gets shown by accident.

### D-149 `[DEFINED]` Kawaii is the house style, for every image in the project
Not a preference for stickers: **a rule for all artwork**, colouring pages
included. Rounded, plump, cute shapes with soft corners, and a **thick bold
outline of even weight**. A thin, delicate or varying line is wrong. A neat
generic colouring-book line is wrong.

**Consequence: the seven colouring pages must be regenerated.** The feather, the
hand and the cushions are generic line art of the kind found on any colouring
site. It was noticed and named earlier — *thin and generic* — without the
conclusion being drawn. Ricardina drew it.

Not wasted work: the scene prompts, the internal divisions and the six-area
rule all stand. Only the style block changes, and the checker already measures
the result in one command.

**One boundary, or this goes wrong.** Kawaii in the *shapes* — chubby
proportions, rounded corners, thick line — always. Kawaii *with a face* on
objects is case by case. A cushion with eyes and blushing cheeks is fine. **The
hand must not have a face**: it is the child's own hand, and a hand with eyes
stops being hers. The body map figure stays faceless by D-106, which this rule
does not override.

The style block for every colouring-page prompt from here:

```
STYLE — KAWAII, THICK AND ROUNDED
Cute kawaii style, the same family as a plump sticker: every shape is rounded,
full and slightly chubby, with soft corners and no sharp points or thin spikes.
Objects are drawn plump rather than realistic — a cushion is pillowy, a feather
is soft and full, a hand is padded.

THICK, BOLD black outline of even weight throughout, the confident chunky
outline of a sticker. A thin, delicate or varying line is WRONG. A neat generic
colouring-book line is WRONG. It must look hand-made and warm, not technical.

No colour, no fill, no grey, no shading, no gradient, no texture, no hatching,
no drop shadow.
```

### D-150 `[DEFINED]` The style is kawaii, Jellycat soft toy, cozy — and it has one home
Refined from D-149. **Jellycat** is not merely cute: it is *plush* — fat, full,
slightly lumpy, as though sewn by hand and lightly overstuffed, imperfect
rather than symmetrical. **Cozy** is calm and huggable rather than bright and
loud. Together they explain the earlier faults better than "kawaii" alone did:
the feather and the hand were not only thin, they were **rigid**. A Jellycat
feather is fat and soft; ours was a well-drawn feather.

**One exclusion the reference brings with it and must not keep:** no stitching,
no seams, no fabric tags. They would look right on a plush toy and would break
the rule that matters more — on a colouring page they are fine lines a child
cannot colour, undoing the requirement for large fillable areas. **The plush toy
is the feeling, not the subject.**

`docs/ART-DIRECTION.md` is now the single source for how artwork looks, and the
three prompt documents point at it. It also gathers what was scattered: the
face rules, the rim rule, sealing, the six-area floor, the prompting lessons,
and the standing instruction to verify by measuring rather than by looking.

**Also to revisit:** the body map figure was drawn before this rule existed. It
is a correct neutral outline and probably too rigid for the family it now
belongs to.

### D-151 `[IMPLEMENTATION]` The three generic pages redrawn in the house style
Hand, feather and cushions regenerated with the Jellycat block. All three pass:
7, 10 and 12 fillable areas, no leaks. The cushions now keep off the wall/floor
line, so wall and floor are two areas as intended.

The feather has a face and the hand does not, per ART-DIRECTION.md. The
cushions were left faceless: four identical faces would turn a quiet corner
into a crowd staring back.

### D-152 `[IMPLEMENTATION]` Line weight is measured by stroke width, not ink share
**Ink share was a poor proxy and it misled us earlier.** A simple drawing with
few lines has little ink even with a fat stroke: the new feather sits at 4.8%
ink and 8.2px of stroke, the elephant at 10.1% and 11.7px. Most of that gap is
how much there is to draw, not how thick the line is.

`scripts/prepare-colouring.py` now reports **stroke width** — twice the
ninetieth percentile of the distance transform of the ink, which is the ridge
running down the middle of a stroke — and flags anything under 7px.

**Warned, not refused.** A drawing may legitimately be simple, and a hard floor
here would reject good art. The house style asks for thick; the number tells us
when to look.

This corrects the reasoning behind an earlier error: the people pages were told
to slim down to match the object pages on ink share, when ink share was never
measuring what we thought.

---

# Increment 27 — The three ways in (2026-08-16)

### D-153 `[DEFINED]` Free, Premium and Professional live in the adult area, not the home page
Proposed as three buttons on the home page. **Moved.**

Free and Premium are subscription levels of a family account; **Professional is
not a third subscription** but a different audience, product and price. Three
equal buttons say they are three doors to the same place.

And the home page is the child's. D-036 removed the parents button from the top
bar because a five-year-old taps everything, and a large button reading
*Premium* is the nearest thing to a purchase button we could put in front of
her — D-039 keeps price and purchase off every child screen. It carries no
price, but it teaches her to ask.

They sit in `/parents`, where the adult door already is. Free and Premium stop
being doors and become what they already are: the state of an account, decided
on the adult side.

### D-154 `[DEFINED]` The professional line splits: health and education
A deeper distinction than it looks. **A psychologist may use material that
opens** — exploratory questions, family dynamics, a clinical sheet. **A teacher
has thirty children, forty-five minutes and no clinical frame**, and material
that opens in a classroom opens and stays open.

**The angry workbook, as written, must not go to a teacher.** What serves a
school is a different body of content: the seven cards, the vocabulary, group
activities, and no question asking a child to disclose anything in front of the
class. It is a line to be written, not a variant of what exists.

The education half is therefore shown and **marked as unbuilt**, rather than
pointed at the clinical workbook.

### D-155 `[DEFINED]` Plan names are brand; the description beside them is not
The three badges carry their word in English, painted into the artwork, and are
**not translated** — they behave as brand, like the section names (D-110).

Objected to: *free*, *premium* and *professional* are not universal. They read
in the European languages and mean nothing in Chinese or Hindi. **Resolved by
the arrangement rather than by the word:** a description in the reader's own
language always sits beside the badge, from the language file. The badge does
not have to explain itself, so the English word costs nothing.

**All three badges were regenerated together**, and the taglines came out. The
Premium badge previously read *exclusive content · premium experience · more
love, more fun* — sales copy, not brand: seven translations, promises made, and
in a product built on not selling to children it was the one line anywhere in
the material that sounded like an advertisement. With the description now
beside the badge, a tagline inside it would say the same thing twice in two
languages in the same place.

Regenerating approved artwork is an exception to rule 6 and is taken
deliberately: the ribbon is now empty in all three, and pieces generated in one
sitting match, which pieces generated months apart do not (D-132).

---

# Increment 28 — The whole deck redrawn in the house style (2026-08-16)

### D-156 `[IMPLEMENTATION]` The angry fine words pass the silhouette test
*Chateado · irritado · furioso*, drawn so the **body** carries the difference.
Rendered as flat silhouettes with no face at all, the three are still told
apart: chateado is a closed mass turned away, irritado shows fists as bumps in
the outline with steam on one side only, furioso opens into a cross with three
puffs.

**This settles the objection raised in D-147.** Those three words differ largely
by intensity, and the defence was that a child *names* rather than *grades*.
The silhouettes show the defence holds: they are three states with their own
posture, not three volumes of one. Had they been indistinguishable, it would
have been the layer that needed rethinking, not the art. Drawing them was the
test.

### D-157 `[DEFINED]` All seven family cards redrawn to match — regenerating the whole deck
The three fine-word cards came out in a different hand from the seven: softer
line, plumper body, flat colour with no gloss streak. Beside the old red heart
it showed immediately.

**It had to be all or nothing.** Redrawing only the angry mother would have left
it matching its own children and clashing with the other six. Redrawn: all
seven, in the new hand.

Deliberate exception to rule 6 and D-003. Justified because the new cards are
better, because twenty-three fine cards are still to come and the new style
will dominate the deck, and because these seven are the most visible object in
the product — screen, paper, and the workbook cover.

**Everything held on re-verification.** Coloured pixels 26.7–34.5% — bored at
31.5%, no repeat of the 0.9% that would have read as *disabled* (D-093). All
seven survive greyscale; angry is the darkest at 107.6 mean luminance. Only sad
carries a tear. Ashamed is turned away with one hand shielding its face, not
rubbing its eyes.

Card tints in `emotions.ts` and the canvas palette are now **sampled from the
artwork** rather than specified, so the body-map colour and the card cannot
drift apart.

### D-158 `[IMPLEMENTATION]` Scale normalisation ignores detached props
The angry card came out visibly smaller than the rest. Cause: mass
normalisation (D-122) counted the steam puff, which floats free of the body —
so the card measured larger and was scaled down to compensate.

Only the **largest connected piece** counts now. Measured after the fix, heart
widths are 522–566px across the six comparable cards, under 5% from the median,
which is not a real difference. Happy measures 689 only because its raised arms
fall inside the band the measurement looks at.

---

# Increment 29 — The fine words, all seven families (2026-08-16)

### D-159 `[DEFINED]` Twenty-four fine cards, drawn and integrated
All seven families now have their fine words in PT-PT, drawn in the house
style. `scripts/prepare-fine-cards.py` processes them from
`artwork/fine/family__word.png`.

**Scale is normalised within a family, not across the deck.** A fine word is
only ever seen beside its own siblings and its own mother, never beside a card
from another family, so that is the set that has to match.

Counts are uneven by design (D-101): angry 3, happy 4, calm 3, sad 4, scared 3,
ashamed 3, bored 4. Twenty-four rather than the twenty-three estimated, because
*tranquilo* was kept.

### D-160 `[DEFINED]` The silhouette test is a guide, not a rule
Applied to every family. Results, honestly:

- **Angry and happy** — all four distinguishable in silhouette.
- **Sad** — two of four. *Desiludido* and *magoado* share a shape.
- **Scared** — one of three. *Preocupado* and *tímido* share a shape.
- **Bored** — all four, the best separated set of all.
- **Ashamed** — all three, and the clinical distinction came through: guilt
  closes in, *arrependido* moves toward the viewer to put something right.
  It is the only card in the deck that reaches out.
- **Calm** — all three, which was not expected: standing, sitting on the
  ground, and hugging itself.

**Not every fine word has a posture of its own, and that is the words' nature
rather than a failure of the drawing.** *Preocupado* and *tímido* live in the
face and the gaze. Forcing them onto the body produced a deformed character —
a prompt asking for "a large hole of empty space between the arm and the body"
returned two white triangles cut out of the heart.

So the rule is corrected: **where two fine words share a silhouette but differ
in the face, that is acceptable** — a child reaching the fine layer already
reads. **Deforming the character to pass a test of ours never is.**

### D-161 `[OPEN QUESTION]` *Tranquilo* is a synonym of *calmo*
The art solved it — open eyes, arms behind the head, the only card in the deck
that is awake and looking out. The vocabulary problem stands: *tranquilo* is
the family again under another name, not a finer word inside it. Worth
revisiting when the English set is authored, where *calm* and *tranquil* have
exactly the same problem. *Satisfeito* was proposed as a replacement.

### D-162 `[IMPLEMENTATION]` The fine layer is reached after the activity closes
The child is thanked, and *only then* is offered "do you want to say it
better?". Choosing a fine word changes nothing and leads nowhere — it is a
better name for what she already said, not a second question.

This is D-100 in code: no child meets a wall, because the activity has already
ended before the premium layer exists for her.

### D-163 `[DEFINED]` Who gets what in My Inner World
| | Families | Fine words | Workbook |
| --- | :---: | :---: | :---: |
| Family — free | yes | — | — |
| Family — premium | yes | yes | — |
| Professional — education | yes | yes | — |
| Professional — health | yes | yes | yes |

Written into `src/data/access.ts` and wired into the activity.

**A teacher gets the vocabulary and not the workbook**, per D-154: the angry
workbook as written must not go to a classroom, because material that opens,
opens and stays open where there are thirty children, forty-five minutes and no
clinical frame.

**Declared, not enforced.** Without accounts (Q-010) there is no session to
check, so every visitor is treated as a free family and the fine layer is
visible in the preview build. **That is a gap, not a decision**, and it closes
with the account system. Writing the rule first means the account work has
something to implement rather than something to invent.

### Q-034 `[OPEN QUESTION]` Education and premium are identical here
For this activity a teacher and a paying family get exactly the same thing. That
is coherent — the workbook is the only piece that must not cross — but it means
**the education licence has to earn its price somewhere else**: group
activities, classroom sequences, material for thirty children rather than one.
Until that content exists, an education licence priced above a family
subscription would be hard to defend.

### D-164 `[IMPLEMENTATION]` Spelling: *Pediatric*, not *Paediatric*
Corrected everywhere it appears as text: `src/data/credits.ts` (which feeds the
footer on every page, live and preview) and `holding/index.html` (the coming-soon
page on the domain).

**Two places it survives, because it is painted into artwork:**
`colorhugs-professional.webp` and the workbook cover that uses it. Those need
regenerating — text inside artwork cannot be corrected by a find-and-replace,
which is the D-081 rule demonstrating itself in the least convenient way.

`ricardina-correia.webp` is unaffected: it reads *Psicologia Pediátrica*, in
Portuguese, and is correct.

The colouring-page PDFs are unaffected: their footer is `colorhugs.pt · ©
year ColorHugs` and carries no role line (D-137).

### D-165 `[DEFINED]` The fine words sit beside the way out, not behind it
Two faults found by using it.

**The angry family could not reach its fine words at all.** Its path goes body →
strategies → colour → done, and the fine layer only appeared at *done*. The
strategy screen had no way forward: the only exits were picking a strategy or
starting over. A child who wanted none of them was stuck, and the app was
refusing to let her finish. A **Not now** button now leads straight to done.

**And the fine words were in the wrong place.** Reaching them meant tapping
*I would rather not say* and walking to the end — which made the finer
vocabulary read as a consolation for having skipped. It is the opposite: a
child who wants a better word for what she feels should find one where she is.

*Do you want to say it better?* now sits **beside** the way out, on the body
screen, and on every screen after it. Back returns her where she came from
rather than dropping her somewhere she never was.

**D-100 still holds.** The layer is an option and never a wall: by the time it
appears she has already named what she feels and already been met. What changed
is that the option is now visible where she is, instead of at the end of a
corridor.

### D-166 `[DEFINED]` The holding page shows the word, not the artwork
The full lockup was sitting on the public domain. **The mark is not registered,
and in the EU it belongs to whoever files first** — so publishing the artwork
before the filing is a real risk. Not a legal opinion, and worth confirming with
someone who is a lawyer, but the instinct has a basis.

**Replaced with plain text, not with another image.** A placeholder drawing
would only swap a valuable piece for a worthless one; **text exposes nothing at
all, because there is no drawing to copy.** It also scales, reads to a screen
reader, and needs no file — the banner is no longer copied to the domain at
all, so it is not merely unreferenced but absent.

`scripts/assemble-holding.sh` no longer publishes `holding-banner.webp`. The
line to restore is left in place, commented, for when the mark is registered.

**`/preview` is deliberately unchanged.** It carries the full artwork on every
page, and that is wanted: it is where the brand is being developed and reviewed.
It is unlinked and not indexed, which is the accepted trade.

### D-167 `[IMPLEMENTATION]` Both endorsed lockups regenerated with the correct spelling
*Pediatric*, not *Paediatric*, verified by enlarging the line rather than
trusting the thumbnail: the parents lockup reads *by Ricardina Correia ·
Pediatric Psychology* in script, the professional one *RICARDINA CORREIA* above
*Pediatric Psychology*.

**Two, not one.** The parents lockup was missed on the first pass because the
search was run over the code and the code has no idea what a picture says. Text
inside artwork is invisible to every tool that finds text — which is the cost
D-081 exists to avoid, showing itself again.

Processed without a die-cut rim: a lockup is a mark, not a collectable (D-083).
The angry workbook cover regenerates from the new file and now carries the
correct spelling.

### D-168 `[IMPLEMENTATION]` The workbook builds to a PDF
`scripts/build-workbook-pdf.py angry` → `docs/materials/zangado-caderno.pdf`,
ten pages including the cover.

**The markdown is where the content is written and reviewed; the PDF is what a
colleague buys.** A licensed material arriving as a `.md` file is a draft,
however good the writing.

Markdown → HTML → PDF, printed by headless Chromium, rather than a PDF library:
the layout is typographic — running page numbers, tables, callouts, headings
that must not strand at a page foot — and CSS states all of that in a few lines
where a drawing API would take hundreds.

**The cover is page one, full bleed, no header or footer.** It is already a
finished composition; framing it would be framing a frame.

**The family name appears here, unlike on a colouring page.** D-120 keeps a
child's own choice off anything she carries home. A workbook is not a record of
a child — it is material about a feeling, and the practitioner needs to see at a
glance which one they are holding.

**One fault, caught by looking at every page.** Treating the markdown `---` as a
page break gave sixteen pages, half of them ending in white space with a heading
stranded at the foot of the previous one. The rule is a section separator, not a
break; the heading rule already separates sections visually. Ten pages, and no
heading now sits alone at the bottom of a page.

### D-169 `[DEFINED]` Music is a thread, not an eighth section
Proposed as an eighth section beside the seven. **Rejected as a section,
accepted as a thread.**

**The product already promises too much.** Seven sections and thirty-one
activities, of which one is built. A child opening the site today meets thirty
tiles saying *being made*. An eighth door before the first room is furnished
widens that gap — and the gap between what is promised and what exists is what
makes a parent give up.

**And the intellectual-property risk is the largest in the project.** Any
recognisable melody is licensed. Traditional children's songs are not the
escape they appear to be: the melody may be public domain, but the arrangement
and the recording almost never are. A music section without a licensing budget
means composing everything from scratch — and twenty-six spoken lines are not
generated yet.

There is a hosting cost too: the site is static on GitHub Pages, and the audio
layer built so far is sized for speech.

**As a thread it enters through the door of the problem it solves**, inside
sections that already have a reason to exist:

- **My Inner World / Calm My Body** — sound for regulation, the use with the
  longest clinical tradition.
- **Learning Hub** — rhythm and phonological awareness, one of the
  better-established links between music and reading.
- **Brain Gym** — rhythmic sequences for memory.

Nothing in the architecture changes, no new section is announced, and each piece
is born inside an activity that already justifies itself.

**Still to decide when the first piece is built:** whether the sound is composed
for ColorHugs or licensed, and where the files live. Neither blocks anything
today.

---

# Increment 30 — What the workbook is made of (2026-08-16)

### D-170 `[DEFINED]` One workbook, three layers — never two documents
Proposed: a second workbook for parents. **Rejected.**

**A parents' workbook cannot exist in the form of a workbook.** What serves a
family is the printed sheet, the card, the colouring page — things that close
themselves (D-094, D-095). A workbook is made of exploratory questions and
dynamics, which are things that open. A parents' version would either be
hollowed out until useless, or it would be material that opens on a kitchen
table with nobody there to receive it.

**But guidance for parents belongs inside the practitioner workbook**, because
there it is not material handed to a family — it is **the clinician knowing what
to say to the parents**. A section on what to say to a father who asks why she
does not listen when she is like that is content for whoever applies it, even
though its subject is parents.

It is also where the evidence is strongest: **parent-mediated intervention is
among the best supported approaches at this age**, and leaving it out would mean
leaving out the best-supported thing we have.

**Three layers, one document:**

1. **The workbook** — the clinician's, and it opens.
2. **A parent-guidance section inside it** — also the clinician's: what to say,
   what to correct, what to avoid.
3. **Take-home sheets, as an annex** — the family's, and they close themselves.

This avoids the worst outcome, which is two documents with overlapping content
drifting apart over time.

### D-171 `[DEFINED]` The therapeutic bases the workbook may draw on
The workbook reaches only people with training, so it may rest on things a
family material never could.

**In:**
- **Emotion-focused therapy for children and parents** — the only one here that
  treats emotion as information rather than as something to manage, and the
  closest fit to the vocabulary already built. Reasonable, and growing.
- **Systemic and family approaches** — a child's anger happens inside a system,
  and sometimes what changes is the adult's response.
- **Parent–child interaction principles (PCIT and kin)** — probably the
  best-established evidence in this whole list for behaviour difficulties at
  pre-school age. **Principles only: it is a programme with its own training,
  and we may not imply the protocol.**
- **Structured play therapy** — the natural vehicle from four to seven, and the
  material is already half a game. Evidence uneven by branch; say so.
- **Narrative therapy** — externalising *the Anger* as a character separate from
  the child fits the red heart already drawn. Practice, with little controlled
  research.
- **Child-adapted mindfulness**, sparingly — partly present already in the
  breathing strategies, and thinner than its popularity suggests.

**Out, deliberately:**
- **Psychodynamic** — it does not turn into worksheets without becoming
  interpretation, which is the line this material does not cross (D-109).
- **EMDR and trauma-focused work** — requires assessment and a frame a workbook
  cannot presume. Material that suggests trauma work to whoever bought it online
  is not a risk worth taking.

**Provenance goes in the grading, not in the structure.** Each model has its own
vocabulary, and a workbook that changes vocabulary every two pages confuses
rather than enriches. The workbook is organised by **what is done with the
child**; the model is named on the label beside the evidence level — *base:
externalisation, narrative therapy, practice*.

### D-172 `[DEFINED]` One source, two PDFs
The workbook and the child's sheets are **two files built from one source**, not
two documents written separately — same reasoning as D-170: separate sources
drift, and a colleague ends up with two versions that no longer agree.

It also fixes a problem noticed only when thinking about printing: as it stands,
handing a sheet to a child means printing page nine of a document that carries
evidence gradings and limits, which have no business on the table between them.

- **Caderno de aplicação** — the whole thing, read once.
- **Fichas da criança** — the fillable pages alone, printed as often as needed.

One script produces both.

### D-173 `[DEFINED]` Four sheets in angry, chosen per family thereafter
Not a fixed grid across the seven. **Externalising suits angry and scared; the
*lonely* card almost certainly asks for something else.** Each family picks its
own from the set of types.

The four for angry, one from each base, deliberately different so the moulds get
tested against each other:

| | Base | Kind |
| --- | --- | --- |
| O que acontece antes | behavioural — triggers | child's sheet |
| A Zanga vem visitar | narrative — externalising | child's sheet |
| As palavras finas | ColorHugs' own vocabulary | child's sheet |
| O que dizer aos pais | parent-mediated | guidance page |

**ACT is deliberately held back** — defusion, making room, values. It has the
thinnest base and depends most on age. It joins the second round, once these
four have been seen in use.

**Each sheet is both things:** a page the child fills in, and text around it in
the workbook telling whoever applies it what to ask and what to watch for.
*O que dizer aos pais* is the exception — it is read, not filled in.

### D-174 `[DEFINED]` Structure in code, illustration only where it is needed
Mixed, rather than all-drawn or all-generated. The structure — fields, rules,
typography — is drawn in code, so it regenerates when a word changes and so the
sheets exist today. **A generated sheet with fields would come back with
deformed text inside them**, which is exactly what generators do worst.

Illustration is generated only where a sheet actually needs one: *A Zanga vem
visitar* needs a large drawing space; *O que acontece antes* probably needs no
picture at all. One or two generations, not four.

### D-175 `[DEFINED]` Each sheet states its own age range
The material spans four to nine, and **that span does not work on a single
sheet**: a four-year-old writes nothing and orders no words; a nine-year-old does
both and finds a drawing-only page babyish.

Rejected: one mid-range version of everything (serves both ends badly), and two
versions of each sheet (doubles the work, eight pages for four).

**Each sheet is written for the age at which it makes sense, and says so in the
corner.** *A Zanga vem visitar* is drawing, so four to seven. *As palavras finas*
needs reading, so seven to nine. The workbook covers the span through the set,
not through each piece.

**The risk to watch:** if three of four land at the younger end, a nine-year-old
is left with one. The four are distributed deliberately — two down, two up.

### D-176 `[IMPLEMENTATION]` The four angry sheets, and the second PDF
`docs/materials/zangado-fichas.html` defines them; `build-workbook-pdf.py`
produces both files from it. Sixteen pages of workbook, four pages of sheets.

| Sheet | Age | Base |
| --- | --- | --- |
| O que acontece antes | 7–9 | behavioural, triggers |
| A Zanga vem visitar | 4–7 | narrative, externalising |
| As palavras finas | 7–9 | vocabulary |
| O que dizer aos pais | practitioner | parent-mediated |

Two down, two up, as D-175 required.

**The arrow on sheet three is not a scale.** Three boxes, one per fine word, and
a line beneath saying anger sometimes starts at one word and moves to another.
That is a true statement about anger, not a request that the child rate herself
— which would reintroduce the intensity D-096 removed. The distinction is that
she is **recognising words**, not grading a feeling.

**The externalising sheet carries its own warning**, in the workbook text
beside it: externalising is not handing responsibility to the Anger. If a child
says *the Anger hit him*, the answer is that the Anger arrived **and** the hand
was hers. Both at once, without choosing.

Two faults, both found by looking at the printed pages rather than the source:
the explanatory HTML comment at the top of the sheets file printed as body text,
and the guidance page spilled a few lines onto a fifth sheet, stranding one
paragraph alone. Comments are now stripped, and that page sets slightly tighter.

### D-177 `[IMPLEMENTATION]` Running header and footer, and the drawing fills the sheet
Every page carries the family and the document above, and `colorhugs.pt ·
Material licenciado` with a page number below — **except the cover**, which is
printed separately with no margin and no running elements. A header across a
finished composition is a caption on a painting.

Chromium prints the running elements into the page margin, so the margins moved
out of the stylesheet and into the print call.

**The artwork now takes every millimetre the rest of the page does not need**,
because that is where the child draws. The sheet is a flex column and the figure
is the part that stretches.

**One fault worth recording**, because it will happen again: the sheet was given
a *minimum* height, and a percentage height inside a flex column needs a
*definite* one — so the drawing grew until each sheet spilled onto a second
page. A4 less the printed margins is 260mm; the sheet is 256mm.

### D-178 `[DEFINED]` The child's sheets open with an identity page
A name, an age, and a frame to draw herself in — reusing the same frame as the
externalising sheet rather than generating another.

**A first name and an age, and nothing else.** No surname, no school, no
address: a sheet that travels between a clinic and a home should not be able to
identify a child to whoever finds it. Data minimisation applies to paper.

### D-179 `[DEFINED]` The exploration covers the derivatives, not only the family
Section 5 now asks about **chateado, irritado and furioso** separately, each
with its own questions and its own caution:

- *Chateado* — the most ambiguous word in European Portuguese; it serves mild
  anger, sadness and boredom alike, so do not assume which.
- *Irritado* — usually has a near, repeated target. **If the child names the
  same person every time, that is the finding.**
- *Furioso* — a child uses it to ask to be taken seriously rather than to
  measure. The useful question is what happened next, not how big it was.

Plus questions across the three: which she says at home and at school, whether
one has never been said aloud, whether an adult around her uses any of them.

A dynamic was added to match: the three words on three slips, one story each.
**The one that is missing says something.**

### D-180 `[DEFINED]` One sheet per fine word, plus the set sheet
Seven sheets for angry, not four. The overview sheet stays; each derivative gets
its own — **a child who needs to tell *chateado* from *irritado* will not do it
in a three-line box.**

**The sheets use the cards the child already met on screen.** Twenty-four fine
cards were drawn and were being used only in the app; the vocabulary sheet had
three empty boxes where it could have had the three characters. Paper and app
are now recognisably one thing, and recognising the figure saves her an
explanation.

Each sheet asks something different, so the three are not one template with the
name swapped:

- **Chateado** — the most useful of the four, and the only one that exists
  because of Portuguese. It puts the three **mother** cards in front of her —
  angry, sad, bored — and asks which one it was, then asks for a time it was a
  different one. *What to watch: if she always picks the same, the word is doing
  work that another word should be doing.*
- **Irritado** — what repeats, where, what has helped. *If she names the same
  person every time, that is the finding.*
- **Furioso** — the aftermath rather than the size: who noticed, what happened
  once it passed. *A child who says nobody noticed is saying two things at once.*

Across the seven families this means **24 individual sheets** eventually. The
mould is written once; each is filling in.

### D-181 `[IMPLEMENTATION]` The identity page has its own portrait space
It was reusing the externalising frame. **The same picture on two sheets makes
the second look like a repeat**, and these two ask for opposite things — one for
her own face, one for the Anger's.

Drawn in code for now: a soft rounded field labelled *Eu*. A plush hand-mirror
has been prompted to replace it, which suits the page better than a picture
frame — a mirror is what you look into to draw yourself.

### D-182 `[DEFINED]` The missing sheet: *Da próxima vez*
Nothing in the workbook asked the child what she could do differently. **A real
gap**: generating alternative responses and choosing one is problem-solving
training, among the best-studied things behavioural work offers at this age.

**It is not the cognitive reappraisal this material excludes** (section 9).
Reappraisal is *seeing the situation differently*, developmentally out of reach
for a small child. This is *what I do next*, which is behavioural and within
reach. Different things, and the workbook now says so, because the two are easy
to confuse and one of them we have promised not to do.

**The wording is the part that matters.** *What should you have done* is a
telling-off dressed as a worksheet, and a child sees through it immediately. The
sheet asks **da próxima vez, o que queres experimentar** — forward, with no
verdict on what already happened.

It uses the five strategies already drawn, so the child recognises the same five
pictures she met on screen, and leaves room for an idea of her own. *What to
watch: whether she picks one of ours or invents one. Her own is worth more —
it is the only one that arrives with her situation already inside it.*

A last line is for afterwards: what happened when she tried it. That closes the
loop from experiment to result, which is the whole point of the behavioural
frame.

### D-183 `[DEFINED]` *Compor as coisas* — the repair sheet
Two speech bubbles: what she wants to say, and what she can say later if the
other person will not talk yet — because **a refused repair is not a failed
repair, it is a repair with different timing.**

**Practice**, with indirect support: it is what the guilt–shame distinction
predicts. Guilt moves toward repair, and repair is one of the few things a small
child can actually do after anger. It is also the sheet that connects to
*arrependido*, the only fine card in the deck that reaches toward the viewer.

**The error this sheet exists to avoid.** An adult-ordered *say sorry* produces
compliance, not repair: the child learns the formula that makes the adult stop
and learns nothing about the other person. So the sheet asks **what do you want
to say**, and the word *desculpa* appears nowhere on it.

**Two cautions written into the workbook.** Do not use it on the day — while
arousal is still coming down, repair is not yet possible, which is what the
schema in section 4 explains. And *what to watch*: whether she writes about what
she did or about what she felt. **A child who can only explain herself has not
yet reached the other person, and that is information rather than failure.**

### D-184 `[IMPLEMENTATION]` The mirror, and a background that was not white
The identity page now carries a plush hand mirror, replacing the field drawn in
code. **A mirror is what you look into to draw yourself**, which suits the page
better than a picture frame, and it is visibly not the externalising frame.

**A fault worth recording.** The generator's background is a shade off pure
white, and the alpha cut was measured against pure white — so every worksheet
image carried a faint grey panel behind it, invisible on screen at small size
and obvious on a printed sheet. The threshold now cuts at 248 rather than 255,
and all four worksheet images were reprocessed.

It is the same lesson as the rest of this project: **the fault was invisible in
a thumbnail and plain in the artefact.** Look at the printed page, not the file.

### D-185 `[DEFINED]` Boxes, not ruled lines — every sheet takes a drawing
The sheets were written to be filled in with writing. **That excludes more than
the youngest children**: any child with a written-language difficulty, who is
precisely the child a psychologist has in front of her. A material for clinicians
that fails on dyslexia fails at its own job.

Rejected: two versions of each sheet, drawing and writing. That doubles the work
to eighteen sheets a family and forces the clinician to choose before she knows
the child.

**Every ruled line became an empty box**, sized to the writing it replaced, and
**each box says what is wanted** — *escreve ou desenha o que se repete*, *aponta,
escreve ou desenha o que aconteceu*. A box takes a sentence, a drawing, or both,
and nobody has to decide in advance.

The four table columns carry the same hints, including *nome ou desenho*. That
sheet stays the most writing-dependent of the nine, by its structure; with a
younger child the adult writes while she talks, which is what happens in a
session anyway.

Some boxes point at the cards instead: *escreve a palavra ou aponta para a
figura*. Twenty-four fine cards and seven family cards are already drawn, so a
child who does not write can answer by pointing.

### D-186 `[DEFINED]` *Assinala*, not *aponta* — and one treatment for every box
**Pointing leaves nothing behind.** A child who points answers in the moment and
goes home with a blank space, and the whole point of paper is that she takes it
with her. Every prompt now says *assinala*.

**No art inside the boxes.** Two treatments were built and compared on the
printed page:

- *soft* — a warm fill, no outline. Gentler, and **invisible in a black-and-white
  photocopy**, which is how much of this will be printed.
- *corner* — a small heart in one corner. It looked good, and it quietly took
  that corner away from the child: a large drawing would have to go round it.

**Adopted: a warm fill *and* an outline.** Survives the photocopier, belongs to
the project, and the middle stays empty — which is the rule the corner motif
broke. The middle of a box is where the child draws, and anything printed there
competes with her and tells her where she may not go.

### D-187 `[IMPLEMENTATION]` Boxes grow to fill the sheet
`data-lines` stopped being a height in millimetres and became a **share**: a box
asking for three gets three times the leftover space of one asking for one. The
sheet is a flex column, prompts keep their natural size, and the boxes take
everything that is left.

The result is a page that fills itself whatever else is on it, and **a child who
gets room to draw rather than room to sign her name**. Table rows grew to 26mm
for the same reason.

**A fault the experiment exposed**, worth recording because it was silent: the
regular expression that turns a box into HTML assumed the box carried no other
attributes. The experiment added a class and a style, and **every one of those
boxes vanished from the page without an error** — the page simply rendered
without them. Now tolerant of any attributes.

A second, from the same run: giving the card figures a flex column stretched the
emotion cards wide. `object-fit: contain` restored their proportions, and the
caption box below takes the leftover height instead.

### D-188 `[DEFINED]` Three files from one source, and each addressed to one reader
- `zangado-caderno.pdf` — everything, for the clinician.
- `zangado-fichas.pdf` — the child's sheets.
- `zangado-pais.pdf` — one page, for the family to take home.

Sheets are tagged `data-for` and the build selects. **What to say to the parents
left the child's book**: it is written for whoever applies the material, and a
page that talks over a child's head has no business in something she carries.

The parents' page is the take-home layer D-170 described, now real: it **closes
itself** (D-095) — nothing on it asks a question that needs someone present to
receive the answer. Everything that opens stayed in the workbook. It carries the
family's own card, so a parent recognises what the child has been holding.

### D-189 `[DEFINED]` The child gets psychoeducation written to her
The child's book had nine things to fill in and nothing that told her anything.
It now opens with **A Zanga**: three statements and the schema, with nothing to
complete.

The three are the workbook's own foundations in her language: anger appears when
something seems unfair; **anger is not bad** — it is the body saying something
matters; and **being angry is not the same as doing harm**, which is the
distinction the whole workbook rests on.

**The schema needed a second version.** The one in section 3 carries a line
addressed to the clinician — *aqui a estratégia ainda está a agir, mesmo que ela
ache que não*. That sentence is **about** the child rather than **to** her, and
on a page she reads herself it talks over her head. `figure-arousal-curve.py`
now writes both; the child's page uses the one without it, and closes on the
same idea in her own terms.

### D-190 `[DEFINED]` The workbook recipe is written down
`docs/WORKBOOK-RECIPE.md`, and `HANDOFF.md` points at it. **Written after the
fact, from what the angry build actually needed**, so it records rather than
predicts.

It holds the three-file structure, the section order, the sheet menu with ages
and bases, the grading rules and permitted therapeutic bases, and the
non-negotiables: boxes never lines · *assinala* never *aponta* · nothing printed
inside a box · boxes grow to fill the page · reuse the deck before generating
art · the child's page speaks to her, not about her · the identity page asks a
first name and an age and nothing else · the parents' page closes itself.

It ends with the list of faults from the angry build, because **every one of
them was invisible in the source and obvious on the printed page**: a comment
printed as body text, a paragraph stranded on an extra sheet, an off-white
background printing as a grey panel, cards stretched by a flex column, and boxes
that vanished without an error because a regular expression assumed no extra
attributes.

**The angry family is closed** — interactive, printable, and the professional
line in three files for three readers.

### D-190 `[DEFINED]` The child's book is a *Caderno de exploração*, with its own cover
It had none — it began at the identity page, which made it read as a printout
rather than as hers.

Same composition as the workbook cover, with two differences that matter:

- **The plain ColorHugs logo, never the endorsed professional lockup**
  (D-063, D-065). The endorsement is addressed to a colleague; a child holding
  her own book has no use for a credential.
- **No licensing strapline and no clinical disclaimer.** Both speak over her
  head, and the child's material does not do that (D-189).

`figure-workbook-cover.py <family>` now writes both covers in one run, and the
file is `<familia>-exploracao.pdf`.

### D-191 `[DEFINED]` `docs/WORKBOOK-RECIPE.md` — how the next six get built
Written from what the angry build actually needed rather than from a plan: the
three files and their readers, the eleven workbook sections in session order,
the sheet menu with ages distributed, the non-negotiable rules (boxes not lines,
*assinala* not *aponta*, nothing printed inside a box, boxes that grow, reuse the
deck), the grading discipline, and the list of faults that were invisible in the
source and obvious on the printed page.

It exists so the next family is filling in rather than deciding again.

### D-192 `[DEFINED]` The parents' page is a letter, not a handout
It was five sections of advice, written in the workbook's register. **Rewritten
as a letter addressed to the parents themselves.**

The strategies belong in the intervention, not on the sheet that leaves the
room. What the letter carries instead is **systemic framing and care for the
adult**:

- A child's anger happens in a house, between people, on a day that was already
  hard. Said explicitly **not to hand out responsibility** but because it is why
  their part counts.
- **It is exhausting**, nobody does it well every day, and one bad day does not
  undo the rest. *A relationship is not judged on its worst minute.*
- **Look after yourselves.** An adult at their limit cannot lend calm to anyone,
  so sleeping and eating are part of the work rather than time taken from the
  child.

It ends relationally rather than instructionally: *if something here does not
fit your house, tell me next time — this is written with you, not for you.*

**A correction worth recording:** *FBT* names the Maudsley family-based
treatment for eating disorders specifically. What this letter draws on is
systemic family thinking generally, which is what was meant, and the workbook
says the latter.

### D-193 `[DEFINED]` The clinician's table becomes a clinical record
A flat ten-row table nobody would fill in during a session. **Restructured into
four blocks, and the order is the argument:** what was done · what was seen ·
what is read from it · what was agreed.

**Observation is kept apart from interpretation on purpose.** What the child
said and what it means are different things, and putting them on one line is how
the difference gets lost — the same principle that keeps the workbook from
telling a clinician what an answer means (D-144).

**No name on it.** A code or the clinician's own case reference: a working sheet
does not need to identify anyone, and it does not replace a case file.

Two faults caught on the printed page: the record's tables had empty heading
rows printing as grey stripes, and the writing cells had no borders at all — a
form to fill in with nowhere to write.

### D-194 `[DEFINED]` The workbook carries guidance about each sheet, not the sheets
The worksheets were bound into both files. **Removed from the workbook**: they
live in the child's exploration book, a licence gives both files, and printing
them twice makes two copies that can drift apart.

What the workbook carries instead is **one page per sheet**, generated by
`scripts/build-sheet-guides.py`, with the same seven rows every time — age,
base, objective, how to run it, what to notice, cautions — then the exploration
questions, then **space to record the session it was used in**, identified by
code and never by name.

Generated rather than written by hand because there are nine per family and
**sixty-three in all**: the shape must be identical every time, and a table
written out sixty-three times drifts.

### D-195 `[DEFINED]` Never *você* or *vocês*
In all Portuguese materials, address the reader as *vós* or name them — *os
pais*, *quem cuida*, *a criança*. The parents' letter was rewritten accordingly.

### D-196 `[IMPLEMENTATION]` The workbook sets smaller than the sheets
9.2pt against 10.5pt. It is a technical document read by a professional; the
sheets are read by a child, and the two should not be set the same. Twenty-one
pages rather than twenty-nine.

### D-197 `[DEFINED]` One guide, one page — and dynamics per sheet, banded by age
**Each sheet's guidance now begins on its own page and ends on it.** Looking up
sheet nine should not turn up the limits section halfway down it, and a guide
split across a page break is worse still: the record box lands away from the
guidance it belongs to. The guides set at 8.4pt so they fit.

**Each guide gained its own dynamics**, four apiece, banded by who they suit:
age ranges, plus *com a família* and *qualquer*. These are what that sheet opens
up, distinct from the general dynamics in section 6, which stay where they are.

Written to be genuinely different activities rather than restatements. Some
examples of what that means:

- *A Zanga vem visitar* → **ask her to draw the Anger of an adult in the house**.
  It usually says more than her own.
- *Chateado* → **three piles**: five situations sorted onto the three mother
  cards. It shows her the ambiguity instead of explaining it.
- *Da próxima vez* → **check where the chosen strategy is actually possible** —
  school, car, classroom. Many are not.
- *Compor as coisas* → **repair without speaking**, for children for whom words
  are the hard part.

Thirty-six dynamics for angry; **252 across the seven families**, which is why
they are generated from a table rather than written into prose.

### D-198 `[IMPLEMENTATION]` The physical deck — thirty-one cards, no new artwork
`scripts/build-card-deck.py` lays the existing deck out for print: seven family
cards and twenty-four fine cards, nine to a sheet of A4, with cut marks in the
margin and a duplex-ready back sheet mirrored to line up.

**The back is identical on every card.** If backs varied by family a child could
read a card face-down, which silently ruins any dynamic that turns one over.

**The deck carries the words**, unlike every other piece of artwork (D-081). A
printed deck is made for one language and reprinted for the next, so there is
nothing to gain by leaving them off and real usefulness to lose. Labels come
from the language file, so `build-card-deck.py en` produces the English deck.

Word size is fitted rather than fixed: *Entusiasmado* is more than twice the
width of *Feliz*, and a deck where one word is visibly smaller reads as a
mistake rather than as a long word.

### D-199 `[DEFINED]` The deck does not sort by intensity
Ordering the cards from smallest to biggest is the first dynamic anyone thinks
of, **and it is the one thing this material has refused throughout**: no scales
in the app (D-096), and the sheets ask the child to *name* rather than *grade*
(D-147). Sorting them by size puts back by hand exactly what was taken off the
screen.

Nothing stops a clinician doing it; it is simply not something the material
proposes. What the workbook proposes instead:

- **by frequency** — which she says most, which she has never said
- **by how hard it is to say out loud**
- **by who is there** — home, school, alone
- **by recognition** — which she knows in her body, which only by name

**The last three yield clinical information; sorting by size yields a number.**

### D-200 `[DEFINED]` The cards are 90×120mm, not playing-card size
Small hands hold them. Four to a sheet instead of nine, and sixteen sheets
instead of eight — **worth it**: a card a four-year-old can pick up, turn over
and put down without knocking the pile over is more useful than a deck that
prints economically.

The figure and the word grew with the card rather than floating in more white
space, and the border thickened to match.

### D-201 `[DEFINED]` The recipe is rewritten from what the build actually took
`docs/WORKBOOK-RECIPE.md` replaced, not amended. The first version was written
before the sheets, the guides, the deck, the letter and the two covers existed,
and described a shape the build then moved away from twice.

It now carries: the four outputs and the two files to edit · the eleven sections
in session order · the child's book · how to choose sheets per family · the
non-negotiable rules · the grading discipline · and the pre-flight list.

**Two things in it are worth more than the rest**, because they are the ones
that cost the most to learn:

**Find the governing distinction first.** Angry's is *anger is not aggression*,
and everything else hangs off it. Candidates named for the others so the next
build does not start from nothing: sadness is not depression · fear is not danger
· shame is not guilt · boredom is not laziness.

**Look at every printed page, not the source.** The list of six faults is
reproduced there in full, because each was invisible in the file.

Also linked from `docs/HANDOFF.md`, so whoever picks the project up finds it
without knowing to look.

---

# Increment 31 — Where the account lives (2026-08-17)

### D-202 `[DEFINED]` Two systems with opposite requirements — closes Q-010
The question was asked as *where does the account system live*. It has two
answers, because there are two kinds of state here and they pull in opposite
directions.

**Commercial state lives on a server.** Who the adult is, verified consent, what
was bought, how many times it was downloaded, which licence is held. This is the
half that must be counted somewhere the child cannot reach — a limit counted in
the browser is a limit that can be erased.

**The child's trail lives on the device, and never syncs** (D-097). The last few
cards, in order. It does not travel between devices and it is not sent anywhere.

**Why the split, and not one store for both.** If the trail sits on a server
under the parent's account, D-098 — *nothing in My Inner World is visible to the
parent* — becomes a promise the law can override: a parent is the child's legal
representative and can exercise a right of access over her data. On the device
there is nothing to hand over, so **D-098 stops being a policy and becomes a
fact of the architecture**. It also means the worst case of a breach is a list of
adult email addresses rather than a record of children's feelings.

**The cost, stated plainly:** the trail is lost if the browser is cleared or the
device changes. Accepted. D-097 built it as something nobody should depend on —
short, never aggregated, never reported — and a trail that survives a house move
is a record, which is the thing this activity refused to become.

**The order of building:**

| | For | Built |
| --- | --- | --- |
| External store (Payhip, Gumroad, Etsy) | printables and professional licences | nothing to build; it pays, delivers and counts downloads |
| Managed EU backend (Supabase or equivalent) | adult accounts, child profiles, subscription | only when the family subscription line arrives |
| Own server | — | rejected: security and maintenance fall on one person |

**What this unblocks and what it does not.** The short trail no longer waits on
anything and can be built into *Como Me Sinto?* as device-local storage.
Verified parental consent still needs legal validation before it exists, whatever
host it lives on (rule 9). And until the managed backend exists, **the Free
boundary inside the app stays declared and not enforced** — which is acceptable
only while the revenue comes from printables sold through a store, and stops
being acceptable the day a subscription is sold.

### D-203 `[IMPLEMENTATION]` Piper cannot run in this environment; it runs on the author's machine
`piper-tts` installs, but the voice catalogue and the models are hosted on a
domain this environment cannot reach — `x-deny-reason: host_not_allowed`. D-127
recorded that no voice had been downloaded and that the first real run needed
watching; this is the confirmation that **the run has to happen on Ricardina's
own machine**, not here.

Nothing about the design changes: files are still named from the string key, a
real recording still replaces a generated one with no code change, and the
manifest still lists only files that exist so the Listen button is absent rather
than broken.

---

# Increment 32 — The banner frame, and the finer word leads somewhere (2026-08-17)

### D-204 `[IMPLEMENTATION]` The frame takes the artwork's shape, not the reverse
`SectionBanner` framed every banner at 1568×644 and used `object-cover`, so
anything of another shape was cropped to fit. **Three of the eleven banners are
1568×784** — My Inner World, Brain Gym and Kids Draw — which meant eighteen per
cent of each was cut away, top and bottom. On My Inner World that took the top
of the heart and pushed the ribbon against the edge.

**Cropping approved artwork to fit a frame is redrawing it by another means**
(rule 6, D-003). The frame now takes each banner's own proportions.

Measured rather than typed, by `scripts/measure-banners.py` into
`src/data/banner-sizes.json` — **the number that was wrong before was a typed
one**, and a new banner of a fourth shape would have been cropped in silence.
The script reads the WebP header directly rather than through an image library,
so the build does not gain a dependency.

Verified on the rendered page, not in the source: `aspect-ratio:2` on the three
tall banners, `2.4347826086956523` on the rest, and the whole composition inside
the frame in a browser screenshot.

### D-205 `[DEFINED]` The finer word continues the path — supersedes part of D-162
D-162 said the fine layer is *a better name for what she already said, not a
second question*, and the code did exactly that: the three cards appeared and
tapping one did nothing at all. In use that reads as a dead end, not as
restraint.

**Choosing a finer word now returns her to the body map under that word, and on
to the strategies.** The reasoning is clinical rather than technical: the place a
feeling is felt is not always the same once it has a finer name, and **the
strategy that helps *chateado* is not the one that helps *furioso***. Asking
where she feels *that* is a genuinely different question, so the zone is cleared
rather than carried — answering it for her would be the app deciding.

**What does not change.** D-100 still holds: the layer is reached only by asking
for it, always after she has already named what she feels and been met, so no
child meets a wall and the child who does not read still ends in the same place
as everyone else. Nothing new is recorded. No intensity appears anywhere: the
three words are still three names, never three sizes (D-096, D-199).

**Three consequences, worth stating because they were decisions and not
mechanics:**

- **The word travels.** The card and the label on the body, strategy and closing
  screens are the finer word once she has chosen one. The strategy screen showed
  nothing of it at first, and a screen that forgets what she just said reads as
  not having heard her.
- **The invitation stops being offered once she has answered it.** There is no
  finer layer beneath *furioso*, and a button leading back to a list she has
  already answered is the same fault in the other direction.
- **The Listen button moved outside the card.** The card became a button, and a
  button inside a button is not something a browser can resolve — a screen reader
  announces the pair as one control.

Walked end to end in a real browser rather than read in the source: family →
*say it better* → *furioso* → body map → strategies → colouring → closed.

### D-206 `[DEFINED]` Her mark on the figure survives the finer word
Taken as a judgement rather than asked again, and easily reversed if it reads
wrong in use.

Choosing a finer word cleared the body zone, on the reasoning that *where do you
feel* **furioso** is a different question from *where do you feel* **zangado**.
Clinically that is true. In use it is worse: she points at her chest, asks for a
better word, and is put back in front of the same empty figure being asked the
same thing about the same moment — which reads as the app not having believed
her the first time. **That is the "going backwards" reading**, and it comes from
the answer disappearing, not from the screen repeating.

**The zone is now kept.** Two cases, and the same rule serves both:

- She had already pointed. Her answer stands and she sees it still there under
  the new word — visibly a refinement, not a repeat.
- She had not, because she asked for a better word before answering. The figure
  is empty and the question is genuinely still open.

Either way the finer word gets the body question at least once, and nothing is
ever answered on her behalf. Verified in a browser: the marked zone is still
marked after *furioso* is chosen.

---

# Increment 33 — The avatar, built as the skeleton everything plugs into (2026-08-17)

Built before the remaining activities rather than after them, because it is the
one piece every other piece depends on: an activity that cannot say *she was
here* has to be reopened later to learn how.

### D-207 `[DEFINED]` The first choice happens on the home page; My ColorHugs holds the change
Two pieces, not one, and separating them is what makes this work:

- **The avatar in the corner is the frame**, not a section. It belongs to every
  page (D-078), and it appears only once she has chosen — an empty slot with a
  prompt in it would be a nag on every screen.
- **The picker is an activity**, and it is now the first sticker in My ColorHugs.

**But the first choice cannot live only in My ColorHugs.** A child who arrives
and goes straight to *Como Me Sinto?* would spend her first activity with an
empty corner — the one that matters most. So the home page carries it: if she
has no avatar, the ten stand where the avatar would be.

**It is not a wall.** The section grid renders either way, so nobody is stopped
on the way in. That is D-048 intact — the gate is on the action, never on the
door. What changed is only that the choice is now *in front of* every child
instead of hidden behind a section she may never open.

`markVisited(area)` is the whole contract. One line in an activity connects it.
Wired into *Como Me Sinto?*, *Explore & Color* and the picker itself. **It fires
on arrival, not on completion** — colour is for having been there (D-067), and
there is nothing in these activities that has to be finished.

The new sticker does not exist and is shown as *artwork pending* (D-004): a
substitute graphic quietly becomes a brand asset.

### D-208 `[DEFINED]` The colour belongs to the child, not to the avatar
Changing avatar carries every earned colour across, and the picker shows all ten
already wearing it.

If the colour stayed with the character, **changing her mind would cost her what
she had earned**, and nothing in ColorHugs is ever taken away (rule 38, D-082).
The cost on the other side is small and worth naming: the new avatar arrives
already painted, which can read as unearned. Between a small oddity and a
punishment for changing your mind, the oddity wins.

Consequence for the data: the state is `{ avatar, painted[] }` — the character
and the areas, kept apart. `src/lib/avatar-store.ts` is the only file that knows
where it lives, so **moving it to a server when accounts arrive (D-202) is one
file, not surgery**.

**And the honest part.** It lives on the device today, which for the short trail
was fine because the trail was built to be unimportant. **The avatar is the
first thing in ColorHugs with something to lose** — it accumulates over weeks
and it is the child on the screen. Clearing the browser takes it. That is
written into the storage module itself, because it is the strongest argument the
backend will ever have.

### D-209 `[IMPLEMENTATION]` The fill map completed, and three faults worth recording
`manifest.json` had seed points for the seven areas. Flood-filling from them,
**between 1.6% and 42.8% of the character stayed white** depending on which one
the child picked — the dino came out almost fully coloured, the fox nearly half
blank, for the same work. **That is the D-069 fairness rule failing in another
shape**: the choice of avatar was quietly a choice about how much reward was
visible.

`scripts/prepare-avatars.py` now assigns **every** sealed region to the area it
shares the most border with — adjacency, not distance, because a cat's muzzle
belongs to the head it sits inside and a centroid would sometimes disagree. All
ten now reach 0.00% unpainted with all seven areas present.

Three faults, each invisible in the file and obvious on the page:

- **The colour goes underneath the line art, not inside it.** The artwork is
  transparent everywhere except the line, so using its alpha as a mask over a
  filled canvas throws the fill away and returns a blank avatar.
- **Four of the ten had a seed sitting on the line itself.** That area got no
  region at all, so one whole section stopped giving colour on those avatars —
  the same fairness failure again. Seeds now snap to the nearest sealed space.
- **A CSS mask reads alpha, not luminance.** The masks were written as greyscale,
  which is opaque everywhere, so the browser painted the entire bounding box a
  flat colour: on the page, a gold rectangle where a rocket should have been.

A fourth, from the layout rather than the artwork: sizing the tiles by width
made the rocket tall and thin and the house short and wide, the rows went
ragged, and some avatars looked more important than others. **Fitted by height
instead**, so all ten stand the same size.

### D-210 `[OPEN QUESTION]` Two areas are very small on some avatars
With everything assigned, the shares are uneven: My ColorHugs is 1.2% of the
bear and Brain Gym 2.2% of the butterfly, against 40%-plus for the head on most
creatures. Nothing is left white any more, which was the serious version of this
problem — but a child whose avatar is the bear will barely see the colour that
one section gives her. It may not matter at all; it needs looking at with a child
rather than reasoning about.

### D-211 `[DEFINED]` Each avatar carries its own palette — the section colours are dropped
Painting each area in its section's accent made a harlequin of every character:
a fox with a green torso, a purple chest and red legs. **The avatar's whole job
is to be something a child likes looking at**, and a colour scheme nobody would
choose for a drawing fails at that before it does anything else.

**Ten palettes, one per character**, in `scripts/prepare-avatars.py` and written
into `src/data/avatars.json`. A ginger cat with pink ears and a cream belly. A
fox with a white front and dark socks. A brick roof on a cream house.

**What is lost, stated plainly.** Colour is no longer readable as *which
section*: purple no longer means My Inner World everywhere. That reading was
theoretical — it needed a key, and nobody decodes a key. **What it cost was
real**, and the trade is the right way round.

**What is not lost.** The zone-to-section mapping is untouched (D-069, D-075):
head is still Learning Hub, chest is still My Inner World, and every character
still exposes exactly seven areas of comparable weight. Only what fills them
changed.

**Two craft rules held while choosing them**, and the second is measured:

- *One family per character, varied by tone.* A cat is ginger nearly everywhere.
  If head, arms and torso were the same swatch, a child would paint a whole
  section and see nothing change — so they are one hue at different lightness,
  with one or two honest accents.
- *Touching areas must be far enough apart to read.* `check_contrast()` walks
  the actual adjacency of the regions and warns below a perceptual distance of
  9. All ten pass.

Checked on the progression, not only on the finished state, because that is
where the avatar spends nearly all its life: a fox painted one area at a time
comes to life step by step rather than looking broken half-done.

### D-212 `[DEFINED]` Changing avatar can be taken back, once, in the moment
The change was immediate and final — tap the bear and the cat is gone. Nothing
was lost but the character, and **a small child taps to see what happens**.

The picker now offers the way straight back, showing the previous character and
naming it: *não, quero outra vez o Gato*. It names the character rather than
saying *undo*, which is a word for someone who already knows she made a mistake.

**Held in memory, never saved.** It is an immediate undo, not a history: coming
back tomorrow and being offered yesterday's avatar would be the product
second-guessing a choice she has since lived with. It also only appears after a
real change — tapping the one she already has offers nothing.

### D-213 `[IMPLEMENTATION]` The corner avatar was too small
44px, rising to 56 on wider screens. Two things wrong with that, and only the
first was visible:

- It read as a speck. The point of a constant avatar is presence, and something
  that small is decoration in a corner.
- **It was below this project's own 64px tap-target floor** (D-013), for a link
  shaped like the child herself — the one thing on the page a small hand is most
  likely to reach for.

Now 64px, and 80 from the small breakpoint up. Measured on the built page: 80px
tall on a desktop width, 64 on a phone.

D-078 is unchanged: the home page is still where the colour is read properly.
This is presence, not a display.

---

# Increment 34 — The sad family (2026-08-17)

### D-214 `[DEFINED]` The governing distinction: *consolar não é animar*
Angry's distinction does three jobs at once — it separates feeling from action,
it names the error the family makes, and every one of the nine sheets hangs off
it. Any candidate for sadness has to do all three.

**Rejected: *tristeza não é depressão***, which the recipe had listed. It
reassures the adult, governs no sheet, and a seven-year-old does not have the
question. It is also a diagnostic distinction, and putting one at the head of a
workbook that promises not to diagnose walks it toward the line it exists to
stay behind.

**Rejected: *tristeza não é fraqueza***. Real, and it governs hiding and crying,
but narrower — and it drags a framing about gender that has no business in
material for a child of four to nine.

**Adopted: *a tristeza não se tira, acompanha-se*.**

Anger's error is confusing feeling with doing. **Sadness's error is the adult's,
and it is confusing comfort with cheering up** — *não fiques triste*, *vamos
fazer uma coisa gira*, *já passou*. It governs sheets that can actually be
written: who I want near me, what helps and what does not, what people say that
does not help, what I wish they would say instead.

**The child's own version**, as anger's had one: *a tristeza passa, mas não
passa por a empurrarmos*.

**One honesty condition, and it binds the whole family.** That sharing relieves
sadness has support, but thinner than its popularity suggests and thinner again
in children. **The material may not promise that talking makes sadness pass
faster** — a child who talks and stays sad concludes she did it wrong or that
something is broken in her. The formulation that holds is *with company it is
easier to carry*, which is a different claim. Graded **razoável**, never
established, and the workbook says so.

**Consequence the recipe predicted:** the arousal curve does not apply. Sadness
does not rise and fall in that shape, and its schema has to be a different
figure — the same sadness carried alone and carried with someone, and no numbers
on any axis (D-201).

### D-215 `[DEFINED]` The middle step for sadness: *o que te faz companhia quando estás triste?*
Anger's middle step asks *qual queres experimentar* and offers five strategies
of descent — move away, count slowly, breathe slowly, move your body, go and
tell someone. They work because anger rises and has to come down.

**Four of the five contradict D-214 when applied to sadness.** Breathing,
counting and moving offered to a sad child are precisely the *vamos fazer uma
coisa gira* that the parents' letter tells the family not to do. Only the fifth
survives, and it is the only one that accompanies rather than removes.

Two formulations were considered and one was corrected.

- ***Quem queres por perto*** was too narrow. Sadness is not only relational: a
  child who wants the dog, or a blanket, or her own room for a while is not
  answering badly — she is answering a question nobody asked her.
- ***O que te faz sentir melhor*** widens it correctly and **promises exactly
  what D-214 says may not be promised.** It is the child's version of *cheer
  up*, and it carries a cost that only shows later: she chooses, she does it,
  she is still sad, and what she concludes is that she chose wrong or that
  something is broken in her.

**Adopted: *o que te faz companhia quando estás triste?***

The content the second formulation wanted is right — a blanket, the dog, a
person sitting there. None of it removes sadness; all of it accompanies. **The
fault was in the word, not in the list.** *Fazer companhia* joins the who and
the what into one answer, which is how it lives in a child's head — the blanket
and her mother are the same reply. It carries the distinction inside its own
verb. And it promises nothing, so it cannot fail her: a child who picks the
blanket and stays sad got exactly what she asked for.

**Two consequences, fixed now:**

- **No strategy in disguise.** Breathing and counting do not enter this set.
  They belong to a family that has to come down; this one does not.
- **A way past it**, as anger has *agora não*. A child for whom nothing is
  company today must not be held there choosing one.

### D-216 `[DEFINED]` The five, and the honest limit of what evidence chose
Asked to pick the five best supported. **The evidence separates three, and then
it stops** — saying otherwise would be the overclaiming this project exists not
to do. The five, with the base marked and every claim flagged for verification
before it is written into the material (no reference is recorded from memory):

| | Base | Grade |
| --- | --- | --- |
| Alguém ao pé de mim, sem falar | co-regulation; responsive caregiver availability | **estabelecido** as a mechanism; the silent form specifically, prática |
| Contar a alguém | social sharing of emotion | **razoável**, with the caveat below |
| Uma coisa macia | comfort object | **razoável** — verify; the theory's origin is psychodynamic, which D-171 excludes as a *base*, so it is carried as the empirical finding and not as the theory |
| Uma coisa que me lembra alguém | symbolic representation of the absent person | **prática** |
| Um bocadinho no meu sítio | constructive solitude | **prática** |

**The caveat on sharing is the same one D-214 fixed**, and it is worth stating
twice because it is easy to lose: the literature on telling someone is
consistent about the *bond* strengthening and equivocal about the *feeling*
lifting. That is not a weakness of the option — **it is the exact shape of this
family's distinction**, arriving from the evidence rather than from us. Company
makes it easier to carry. It does not make it pass faster.

**Four and five were not chosen by evidence**, because at that point there is
none to choose with. They were chosen on two other grounds, said out loud:

- *Um bocadinho no meu sítio* is structurally necessary. Without it the activity
  prescribes company, and a sad child who wants to be alone would have no true
  answer on the screen.
- *Uma coisa que me lembra alguém* is the only one that houses **com saudades**,
  one of the four fine words of this family, which otherwise has nowhere to land.

**Art:** two reuse existing pages — the bench for *contar a alguém*, the quiet
corner for *um bocadinho no meu sítio*. Three are new and must pass the sealing
test and the six-area floor (D-129).

### D-217 `[DEFINED]` The rest go to the workbook as suggestions, not to the screen
Seven more were considered. They are not discarded — **the clinician's guidance
page for this sheet carries them as things to offer a particular child**, which
is exactly the place for something that suits one child and not another. The
screen has to work for every child unattended; a session does not.

| | Why not on the screen |
| --- | --- |
| Um abraço | the only one where a wrong tap can end in a touch she did not want. On a screen it is a suggestion; in a room there is someone reading her face |
| Um bicho | prática, and it excludes every child without one |
| Falar com alguém que está longe | no separate base beyond social sharing; and it needs a device and an adult |
| Música | not blocked by the content — sad music heard by a sad person accompanies rather than cheers, and the evidence there is friendlier than expected. Blocked by licensing (unresolved) |
| Enrolar-me | prática, near nil. It is what a sad body does, not something to choose |
| Esperar que passe | the purest form of the distinction, and the one a six-year-old is least likely to choose. It also edges toward the acceptance work D-173 deliberately held back |
| Chorar | **not company — permission.** It belongs with the three psychoeducation statements in the child's book, not in a list of things to pick |

### D-218 `[DEFINED]` Six, not five — the pet stays and the keepsake stays
The pet was dropped as *prática* and excluding children who have none. Corrected,
and the correction is worth recording because the reasoning was wrong in a way
this project should not repeat: **prática does not mean it does not work — it
means it has not been well studied.** For a choice that belongs to the child
rather than to us, what children actually say outweighs a thin literature, and
children say the dog constantly.

Six rather than five. Nothing requires five: the recipe says sheets are chosen
per family and not to a grid. **The grid is also better** — six fills two rows of
three and two of two, where five leaves one option alone with an emphasis it has
not earned, which is the D-104 problem again.

| | Base | Grade |
| --- | --- | --- |
| Alguém ao pé de mim, sem falar | co-regulation | estabelecido as a mechanism |
| Contar a alguém | social sharing of emotion | razoável |
| Uma coisa macia | comfort object | razoável, to verify |
| Um bicho | animal company | prática |
| Uma coisa que me lembra alguém | representation of the absent person | prática |
| Um bocadinho no meu sítio | constructive solitude | prática |

**The four fine words all have somewhere to land**: *sozinho* in the first or the
last, *com saudades* in the keepsake, *magoado* and *desiludido* in telling
someone. Cost: four new colouring pages instead of three, two reused.

### D-219 `[IMPLEMENTATION]` The sad family's schema: two paths, drawn in code
`scripts/figure-sadness-paths.py`, in both versions (D-189).

**Not the arousal curve, and it could not be.** Anger rises fast and comes down
slowly. Sadness does not, and drawing it as that curve would say something false
about it before a word was read.

It draws **the same sadness carried two ways** — alone, and with company — from
one arrival to one ending.

**The thing it had to get right:** the accompanied line must not end sooner. A
figure where company makes sadness finish faster promises exactly what D-214
forbids. So the two lines end together, and what differs is how far down the
accompanied one runs: *easier to carry*, never *over sooner*. The clinician's
version names the error — *aqui é onde se tenta animar, e é o que faz a linha de
baixo desaparecer* — and the child's version does not, because that sentence is
about her rather than to her.

No numbers on either axis (D-201).

**Three faults, all invisible in the code and obvious in the render:**

- **The first draft spiked.** It rose almost vertically and read as anger in
  another colour. Sadness arrives over a while, settles, and thins — and it does
  not reach zero inside the picture, because it usually does not reach zero
  inside a week either.
- **The event mark landed halfway up the rise**, so the picture said the sadness
  began before the thing that caused it.
- **Two labels sat on top of the lines they described**, and *com companhia* was
  printed on the baseline.

### D-220 `[DEFINED]` Nobody in the sad family's colouring pages is sad
Not a tear, not a downturned mouth, not a hunched back. The four new pages are
about **company**, not about sadness.

The reason is not aesthetic. D-120 already keeps the feeling out of the filename
and out of the folder, so that a parent finding the downloaded PDF cannot read
back what the child chose. **A drawing of a weeping child defeats that on the
page itself** — a filename can be neutral, a crying figure cannot. The same
promise, at the one place it had not yet been applied.

Faces are the ordinary calm kawaii face of the rest of the library.

### D-221 `[IMPLEMENTATION]` The four prompts, and what art the family still needs
`docs/COLOURING-PROMPTS.md`, inheriting from `ART-DIRECTION.md` and written to
the discipline it records: state what must exist, forbid details one by one,
phrase the critical instruction three ways, ask for eight areas rather than the
six that are required.

**Four new pages**: alguém ao pé de mim · uma coisa macia · um bicho · uma coisa
que me lembra alguém. **Two reused**: the bench for *contar a alguém* and the
quiet corner for *um bocadinho no meu sítio* — a data change, adding `sad` to
their families list, not new artwork.

**What needs no art at all**, recorded so it is not generated by mistake: the
family card and its four fine cards exist; both covers are drawn in code from
the family card; the schema is drawn in code (D-219); the identity page's hand
mirror is family-independent and already exists.

**What is still unknown:** the worksheet illustrations, because the sheet menu
for this family has not been chosen. *A Tristeza vem visitar* is not assumed —
externalising suits angry and scared, and inviting a child to put her sadness
outside herself and be rid of it is the one thing D-214 says the material does
not do.

### D-222 `[DEFINED]` The sad family's sheet menu, and the three of anger's that do not cross
Nine for the child plus the practitioner's page, as anger has — but the axis is
different, and it is the governing distinction that decides which of anger's
moulds survive.

| Sheet | Age | Base |
| --- | --- | --- |
| Psicoeducação — A Tristeza | 6–9 | to read, nothing to fill |
| Quando é que ela aparece | 5–8 | behavioural, pattern |
| O que me faz companhia | 4–7 | co-regulation · comfort object |
| O que as pessoas dizem | 7–9 | parent–child interaction principles |
| As palavras finas | 7–9 | the set together |
| Desiludido | 7–9 | behavioural |
| Sozinho | 6–9 | social support |
| Com saudades | 4–7 | representation of the absent person |
| Magoado | 7–9 | systemic |
| O que dizer aos pais | practitioner | parent-mediated |

**Three of anger's do not cross, and D-214 is what bars them:**

- ***A Zanga vem visitar*** — externalising invites the child to put the thing
  outside herself and be rid of it. That is the one move this family does not
  make.
- ***Da próxima vez*** — asks her to solve the sadness. For anger the question
  is behavioural and within reach; here it is cheering up under another name.
- ***Compor as coisas*** — there is nothing to repair. Sadness leaves nobody to
  apologise to.

**One is new and has no parallel: *quando é que ela aparece*.** Anger's
equivalent hunts triggers, which is causal. **Looking for the cause of sadness
puts a child to explaining herself, and often to blaming herself.** A temporal
pattern is descriptive, asks for no explanation at all, and says more
clinically — bedtimes, Sundays, transitions.

**Age distribution, which the recipe says to watch:** it is top-heavy, five at
7–9. The reason is honest rather than an oversight — three of this family's four
fine words are concepts that need reading, unlike anger's. *Sozinho* is the one
that could come down, using pictures of places.

### D-223 `[DEFINED]` *O que as pessoas dizem* stays a child's sheet — the clinician is the gate
The sheet asks a child to mark what the adults around her say that does not
help, and it goes home in her book. It is the most useful sheet of the set,
because it is the distinction made concrete, and it is the only one that can
reach the hands of the people it describes.

Proposed moving it into the workbook as a spoken dynamic. **Rejected**, and the
reasoning generalises: **this is practitioner-licensed material, and the
clinician decides what leaves the room.** A safeguard in the guidance page is the
right instrument, not removing the sheet from the child who benefits from it.

**The scope limit, written down now so it is not lost later:** that reasoning
holds *because* there is a person there. It does not transfer to the family
printable line. **This sheet must never appear in a printable sold to a family**
— a printed sheet does not choose who is in the room, and nobody is there to
decide whether it goes on the fridge.

### D-224 `[IMPLEMENTATION]` The middle step is per family, and so are the picture names
Found by using it rather than by reading it: choosing *triste* produced anger's
screen — *which would you like to try?*, over pages called *go and tell someone*
and *move away from it*. Both strings were global, written when one family
existed.

Both are now per family with a fallback. Sadness asks **what keeps you company**,
and the same two drawings are called *contar a alguém* and *um bocadinho no meu
sítio* rather than *ir ter com alguém* and *sair dali*.

**The same drawing doing a different job in each family is not a compromise —
it is the reason a page is named for what it shows and never for the strategy**
(D-120). The bench is the bench. What it is *for* belongs to the family, and now
lives where the family's words live.

The two reused pages are wired (`families: ["angry", "sad"]`), each carrying its
own evidence note for the second family — including, on the bench, the caveat
that must not be lost: company makes it easier to carry, not faster to pass.

### D-225 `[DEFINED]` The child's three statements and the literacy line
Anger's three are in her book already; sadness's are the same shape.

1. *A tristeza aparece quando perdemos alguma coisa de que gostávamos — uma
   pessoa, um sítio, uma coisa, ou uma ideia do que ia acontecer.*
2. *A tristeza não é má. É o corpo a dizer que aquilo era importante.*
3. *A tristeza passa, mas não passa por a empurrarmos.*

The third is the governing distinction in her words (D-214). The first is
written to cover disappointment as well as loss, because *desiludido* is one of
this family's four fine words and a statement about losing a person would leave
it outside.

**The literacy line on screen carries the honesty condition rather than hiding
it**: *com alguém ao pé, não passa mais depressa — mas é mais fácil de carregar.*
It would have been easy to write the warmer, false version. A child who is told
that talking makes it pass, and then talks and stays sad, learns that she did it
wrong.

### D-226 `[IMPLEMENTATION]` The four filenames, fixed before generation
`sitting-beside` · `soft-blanket` · `dog-beside` · `keepsake-shelf`, into
`artwork/colouring/strategies/`, then `python3 scripts/prepare-colouring.py`.

Fixed now rather than after the images arrive, because **the filename is the one
part of a colouring page that travels into the child's house.** She downloads the
PDF; whatever it is called lands on someone's desktop. Each of these names the
picture and none names the feeling (D-120) — *keepsake-shelf* rather than
*missing-someone*, *sitting-beside* rather than *comfort*.

### D-227 `[IMPLEMENTATION]` The four pages passed, and the family is live at six
Measured before exporting, then flood-filled region by region and looked at.

| | Fillable areas | Stroke |
| --- | ---: | ---: |
| sitting-beside | 17 | 8.0px |
| soft-blanket | 12 | 8.0px |
| dog-beside | 11 | 8.0px |
| keepsake-shelf | 13 | **6.3px** |

All four clear the six-area floor comfortably, and no colour crossed between
regions in any of them. **Three sit in family with the accepted pages** (the
quiet corner is 7.2, jumping 8.2, the feather 8.2).

**One warning, and it is the one the script warns about rather than refusing:
`keepsake-shelf` at 6.3px is under the 7px floor** — the thinnest page in the
whole library. It is not a failure and the page works, but it is the one drifting
toward the generic colouring-book line the house style rules out. Recorded rather
than acted on: the page passes, and redrawing accepted art needs a reason better
than a number just under a threshold.

**One thing the prompt asked for and did not get, on three of the four.** The
ground line was specified as spanning edge to edge, and only `soft-blanket` has
it. On the others the floor is therefore not a sealed region and cannot be
coloured — a small loss and not a fault, since `dog-beside` has a rug instead and
`keepsake-shelf` has the shelf. **Worth noting for the next family**: the
instruction was phrased three ways and still did not take on three drawings out
of four, which suggests the fault is in the instruction rather than the model.

The six are wired, each with its own evidence note, and the screen now asks
**what keeps you company when you are sad?** over six pictures.

### D-228 `[DEFINED]` A landscape drawing gets a landscape sheet
Found on the printed A4 and nowhere else. The four new pages are wide, the sheet
was always tall, and the drawing sat in the top third with a hand's width of
white beneath it before the mark.

Measured rather than judged: the four filled **48–59% of the art box**, against
70–82% for the square pages already accepted. `keepsake-shelf` was worst at
47.7%. **The child was getting a smaller picture for no reason but the shape of
the paper.**

`to_pdf` now chooses the orientation, and chooses it **from the trimmed drawing
rather than from the file** — the generator's framing is not the drawing. The
same four now fill 71–88%, and nothing that was already accepted changed, since
the square pages stay portrait.

It is the same lesson as every other fault in this project: it was invisible in
the source, invisible in the WebP, and obvious on the page.

### D-229 `[IMPLEMENTATION]` The build refuses instead of producing an empty document
Building the sad family before its sheets existed produced **a one-page parents'
letter with a header, a footer and no letter**, and a three-page exploration book
with nothing to explore. `load_sheets` returned an empty string when the file was
missing, and everything downstream carried on politely.

Files that look finished and are not are exactly what D-004 exists to prevent,
arriving through the build rather than through the data. It now raises.

**The workbook alone is allowed**, because it is prose and stands without the
sheets — a family being written can be read before it is complete. The child's
book and the parents' letter cannot: they are made of sheets.

### D-230 `[IMPLEMENTATION]` The sad workbook's prose is written — fifteen pages
`docs/materials/triste-caderno.md`. Sections 1–8, 10, 11 and the annexes;
section 9 is a marked stub, because the guides are generated and the sheet
menu has to become real sheets first.

Things in it that are decisions rather than writing:

- **Section 3 says out loud, before the table, that the evidence separates three
  of the six and then stops.** The alternative was six entries with the same air
  of support, three of which do not have it.
- **The two *practice* entries that are in the set for stated non-evidential
  reasons say so in their own paragraph** — the keepsake because it houses *com
  saudades*, the quiet place because without it the activity prescribes company.
- **The missing word of this family is not the missing word of anger.** Anger
  lacked a child's word for injustice. Sadness lacks **a name for the sadness
  that has no cause** — and a child who is sad and cannot say why, when asked
  why, invents a cause to satisfy whoever asked. That is the clinical reason
  sheet 2 asks *when* and not *why*, and the workbook now says so.
- ***Sozinho* is this family's *chateado***: European Portuguese uses one word
  for being without anyone and for feeling alone among people, and the second is
  much heavier. **The question that separates them is *está lá gente?***
- **Sorting by intensity is refused more easily here than anywhere else**, and
  for a new reason: these four words differ by *cause* and by *target*, not by
  size. *Sozinho* is not more or less than *magoado* — it is something else.

### D-231 `[IMPLEMENTATION]` *O que dizer aos pais* was reaching nobody
A sheet marked `data-for="practitioner"` was kept out of the child's book,
because it talks over her head (D-188), and out of the parents' letter, because
it is not addressed to them. **And it was never put into the workbook either.**

So in both families it was written, built and delivered nowhere — a page of
clinical content that existed in the source and in no document. Found by
searching the three PDFs for its own title.

It is now an annex to the workbook, after the closing signature. No heading was
added: the sheet carries its own title, and a second one prints the same words
twice.

**Two faults fixed on the way, both from the printed page:**

- Appended after the signature, the signature was pushed onto a sheet of its
  own with one line on it.
- The workbook's closing footnote then did the same thing, opening a further
  page for a single grey line — **in both families, and unnoticed since the
  angry build**. It now sits inside the last sheet.

The angry workbook goes from 24 to 25 pages by gaining the page it should always
have had, and loses the blank one it should never have had.

### D-232 `[IMPLEMENTATION]` The sad family's sheets, and its letter
`docs/materials/triste-fichas.html`. Nine for the child, one for whoever applies
it, one for the family. The child's book is twelve pages; the letter is one.

Two card layouts were needed and did not exist: **four** fine words instead of
three, and **six** figures on the company sheet, both set smaller than the
three-card row so the row still leaves the child room to write beneath it.

Things in the sheets that are decisions:

- ***Quando é que ela aparece* asks when, and says so in its own opening line** —
  *não vamos procurar porquê*. A child asked why she is sad, who does not know,
  invents a cause to satisfy whoever asked.
- ***O que as pessoas dizem* has three boxes and the third is the one that
  matters**: a thing she wishes someone would say, and nobody says. The first two
  are what makes the third askable.
- ***As palavras finas* opens by saying they are not bigger and smaller — they
  are different things.** In anger that sentence could not be written; here it is
  true, and it does the work of keeping intensity out.
- ***Sozinho* asks *estava lá gente?*** — the question that separates being
  without anyone from feeling alone among people, which European Portuguese does
  not separate.
- ***Magoado* ends with what she would say to the person**, and stops there. It
  is not the repair sheet: there is nothing here for her to put right.

**The letter carries the distinction to the people who make the error.** Its
second paragraph is the one that had to be written carefully — *estar ao pé sem
dizer nada é uma coisa a sério* — and its third says outright that talking does
not make it pass faster and that this is not a bad sign, so that a parent whose
child talks and stays sad does not conclude that it failed.

### D-233 `[DEFINED]` The tenth sheet: *O que eu posso pedir* — the family had no way forward
Caught by Ricardina on reading the set: **the sad arc ended in description.**
Anger closes looking forward — *da próxima vez* and *compor as coisas* — and both
were removed here for good reasons (D-222), with nothing put in their place.

**Ending in description is itself a message, and the message is *there is
nothing you can do*.** That is not what D-214 says. The distinction says sadness
cannot be taken away; it does not say the child has no part.

What it could not be is *da próxima vez* under another name. Asking a sad child
what she will do so as not to be sad is asking her to solve the sadness.

**What closes this family is asking.** Sheet 3 finds what keeps her company —
and almost none of it depends on her alone. A child who knows that what helps is
her mother sitting beside her without speaking still does not have it, because
she cannot ask for it, and what adults do spontaneously is usually the other
thing. **The sheet closes the distance between what she found and what she
receives**, and promises nothing while doing it: asking does not make sadness
pass, it lets the company arrive.

Three parts, and the third is the one that cannot be missing: what I want to
ask · who I ask · **and if that person cannot right then?** Without it the sheet
prepares her for a refusal she will read as rejection. It is the reasoning of
anger's repair sheet in the other direction: **a request refused is not a
request failed, it is a request with different timing.**

**Base: prática.** The company itself rests on established ground; what is hard
is not the company but the asking, and on children's help-seeking and needs
communication the literature is thin. Said as such.

6 to 9, which also pulls the age distribution down slightly — it was top-heavy.

The child's book is now thirteen pages, and the workbook's section 1 gained a
paragraph, *Onde é que esta família acaba*, so that the next family is not built
without asking the same question.

### D-234 `[IMPLEMENTATION]` The sad family's ten guide pages and forty dynamics
`scripts/build-sheet-guides.py` now takes a family. Ten pages, each beginning
and ending on its own page — verified by searching the built PDF for each title
and confirming it appears on exactly one page (D-197). The workbook is 29 pages.

The dynamics are written as genuinely different activities rather than
restatements. Some that carry a decision inside them:

- *Quando é que ela aparece* → **the day it did not appear.** Finding a day it
  did not come and seeing what was different usually yields more than the days
  it did.
- *O que me faz companhia* → **the adults guess.** They pick which they think are
  hers before seeing her choices. The gap is the conversation.
- *O que as pessoas dizem* → **the sentence handed over**, and it carries its own
  limit: only if she wants to, and never by our decision.
- *Sozinho* → **the playground.** Ask the adults what they know about her
  breaks. They usually do not, and that is where this lives.
- *Magoado* → **do not bring this sheet if the person named is in the room.**
  Work on what stops her saying it instead.
- *O que eu posso pedir* → **rehearse with me**: she asks the clinician for the
  thing she means to ask for at home, there and then.

**Two cautions in the guides that are new rules rather than advice.** Sheet 4
says the sheet goes home with her and that the clinician decides whether it
should, naming the case where it should not (D-223). Sheet 8 says **do not
assume bereavement**: the same drawing serves a grandmother who moved house and
a grandmother who died, and if it is bereavement this sheet does not reach.

**The sad family is closed** — interactive, printable, and the professional line
in three files for three readers, as angry is.

---

# Increment 35 — The scared family (2026-08-17)

### D-235 `[DEFINED]` The governing distinction: *o medo não manda ficar parado*
**Rejected: *medo não é perigo***, which the recipe had listed and which is true.
It fails on where it leads rather than on what it says: **if the axis is *this is
not as dangerous as it feels*, every sheet ends up asking the child to appraise
the danger** — and that is cognitive reappraisal, which this material excluded
deliberately as developmentally out of reach for a small child (D-182). The most
obvious distinction of this family points straight at the one technique we said
we do not do.

**Adopted: *o medo não manda ficar parado*.** The fear arrives; what is done next
is chosen.

**It has anger's structure exactly** — feeling is not doing. Anger separates the
emotion from the behaviour it seems to demand; fear does the same, and the
behaviour is avoidance.

**And it is the first family whose distinction is *estabelecida* rather than
*razoável*.** That avoidance maintains fear is among the most solid findings
child psychology has, more solid than anything supporting the six of the sad
family. Every distinction so far has rested on reasonable ground; this one does
not have to.

**It names the error the family makes, and the error is accommodation** — taking
the thing out of the way. Answering for her at the counter, excusing her from the
party, no longer going where there are dogs. Each is immediate relief and
long-term worsening, and none of it is ill will: it is the same mechanism that
makes an adult try to cheer up a sad child.

**The child's version:** *o medo diz cuidado — não diz não vás.*

**What this family costs and what it does not.** Four of anger's five strategies
cross intact, because fear also rises and has to come down, so the artwork is
largely already drawn. What it needs that no family has needed yet is **something
that lets her approach by steps** — and that is new content, not one more
colouring page. Before building it, check whether a tool for this already exists
in Ricardina's own clinical materials: the workbook should point at it rather
than build a second one over the top.

### D-236 `[DEFINED]` Nothing in a workbook may depend on a tool the licence does not carry
The scared family's approach piece was going to point at Ricardina's own
*Escada da coragem*, which exists already. **Rejected, and the reasoning
generalises past this family.**

A workbook licensed to a colleague has to work whole in her hands. Pointing at an
application she has no access to turns a central piece into a dead reference, and
makes the material look deliberately incomplete. **Nothing in any ColorHugs
workbook may depend on a tool that does not come with the licence** — no app, no
site, no material only the author has.

Worth recording so it is not misread later: this is not the same object under
another name. One lives in an application, with screens and state; the other is a
sheet that closes on itself and that a colleague prints. Sharing the idea of
steps does not make them competitors.

### D-237 `[DEFINED]` The approach sheet may order situations, because it orders situations and not the child
The hierarchy — steps ordered from easiest to hardest — is the classic
instrument, and it is also **the only thing in this project that looks like a
scale**. Ordering from less to more is what has been refused throughout: cards
are not sorted by size (D-199), the fine words *name* rather than *grade*
(D-147), and there is no intensity anywhere (D-096).

**What saves it here is what is being ordered.** In the other families, sorting by
size grades *the feeling* — *a minha zanga é 5*. Here what is ordered are
**situations**, not feelings. *Seeing a dog across the road* is easier than
*stroking one* as a fact about the world, not as a measurement of her.

Approved with the distinction stated, and with two things fixed now because they
are how it would erode:

- **No numbers on the steps.** A ladder with rungs numbered one to six is a scale
  wearing a picture, and *estou no 3* is one sentence away.
- **The sheet never asks how frightened she is.** It asks which situation comes
  before which. The moment it asks for a level, it has become the thing this
  project refused.

### D-238 `[DEFINED]` Four of anger's five cross to scared — and the fifth is barred
Four work intact, because fear also rises and has to come down: the bench, the
hand, the feather, the jumping child. Wired, and **no relabelling was needed** —
*ir ter com alguém*, *contar devagar*, *respirar devagar* and *mexer o corpo*
mean the same thing to a frightened child as to an angry one, unlike the sad
family where two pages needed new names (D-224).

**The fifth cannot enter, and it is the one that looks harmless: *sair dali*.**
For anger, leaving the situation is situation modification and good strategy.
**For fear it is avoidance** — the thing D-235 says maintains it. Offering it on
screen would be the product proposing to the child exactly what the workbook
tells the parents not to do.

It is the sad family's finding in reverse. There, four of five fell and one
survived; here four survive and one falls, and the one that falls is the one
nobody would have questioned.

### D-239 `[DEFINED]` The screen gets the mechanism as a picture, not as a task
The approach ladder belongs to the workbook, because it opens and a child alone
has nobody to receive it. That left the app, for this family, offering four ways
to bring arousal down and **nothing at all of what the distinction actually
says** — on screen, scared would have read as *calm down*, which is half the
message.

That is new. In angry and sad, the screen's options *are* the content; here the
main content sits on the paper side.

**Two pieces close the gap, and neither asks the child for anything:**

- **The literacy line carries the mechanism**: *o medo fica mais pequeno quando
  nos aproximamos devagar — não quando fugimos.* It is the first literacy line in
  the product that states a mechanism rather than describing the feeling, and it
  can, because this family's distinction is established rather than reasonable.
- **One new colouring page, `stepping-stones`** — a child part-way across a path
  of stones towards a waiting cat. **She looks at it; she is asked for nothing.**
  It is the only page in the library that carries a mechanism rather than an
  action.

**The stones must be visibly different sizes.** Five identical stones in a row is
a scale, and the approach sheet was only allowed at all because it orders
situations rather than levels (D-237). Uneven stones read as a path; even ones
read as rungs. Written into the prompt as a rule with its reason.

Nobody in the drawing is frightened, for the same reason nobody in the sad pages
is sad (D-220).

### D-240 `[DEFINED]` The three pre-style pages, and what is actually wrong with them
`HANDOFF.md` has carried "three colouring pages need regenerating" since the
house style was extended to colouring pages. Looked at side by side with the
pages accepted since, **the recorded reason is wrong**: it was read as thinness,
and `counting-fingers` is the thickest page in the library at 10.8px. **The fault
is that nothing in them is plush.**

- **`quiet-corner` is the worst**, and it breaks an explicit rule rather than a
  feeling: a straight wall, a straight skirting and a straight window edge. *No
  straight edges* is not a preference here.
- **`counting-fingers`** is a bare flat hand with no warmth at all.
- **`floating-feather`** is closest to passing — the clouds and the face are
  right — but the feather has a straight shaft and ruled diagonal veins.

Prompts written for all three, plus `stepping-stones`, to be generated in one
conversation (D-140). **The subject does not change**: a hand stays a hand, a
feather a feather, cushions cushions. These are replacements, so the data, the
names and the meanings stay where they are, and rule 6 is not touched — this is
the retroactive application of a style decision that was already made, not a
reinvention.

Two traps written into the prompts because they have already cost something:
**no numerals beside the fingers**, since that is how the first hand passed the
six-area check while still giving a child one colour; and **no faces on the
cushions**, since four identical faces turn a quiet corner into a crowd staring
back.

**What needs no art at all for the scared family**, recorded so it is not
generated by mistake: the family card and its three fine cards exist; both
covers are drawn in code; the schema will be drawn in code; the externalising
sheet reuses `frame.png`; the identity page reuses `mirror.png`; and the
approach sheet's structure is drawn in code, because a generated sheet with
fields comes back with deformed text in them (D-174).

### D-241 `[IMPLEMENTATION]` Three of the four passed; the hand did not, and it is worse than the one it replaces
Measured, flood-filled region by region, and looked at on A4.

| | Áreas | Linha | |
| --- | ---: | ---: | --- |
| stepping-stones | 13 | 6.3px | passa, linha fina |
| floating-feather | 12 | 8.2px | passa |
| quiet-corner | 11 | 7.2px | passa |
| **counting-fingers** | **6** | 10.8px | **passa o piso e falha o desenho** |

**The three that passed are in.** The feather is now plush, with six soft lobes
and a padded shaft in place of the ruled veins; the cushions have no wall, no
window and no straight line but the ground; and the stones are visibly uneven,
so the path does not read as rungs. No colour crossed between regions in any of
them, and the ground line reached both margins on both landscape pages — the
instruction that failed on three of four in the sad build.

**The hand is held back.** Its thumb is not sealed: the line at the base of the
thumb stops in the middle, so paint poured into the thumb runs into the palm and
the two are one region. It clears the six-area floor **only by counting the
merged palm-and-thumb as one**, and the page it would replace has seven.

So the replacement is better in style and **worse in the thing the page exists
for**: a hand whose thumb cannot be coloured separately looks to a child like a
mistake. The old page stays until a version arrives with the thumb closed.

It is the third time a page has passed a check for the wrong reason — after the
numerals counted as five areas, and after ink share was read as line weight.
**The check tells you a page is not broken; it does not tell you the page is
right.**

### D-242 `[IMPLEMENTATION]` The hand passes — seven areas, and the thumb is one of them
`counting-fingers` regenerated with the thumb line closed at both ends. **Seven
sealed areas**, and the flood-fill shows the thumb in its own colour, separate
from the palm. Line at 12.0px, the thickest in the library.

**The four regenerations of D-240 are now all in**, and every page of the
strategy library meets the house style. What changed in each was what the
measurement had not been catching: the feather gained six plump lobes and a
padded shaft in place of ruled veins; the cushions lost the wall, the window and
the skirting; the hand became a mitten with a closed thumb.

**What made the difference on the hand was naming the failure rather than the
requirement.** The first prompt said the thumb must be its own sealed area, in
general terms, and it came back open. The second described the exact wrong line
— one that starts at the web and trails off into the middle of the palm — and
gave a picture of the right one, a seam sewn all the way across. It is the
three-ways rule from `ART-DIRECTION.md`, and this is the clearest case of it
paying so far.

### D-243 `[IMPLEMENTATION]` The scared family's schema: what avoidance does across episodes
`scripts/figure-avoidance-cycle.py`, in both versions (D-189). Thirteen-page
workbook; section 9 is a marked stub until the sheets exist.

**Neither of the two shapes already drawn would do.** Anger's figure is one
episode. Sadness's is one episode carried two ways. **Fear's problem is not
inside an episode at all** — it is what happens across them, and no picture of a
single occasion can show it.

So it draws **four encounters with the same thing, twice over**. Running away
gives relief inside each and a taller peak in the next; staying — even a little,
even badly — gives a worse minute and a lower peak next time.

**The line underneath is the one that does the work with parents:** *a versão que
piora é a que sabe melhor no momento. É por isso que ninguém a escolhe de
propósito.* It takes the blame out of the conversation without taking out the
information.

No numbers on any axis, and **that matters more here than anywhere else**,
because the approach ladder is the only thing in this project that resembles a
scale and the figure must not lend it cover.

### D-244 `[IMPLEMENTATION]` The scared workbook's prose
Things in it that are decisions rather than writing:

- **Section 3 says the four screen options are not this family's main piece.**
  They lower arousal, and arousal is not the problem — fleeing is. They are
  presented as what makes staying possible: **not for the fear to pass, but to
  get through the little while.** No other family's strategy section has to
  demote itself.
- **The same action reads two ways, and the workbook keeps asking which.** Going
  to someone can be approach — asking for company in order to stay — or flight
  under another name. Distracting can be either. **The difference is never in the
  technique; it is in what happened next.** Two lines exist in the clinical record
  for this alone: *serviram para ficar ou para sair*, and *pede garantias*.
- **Reassurance-seeking is named as avoidance**, in the *preocupado* entry: the
  guarantee given relieves and feeds, exactly as flight does. It is the form
  hardest to see, because it looks like conversation.
- ***Tímido* is the only fine word in the whole deck that others use to describe
  the child**, often in front of her — so it hands her an identity rather than a
  word. The workbook separates temperament from social avoidance and says plainly
  that **a shy child with friends has no problem at all.**
- **The missing word:** European Portuguese has no child's word for social fear.
  *Tímido* names the temperament, not the avoidance, and a seven-year-old does
  not say *envergonhado de falar*. What goes unnamed is precisely what is most
  worked on at this age.

**Section 10 carries a limit no other family needed.** *Medo que tem uma causa
real não se trabalha assim*: a child afraid of someone at home does not have an
avoidance problem, she has a reason. **It is the only family in the set where the
thing the child avoids may be the thing she should be kept away from**, and no
sheet is applied before that is excluded.

It also states that **approach by steps is not exposure**: the sheet is
psychoeducation and planning, has no dose and no duration, and material sold
online may not imply it contains a treatment.

### D-245 `[IMPLEMENTATION]` The scared family's sheets, and the ladder
`docs/materials/assustado-fichas.html`. Nine for the child, one for whoever
applies it, one for the family. The child's book is twelve pages.

**Externalising is back.** It suits angry and scared, and it does not carry the
risk it carried for sadness: putting the Fear outside herself and being rid of it
is not this family's failure mode, because the distinction is about what she does
next rather than about keeping the feeling.

**Sheet 8 is the ladder, and it is the only sheet in the project that orders
anything.** Its columns are named rather than numbered — *por onde começo · depois
· depois · onde quero chegar* — and **the sheet asks nowhere how frightened she
is**. Checked on the built PDF: the only digits anywhere on it are the age range.

Three things in it that are decisions:

- **The first step is small on purpose**, and the sheet says so in its opening
  line: *tão pequeno que dê para fazer hoje*. The commonest way this goes wrong
  is a first step nobody can take.
- ***Quem vai comigo no primeiro?*** — company is part of the step, not an
  admission of failure.
- ***E se eu tentar e não conseguir, o que fazemos?*** and the closing line,
  **não conseguir uma vez não estraga nada — quer dizer que aquele bocadinho era
  grande de mais.** Without it the sheet sets her up for one attempt to decide
  everything. It is the sad family's *e se a pessoa não puder* in another shape:
  the refusal is planned for before it happens.

**Two other sheets do work no other family's do.** *O que eu faço quando ele
chega* asks, in its third column, **fico ou saio?** — which is the whole
distinction turned into something a child can tick. And *Preocupado* asks how
long the reassurance lasts, which is how a child discovers for herself that the
guarantee feeds the thing it relieves.

**A layout fault, fixed:** a one-row table is not a table with room. The ladder's
single row has to take a drawing, so it now gets the height four rows would have
had.

### D-246 `[IMPLEMENTATION]` The scared family's nine guides — and the family is closed
Twenty-five pages. Each guide begins and ends on its own page, verified by
searching the built PDF; thirty-six dynamics.

**Guide 9 did not fit at first**, and the way it failed is worth recording: the
title stayed on its page and **the session record slid onto the next one, alone**
— so a search for the title said the guide was intact while the printed page said
otherwise. It is the longest guide in the project, because the ladder needs the
most said about it. Four of its six fields were tightened until it fit.

Cautions in these guides that are rules rather than advice:

- **Sheet 3:** do not turn body awareness into symptom monitoring. A child who
  starts watching her body always finds something, and that feeds rather than
  relieves.
- **Sheet 7:** do not withdraw reassurance suddenly. What is agreed —
  *answer once, then answer the question and not the anxiety* — **is agreed with
  the adults, not with her.**
- **Sheet 8:** a shy child with friends has no problem at all, and this sheet is
  not applied as though she had. Absence of speech in specific settings is a sign
  to assess, not to apply more sheets.
- **Sheet 9:** never ask how frightened she is at each step, and no reward and no
  punishment — approach with a punishment on top stops being approach.

The most useful dynamic of the set is on sheet 4: **o que deixámos de fazer**,
put to the family. It measures accommodation without using the word, and the list
surprises the people making it.

**The scared family is closed.** Three of seven: angry, sad, scared.

### D-247 `[DEFINED]` The age range belongs to the workbook and never to the child's book
The sheets carry `data-age`, and the chip was being printed in both documents.
**Removed from the child's exploration book**; it stays in the workbook, where
every guide states the range in its first row.

The reason is not tidiness. The range is a decision for whoever applies the
material, **and one she often needs to override** — a sheet marked 7 to 9 is
frequently exactly right for the six-year-old in front of her, and the point of
her being in the room is that she can tell.

**Printed on the sheet the child holds, it does the opposite of helping.** A
child who reads *7 aos 9 anos* on a page she was given at six has been told she
is early; at ten, that she is late. Either way the number arrives before the task
and answers a question she had not asked.

All three families rebuilt and verified by searching the built PDFs: **zero age
ranges in the three exploration books and in the three parents' letters; nine,
ten and nine in the three workbooks.**

Checked at the same time, and correct in all three: the child's cover reads
**Caderno de exploração** beneath the family name, with the plain logo and no
licensing strapline (D-190).

---

# Increment 36 — The ashamed family (2026-08-17)

### D-248 `[DEFINED]` The governing distinction: *o que aconteceu não é quem eu sou*
Three were considered, and the second was taken apart by the thing it assumed.

**Rejected: *vergonha não é culpa***, which the recipe listed. True, and well
supported — guilt looks at the act and moves toward repair; shame looks at the
person and moves toward hiding. **But it is a clinician's taxonomy, not a child's
sentence.** No seven-year-old has that question, and no sheet hangs off it.

**Rejected, after being chosen: *o que eu fiz não é quem eu sou*.** It has the
right structure and it names the adult's error exactly — *és malcriada* instead
of *isso que fizeste magoou-o*. **It was taken apart by its own premise: it
assumes there was an act.** Much of childhood shame has none — being laughed at,
wetting the bed, being the poorest in the class, a parent who drinks, something
that was done to her. For those the sentence does not reach, and worse, it
implies she did something. **In a family that touches things that may have been
done *to* her, that is not a matter of wording.**

**Adopted: *o que aconteceu não é quem eu sou*.** It keeps the structure and
covers both origins — what she did and what happened to her.

**The child's version:** *a vergonha diz "tu és" — mas o que aconteceu não é quem
tu és.*

**Hiding is this family's mechanism, as avoidance is fear's.** Shame orders
concealment, and concealment is what maintains it: it blocks repair, and it
blocks the discovery that nobody thinks of her what she believes they do. The
workbook is organised around that, not around the guilt-shame distinction — which
stays in the clinician's framing where it belongs.

### D-249 `[DEFINED]` *Embaraçado* is not shame, and its sheet is where the language gets corrected
Embarrassment is a different emotion — social, light, passing — and European
Portuguese puts it inside *envergonhado* along with shame. **A child who says
*estou envergonhada* may be describing a trivial moment in the playground or a
global condemnation of herself.**

**It is this family's *chateado*, and the heaviest of the three found so far**:
*chateado* confuses three families of feeling, *sozinho* confuses two intensities
of one, and this one confuses a passing social moment with the emotion most
associated with concealment and with harm done to a child.

**It stays in the family, and its sheet is about the difference.** Rejected:
leaving it in with the workbook merely explaining the distinction, which would
leave the weakest sheet of the set doing another emotion's work; and taking it
out, which would clear the axis and leave **one of the most frequent experiences
of this age with no name anywhere in the product**, besides discarding a card
already drawn and approved.

The reasoning is the *chateado* reasoning: **the ambiguity does not go away by
removing the card — it lives in the child's head either way.** Better inside a
sheet that treats it than inside a silence.

So the sheet becomes the one that teaches what the language erased: **isto passa
em cinco minutos, e aquilo fica.** It stops being the family's weakest page and
becomes the one carrying its own distinction, exactly as *chateado* does in the
angry family.

**The family therefore has one axis and one correction**, not two axes: hiding is
the mechanism throughout, and the *embaraçado* sheet exists to stop a passing
social moment being filed under it.

### D-250 `[DEFINED]` The middle step: *quem é que continua a gostar de ti na mesma?*
**None of the nine pages already drawn serve this family.** Anger's five are ways
down, and shame does not rise and fall like that. Sadness's six are company —
**and shame, unlike sadness, makes a child want to be alone, and that wanting is
the problem rather than the answer.** Offering *um bocadinho no meu sítio* here
would be proposing the mechanism that maintains it.

The question comes straight out of the distinction. Shame's claim is that if she
were seen as she is, nobody would want her. **The screen does not argue with
that — it asks her to name.**

**It is also the only thing that can be offered here without opening anything.**
Naming people closes on itself. Telling, showing and repairing do not: each needs
someone present to receive it, and those belong to the workbook.

**One constraint, fixed now.** A child who can name nobody is the child this
family is most about, and on a screen with nobody there she must not be left
staring at a blank. **At least one option has to be available to every child** —
the role *uma coisa macia* played in the sad family. The set is chosen with that
as a requirement, not as a nicety.

### D-251 `[DEFINED]` The five, and the one that goes to the workbook
| | Base | Grade |
| --- | --- | --- |
| Alguém cá de casa | vinculação, disponibilidade do cuidador | **estabelecido** as a mechanism |
| Alguém que já sabe | a revelação não confirmou a previsão | **razoável** |
| Um bicho | companhia sem julgamento | **prática** |
| Alguém que também já se enganou | normalização entre pares | **razoável** |
| Uma coisa que continua igual | continuidade e previsibilidade | **prática** |

Three reuse artwork — *alguém ao pé de mim*, the bench, the dog — and two are
new.

***Alguém que já sabe* is the one that does the work.** Shame predicts that being
seen would end the relationship. Naming somebody who has already seen and is
still there is that prediction failing, and the child produces the
counter-evidence herself rather than being argued out of it. **The screen never
asks what that person knows**, only who they are.

***Uma coisa que continua igual* is there because of the constraint** (D-250): a
child who can name no person must still have something to name. The bed, the
route to school, the same breakfast. It is *prática* and it is not in the set for
its evidence — it is in the set so that nobody meets a blank.

**Held back to the workbook: *alguém de quem eu gosto na mesma*.** It inverts the
question — who does *she* still love, knowing what she knows about them — and it
is the sharpest of the six. It is also the hardest to grasp alone on a phone, and
it needs a person to say it. It goes into section 6 as a dynamic, where the
inversion can be walked through.

**The pattern is now three families deep and worth naming:** every family loses
something at the screen and keeps it in the workbook, and it is always the piece
that needs a person. Sadness lost nothing; fear lost the ladder; shame loses the
inversion. **The workbook is not a longer version of the app — it is where
everything that opens has gone to live.**

### D-252 `[DEFINED]` Nobody is being looked at in the ashamed pages
Each family has now added one rule to the artwork, and they are not the same
rule. In the sad pages **nobody is sad**; in the scared pages **nobody is
frightened**; here **nobody is being looked at**.

No pointing, no group of faces turned towards one child, no figure standing alone
in front of others. **Shame's whole content is being seen**, and a drawing that
stages it hands the child the feeling instead of the way out. It is a stronger
version of the D-220 reasoning: there the risk was the page reporting what she
chose; here the page would also be doing the thing the family is about.

### D-253 `[IMPLEMENTATION]` The two new pages, and why one has no people in it
`also-got-it-wrong` — two children side by side behind a fallen tower of blocks,
both calm, both facing out. **Neither is at fault and neither is pointing**: the
page has to show two people in something gone wrong without staging blame, which
is the hardest composition asked for so far.

`same-as-always` — a corner of a bedroom in the morning, **with nobody in it**.
Chosen over the route to school because every child has a bed and not every child
has the same walk. It is the quietest page in the library on purpose: it exists
so that a child who can name no person still has something to name (D-250), and
**that is exactly why it must contain no people at all.** A person in it changes
the subject back.

Both carry the ground-line instruction, which has now worked on every landscape
page since it was rephrased.

### D-254 `[IMPLEMENTATION]` The two ashamed pages passed, and the family is live at five
| | Áreas | Linha |
| --- | ---: | ---: |
| also-got-it-wrong | 20 | 7.2px |
| same-as-always | 15 | 6.3px, avisado |

No colour crossed between regions in either. The block page has the most fillable
areas of any page in the library. `same-as-always` sits under the 7px floor, as
`stepping-stones` and `keepsake-shelf` do — recorded, not acted on.

Both hold the rule this family added: **nobody is being looked at.** Neither
child at the blocks is pointing, both face out, and the bedroom has nobody in it
at all.

The screen now asks **quem é que continua a gostar de ti na mesma?** over five
pictures, and the literacy line carries the mechanism as the scared one does:
*ela diz «tu és» — mas o que aconteceu não é quem tu és. E dá vontade de
esconder, que é a única coisa que a faz ficar.*

**Four families are live on screen, and each asks a different question.** Anger:
*qual queres experimentar*. Sadness: *o que te faz companhia*. Fear: *qual queres
experimentar*, with the mechanism carried by the literacy line and one picture.
Shame: *quem continua a gostar de ti na mesma*. **The question is now the part
that identifies a family**, more than the pictures under it — two of the five
ashamed pages are the same drawings the sad family uses, doing different work.

### D-255 `[IMPLEMENTATION]` The ashamed schema is a loop, not a graph
`scripts/figure-shame-loop.py`, in both versions. **The first schema in the
project that is not a graph.** Anger's is one episode over time, sadness's is one
episode carried two ways, fear's is a series of episodes. **Shame's mechanism has
no time axis worth drawing** — it is a circle that closes on itself, kept closed
by the prediction never being tested.

Four boxes, one loop, one arrow leaving it. **The arrow that leaves is the whole
intervention: *alguém vê e fica*.**

**A fault worth recording, because it was a fault of reasoning and not of
drawing.** The first version had hiding *after* nobody being able to contradict
her. The causal order is the other way — she hides, and *that* is why nobody can
— and with the boxes in the wrong order the figure taught the mechanism
backwards. The event now enters the loop from outside, since it does not repeat.

### D-256 `[IMPLEMENTATION]` The ashamed workbook's prose, and its warning at the top
Thirteen pages; section 9 is a stub. **It is the first workbook that opens with an
instruction to read the limits before applying anything**, because it is the only
family in the seven where what the child is ashamed of may be something done to
her.

Decisions inside it:

- **Section 1 records both rejected distinctions and why**, including the one
  that was chosen and then taken apart by its own premise.
- **The error of this family is naming rather than acting: *rotular*.** *És
  malcriada* tells a child exactly what shame already tells her, with an adult's
  authority behind it. **And the workbook extends it to praise**: *és uma menina
  tão boazinha* installs the same equation and prepares *então sou má*.
- **Section 3 flags the danger inside the strongest option.** *Alguém que já
  sabe* works because the child produces the counter-evidence herself — **unless
  the person who already knows is the person who shamed her**, in which case the
  figure points at the problem. The guidance says to ask who it is, every time.
- **The *culpado* entry carries the question that splits this family in two:**
  was it something she did, or something that happened? Guilt over an act is
  workable and leads to repair. **Guilt over an event — a separation, an illness,
  something done to her — is not guilt at all, and repair has nothing to hold.**
- **Section 8 names the missing word, and it is the most consequential of the
  seven families:** European Portuguese has no child's word for shame that comes
  from nothing she did. *Humilhado* is adult and implies someone humiliating.
  **What goes unnamed is exactly the shame that most needs saying.**

**Section 10 is unlike any other family's.** It states that the questions are
about the prediction and never about the content — *o que achas que aconteceria*,
never *o que é que fizeste* — that sheet 8 is not applied without knowing who the
person is, that sheet 9 is not applied where there was no act, and that **if
suspicion of harm appears the workbook stops there**: what follows is the legal
duty to report and the institution's procedure, and nothing here substitutes for
either.

### D-257 `[IMPLEMENTATION]` The ashamed family's sheets, and the two that are conditional
`docs/materials/envergonhado-fichas.html`. Nine for the child, one for whoever
applies it, one for the family. The child's book is twelve pages.

**Nothing in the file asks the child what she hides.** Every question is about
the prediction — *o que achas que aconteceria se soubessem* — and never about the
content. If she tells, it is received; it is not gone looking for.

**Two sheets are conditional, and the workbook now names them rather than
numbering them**, so the condition cannot come loose from the sheet if the order
ever changes:

- ***Quem já sabe*** is not applied without knowing who that person is.
- ***Arrependido*** is not applied where there was no act.

Sheets that do work no other family's do:

- ***O que eu fiz e o que eu sou*** is the distinction as two columns, and it
  ends with the move that does most of the work: **if a friend said that about
  himself, what would you say to him?** Almost every child is far more generous
  with others than with herself.
- ***Culpado* asks the question that splits the family**: was it something you
  did, or something that happened? And it closes with the sentence that has to be
  in her book and not only in the clinician's — *sentir-se culpada não quer dizer
  que se seja culpada.*
- ***Embaraçado* teaches what the language erased**, by asking for one moment
  that has stopped mattering and one that has not. **A primeira passa em cinco
  minutos. A segunda fica.**
- ***Quem já sabe* ends by naming the evidence out loud**: *a Vergonha disse que
  ia acontecer uma coisa, e não aconteceu.* It is the only sheet in the project
  where the child is shown a prediction of her own failing.

**The letter carries the correction to the people who make it**, in both
directions: *isso que disseste magoou o teu irmão* instead of *és malcriada* —
and *és uma menina tão boazinha* named as the same equation in reverse. It closes
by saying that almost every adult carries old shame, and that it tends to wake
when a child goes through the same: **reparar nisso é a diferença entre responder
a ela e responder à nossa memória.**

### D-258 `[IMPLEMENTATION]` The ashamed family's nine guides — and the family is closed
Twenty-six pages, thirty-six dynamics. Each guide begins and ends on its own
page, and **each one's session record is on the same page as its title** —
checked explicitly this time, because that is exactly how guide 9 of the scared
family failed while looking intact to a title search.

Cautions in these guides that are rules rather than advice:

- **Sheet 2:** do not correct the character with facts. A child who draws an
  enormous Shame is not answered by being told it is not that big — she is asked
  where it sends her.
- **Sheet 3:** do not argue with the right-hand column. **Arguing against a
  global label reinforces it**; what undoes it is hearing herself say something
  else to somebody else.
- **Sheet 4:** if she can name nobody, **do not fill it in for her and do not
  press**. Naming somebody to please us produces a false list and closes the
  subject.
- **Sheet 6 → 7 is conditional:** if the answer was *it happened*, the repair
  sheet is not used at all.
- **Sheet 8:** the sheet asks whether it still stings, **not what it is**.
- **Sheet 9:** not applied without knowing who the person is, and not applied at
  all if she can name nobody.

Two dynamics carry decisions rather than activities. **Sheet 6, with the
family:** if it is a separation or an illness, the adults say out loud, in front
of whoever applies it, that it was not her fault — **she needs to hear it from
them, not from us.** And **sheet 8, with the family:** stop telling her
embarrassing story to other people as an anecdote. It is frequent, it is
affectionate, and it is precisely the mechanism.

One dynamic asks the child for something the language cannot give her: **what
word she would use for shame that comes from nothing she did.** There is none in
Portuguese, and children usually invent a good one.

**Four families are closed: angry, sad, scared, ashamed.** Three remain — feliz,
calmo, tédio — and they are the ones with no strategies of descent at all.

### D-259 `[DEFINED]` *Arrependido* becomes two sheets — the wish and the saying
The single sheet asked two things that a child can manage separately: what she
would have done differently, and what she wants to say to whoever was hurt.

**They are not the same task.** The first is hers alone — she can complete it in
the room, with nobody else's agreement needed. **The second depends on another
person being willing to hear it.** Together on one page, a child who cannot
manage the second leaves believing she failed the first as well.

- ***O que querias ter feito de outra maneira*** — the wish turned into an
  alternative, and forward: *se voltasse a acontecer amanhã, o que farias?*
- ***O que querias dizer a quem ficou magoado*** — the speech bubbles, and it
  closes with **se ela não quiser ouvir hoje, não quer dizer que não queira
  nunca.**

**Both are conditional on the same answer** in *Culpado*: something she did, not
something that happened. The workbook now names both in the limits.

**The caution that guards the first is the same one anger's forward sheet
needed** (D-182), and it is worth repeating because the two are one word apart:
**never *o que é que devias ter feito*.** That is a telling-off dressed as a
worksheet. The question is about what **she** wanted.

The family goes to ten child sheets and the child's book to thirteen pages; the
workbook to twenty-seven.

**Guide 7 failed the same way the scared family's guide 9 did** — the title held
its page and the session record slid onto the next — and it was caught by the
check added after that one, which now looks for a record on every page carrying a
title. Four fields tightened until it fit.

---

# Increment 37 — The bored family (2026-08-17)

### D-260 `[DEFINED]` The governing distinction: *o tédio não é um problema para resolver* — with a sheet that corrects the language
**This is the first family where the feeling is usually fine.** The other four
needed containing or accompanying; this one mostly needs leaving alone. So the
distinction has two jobs at once: protect boredom from being treated as a fault,
and still catch the cases where it is not boredom at all.

**Rejected: *tédio não é preguiça***, which the recipe listed. It defends the
child from a label and names the adult's error, but it is a sentence about what
she is not, and no sheet hangs off it.

**Adopted as the axis: *o tédio não é um problema para resolver*.** It names what
almost every adult does — filling the emptiness immediately, now nearly always
with a screen — and it governs sheets about tolerating rather than filling.

**And adopted as a sheet, not as the axis: *não ter nada para fazer não é o mesmo
que não conseguir começar*.**

European Portuguese puts two very different things inside *aborrecido*:

- **there is nothing to do** — under-stimulation, and useful. It is not treated;
  it is tolerated.
- **I cannot start** — which may be anxiety, low mood, avoidance of a task,
  attention difficulty, or a task pitched wrong. **That is not boredom, and it is
  the only thing in this family that asks for intervention.**

**Why it is a sheet and not the axis**, which was the question that took the
longest: an axis of *these are two different things* leaves the child who is
bored and inventing something — the best thing boredom does — unprotected, since
the frame would be about telling states apart rather than about leaving one
alone. **But an axis of *leave it alone* alone gives the child who cannot start
the advice meant for the other one.**

The precedent is the ashamed family: **one axis and one correction** (D-249).
Hiding is the axis there and *embaraçado* is the sheet that corrects what the
language glued together. Here the shape is identical.

**One caution written into the framing, at Ricardina's prompting and against the
temptation to overclaim.** That boredom produces invention is worth saying — a
child who is never bored never needs to invent anything — but the literature
linking boredom to creativity is **modest and mostly adult and laboratory-based**.
Graded **razoável**, and said as such. It is too attractive an idea to assert
carelessly.

### D-261 `[OPEN QUESTION]` The bored path on screen was designed to suggest activities
D-119 made boredom the one family where the product may propose something to do
without implying anything is wrong — the `now` path, *o que posso fazer agora*.

**Under D-260 that is the product doing what the workbook tells the parents not
to do.** Suggesting an activity the moment she says she is bored is filling the
emptiness for her.

It needs resolving before the family is built, and it is not obvious: removing
the suggestions leaves the screen with nothing to offer, which in this family may
be exactly right.

### D-262 `[DEFINED]` Boredom waits to be asked — closes Q on D-261
The screen shows the line first and keeps the suggestions behind one button.

> **Não faz mal nenhum não ter nada para fazer. Não tens de encontrar já uma
> coisa.**

**Ainda estou aborrecida** · Pronto · Escolher outro sentimento

Tapping the first opens the grid where it stands. No intervening screen: **it is
one more button of the kind she already taps everywhere, not a step added to the
path.**

**The word *avaria* was rejected from the line, and the reason generalises.** The
first draft read *o tédio não é uma avaria*. It is an engineer's word, it is
mine, and it tells a child she might have been broken — introducing the idea in
the one place we wanted it absent. **It is the scales trap in another form:
naming a thing in order to deny it leaves it in the room.** The line that
replaced it names nothing and only lifts the pressure.

**The button says *ainda estou aborrecida*, not *quero ideias*.** The second
makes her someone requesting help; the first leaves her describing how she is,
which is all this activity asks of her in every other family.

**A child who invents something never reaches the suggestions**, and leaves by
the same exit as everyone else, with nothing said about having done better.

This resolves the only inconsistency between a workbook and the screen in five
families: the workbook tells parents that filling the emptiness immediately is
this family's error, and the product now waits to be asked.

**Built and typechecked; not yet observable.** No colouring page is wired to
`bored`, so the family still closes after the body map, which is correct while
there is nothing to offer. The mechanism is in place for when the suggestions
exist.

### D-263 `[DEFINED]` The six bored options carry both axes at once
Asked whether the suggestions should be organised by **material** or by **kind**,
the answer was both — and the literal cross would have been twenty pages and a
matrix no child reads.

**The name is the kind; a line beneath it says what it needs.** A drawing can
only show an activity, so the activity is the name. The set is then chosen so
that the six together cover both axes: **each kind appears once, and the
materials run from *nothing* to *another person*.**

| | Precisa de |
| --- | --- |
| Não fazer nada de propósito | nada |
| Inventar uma história | nada |
| Fazer uma coisa com as mãos | papel, lápis, uma caixa de coisas |
| Mexer o corpo | espaço |
| Ir lá para fora | lá fora |
| Uma coisa com outra pessoa | alguém |

A child asking *what can I do right now* reads the right-hand column; a child
asking *what do I feel like* reads the names.

***Não fazer nada de propósito* is the most important of the six**, and the one
no list of suggestions ever has. Putting it inside a list of things to do is the
family's distinction on the screen itself — **and it is the only figure that
tells her the thing she is already doing is one of the options.**

*Mexer o corpo* reuses the jumping child; the other five are new. **It is the
most expensive family for artwork and the last one that needs any**: happy and
calm have no options at all.

### D-264 `[DEFINED]` Nobody is bored in the bored pages, and there are no screens
Each family has added one rule to the artwork. Sad: nobody is sad. Scared: nobody
is frightened. Ashamed: nobody is being looked at. **Bored: nobody is bored** —
no slumped shoulders, no head on a hand, no sighing face. These are pictures of
what she might do, not of what she is feeling.

**And no screens anywhere in the five.** No television, no tablet, no phone.
**Filling the emptiness with a screen is the commonest version of this family's
error**, and a screen drawn on the page would be the material proposing it. It is
the first artwork rule in the project that exists to keep something out of the
picture rather than to keep something in.

### D-265 `[IMPLEMENTATION]` Three of five passed; two leaked into the sky and go back
| | Áreas | Linha | |
| --- | ---: | ---: | --- |
| doing-nothing | 12 | 6.3px | passa |
| making-something | 12 | 6.3px | passa |
| with-someone | 12 | 6.3px | passa |
| **making-a-story** | 8 | 6.3px | **falha** |
| **going-outside** | 10 | 6.3px | **falha** |

**All five clear the six-area floor, and two of them are broken anyway.** The
count did not catch it; a second check did.

**The new check, and it is worth keeping.** Instead of counting sealed regions,
measure how much of the page is reachable from the frame — everything a flood
from outside can touch. On a good page that is the background and nothing else.

| | Alcançável a partir da moldura |
| --- | ---: |
| doing-nothing | 42% |
| making-something | 51% |
| with-someone | 57% |
| making-a-story | **68%** |
| going-outside | **71%** |

**In `making-a-story` the child's whole body is open to the sky** — the ground
line passes behind her and her outline is broken where they meet, so her top,
her arms and her trousers are one region with the background. A child taps her
jumper on screen and the sky fills. **The subject of the page is the part that
cannot be coloured.**

**In `going-outside` the tree and the grass are open to the sky** for the same
reason, so the two largest shapes on a page about going outside are unfillable.

Both pass the six-area rule because the toys, the clouds and the bushes carry the
count. **It is the fourth time a page has passed a check for the wrong reason** —
after the numerals, after ink share read as line weight, and after the thumb. The
region count says a page is not empty; it does not say the right things are
sealed.

`with-someone` is accepted with its floor open to the background, which is a
small loss and not a fault: the children, the board and the pieces are all
fillable, and several accepted pages have no separate floor at all.

**A drift worth naming:** every page generated in the last two rounds comes in at
6.3px — six of the fifteen in the library are now under the 7px floor, and none
of them was under it before. The floor warns rather than refuses, deliberately,
but six is no longer a stray case. **Worth watching, and worth a decision if the
next batch is 6.3 too.**

### D-266 `[IMPLEMENTATION]` The bored family is live, and the button now does something
Four options wired — the three new pages plus *mexer o corpo*, which reuses the
jumping child. Two more arrive when the two failed pages come back.

Walked in a browser: choosing *aborrecido* shows the card, the line **não faz mal
nenhum não ter nada para fazer — não tens de encontrar já uma coisa**, and three
buttons. **The pictures are not there.** Tapping *ainda estou aborrecida* opens
them in place, and the question *o que te apetece agora?* appears with them.

It is the only family in the product whose middle step has to be asked for, and
on screen it reads as one more button rather than as a step.

### D-267 `[IMPLEMENTATION]` Both came back sealed — and the thickness instruction worked
| | Áreas | Linha | Alcançável de fora |
| --- | ---: | ---: | ---: |
| making-a-story | 10 | **10.0px** | 58.3% |
| going-outside | 12 | **10.0px** | 53.9% |

The child's body is a closed shape in one and the tree is in the other, verified
by flood-fill. Both sit comfortably under the 60% the new check asks for.

**Two things were changed in the prompt and both took.**

**The ground-line instruction, phrased as a failure rather than as a
requirement.** The earlier version asked for a line spanning edge to edge and got
one that cut through the figures. The new one names the exact wrong outcome —
*the line ran behind the child and left a gap in her own outline; her jumper
became one region with the sky* — and gives the picture that fixes it: **each
figure is a paper sticker laid on a drawn horizon; the horizon passes behind, the
sticker's edge goes all the way round.** It is the third time this year that
naming the failure worked where naming the requirement had not, after the ground
line itself and the thumb.

**And *make the outline noticeably THICK — thicker than a normal colouring
book*** took the stroke from 6.3px to 10.0px in both. That is the answer to the
drift recorded in D-265: **the thinning was a prompt problem, not a generator
one**, and the line is now among the thickest in the library. The remaining six
pages at 6.3px are candidates for the same one-line addition, though none of them
fails anything.

### D-268 `[IMPLEMENTATION]` The bored family is complete on screen — six options
All six wired and walked in a browser. Choosing *aborrecido* gives the card and
the line and nothing else; **ainda estou aborrecida** opens the six in place
under *o que te apetece agora?*.

**Five families are now live on screen**, each asking a different question, and
this is the only one that has to be asked before it answers.

Two remain — feliz and calmo — and neither has options at all, so this was the
last artwork any family needed.

### D-269 `[IMPLEMENTATION]` The bored family's schema: a strip of time, not a curve
`scripts/figure-boredom-time.py`, in both versions. **The fourth different shape
in five families.** What matters here is not how a feeling moves but **what fills
a stretch of empty time**, so the figure is a strip of time with blocks in it.

Two strips. In the first the emptiness is filled the moment it appears, the
discomfort ends at once, and nothing of hers happens. In the second the
discomfort lasts a little longer, there is a stretch of nothing, and then
something that came from her.

**The last block is drawn with a dashed edge on purpose.** The figure may not
promise that the invention arrives, because it does not always and the evidence
is thin (D-260). The clinician's line says so: *a parte que custa é o princípio,
não o todo — e o que vem no fim não vem sempre nem por encomenda.*

### D-270 `[IMPLEMENTATION]` The bored workbook's prose — thirteen pages, and short on purpose
Section 9 is a stub. **It is the shortest of the five and the workbook says so in
its own opening**: the other families had a mechanism to explain, and this one has
mostly one thing to ask of adults.

Decisions inside it:

- **Section 3 states that none of the six options has an evidence base of its
  own**, and it is the only family of which that can be said. They are activities,
  not strategies, and no literature compares making something with going outside.
  **Prática, all of them.** What makes them a set is the coverage of the two axes,
  and that is all that may be claimed.
- **What matters clinically is not which she picks but what kind** — and **not
  pressing the button at all is the most interesting answer the activity can
  give**, which is what the whole mechanism was built to make possible.
- ***Sem vontade* is named as the word that points outside this workbook.** It may
  be boredom and it may be low mood, and it is the only fine word in all seven
  families that leads directly to an assessment. Its sheet exists to notice it,
  not to work on it.
- **The missing word is the most revealing of the seven families:** European
  Portuguese has no child's word for empty time that is good. *Ócio*, *sossego*
  and *lazer* are adult. **Everything a child has for saying she has nothing to do
  is a complaint** — and it is hard to value something whose only available word
  is a grievance.

**Section 10 carries a limit no other family needed**: that the boredom-creativity
link is reasonable and not established, that the workbook does not assert it and
the figure does not promise it. **A material that sold it as certain would be
doing with an attractive idea what this project refuses to do with every other
one.**

It also says that nothing here is about screens as such — the screen appears
because it is what fills the emptiness fastest today, not because this workbook
has a position on screen time.

### D-271 `[IMPLEMENTATION]` The bored family's sheets — and no externalising sheet
`docs/materials/tédio-fichas.html`. Nine for the child, one for whoever applies
it, one for the family. Twelve pages in the child's book.

**There is no *O Tédio vem visitar*, and that is a decision.** Turning boredom
into a character to be sent away is the opposite of what this family says: the
whole point is to tolerate the thing rather than get rid of it. Angry and scared
externalise; ashamed does too, because shame says *you are* and a character puts
it outside her. **Boredom is the one feeling in the set that should stay where
it is.**

What replaces it is ***A coisa que eu inventei*** — a frame to draw something she
once made up because there was nothing to do. It uses the same picture the
externalising sheets use, doing the opposite work: **instead of putting the
feeling outside her, it puts something of hers on the page.**

Sheets that do work no other family's do:

- ***Aborrecido* is the correction sheet**, and it is the only one here that leads
  anywhere: one box for a time there was genuinely nothing to do, one for a time
  there were things — *até coisas de que gostas* — and she still could not start,
  and a third asking what seemed to be stopping her. It closes with **a primeira
  não precisa de ser resolvida; a segunda é outra coisa.**
- ***Sem vontade* is the only child's sheet in all seven families that tells her
  to talk to an adult.** *Se isto durar muito tempo e for de tudo, não é tédio.*
  Every other sheet closes on itself; this one deliberately does not, because the
  thing it might be catching is not something a worksheet closes.
- ***Quando é que ele aparece*** ends by asking whether she found something
  herself or somebody gave it to her — which is the family's whole distinction
  turned into one question a child can answer.

**The letter opens by naming what it is:** *esta é a única carta destas em que o
que vos peço é para não fazerem*. And it says *costumam* rather than *sempre*
about what comes out of the empty time, in the letter itself, because the caveat
belongs where the parents read it and not only in the workbook.

### D-272 `[IMPLEMENTATION]` The bored family's nine guides — and the family is closed
Twenty-six pages, thirty-six dynamics. Each guide whole on its own page, record
included.

Cautions in these guides that are rules rather than advice:

- **Sheet 1:** do not promise the idea comes. The page says *às vezes* and that
  is to be read as written. **A child who waits and invents nothing has not
  failed.**
- **Sheet 3:** none of the six is better than another, and doing nothing is not
  the worst. If the last box stays empty, do not fill it for her.
- **Sheet 4:** do not praise the invention as performance. **It is evidence, not
  a gift** — turning it into praise puts pressure exactly where this family is
  trying to take it away.
- **Sheet 6:** if the answer is *não consigo começar*, **we have left boredom**,
  and the rest of this workbook is not the right material.
- **Sheet 9:** it is the only child's sheet in the project that does not close on
  itself, and that is deliberate. **If the answers point that way, the path is
  assessment and not more sheets.**

Two dynamics carry decisions. **Sheet 6, with the family: if the answer is *I
cannot start*, say so to the adults in front of her** — it is the correction of
the *preguiçosa* label, and she has to hear it. And **sheet 9, with the family:
ask them the same three questions, and if the answers agree, this leaves the
workbook.**

One dynamic asks the child what the language cannot give her: **what word she
would use for empty time that is good.** There is none in Portuguese, and her
answer is usually better than ours.

**Five families are closed: angry, sad, scared, ashamed, bored.** Two remain —
feliz and calmo — and neither has options, a mechanism to correct, or a family
error to name. **They will need a shape none of the five has used.**

---

# Increment 38 — The two that are not problems (2026-08-17)

### D-273 `[DEFINED]` Happy and calm are resource families — the three logics in order
Neither has what the other five had. **No family error to name** — nobody brings
a child because she is happy. **No mechanism maintaining it** — avoidance keeps
fear, hiding keeps shame, and nothing needs correcting here. **No options to
offer** — there is nothing to give someone who is well. And the distinction that
carries the other five always presupposes an error to avoid.

D-119 already gave them their own path on screen — *momentos em que me sinto
assim* rather than *o que queres experimentar* — and the shape grows from there.

**The one thing that is true of both: these families are not worked when they
appear, they are worked so that they can appear.**

Three logics were considered and **all three are adopted, in an order that is
itself the argument:**

1. **Reconhecimento — the raw material.** Where, with whom, what the body does. A
   child with words only for what goes wrong has half a vocabulary, and one who
   recognises calm recognises its absence better. On its own it is thin.
2. **Saboreio — the method.** Staying with the good instead of passing through
   it. **It is the only one of the three with an identifiable evidence base**, and
   it is reasonable rather than established.
3. **Recurso — the purpose.** What is gathered on the good days is what the bad
   days draw on. It is *uma coisa que me faz companhia* and *quem continua a
   gostar de mim*, collected while everything is fine rather than in the middle
   of the storm.

**Recognition is what is gathered, savouring is how, and resource is what for.**

**The consequence that matters most:** these two become the families applied
**first** rather than last. **The store is built before it is needed** — and the
other five gain somewhere to send the child to fetch from, which is what makes
these part of the system rather than a pleasant appendix.

### D-274 `[DEFINED]` Two workbooks, not one — and activation is what separates them
Happy and calm share everything D-273 decided: the same three logics, the same
path on screen, the same absence of an error to correct. Written like the other
five they would produce **two nearly identical workbooks**, which is the worst
thing to hand a colleague — she reads the second believing she opened the wrong
file.

**Rejected: one workbook in two halves.** It would have avoided the duplication
by construction and it assumes the two are applied together, which is probably
true. **It was rejected on a commercial ground rather than a clinical one**: the
line is sold by family, and a double workbook breaks the shelf for all seven.

**Adopted: two, with activation as the axis of each.** They are both positive and
they differ in activation, which is a real distinction with its own literature.

- **Feliz is positive and activated.** It wants to share, to move, to tell. **It
  builds a store of memories and people.**
- **Calmo is positive and deactivated.** It wants to stay, and for nothing to
  change. **It builds a store of places and body states.**

**And they are not interchangeable clinically**, which is what makes two
workbooks honest rather than tidy: **an anxious child needs the calm one; a flat
child needs the happy one.** A single workbook would have let a colleague reach
for whichever half came first.

**The obligation this creates, and it is recorded as a test rather than an
intention:** if the two prose sections end up saying the same things in different
words, the decision was wrong and should be revisited. Each must be readable
without the other and must not be a rewrite of it.

### D-275 `[DEFINED]` The calm family: *a calma não faz barulho*
Four candidates, and the one that had been recommended was taken apart by
Ricardina before it was written down.

**Rejected: *calmo não é aborrecido*** — makes a positive family into a defence
against another one, and governs nothing.

**Rejected: *calmo não é estar quieto*** — closest to a real distinction, and it
corrects a real adult error (ordering a child to sit still and calling it calm).
But it is a sentence about discipline rather than about the child.

**Rejected: *a calma treina-se*** — true and useful, and it turns the family into
a programme of exercises. The axis is gathering, not training.

**Rejected, after being recommended: *já estiveste calma antes — e isso serve*.**
It presupposes its own answer. **A child who cannot remember is met with a
statement about herself that she cannot confirm — and she is precisely the child
this family is for.** It is the *avaria* mistake in another form: the sentence
puts something in the room that we wanted absent.

**And the objection has a second layer that only appeared under it.** Many
children do not recognise calm **because it has no signal**. The other six
families announce themselves — the body speeds up, tightens, weighs, hides.
**Calm is the absence of announcement, and an absence is not noticed.** It is not
a failure of memory; there was nothing to remember.

**Adopted: *a calma não faz barulho*.** It names exactly that, and it presupposes
nothing: it starts from now rather than from recall.

**The child's version:** *a calma não faz barulho — por isso às vezes ela está lá
e a gente nem dá por ela.*

**Two consequences, fixed now.**

**The first sheet stops being about remembering and becomes about noticing now** —
the body, in the room, with the clinician there. Only after that does asking
about places and other times make sense, because only then does she know what she
is looking for.

**No breathing in this family.** It already lives in angry and scared, where it is
response modulation and exists to bring an activation down. **Here there is
nothing to bring down.** If breathing enters, this becomes a relaxation manual and
loses what makes it distinct. The axis is the body and the place, never the
technique.

**And the schema cannot explain a mechanism, because there is none.** It will
have to do something else — most likely show the store and the arrows leaving it
towards the other families, which is the only place the whole system would be
visible at once.

### D-276 `[DEFINED]` Calm has no location in the body — and the map stays anyway
**Calm is general deactivation.** In the other six families the body signals at a
point — the chest, the stomach, the throat, the legs. Here what changes is the
**tone of the whole body**: softer, stiller, slower, looser.

**That is the reason underneath *a calma não faz barulho*.** It is not only that
it is quiet — **it is that there is nowhere to point.** So the questions ask for
the state and never for the zone, and the words looked for are tone words: *mole,
pesado, quieto, solto, devagar*.

**Removing the body map from this family was proposed and rejected**, and the
rejection came from Ricardina. The map has never obliged anyone to point and
always has the way out beside it. **A child who does locate calm is not mistaken —
she is saying something about herself**, and a product that had taken the map away
would never have found out.

So: **the map appears in all seven, as always.** What changes is only what is
written around it. **The absence of a location is what is expected; the presence
is the finding** — the exact opposite of every other family.

**And it separates calm from happy more sharply than any other decision.**
Happiness does locate — excitement in the chest, restlessness in the legs — so
the same question carries two opposite clinical meanings. That is better than
taking the map away from either.

### D-277 `[DEFINED]` The screen question is the longest of the seven, and deliberately so
> **O teu corpo fica assim em que sítios, ou em que alturas?**

**Two doors instead of one.** *Quando* asks for a moment and a moment asks for
memory, which is exactly what this family cannot presuppose. *Onde* is easier,
because the place exists today and she can go there. But a child whose answer is
*ao colo da minha mãe* must not be left thinking she answered the wrong question.

**The separation between places and moments existed only in the words.** Every
figure is a place and a moment at once, and dividing in the question what the
image does not divide would have been an arrangement rather than a distinction.

**What actually separates the two positive families is the body**, not the type of
question: activated in happy, deactivated in calm. Both ask where, with whom, and
what the body does.

### D-278 `[IMPLEMENTATION]` The calm schema is the map of the system
`scripts/figure-calm-store.py`. **The only figure in the material that is not
about one family.**

The other five explain a mechanism. Calm has none — nothing to bring down,
nothing maintaining it, nothing to correct. What it has is the thing no other
family has: **it points outwards.** The store fills here and is spent elsewhere.

So the figure is the store at the centre with arrows leaving it: to **assustado**,
which needs the calm body in order to stay; to **zangado**, which needs it to come
down after the peak; to **triste**, which needs to know where her place is.

**It is the only place in the whole material where the seven families are visibly
one system** rather than seven separate things.

A body map was considered for this figure and rejected for the reason in D-276.
The two versions are further apart than in any other family: a map is abstract,
and the child's carries fewer words and no explanation.

### D-279 `[IMPLEMENTATION]` The calm workbook's prose — thirteen pages
Section 9 is a stub. It opens with an instruction that no other workbook has:
**this is the one applied first.** Applied last, it arrives too late.

Decisions inside it:

- **No breathing in this family**, and the workbook says why: breathing already
  lives in angry and scared, where it exists to bring an activation down, and here
  there is nothing to bring down. It would turn this into a relaxation manual and
  lose what distinguishes it.
- **Section 3 is the shortest in the material**, because there are no strategies
  and no per-option evidence to grade. What it carries instead is what to notice —
  including that **a child who can name no calm place may not have one**, which is
  the most important thing this activity can hear.
- ***Seguro* is named as the heaviest of the three fine words**, and the one that
  can leave the workbook: it is the exact opposite of scared, and *onde é que não
  te sentes segura* belongs to this family as much as to that one.
- ***Tranquilo* is carried as an unresolved problem** rather than quietly used
  (D-161): it is the family again under another name. The workbook says so, gives
  the practical distinction that saves it for now — calm **after** something — and
  records *satisfeito* as the proposed replacement.
- **The missing word is the most curious of the seven families:** all three fine
  words presuppose a *before*. **There is no child's word for calm that came after
  nothing** — the baseline state, where a child spends most of her good days, and
  which for having no name goes unnoticed. **It is the linguistic version of *a
  calma não faz barulho*.**

**Section 10 says the family treats nothing**, and that a child who cannot name a
single calm place may simply not have one — which is not solved with worksheets.
And **nothing here measures**: a store that is measured stops being a store and
becomes a target.

### D-280 `[IMPLEMENTATION]` The calm family's sheets, and the one that carries the store out
`docs/materials/calmo-fichas.html`. Nine for the child, one for whoever applies
it, one for the family. Twelve pages in the child's book.

Three rules govern this file and none of them governs any other:

- **The first sheet is about now, not about remembering.** *O meu corpo agora*
  asks what her body is doing at that moment, in the room, and ends by saying
  **não há resposta certa, e não é preciso que o teu corpo esteja calmo agora.**
  Only after it does *Onde e quando* make sense, because only then does she know
  what she is looking for.
- **No breathing and no exercise of any kind.** This family gathers; it does not
  produce the state.
- **Tone words, never zones.** The word list on sheet 2 is *mole · duro · quieto
  · a mexer · devagar · depressa · pesado · leve · solto · apertado* — every one
  of them about the whole body.

***O meu depósito* is the sheet that makes this family part of the system.**
Three lines — *quando eu estiver com medo · zangada · triste, vou buscar…* — and
it closes with **guarda esta folha; não é para hoje.** It is the only sheet in
the project written to be used in a different family's session.

**Two others carry decisions:**

- ***Demorar-me*** is the savouring sheet, and it asks her to tell one small good
  thing **slowly**, with what could be seen and heard. It is the only part of
  this family with a base of its own, and it is graded reasonable.
- ***Seguro*** asks where and with whom — and **whether it is the place or the
  person**. That last question is the one that can take the session out of this
  workbook, and the guidance says so.

**The letter opens by naming what it is:** *esta é a única destas cartas que não
é sobre um problema*. It asks parents to notice rather than produce, and carries
the caution that is easiest to miss: **a room used as punishment cannot be her
calm place** — the body learns what a place means, and that meaning does not
divide in two.

**A fault caught before printing:** markdown asterisks do not render inside the
sheets file, and a `**…**` in the letter would have printed as literal asterisks
on the page a family takes home. Checked for explicitly now, alongside the age
ranges.

### D-281 `[IMPLEMENTATION]` The calm family's nine guides — and the family is closed
Twenty-five pages, thirty-six dynamics, each guide whole on its own page.

Cautions in these guides that are rules rather than advice:

- **Sheet 2:** it is not necessary for her to be calm, and the sheet says so.
  **Asking her to become calm turns this into an exercise**, which is exactly
  what this family is not.
- **Sheet 3:** a child who can name no calm place **may not have one**. It is not
  a vocabulary failure and it is not solved by pressing.
- **Sheet 4:** do not praise the story. **Praise turns savouring into
  performance**, and she starts telling it to please.
- **Sheet 5 and 6:** if she cannot tell *tranquilo* from *calmo*, accept it and
  move on. **The problem is the word's and not hers** — do not build a
  distinction the language does not support.
- **Sheet 7:** do not link rest to merit. *Descansaste porque trabalhaste* is an
  adult's sentence and installs a condition where none is needed.
- **Sheet 8:** it is the one that can take the session out of this workbook.

**Sheet 9 carries the only caution in the project about what happens after the
session ends:** *guardar a folha e voltar a ela nas outras famílias.* **A
depósito sheet that stays in the file and is never reopened has done nothing** —
it is the only sheet in the material whose value depends entirely on being
reopened, and the family dynamic exists to make that agreed rather than hoped
for.

Two dynamics ask the child for what the language cannot give: **what word she
would use for calm that came after nothing**, and **what word she uses at home**,
which is often none of the three.

**Six families are closed: angry, sad, scared, ashamed, bored, calm.** One
remains — feliz — and it is the other half of D-274: activated where calm is
deactivated, memories and people where calm has places and body tone. **If it
comes out reading like a rewrite of this one, D-274 was wrong.**

---

# Increment 39 — The happy family (2026-08-17)

### D-282 `[DEFINED]` The happy family: *a alegria acontece — e o que fizeres com ela é que fica*
**Happiness is the one family of the seven that a child already recognises.**
Calm makes no noise and slips past; happiness makes noise — the body laughs,
moves, wants to tell. Nobody needs teaching to notice it.

**So what this family works is not noticing but keeping.** That is why savouring,
which was one of three layers in calm, is nearly the whole of this one.

**Four candidates, and the recommended one was wrong.** It read *a alegria passa
depressa — mas o que fizeres com ela fica*, and Ricardina asked why it passes
quickly. **There is no basis for saying it does.** Sadness can last weeks, anger
minutes, and happiness varies like the others; the claim was smuggled in as
atmosphere.

**What was actually meant was a different claim** — that a bad moment repeats
itself unbidden and a good one has to be held or it leaves nothing behind. **The
asymmetry between what the bad and the good leave behind is on much firmer
ground.** But said to a child, *a alegria não deixa rasto* is a sad sentence: it
tells her the good is fragile, and no family opens by telling a child that what
she feels is slight.

**Adopted, with no claim about duration at all:**

> **A alegria acontece — e o que fizeres com ela é que fica.**

**The child's version:** *a alegria vai e vem — o que ficar guardado, ficaste tu
que guardaste.*

**And it separates happy from calm exactly where D-274 required.** **Calm gathers
what was already there and unseen; happy keeps what was in plain sight and was
going to go.** One is noticing, the other is retaining — and the questions, the
sheets and the figure all come out different because of it.

**Recorded as a rule, because it was caught rather than avoided:** an atmospheric
claim about how a feeling behaves is still a claim. *Passa depressa* had no
evidence, no grading, and no reason to be there beyond sounding right.

### D-283 `[DEFINED]` The happy family has four layers, an adult error, and a complaint that brings people in
Ricardina's addition, and it changes the family from the thinnest of the seven
into one of the fullest. Recorded in the order it arrived, because the last piece
reframed the others.

**Four layers, and each yields sheets:**

1. **Nomear** — the degrees and kinds: contente, entusiasmado, orgulhoso,
   aliviado. The four fine words already exist.
2. **Guardar** — the five ways of keeping, with **agradecer** inside it.
3. **Reactivar** — memories, and plans. **It is the only family that looks
   forward**: making plans is anticipated joy, and it is a capacity rather than a
   pastime.
4. **Estar no momento** — the new layer, and the one that gives this family its
   clinical weight.

**The fourth layer holds two complaints that are the same mechanism in two
tenses.**

**The emptiness after the peak.** The party that ended, the holiday that ended,
Sunday evening. It was in no part of the material, and it is almost always
misread: the child is low after something good, and either she is told she has no
reason to be, or the good thing is judged to have gone wrong.

**And the joy that is never inhabited** — the commonest parental complaint of
all: *ela quer muito uma coisa, fica entusiasmada, e quando chega parece que não
a aproveita e já quer saber o que vem a seguir.* **The enthusiasm eats the joy.**
The pleasure was all in the anticipation, and the anticipation ended the moment
the thing arrived.

**They are one section, not two** — the same inability to be in the moment one is
in, in two tenses. Separating them would make the workbook repeat itself.

**This gives the family the adult error it was thought not to have: calling it
ingratitude.** *Nunca estás satisfeita* is this family's label, as *és malcriada*
is shame's, and it is corrected the same way — speak of what happened, never of
who she is. **The child is not rejecting the thing; she was never present in it.**

**And it explains the link to anxiety that Ricardina named.** Excitement and
anxiety share the activation: the body speeds up, tightens, will not sleep. Both
live in what comes next rather than in what is. **A child who anticipates a great
deal is frequently the same child who worries a great deal**, and this is the
finest connection the material will carry.

**The distinction stays as adopted** (D-282). It covers naming, keeping and
reactivating, and the fourth layer gets its own section rather than a rewritten
axis: no single sentence held both keeping and landing without losing the store,
which is what makes this a resource family at all.

### D-284 `[IMPLEMENTATION]` The happy family's schema, and its prose — thirteen pages
`scripts/figure-joy-shapes.py`, in both versions. **The only figure in the
material that draws a positive feeling**, and it exists for the two complaints in
D-283.

**Two panels.** In the first the charge is all in the *before*: a long climb, a
small bump at the thing itself, and a fall that goes **below the line it started
from**. It is what families read wrong twice — first as *não aproveitou*, then as
*afinal não gostou*.

**The second panel is not *the right way*.** No technique is promised. It is what
it looks like when the charge is spread.

**The baseline is drawn deliberately**, because the point of the *after* is that
it passes below where it began and comes back. **The dip is normal, and the
figure says so.**

**A fault fixed before it printed:** the first version masked the curves at the
moment with a hard cut and produced a vertical jump. **A discontinuity reads as a
drawing error** — the drop is meant to be steep, not instantaneous — so the two
halves are now blended.

Decisions in the prose:

- **The screen question is the only one in the product that asks the child to do
  something** rather than choose between things: *o que é que queres guardar
  disto?*
- **Only one of the five ways of keeping has a base**, and the workbook says so.
  *Contar a alguém* is reasonable and the best of the set — **and it is the only
  one whose outcome is not in her hands.** A child who tells a good thing and is
  met with indifference is left worse than if she had said nothing, so the
  guidance says to choose the person before telling her to tell.
- ***Agradecer* goes inside *contar a alguém*** rather than becoming a sixth
  option. Said to the person it is sharing; written in a diary it is a record.
  **As good manners it is nothing** — and this material does not teach courtesy.
- **The body map is used properly here**, unlike in calm: happiness has a
  location, and **the child who cannot locate it is the exception rather than the
  rule** — the exact inverse of D-276.
- **The missing word is the one that costs this family most:** there is no child's
  word in European Portuguese for **shared joy** — the kind that exists only
  because somebody else is feeling it at the same time. **What goes unnamed is
  exactly what the best-supported way of keeping exists to produce.**

**Section 10 carries the limit this family most needed:** that *contar a alguém*
depends on who receives it, which is outside the child's reach and outside this
material's — **it is not a technique she can apply alone with any guarantee.**

### D-285 `[IMPLEMENTATION]` The happy family's sheets — eleven, the largest set of the seven
`docs/materials/feliz-fichas.html`. Eleven for the child, one for whoever applies
it, one for the family. Fourteen pages in the child's book — the biggest, because
this family has four layers.

**There is no externalising sheet.** Turning joy into a visiting character would
put it outside her, and this family exists to keep it inside.

Sheets that do work no other family's does:

- ***Onde é que eu sinto*** uses the body map properly, and asks whether
  *contente* and *entusiasmado* are felt in the same place. **It is the exact
  inverse of the calm family**, where locating anything is the exception.
- ***Contar a alguém* chooses the person before it tells her to tell.** The first
  question is *quem é que fica mesmo contente quando te corre bem?*, and the
  second asks how she knows — because this is the only way of keeping whose
  outcome is not in her hands.
- ***A espera e a coisa*** is the fourth layer as two squares: how the waiting
  was, how the thing was, and **which square came out fuller**. It turns the
  commonest parental complaint into something a child can answer about herself.
- ***Quando acaba*** names the hole and closes with the sentence the whole family
  was built around: **o buraco a seguir não quer dizer que a coisa boa correu mal
  — quer dizer só que era boa.**
- ***Contente* asks for three small things**, and closes with *não é preciso ser
  grande para contar*. A child who has words only for the extremes ends up
  believing ordinary days do not count.

**The letter is the longest of the seven**, and it is the only one that quotes the
parents back to themselves — *parece que nunca está satisfeita com nada* — before
offering the reading that dissolves it. It ends on the smallest instruction in
the whole material and possibly the most useful: **when she tells you something
good, stop, look, and ask one more question. Three seconds.**

**A check added to the pre-flight, and it now runs over all seven families:**
markdown asterisks that survive the sheets HTML and reach the printed page. Two
were caught in this family and one in calm before printing; all twenty-one built
PDFs are now clean.

### D-286 `[IMPLEMENTATION]` The happy family's eleven guides — and the seven are closed
Twenty-eight pages, forty-four dynamics, each guide whole on its own page.

Cautions in these guides that are rules rather than advice:

- **Sheet 3:** none is better than another **on her sheet**, even though one has
  a better base. **The hierarchy is the workbook's, not the child's.**
- **Sheet 4:** do not tell her to tell before the person is chosen.
- **Sheet 7:** do not suggest she be less excited. **The excitement is not the
  problem** — the problem is that nothing is left for the moment.
- **Sheet 10:** **never say she should have made more of it.** It is the
  consulting-room version of this family's label, and a child hears it at once.

The most useful dynamic of the set is on sheet 4, with the family: **parar,
olhar, e fazer uma pergunta a mais.** Three seconds.

**All seven families are closed.** Twenty-one PDFs: seven workbooks, seven child
books, seven letters.

### D-287 `[DEFINED]` The child's materials carry no gender, and this was a fault in all seven
Ricardina's requirement: the child's books must be usable with a boy or a girl.
**They were not.** Portuguese forces agreement, and the sheets had been written
throughout in the feminine.

**Two strategies, chosen case by case:**

- **The double form where the word *is* the feeling** — *nervoso ou nervosa*,
  *tímido ou tímida*, *orgulhoso ou orgulhosa*. The word is the point of the
  sheet, and the child has to see herself or himself in it.
- **Rewriting where the agreement was incidental** — *sentir culpa* for
  *sentir-se culpada*, *com muito entusiasmo* for *muito entusiasmada*, *sem
  ninguém a ajudar* for *sozinha*, *com zanga* for *zangada*.

**And the citation form, in the masculine, where the sentence defines the word
rather than describing the child:** *Arrependido é quando…*, *Orgulhoso é
quando…*, *Aliviado é a alegria de…* — matching the card, which already carries
the masculine as the name of the word.

**Three faults on screen, and the third was the least obvious:**

- **The bored button said *Ainda estou aborrecida*** → **Ainda estou assim**,
  which is shorter, keeps the descriptive framing, and carries no agreement.
- **The scared literacy line said *ficar parada*** → *ficar sem te mexer*.
- **The closing line said *Obrigada por me contares*.** That is the product
  speaking about itself in the feminine — and *Obrigado* would only move the
  problem. **A child reading it can take it as being about her.** Replaced with
  **Ainda bem que me contaste**, which has no agreement at all.

**Verified by search across the built PDFs**: the fourteen sheets a child or a
family takes home carry no loose feminine agreement, no age ranges, and no
markdown asterisks. The workbooks keep the feminine where it belongs — they speak
of *a criança*, which is a feminine noun in Portuguese and says nothing about the
child in the room.

---

# Increment 40 — Three commercial lines (2026-08-17)

### D-288 `[DEFINED]` Three audiences, and teachers are not a third version of the same thing
The material to be sold divides by **audience**, and the division is not cosmetic.

**Parents and clinicians share the child.** They speak about her, they know who
she is, and what is said is about her.

**A teacher has thirty.** No individual sheets, no session, no framing to receive
what a sheet opens. **And a limit not yet written anywhere: the teacher must not
receive what the child discloses in session.**

That makes the teacher line the hardest of the three and **the only one that
needs genuinely new material** — the other two are largely assembly of what
exists.

| | O que leva |
| --- | --- |
| **Pais** | as sete cartas, um guia curto por família, páginas para colorir por temas, o baralho. **Nada que peça observação estruturada e nada que meça.** |
| **Professores** | poster, guia de vocabulário para a sala, cartões dos esquemas, e o que fazer e não fazer na aula |
| **Psicólogos** | os sete cadernos, mais o mapa corporal em papel, bloco de registo, grelha de acomodação, registo dos degraus, plano de oito sessões, ficha de devolução à escola, enquadramento e consentimento, mapa A3 do depósito |

**One piece crosses two lines:** the *ficha de devolução à escola* — written by
the psychologist, read by the teacher. It is where the limit on what is not
transmitted has to be written.

### D-289 `[DEFINED]` The teacher line: *o professor não trata; nomeia*
It is this line's governing distinction, and it does the same work a family
distinction does: it limits and it gives something real to do.

**A teacher cannot do what this material does.** The sheets open, and he has
thirty children, forty-five minutes, and no framing to receive what opens. **Given
simplified sheets he will apply them in good faith and open things in the
classroom he has no way of closing.**

**Naming is what he can do well and what nobody does:** give the children the
words, use them aloud, and recognise what is happening without touching anyone's
story. **It is half the value of this project and it is the half that fits in a
classroom.**

**It splits the material into two groups that do not mix:**

- **For the whole class** — vocabulary, poster, language activities. **It is not
  psychology, it is emotional literacy**, and it enters the curriculum through
  that door.
- **For one child in particular** — **no sheets.** Only what to do and what not
  to do in the moment, and when to refer. One page per family, four or five lines
  each.

**And a third thing, the most delicate:** what to do when a child tells him
something. It is not rare, and **the teacher is frequently the first person told**.
It needs writing, with the limit explicit: receive, do not investigate, and to
whom it goes.

### D-290 `[IMPLEMENTATION]` The teachers' classroom pages — nine pages, and no worksheet in any of them
`docs/materials/professores-sala.html`, built by `scripts/build-teacher-pages.py`
into `professores-sala.pdf`. **A separate builder**: the workbook one knows about
families, evidence gradings, session records and child sheets, and none of that
exists here.

**The same five headings on every page, in the same order**, because a teacher
with thirty children does not read seven different structures: *o que se vê na
sala · o que ajuda · o que não ajuda · a frase que serve · quando falar com
alguém.*

***A frase que serve* is the centre of each page.** A teacher does not need the
arousal curve — **he needs to know what to say in the five seconds while it is
happening**, and that is the line that gets stuck inside a planner.

Things in these pages that are decisions:

- ***Assustado* is described by what is not seen.** In a classroom fear usually
  shows as **a child who does not do things** — not going to the board, being ill
  on Tuesdays, forgetting the material for one subject. And **dispensar** is
  named as the error: it solves the lesson and worsens the month.
- ***Envergonhado* includes the opposite presentation**: laughing and playing the
  fool, which is the fastest way to choose the reason one is being looked at.
- ***Aborrecido* carries the family's correction into the room where it matters
  most**: the child who cannot start looks exactly like the child who finished
  early, and they need opposite things. Its line is the whole page — *não há nada
  para fazer, ou não estás a conseguir começar?*
- ***Calmo* names the trap a classroom makes:* **uma sala silenciosa por medo não
  é uma sala calma**, and the child knows the difference.
- ***Feliz* reframes two things teachers read as indiscipline** and are not: the
  agitation before a good thing, and the fall the day after.

**The ninth page is the one that matters most: *Quando uma criança conta alguma
coisa*.** Receive, do not investigate, **do not promise secrecy** — with the
sentence that replaces the promise — record in her words, and pass it on. It
closes by saying that if there is suspicion of danger this stops being
pedagogical material, and that **knowing whom one tells, before needing to, is
the only part of it that can be prepared in advance.**

**Two layout faults fixed on the printed page**: the escalation callout was
splitting across a break — an escalation instruction cut in half is the one place
that cannot happen — and the disclosure page overflowed onto a tenth page holding
only that callout. Spacing was tightened rather than content cut.

### D-291 `[IMPLEMENTATION]` The classroom vocabulary guide — eleven pages
`docs/materials/professores-vocabulario.html`. **The big piece of the teacher
line, and the only one that justifies the purchase on its own**: a teacher using
it is giving a language lesson, not doing therapy.

**One builder, two documents.** `build-teacher-pages.py` now takes a name. The
second was going to be a copy of the first with a different cover, and a copy is
two files that drift apart the first time a margin changes.

**The intellectual core is the third page**, and it is what no other emotional
literacy material has: **each family's words separate along a different axis.**
Anger by intensity, sadness by cause and target, fear by time, shame by reach,
boredom by what is missing, calm by what came before, happiness by where they
point.

**Only one of the seven sorts by intensity** — and it is the one everybody uses
as the model for the other six, which is where phrases like *estou um bocadinho
traumatizado* come from. **It is a linguistic observation and not a psychological
one**, which is exactly why it belongs in a language class.

Two pages built from findings that were by-products of the workbooks:

- ***As palavras que a língua colou*** — chateado, sozinho, embaraçado,
  aborrecido. **Each is a whole lesson**, and the activity is the same for all
  four: three situations that would all be described with the same word, and a
  better word for each.
- ***As palavras que faltam*** — the seven gaps, one per family. **The activity
  is to invent the missing word**, and it works because it is true: the word does
  not exist, and children tell the difference between inventing for fun and
  inventing because something is missing. It is also the best door in this guide
  to other languages, in a class with children from several.

***A palavra da semana* is the page to keep if only one survives**, with an order
that is a decision: **start with the easy and good ones** — contente, descansado,
aliviado — because a class that learns to name what is good first reaches the
others with less resistance, and the reverse is not true. **Leave *culpado*,
*magoado* and *sozinho* for late in the year.**

**And the guide never asks a child about herself.** Checked by search: the only
second person addressed to a child in the whole document is the one inside the
rule forbidding it — *a pergunta é sempre quando é que alguém fica assim, e nunca
quando é que tu ficas assim.*

### D-292 `[IMPLEMENTATION]` The poster and the schema cards — assembly, no new content
`scripts/build-teacher-extras.py`, two pieces built from what already existed.

**The poster is A3 and carries the seven families with their fine words**, in the
same seven accents used everywhere else so a wall and a table read as one object.
The seventh sits centred across both columns, because a lone card hugging the
left margin reads as a mistake.

**A fault worth recording because it is the kind that is invisible in a PDF
viewer:** the first version set A3 in the page rule and then sized everything for
a page. Everything was correct and **nothing was readable across a classroom** —
a poster is read from four metres. Body type went from 12.5pt to 17pt, names from
21pt to 30pt, and the grid now stretches to fill the sheet.

**The cards are the six schema figures, A5, two to an A4 sheet** with a cut line
between. They existed and were trapped inside a workbook page: **somebody
explaining the avoidance cycle to a parent wants it on the table, not on page
seven.**

**They use the child's version of each figure** (D-189). A table card is looked at
*with* somebody, and the sentence written to the clinician does not belong on a
surface a child can see. Each carries one line saying what the picture shows, and
nothing else.

**The teacher line is complete**: seven classroom pages plus the disclosure page,
the eleven-page vocabulary guide, the poster, and the six cards.

---

# Increment 41 — Register and technical precision (2026-08-17)

### D-293 `[DEFINED]` Register, for everything written in this project
**Technically careful and professionally serious.** No colloquial or
over-familiar phrasing, no chatty asides, no jokey tone. Clinical and educational
content is written with precision: named constructs, stated evidence level,
explicit limits.

**Warmth stays where it belongs** — the parents' letters and the child's sheets —
**but never at the cost of technical accuracy**, and even there the writing is
sober rather than cute. Those two are a deliberate exception, not an oversight.

### D-294 `[IMPLEMENTATION]` The three evidence levels are now defined, in all seven workbooks
**The material graded evidence in three levels and never said what they mean.** A
colleague reading *razoável* had no way of knowing whether it meant *there are
studies and they are weak* or *there are no studies and the inference is sound* —
which are different things with different consequences for what she may say to a
parent.

A table now opens section 3 in every workbook:

| | O que significa |
| --- | --- |
| **Estabelecido** | Mecanismo descrito por investigação replicada, com consenso sobre a direcção. Pode ser afirmado como facto. |
| **Razoável** | O mecanismo geral tem sustentação; **a aplicação concreta não foi testada.** Fundamentado, nunca demonstrado. |
| **Prática** | Sem investigação directa. Está no material por experiência clínica e coerência. **Não se afirma eficácia.** |

And a sentence that prevents the commonest misreading: **um nível diz respeito à
afirmação, e não à utilidade.** An option graded *prática* may be the most useful
in a given session; what the grading limits is what is said about it.

### D-295 `[IMPLEMENTATION]` Evidence is no longer described by metaphor
**This was the most serious technical fault in the material.** A workbook that
grades evidence in three levels cannot then discuss evidence in figures of
speech, and it did so nineteen times: *terreno mais firme*, *a literatura é
fina*, *melhor apoio*, *o achado mais sólido*, *apoio indirecto* — the last
without ever saying indirect to what.

**It is what a colleague would notice first**, because it is the difference
between a graded claim and an impression.

Each was replaced with something checkable. Examples:

- *o achado mais sólido de todo este projecto* → **a única afirmação central
  deste projecto graduada como estabelecida**, followed by what is replicated and
  in which literature.
- *a literatura sobre companhia animal é fina* → **a investigação é escassa, com
  amostras pequenas e desenhos sem grupo de comparação.**
- *Prática, com apoio indirecto* → **Prática: sem investigação nesta aplicação; a
  fundamentação decorre de X**, naming X.
- *a evidência é mais fina do que a popularidade sugere* → **é a estratégia com
  menos investigação nesta idade**, with the physiological basis and the adult
  studies stated separately.

**Fixed at the source in both places:** the seven markdown files and
`build-sheet-guides.py`, so the generated section 9 does not reintroduce them.
All seven rebuilt and verified: every guide still whole on its own page, session
record included.

### D-296 `[IMPLEMENTATION]` Register raised in the teacher documents
The teacher line had the worst of it, and in three distinguishable kinds.

**Jokes.** *Adoece às terças-feiras* as an example of school avoidance is a joke
at a child's expense in a document a teacher reads about a child in his class.
Replaced with *falta em dias específicos*.

**Conversational shorthand.** *A cara na terceira fila*, *a parte boa*, *resolve
a aula e agrava o mês*, *a maneira mais rápida de*. Each replaced with what it
was standing in for — *apresentam-se de forma indistinguível*, *as mais
produtivas para discussão*, *resolve a situação imediata e reforça a evitação*.

**Opinion presented as content.** *É a parte mais interessante do conjunto*, *é a
melhor actividade deste guia*, *é a página a guardar*. A guide that tells a
teacher which of its own pages is best is advertising itself. The claims were
replaced by the reason underneath them, which was the useful part all along:
**reconhecer o eixo de cada família é o que distingue ensinar um campo lexical de
fazer decorar uma lista.**

**And one that mattered more than the others: *três segundos*.** It had become a
slogan — a section heading in one document and a bolded phrase in another. It
now reads *é uma intervenção de segundos e tem efeito sobre a probabilidade de
ela voltar a contar*, which says the same thing and states the mechanism.

**What was kept: the concision.** The objective was not to make the prose heavy —
it was to remove what was conversation and leave what was information. Both
documents rebuilt at the same length, nine and eleven pages.

### D-297 `[IMPLEMENTATION]` The rhetorical fragments — fewer than expected, and worth naming
The third pass looked for short emphatic closers. **A keyword search returned
twenty-eight hits and most were noise**: *e é a única que…* carries information,
and so does *e mais nada* where it limits a promise. Searching for the phrasing
found the wrong thing.

**Searching for the shape found it.** Sentences of one to five words closing a
paragraph, across the workbooks and the teacher documents: twenty-two, of which
**seven were genuine** — a verbless fragment adding emphasis where the argument
was already made.

- ***Aqui há.*** — three files, closing the paragraph on why the workbook may ask
  what the app may not. Replaced with **na sessão, essa condição está
  satisfeita.**
- ***E a clínica, no resto.*** — two files, in *onde isto assenta*. Replaced with
  **nos restantes pontos, a fundamentação é de prática clínica**, which is what
  it meant.
- ***Uma chegada, um fim.*** — obscure as well as fragmentary. Replaced with **com
  o mesmo início e o mesmo fim.**
- ***E chega.*** and ***e é esse o ponto.*** — replaced with the statement each
  was gesturing at.

**The rest were kept, and the distinction is worth recording**: *Por código, nunca
por nome*, *A última não espera*, *Sem obrigação e sem ronda* are short because
they are instructions, and an instruction is clearer short. **The tic is a
fragment that replaces an argument; a short imperative is not the same thing.**

Everything rebuilt: seven workbooks and two teacher documents, all at the same
page counts, every guide still whole on its page.

---

# Increment 42 — The parents' line (2026-08-17)

### D-298 `[DEFINED]` The parents' line: *os pais não aplicam; acompanham*
**Parents who buy this without a clinician are not the parents who receive the
letter in session.** The letter is written for somebody who has been in a room
with a professional, and it says *combinámos experimentar isto esta semana*. Sold
on its own that sentence has no referent: there was no *combinámos*, and there is
nobody to tell *na próxima vez*.

**So this line is not the clinical material with fewer parts. It is material that
has to close on itself** — no session, no return visit, and nobody to receive
what a sheet would open.

The parallel with the teacher line is exact. **The teacher names; the parent
accompanies** — recognising what is happening, responding better in the moment,
and knowing when it stops being his to handle. **Applying worksheets to his own
child is not his to do**, and it is the first thing he will do if given
worksheets.

**Two consequences, fixed now:**

- **No worksheets in this line.** A child filling in *Magoado* with her mother
  may name her mother, and there is nobody present to receive that. It is the
  same reasoning that kept the sheets off the screen (D-095).
- **The seven letters cannot be sold as they stand.** Either they are rewritten
  without the session sentences, or they leave the line. **Rewritten**: they are
  the best-written text in the project and the thing parents most want to read.

**What the line carries:** the seven letters rewritten, a short guide of *o que
fazer quando ele está assim*, the deck, and the colouring pages. Nothing that
asks for structured observation and nothing that measures (D-288).

### D-299 `[DEFINED]` Two books for parents, and they do not explain each other
Both were adopted: **a narrative book for the parent** and **an illustrated story
to read with the child.** They are separate products for separate readers.

**The parents' book is read alone by the adult** — the seven families as a path
rather than seven loose chapters, beginning with calm and happy because that is
where the store is built (D-273), and the difficult ones in order.

**The story is read *with* the child, and must work whole for somebody who has
never read the other.** If it needs a footnote it is not a story, it is teaching
material in disguise.

**The risk named now, because it is what spoils almost every children's book
about feelings: the character who learns a lesson and says it out loud at the
end.** It is the narrative equivalent of the thermometer — it turns a story into
a worksheet with pictures, and children notice by the second page.

**The rule: the seven feelings happen, and nobody explains them.** The Sad one
does not say *aprendi que a tristeza se acompanha*; the Sad one is accompanied,
and the child sees it. **The story shows; the workbook explains.** A story that
explains has no reason to exist beside the other.

**And the seven cannot be seven chapters**, or it becomes a catalogue. Something
has to happen that runs through them.

### D-300 `[DEFINED]` The story has no child in it — the seven are the cast
Three protagonists were considered: a child with the seven as what happens
inside her; one of the seven with the other six appearing to it; or **the seven
alone, in a world that is only theirs.**

**The third, and the reason comes from the material itself: the seven cards have
never represented children.** They represent feelings, and they have never had
gender, age or an owner. **Putting a child in the story forces a choice between
a boy and a girl** — and the decision immediately before this one was to remove
exactly that from everything (D-287).

It also protects the story from the commonest failure of the genre: a child
protagonist invites the reader to identify and then to be taught. **Seven
feelings living together invite the reader to watch.**

### D-301 `[DEFINED]` The story: the Bored one arrives, and the other six are already there
Two shapes were considered — a single day in a house shared by all seven, and an
arrival. **The arrival.**

**Six live together and a seventh turns up: the Bored one**, who does not
understand what the others are for and asks. **The answers are not explanations:
they are things she sees happen.**

**Boredom is the right character for the part**, and the reason comes from its
own workbook: it is **the only one of the seven that is not a problem** and that
nobody is treating (D-260). That leaves it free to watch. The other six are all
busy being something.

Three things this shape solves:

- **Movement without inventing a journey.** The story advances because somebody
  new is there, not because anyone travels.
- **A companion for the reader** — somebody who also does not know.
- **Order.** The seven appear when the story needs them, not as a list. **Seven
  characters with nothing happening is a catalogue**, which is what the other
  shape risked.

**And an ending that is not a lesson: the Bored one realises she is one of
them.** Nothing is said aloud; something is understood. It satisfies D-299
without a moral.

**Cost, recorded so it is not a surprise:** twelve to sixteen illustrated scenes
with seven characters that must stay identical from page to page. **It is the
most expensive thing this project has attempted**, and the first that needs
character consistency across images rather than isolated figures.

### D-302 `[IMPLEMENTATION]` The story text — sixteen scenes, five hundred words
`docs/materials/livro-historia.md`. Scene descriptions for the illustrator and
the text for each page, written before any image because **a badly decided scene
costs a discarded illustration.**

**The names are the card names** — Zangado, Triste, Assustado, Envergonhado,
Calmo, Feliz, Aborrecido — and not the externalised forms the sheets use (*a
Zanga*, *o Medo*). A child holding the deck and the book should find the same
name in both. All are grammatically masculine, which settles the gender question
by itself: **they are not people, they are feelings, and none of them is a boy or
a girl.**

**Size is the language of the book.** The angry one becomes enormous and returns
to his size; the ashamed one shrinks and comes back; the happy one grows each
time he tells and returns to normal when it ends. **None of these changes is
stated in the text** — they are only seen. It is the main narrative vehicle and
it is what replaces explanation.

**The Bored one never changes size**, because he is the observer and his
constancy is what makes the others readable.

Three things the text does that are the point of it:

- **The Bored one is never corrected.** He pulls funny faces at somebody sad and
  says *é só uma porta* to somebody frightened — the two things the whole project
  tells adults not to do. **Nobody reprimands him**; it simply does not work, and
  he sees what does.
- **The answers he gets are short and mechanical, never moral.** *Porque antes
  ele não ouvia* is the longest explanation in the book.
- **The last scene repeats the first**, same framing, one more character inside.
  **The repetition is the ending**, and it is not said aloud.

Checked against its own rules: no child in the cast, no sentence of the *aprendi
que* kind, no line over twenty-eight words, and **the word *emoção* does not
appear once.**

### D-303 `[DEFINED]` The face never changes — which is what makes the book possible
Character consistency across sixteen scenes was recorded as the project's largest
technical risk (D-301). **It is resolved by a decision rather than by technique.**

**Each character's face is fixed and never changes.** It is not a limitation: it
is what these characters are. **They are not people who have moods — they are the
feelings themselves.** The Sad one always has the tear, because take the tear away
and it is no longer him.

> **A cara é fixa. O tamanho e a postura carregam a história.**

The angry one becomes enormous with the same face. The ashamed one shrinks with
the same face. **And in scene 13, after the good thing has ended, the happy one
keeps his face and sits small and slumped in a corner** — the feeling has not
changed, the thing has ended. That is precisely what the scene has to say, and
the smiling face on a slumped body says it better than a new expression would.

**Only the arms may move**, and only where the scene requires it. Colour, body
shape and face do not change.

### D-304 `[IMPLEMENTATION]` The character sheet and the two test scenes
`docs/materials/livro-personagens.md`. **It is not for generating the book — it
is for finding out whether the book is possible.**

**A cast block to paste into every prompt**, describing the seven exactly as the
deck draws them, with the three details a generator most easily drops named
explicitly: **the blue one's teardrop, the pink one's hand over the face, the
olive one's hand against the cheek.**

**And a new style block**, because this is the first thing in the project that is
not black line on white: flat colour, no gradients, no highlights, no shadows,
simple uncrowded backgrounds.

**Two test scenes, chosen as the hardest in the book:**

- **Scene 4** — the angry one three times the height of the others, four
  characters present, an event on the floor. It tests **size as language**.
- **Scene 15** — all seven at once, around an object that must not be
  recognisable. It tests everything.

**Five countable checks** rather than an impression, and one question that
decides: **put scene 4 beside scene 15 — are they recognisably the same
characters?** If not, **the answer is not to push the prompt but to find another
way of producing the images.**

### D-305 `[IMPLEMENTATION]` The consistency test passed — and found three faults
The two hardest scenes were generated and measured against the five countable
checks.

**The question that decides was answered yes.** Put side by side, the characters
are recognisably the same in both images: the same bodies, the same colours, and
all seven faces correct, including the three a generator most easily drops — the
blue one's teardrop, the pink one's hand over the face, the olive one's hand
against the cheek. **The book is possible**, and D-303's decision to fix the faces
is what made it so.

Seven characters detected in scene 15, five in scene 4, all correct.

**Three faults, all fixable, and one of them mine.**

**The white sticker rim.** It was in the cast block because it is in the deck —
and in the deck it is right, because a card sits alone on white. **In a scene it
turns the characters into cardboard cut-outs pasted onto a photograph**, which is
exactly how both test images read. Removed from the cast block, together with the
drop shadows and the paper texture the generator added to the wall.

**The size was 1.83×, not 3×.** Measured on the pixels rather than judged: the
red one's height against the mean of the others. **If size is the language of the
book, an ambiguous size is an unreadable sentence.** The prompt now gives a
concrete test — *if the mint green one reaches only up to his knee, the size is
right* — and names the failure: *a red one twice their height is WRONG.*

**The object in scene 15 came out as a small house** made of sticks and cloth,
which the prompt had forbidden by listing what it must not be. **Listing
exclusions was not enough**; the prompt now describes what it must be instead — a
lopsided pile balanced by somebody who did not know where it was going, with no
roof, no walls, no opening and no symmetry — and names the failed attempt.

**It is the same lesson as the ground line and the thumb**: naming the failure
concretely works where listing the requirement does not.

### D-306 `[IMPLEMENTATION]` Second attempt: two of three fixed, and the size resists
Measured again, not judged.

| | Antes | Agora | Pedido |
| --- | ---: | ---: | ---: |
| Rebordo branco, cena 4 | 59.3% | **8.2%** | 0 |
| Rebordo branco, cena 15 | 66.6% | **0.0%** | 0 |
| Vermelho / média dos outros | 1.83× | **2.16×** | 3× |

**The white rim is gone**, measured as the proportion of near-white pixels in a
band around each figure. The characters now stand in the room instead of being
pasted onto it, and it is the single biggest improvement between the two
attempts.

**The object in scene 15 is no longer a house.** It is a lopsided pile of blocks,
a stick and a piece of cloth, with no roof and nothing that could be entered —
which is what the scene needs.

**The size did not take**, and it is the one thing that matters most. From 1.83×
to 2.16× after being told three times, given a concrete test and shown the
failure. **The instruction is not the problem; the framing is** — a figure three
times the height of the others does not fit a picture composed around a group.

So the rule changed from a proportion to a composition: **compose the picture
around his size, so that he does not fit comfortably in the frame** — his head
touching or cut by the top edge while the others stand well below the middle. It
is the same move that fixed the ground line: **describe the picture, not the
measurement.**

**Everything else holds.** Seven characters in scene 15, five in scene 4, all
colours correct, all seven faces correct across both images including the
teardrop, the hand over the face and the hand at the cheek. **The consistency
question stays answered: they are the same characters.**

### D-307 `[IMPLEMENTATION]` Third attempt: the size took, and the test is closed
| | 1.ª | 2.ª | 3.ª |
| --- | ---: | ---: | ---: |
| Vermelho / média dos outros | 1.83× | 2.16× | **3.82×** |
| Rebordo branco | 59% | 8% | 8% |
| A coisa parecia uma casa | sim | não | não |

**What changed between the second attempt and the third was not insistence — it
was replacing a measurement with a composition.** Asking for *three times taller*
failed twice. Describing the frame worked at once: *the top of his head touches
the top edge, every other character stands in the lower half, and if all five fit
comfortably side by side the composition is wrong.*

**The generator composes pictures; it does not measure proportions.** It is the
same lesson as the ground line, the thumb and the object — **and it is now three
for three.**

Measured on the image: the red one's head starts at 4% from the top and every
other character begins below 59%. It overshot to 3.82×, which is not a fault:
**in a scene where anger is at its peak, bigger is more readable than exact.**

**The test is closed and the book is no longer a technical risk.** Both scenes
kept as reference art in `artwork/livro/`: they are the two that every subsequent
prompt should be judged against, and the first pair a colleague or an illustrator
would be shown.

**What remains open is not consistency but volume**: fourteen more scenes at this
standard.

### D-308 `[IMPLEMENTATION]` The fourteen remaining scene prompts
`docs/materials/livro-prompts.md`. Sixteen scenes, two already generated,
fourteen written — verified against the story so that none is missing.

**Every scene carries a composition instruction rather than a measurement**,
because that is what worked three times out of three (D-307). Where size changes
— scenes 5, 10, 12, 13 — the frame is described: *he must not fit comfortably*,
*most of the picture is empty room*, *the emptiness around him is the subject*.

**Cast economy is stated as a rule:** only the characters the scene needs appear.
**A scene with seven characters is seven chances to go wrong; a scene with three
is three.** Half the book is two- or three-character scenes.

**Three scenes carry a warning against the generator's instinct:**

- **Scene 6** — the olive one pulling faces at the sad one **must not be
  smiling**. His face never changes, and a generator will want to make him
  cheerful because he is being cheerful.
- **Scene 7** — the yellow one's arms must be **down**, not raised, because he has
  sat down beside somebody.
- **Scene 13** is the most delicate in the book, and its prompt says so: **the
  happy one keeps his face entirely.** *The smiling face on a slumped, small body
  is the entire point of this picture, and changing his face would destroy it.*

**A generation order, in four batches**, and the first is not the beginning of the
book: **scenes 1 and 16 together**, because the last picture repeats the first
and the repetition is the ending. **If those two do not match, the ending does not
work**, and it is worth knowing early rather than at the sixteenth image.

The remaining batches go from easiest to hardest — two characters, then three,
then the full room — so that the cheap scenes stabilise the style before the
expensive ones.

### D-309 `[IMPLEMENTATION]` Twelve scenes generated; fourteen of sixteen in hand
Scenes 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12 and 14 generated and kept in
`artwork/livro/`. **Fourteen of the sixteen exist. Scenes 13 and 16 are
missing.**

**The consistency holds across all fourteen.** Every character is recognisably
itself in every appearance, and the three details that were flagged as fragile —
the blue one's teardrop, the pink one's hand over the face, the olive one's hand
at the cheek — are correct everywhere.

**The instructions that worked against the generator's instinct all took**, which
is the part worth recording:

- **Scene 6:** the olive one pulls faces at the sad one **without smiling**. His
  face is unchanged, which is what the story needs and what a generator resists.
- **Scene 7:** the yellow one sits with his **arms down**.
- **Scene 5:** the red one is back to normal size and small in the frame, which
  is what the scene says.
- **Scene 12:** the yellow one's raised arms are cut by the top edge, exactly as
  the composition instruction asked.
- **Scene 10:** the pink one is genuinely tiny behind the cupboard.

**Three faults, and one is a continuity error rather than a drawing error.**

**The assembled object appears in scene 11**, where it cannot exist: it is built
in scene 14 and seen in scene 15. **A picture book read by a child who turns back
a page will catch this** — and the fault came from giving the generator scenes 11
and 15 in the same batch, where it carried the object across.

**Scenes 8 and 9 have a visibly darker, browner room** than the other twelve.
Measured on the floor: 94 and 87 units from the median against 26 or less
everywhere else. **They were generated as a pair and drifted as a pair** — which
is the cost of batching, and the lesson is to include a scene from the accepted
set in every batch as an anchor.

**Scene 1 has a roof and a brown exterior** that no other scene has. It is not
wrong — the house is seen from outside — but scene 16 must match it exactly, and
that is now the harder of the two remaining pictures.

### D-310 `[DEFINED]` Emptiness needs composition; absence alone reads as unfinished
Ricardina's observation that some scenes are not visually attractive traces to my
own instruction. **Writing *o vazio é o assunto* in five scenes produced pages
that are seventy per cent bare floor** — and a literal void reads as an unfinished
page, not as solitude. A child reads the second thing.

**The correction is the same in all of them: bring the frame in and drop the
camera** to the characters' own height. The figure gets larger, the emptiness
remains, and the page stops looking abandoned.

Applied to scenes 8 and 9 in this pass. **Scenes 5, 10 and 14 have the same
fault** and are candidates for the same fix.

**And a batching rule, learned from scenes 8 and 9 drifting as a pair:** every
batch includes one already-accepted scene as an anchor. A batch generated with no
reference to what exists drifts as a whole, and the drift is invisible until the
scenes are laid side by side.

### D-311 `[IMPLEMENTATION]` Scene 16 works as the ending — fifteen of sixteen in hand
The repetition reads. Same house, same roof, same walls, same floor, same
palette, same sofa and same two tables and the same bookshelf in the same places,
**and seven characters inside instead of six, with nobody left outside.** A child
turning back to the first page finds the picture again with one more in it, which
is the whole of the ending.

**What differs, and it is a judgement rather than a fault.** The rug and the
stool are gone, and the characters are doing different things: the blue one has
the box instead of the plush rabbit, the yellow one reads on the floor instead of
drawing at the table, the mint one has taken the table. **Time has passed in the
story, so the characters having moved is right; the missing furniture is a small
loss and not worth another generation.**

**Fifteen of sixteen scenes are in hand.** Only scene 13 remains — the happy one
small and slumped with his face unchanged, which is the most delicate picture in
the book.

**Not regenerated, and still standing as recorded in D-309:** scene 11 carries an
object that does not exist yet in the story, and scenes 8 and 9 have a room
darker than every other scene. Both were prompted for and neither came back.

### D-312 `[IMPLEMENTATION]` Sixteen of sixteen — the book is illustrated
Scenes 13, 11 and 9 came back and are kept. **All sixteen scenes exist**, and the
whole book laid out as a contact sheet reads as one object with one cast.

**Scene 13 works, and it was the one that could not be salvaged if it failed.**
The happy one sits small in the corner — measured at 0.54 of the olive one's
height — with his face entirely unchanged: eyes closed in curves, wide open
smile. **The smiling face on a small slumped body is exactly the sentence the
scene had to say**, and no generator instinct overrode it.

**Scene 11 no longer contains the object.** The continuity error is gone: seven
characters, loose blocks, nothing stacked, nobody looking at the pink one.

**Scene 9 is now in the book's palette** and framed close, and it is a better
picture than the one it replaces.

**One outstanding: scene 8** was not regenerated and is still the dark brown
room. It is the only scene visibly outside the palette — measured at 99 from the
book's median, against 50 or less everywhere else.

**A palette spread worth naming before layout.** Floors range from [212 149 89]
to [247 207 154]. **No single scene is wrong, but the book drifts warmer and
lighter across batches**, and the reader turning pages will see it. It is
correctable in layout with a single colour adjustment per scene rather than by
regenerating anything — **and that is the cheaper fix**, since the drawings
themselves are right.

### D-313 `[IMPLEMENTATION]` Scene 8 redone — the book is complete
The dark room is gone. Measured on the floor: **99 units from the book's median
before, 29 after.** Five characters, all correct, and the framing is close
instead of a field of bare floor.

**All sixteen scenes exist and are kept in `artwork/livro/`.** *Quem És Tu?* is
written and illustrated.

**The palette spread stands as recorded in D-312** and is now the only visual
work left: scenes 9, 11, 12 and 14 sit 34 to 60 units from the median. **No
drawing is wrong** — it is a levelling job for layout, one colour adjustment per
image, and cheaper and safer than regenerating anything.
