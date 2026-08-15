# ColorHugs — Pre-launch QA Checklist

Run before any release. Items marked **BLOCKER** must pass; a failure stops the
release rather than being logged for later.

## Accessibility

- [ ] Every interactive element is reachable by keyboard, in a sensible order.
- [ ] The focus ring is visible on every control, against every section wash.
- [ ] "Skip to content" appears on first Tab and works.
- [ ] Every image is either given descriptive alt text or explicitly marked
      decorative. **No control relies on its picture alone.**
- [ ] No meaning is carried by colour alone (check status chips and plan badges
      in greyscale).
- [ ] Text contrast meets WCAG AA at every size, including captions on the
      cream and coloured washes.
- [ ] The page is usable at 200% browser zoom and at 320px width.
- [ ] `prefers-reduced-motion: reduce` stops all movement, including hover lift.
- [ ] Headings form a sensible outline (one `h1` per page, no skipped levels).
- [ ] Tested with a screen reader on at least one desktop and one mobile browser.

## Child UX

- [ ] Every tap target is at least 64px, with no accidental neighbours.
- [ ] From any page a child can reach the section and the homepage in one tap.
- [ ] Back always goes somewhere predictable — never browser history.
- [ ] No hidden gesture, dropdown or long-press is required anywhere.
- [ ] No screen depends on reading more than a short label to be usable.
- [ ] Nothing animates continuously while a child is trying to read or choose.
- [ ] No countdown, streak, urgency message or absence guilt anywhere.
- [ ] Premium content is honestly marked and never disguised as free.
- [ ] **BLOCKER** No advertisement resembles a ColorHugs activity or button.

## Content and safety

- [ ] **BLOCKER** No child-facing free-text input ships without input moderation.
- [ ] **BLOCKER** No generated output reaches a child before output moderation.
- [ ] **BLOCKER** No child submission is publicly visible without human review.
- [ ] **BLOCKER** No private messaging, open chat or contact exchange exists.
- [ ] Published artwork never exposes a child's name, school, location or
      contact details.
- [ ] Blocked-content messages are short, non-shaming, and do not repeat the
      prohibited content back to the child.
- [ ] Nothing in My Inner World reads as diagnosis, assessment or treatment.
- [ ] AI-generated artwork is never presented as child-created, and the three
      content origins remain visually and structurally distinct.

## Privacy and data

- [ ] **BLOCKER** No analytics, ad technology, tracker or third-party script
      loads. Verify in the network panel with a clean profile.
- [ ] **BLOCKER** No secret, key or credential exists in client code or in the
      repository history.
- [ ] Fonts, images and scripts are all first-party.
- [ ] Only data with a stated purpose is collected (data minimisation).
- [ ] Child data is not exposed by default anywhere, including in page source.
- [ ] Parental consent flow has been reviewed against each launch jurisdiction.
- [ ] Privacy policy and terms are published and accurate.
- [ ] A Content-Security-Policy is in place. *(Currently missing.)*
- [ ] **BLOCKER** No certification seal or endorsement is displayed that has
      not actually been earned, and no wording implies an assessment that did
      not happen. See `docs/CERTIFICATIONS.md`.

## Technical

- [ ] `npm run typecheck`, `npm run lint` and `npm run build` all pass clean.
- [ ] Static export builds and serves correctly at the configured base path.
- [ ] No layout shift on load; banners and stickers reserve their space.
- [ ] Verified at 390px, 820px and 1440px, and in portrait and landscape.
- [ ] Verified in Safari, Chrome and Firefox, desktop and mobile.
- [ ] All artwork keeps its aspect ratio — nothing stretched or cropped oddly.
- [ ] No `MissingArtwork` placeholder is visible in a released build.
- [ ] 404 page works and offers a way home.
