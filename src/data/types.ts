/**
 * ColorHugs content model.
 *
 * Sections and activities are data, not markup. Adding an activity means
 * adding an object to `src/data/sections.ts` plus its artwork — no new
 * components, no new routes, no layout work.
 */

/**
 * Access level.
 *
 * Free and Premium are subscription levels of a family account. **Professional
 * is not a third subscription** — it is a different audience, a different
 * product and a different price (D-153). They share a badge shape because they
 * are all doors in the adult area, not because they are the same kind of thing.
 */
export type Plan = "free" | "premium" | "professional";

/**
 * How an activity is gated.
 *
 * No activity is ever locked shut. A child on Free opens everything and meets
 * the limit inside, after playing — never a closed door on the way in. See
 * decision D-037.
 *
 *  - `free`     — no limit at all.
 *  - `sample`   — opens normally; the first `freeItems` items are Free.
 *  - `premium`  — the one shape that cannot be sampled, and must say why.
 */
export type Access =
  | { kind: "free" }
  | { kind: "sample"; freeItems: number }
  | { kind: "premium"; reason: string };

/** Build status, so unfinished activities are honestly signposted. */
export type ActivityStatus = "live" | "in-progress" | "planned";

/** Which of the three approved content origins an activity belongs to. */
export type ContentOrigin =
  | "official-library" // ColorHugs-authored content
  | "imagine-and-create" // AI-assisted colouring pages (Color & Create, Premium)
  | "kids-draw-for-kids"; // genuine child-created artwork

/** Who the surface is built for. Adult areas never use the child chrome. */
export type Audience = "child" | "adult";

export interface Artwork {
  /** Path under /public. `null` means the approved artwork does not exist yet. */
  src: string | null;
  /** Descriptive alt text. Required — never decorative for a primary control. */
  alt: string;
  /** Natural aspect ratio, used to reserve layout space and avoid distortion. */
  ratio: "square" | "wide";
}

export interface Activity {
  slug: string;
  title: string;
  /** One short child-facing line. Kept minimal by design. */
  tagline: string;
  sticker: Artwork;
  access: Access;
  status: ActivityStatus;
  origin: ContentOrigin;
  /** Optional group id, used by sections that need internal structure. */
  group?: string;
}

export interface ActivityGroup {
  id: string;
  title: string;
  /** Adult-readable rationale kept in the data for maintainers. */
  description: string;
}

export interface SectionTheme {
  /** CSS class defined in globals.css that sets the --sec-* custom properties. */
  className: string;
}

export interface Section {
  slug: string;
  title: string;
  tagline: string;
  audience: Audience;
  theme: SectionTheme;
  sticker: Artwork;
  banner: Artwork;
  /** Shown on the section page under the banner. Adults read this, not children. */
  purpose: string;
  groups?: ActivityGroup[];
  activities: Activity[];
}
