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
  { id: "happy", src: "/assets/emotions/happy.webp", tint: "#FFCF15" },
  { id: "calm", src: "/assets/emotions/calm.webp", tint: "#A6E5C2" },
  { id: "sad", src: "/assets/emotions/sad.webp", tint: "#7DC0F5" },
  { id: "scared", src: "/assets/emotions/scared.webp", tint: "#C9ADE9" },
  { id: "angry", src: "/assets/emotions/angry.webp", tint: "#E8302C" },
  { id: "ashamed", src: "/assets/emotions/ashamed.webp", tint: "#FC89AE" },
  // Muted olive-khaki, not grey-beige. The first version had 0.9% coloured
  // pixels and would have read as *disabled* beside six bright cards (D-093).
  // Sampled from the card rather than specified, so the body map tint and the
  // card cannot drift apart.
  { id: "bored", src: "/assets/emotions/bored.webp", tint: "#B0A454" },
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

/**
 * The fine words inside each family — the premium layer (D-142).
 *
 * **The count is per language and per family, not a fixed number** (D-101):
 * angry has three in PT-PT, happy four. Forcing a symmetrical grid would mean
 * inventing words no child says.
 *
 * The activity closes before this layer (D-100), so no child meets a wall: she
 * has already named what she feels and already been met. What is sold is the
 * depth, never the essential.
 *
 * Ids are `family__word`. The word part is the PT-PT stem, kept stable across
 * locales so the artwork does not have to be renamed when a language is
 * authored — the label itself comes from the language file.
 */
export const FINE_WORDS: Record<string, string[]> = {
  happy: ["contente", "entusiasmado", "orgulhoso", "aliviado"],
  calm: ["tranquilo", "descansado", "seguro"],
  sad: ["desiludido", "sozinho", "com-saudades", "magoado"],
  scared: ["nervoso", "preocupado", "timido"],
  angry: ["chateado", "irritado", "furioso"],
  ashamed: ["culpado", "arrependido", "embaracado"],
  bored: ["aborrecido", "farto", "impaciente", "sem-vontade"],
};

export const fineCard = (family: string, word: string) =>
  `/assets/emotions/fine/${family}__${word}.webp`;

export const BODY_OUTLINE = "/assets/body/outline.webp";

export const bodyZoneShape = (zone: BodyZone) => `/assets/body/zone-${zone}.webp`;
