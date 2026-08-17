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
