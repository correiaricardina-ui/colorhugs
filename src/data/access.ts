/**
 * Who gets what, in My Inner World.
 *
 * **Declared, not enforced.** There are no accounts yet (Q-010), so nothing
 * here gates anything at runtime. It is written down so the rule exists before
 * the mechanism does, and so the mechanism has something to implement rather
 * than something to invent.
 */

/**
 * The four audiences.
 *
 * Free and premium are levels of a **family** account. The two professional
 * audiences are not levels above premium — they are a different product for a
 * different buyer (D-153), split into health and education because **a
 * psychologist may use material that opens and a teacher cannot** (D-154).
 */
export type Audience =
  | "family-free"
  | "family-premium"
  | "professional-education"
  | "professional-health";

export interface Entitlements {
  /** The seven family cards, the body map, and being met. */
  families: boolean;
  /** The fine words inside each family — the premium layer (D-142). */
  fineWords: boolean;
  /**
   * The practitioner workbook for a family: framing, graded strategies, the
   * arousal schema, exploratory questions, dynamics, the clinician's sheet.
   */
  workbooks: boolean;
}

export const ENTITLEMENTS: Record<Audience, Entitlements> = {
  // Naming what you feel is never sold (D-142). Neither is the audio, nor the
  // first strategies of any feeling.
  "family-free": { families: true, fineWords: false, workbooks: false },

  "family-premium": { families: true, fineWords: true, workbooks: false },

  // A teacher gets the vocabulary and not the workbook. The angry workbook as
  // written must not go to a classroom: material that opens, opens and stays
  // open where there are thirty children, forty-five minutes and no clinical
  // frame (D-154).
  "professional-education": { families: true, fineWords: true, workbooks: false },

  "professional-health": { families: true, fineWords: true, workbooks: true },
};

export function can(audience: Audience, capability: keyof Entitlements): boolean {
  return ENTITLEMENTS[audience][capability];
}

/**
 * Until Q-010 is answered there is no session and no account, so every visitor
 * is treated as a free family. The fine layer is visible in the preview build
 * because there is nothing yet to check against — **that is a gap, not a
 * decision**, and it must close with the account system.
 */
export const CURRENT_AUDIENCE: Audience = "family-free";
