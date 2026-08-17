/**
 * Where the child's avatar and her colour are kept.
 *
 * **This file is the whole of it.** Everything else asks these four functions
 * and knows nothing about where the answer comes from — so moving the state to
 * a server when the account system arrives (D-202) is one file, not surgery
 * across the product.
 *
 * Today it is the device, and D-202 said so deliberately: the commercial half
 * lives on a server, the child's half does not. It carries a real cost that the
 * short trail did not — **the avatar is the first thing in ColorHugs with
 * something to lose.** It accumulates over weeks, it is the child on the screen,
 * and clearing the browser takes it. That is the strongest argument the backend
 * will ever have, and it is written here rather than discovered later.
 *
 * **The colour belongs to the child, not to the avatar** (D-208). Changing
 * avatar carries every earned colour across. The alternative charges a child
 * for changing her mind, and nothing in ColorHugs is ever taken away (rule 38).
 */

/** The seven areas, in the manifest's own letters. One per section. */
export const AREAS = ["LH", "BG", "IW", "KD", "CC", "MC", "CM"] as const;
export type Area = (typeof AREAS)[number];

/** Which section paints which area (D-069, D-075). */
export const AREA_OF_SECTION: Record<string, Area> = {
  "learning-hub": "LH",
  "brain-gym": "BG",
  "my-inner-world": "IW",
  "kids-draw": "KD",
  "color-and-create": "CC",
  "my-colorhugs": "MC",
  community: "CM",
};

/**
 * There is deliberately no colour table here.
 *
 * Colour used to be the section's accent, the same on every character, so that
 * a patch could in principle be read back as *which section*. It made a
 * harlequin of every avatar, and the reading was theoretical — nobody decodes a
 * colour key. **Each character now carries its own palette** in
 * `src/data/avatars.json`, written by `scripts/prepare-avatars.py` (D-211).
 *
 * The mapping below is untouched: the *zones* still belong to the sections.
 * Only what fills them changed.
 */

export interface AvatarState {
  /** The chosen avatar's id, or null before she has picked one. */
  avatar: string | null;
  /** The areas that have been painted. Order is not meaningful. */
  painted: Area[];
}

export const EMPTY: AvatarState = { avatar: null, painted: [] };

const KEY = "colorhugs.avatar";

function isArea(value: unknown): value is Area {
  return typeof value === "string" && (AREAS as readonly string[]).includes(value);
}

/** Read the saved state. Never throws — storage can simply be unavailable. */
export function load(): AvatarState {
  try {
    const raw = window.localStorage.getItem(KEY);
    if (!raw) return EMPTY;
    const parsed: unknown = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object") return EMPTY;
    const { avatar, painted } = parsed as Partial<AvatarState>;
    return {
      avatar: typeof avatar === "string" ? avatar : null,
      painted: Array.isArray(painted) ? painted.filter(isArea) : [],
    };
  } catch {
    // Private mode, blocked storage, or something else's key at this name.
    // An empty state is a perfectly good answer: she picks again.
    return EMPTY;
  }
}

export function save(state: AvatarState): void {
  try {
    window.localStorage.setItem(KEY, JSON.stringify(state));
  } catch {
    // Not remembering is a loss. Failing in front of a child is worse.
  }
}

/**
 * Mark that she was in a section today.
 *
 * **For having been there, never for how much** (D-067): one activity or six
 * paints exactly the same. This function takes no count and returns no total,
 * so there is nothing for a later "nice chart" to be built out of.
 */
export function paint(state: AvatarState, area: Area): AvatarState {
  if (state.painted.includes(area)) return state;
  return { ...state, painted: [...state.painted, area] };
}
