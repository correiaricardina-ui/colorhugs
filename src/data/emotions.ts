/**
 * The seven emotion families.
 *
 * Order is fixed and never shuffled (D-104). A five-year-old learns where her
 * card is and goes straight to it; shuffling would take away the only
 * advantage she has, and it keeps the printed deck and the screen the same
 * object.
 *
 * Not grouped by valence. Pleasant on one side and unpleasant on the other is
 * tidy and teaches that feelings divide into good and bad — and the avatar
 * already paints identically for "furious" and for "calm" (D-067).
 *
 * Happy first because it is easiest and teaches the gesture. Calm immediately
 * after, so a child who is fine without being cheerful finds her card at once
 * instead of defaulting to happy. Sad, scared and angry in the order a small
 * child recognises them. Ashamed after angry, because it arrives later and
 * most often hides behind the one before it. Bored last, because it belongs
 * nowhere and has no neighbour to be confused with.
 *
 * No card carries text. Names come from the language file (D-081), which is
 * what lets one drawing serve every locale — and the fine words differ per
 * language rather than being translated (D-101).
 */

export interface EmotionFamily {
  /** Stable key. Also the artwork filename and the language-file key. */
  id: string;
  /** Card artwork, transparent, with the white die-cut rim kept (D-083). */
  src: string;
  /**
   * Recognition aid only — never the meaning. Every card was checked in
   * greyscale: the posture carries the feeling, so a child who cannot
   * distinguish the colours reads all seven (D-089).
   */
  tint: string;
}

export const EMOTIONS: EmotionFamily[] = [
  { id: "happy", src: "/assets/emotions/happy.webp", tint: "#F5B700" },
  { id: "calm", src: "/assets/emotions/calm.webp", tint: "#8FD9A8" },
  { id: "sad", src: "/assets/emotions/sad.webp", tint: "#6FB2E8" },
  { id: "scared", src: "/assets/emotions/scared.webp", tint: "#A98BDD" },
  { id: "angry", src: "/assets/emotions/angry.webp", tint: "#E63B33" },
  { id: "ashamed", src: "/assets/emotions/ashamed.webp", tint: "#F495B0" },
  // Muted olive-khaki, not grey-beige. The first version had 0.9% coloured
  // pixels and would have read as *disabled* beside six bright cards (D-093).
  { id: "bored", src: "/assets/emotions/bored.webp", tint: "#A89B5C" },
];

/**
 * Body map zones, in the order a child reads a body.
 *
 * The throat is deliberately absent. The lump in the throat is one of the most
 * recognisable signals, but at phone size a neck zone is too small for a
 * child's finger, and a zone that misses reads as the app not listening
 * (D-106). The neck sliver is grouped with the head so nothing stays white.
 */
export const BODY_ZONES = ["head", "chest", "stomach", "arms", "legs"] as const;

export type BodyZone = (typeof BODY_ZONES)[number];

export const BODY_OUTLINE = "/assets/body/outline.webp";

export const bodyZoneShape = (zone: BodyZone) => `/assets/body/zone-${zone}.webp`;
