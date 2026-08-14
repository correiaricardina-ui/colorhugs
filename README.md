# ColorHugs — Website Foundation (Phase 1)

**Create • Learn • Grow • Together**

The foundation of the ColorHugs web app: design system, navigation, homepage,
seven child sections, activity routes and the Parents & Safety entry point.
Activities themselves arrive in later phases.

## Getting started

```bash
npm install
npm run dev            # http://localhost:3000
npm run build          # server build
npm run build:export   # static export in out/ (GitHub Pages)
npm run typecheck
npm run lint
npm run assets         # regenerate /public/assets from the originals
```

## What is in here

```
public/assets/
  branding/            ColorHugs logo
  banners/             section banners + Free/Premium
  stickers/
    sections/          one sticker per section
    plans/             Free / Premium badges
    learning-hub/ brain-gym/ my-inner-world/ kids-draw/
    color-and-create/ my-colorhugs/ community/

scripts/prepare-assets.py   regenerates /public/assets from the originals

src/
  app/
    page.tsx                    homepage — the ColorHugs universe
    [section]/page.tsx          one template for every section
    [section]/[activity]/page.tsx   activity placeholder
    parents/page.tsx            adult area, its own visual language
    globals.css                 design tokens + section themes
  components/
    layout/      ChildShell, AdultShell, Footer
    navigation/  NavBar, BackButton, HomeButton
    stickers/    StickerButton, PlanBadge, MissingArtwork
    cards/       ActivityCard
    sections/    SectionBanner, SectionGrid
    ui/          ProgressIndicator, RewardBadge, StatusChip, ComingSoon
  data/          sections.ts — the single source of truth
  lib/           lookup helpers
docs/            ASSET_MAP.md, DECISION_LOG.md
```

## Adding an activity

Add an object to the section's `activities` array in `src/data/sections.ts` and
drop its sticker into `public/assets/stickers/<section>/`. The route, the card,
the grid placement, the badge and the metadata all follow automatically.

Set `access` to `{ kind: "free" }`, `{ kind: "sample", freeItems: 3 }` or, only
with a stated reason, `{ kind: "premium", reason }`. Sampled activities open
normally on Free — the limit is reached inside, after playing, never as a
locked tile.

If the artwork does not exist yet, set `sticker.src` to `null`. The interface
renders an honest "Artwork pending" tile rather than inventing a graphic.

## Design rules encoded in the code

- **Artwork is never modified in the browser.** No stretching, no filters, no
  recolouring — `object-contain` everywhere, aspect ratios declared in data.
- **Meaning never depends on the picture alone,** or on colour alone. Every
  sticker carries a text label; status carries an icon and a word.
- **Targets are at least 64px** with generous spacing.
- **Motion is feedback.** Hover lift, press, one entrance pop; nothing loops.
  `prefers-reduced-motion` switches it all off.
- **Focus is always visible,** in the active section's accent colour.
- **The adult area looks different from the child area,** deliberately.
- **No child-facing screen shows a price or a payment button.** When a free set
  runs out the child is pointed at a grown-up; buying happens in the parent
  area only.
- **No third-party requests.** No analytics, ads, trackers, external scripts or
  font CDN.

## Not built yet

Authentication, child profiles, consent, moderation, progress persistence,
internationalisation and the activities themselves. `/parents` states this
plainly rather than implying protection that does not exist.

See `docs/DECISION_LOG.md` for what was decided, what is a proposal, and the
six questions waiting on you.

## Deployment

Two modes, one codebase:

- **Server build** — `npm run build`, then `npm start`. Works on Vercel,
  Netlify or any Node host, and keeps the security headers.
- **Static export** — `npm run build:export` writes `out/`.

For a GitHub project page, set these as **repository variables** (Settings →
Secrets and variables → Actions → Variables):

| Variable | Value |
| --- | --- |
| `BASE_PATH` | `/colorhugs` |
| `SITE_URL` | `https://correiaricardina-ui.github.io/colorhugs` |

`BASE_PATH` is passed to the build twice, as `BASE_PATH` and
`NEXT_PUBLIC_BASE_PATH`: the first configures Next, the second reaches
`<Image>`, which does not inherit `basePath` when images are unoptimized. On a
custom domain, leave both variables empty.

Reproduce the Pages build locally with:

```bash
EXPORT=1 BASE_PATH=/colorhugs NEXT_PUBLIC_BASE_PATH=/colorhugs \
  NEXT_PUBLIC_SITE_URL=https://correiaricardina-ui.github.io/colorhugs \
  npm run build:export
```

`.github/workflows/ci.yml` runs typecheck, lint and build on `main`, `develop`
and every pull request. `.github/workflows/deploy-pages.yml` publishes from
`main` only, so the live site always reflects an approved state.

Never commit secrets. Safety-critical logic — AI, moderation, payments — must
run server-side only; nothing sensitive belongs in client code or in this
repository.

### Before launch

Set the repository variable `SITE_MODE` to `holding`. The domain then serves a
holding page and the real site is built under `/preview`, with crawling
disallowed and every page marked `noindex`. Clear the variable and re-run the
workflow to go live.

Nothing on GitHub Pages can be password-protected — `/preview` is unlisted, not
private, and the repository is public.

Before any release, work through `docs/QA-CHECKLIST.md`.
