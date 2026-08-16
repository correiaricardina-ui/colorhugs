/**
 * Colouring pages that How Do I Feel? leads to.
 *
 * They live in Color & Create, inside the Explore & Color library, and are
 * **visible there like any other page** (D-119). Hidden, the choice inside the
 * activity would become a reward to unlock, and a child would start choosing
 * the feeling that gives the drawing she wants — which destroys the only
 * honest thing the activity records.
 *
 * ## The pages are named for what they show, never for the feeling
 *
 * A page called "When I am angry", or a folder called "angry", makes the
 * downloaded file report what the child chose. No screen would say it, but a
 * parent finding that PDF knows — and D-098 promised the product does not
 * report. A drawing of slow breathing is a drawing of breathing.
 *
 * The link between a feeling and a page lives here, in data. Never in the
 * filename, never in the folder, never in the page itself.
 *
 * ## Three paths, because the feelings are not the same kind of thing
 *
 *  - `strategy` — for the difficult feelings (sad, scared, angry, ashamed):
 *    something to try. Offered as a choice, never as an instruction: "which
 *    would you like to try?" closes and leaves the choice with her; "do this"
 *    decides for her, which is a person's work (D-094).
 *  - `moment`   — for the good feelings (happy, calm): moments when I feel
 *    like this. Savouring, not a consolation prize for a feeling that needs
 *    no fixing.
 *  - `now`      — for boredom alone: what I could do now. The only path where
 *    the product may suggest an activity without implying anything is wrong.
 *
 * ## Many-to-many on purpose
 *
 * One page serves several families — slow breathing belongs to angry, scared
 * and sad. That is not an economy measure: **the number of strategies per
 * family is whatever the evidence supports, and the families will not have
 * equal numbers.** A symmetrical grid would look tidy and would be a lie.
 *
 * ## Nothing is written here yet
 *
 * The content is authored from the literature with honest grading, one line
 * per page, in the same three levels the professional note uses. Inventing
 * plausible-sounding strategies to fill this file would be the exact failure
 * the grading exists to prevent.
 *
 * Two things already ruled out, recorded so they do not creep back in:
 *
 *  - **Discharging anger by hitting something.** The catharsis idea is the
 *    first thing most children's apps reach for and the literature points the
 *    other way — it raises arousal rather than lowering it.
 *  - **Cognitive reappraisal as a young child's strategy.** One of the most
 *    studied strategies in adults, and developmentally out of reach for a
 *    five-year-old.
 *
 * And one distinction to hold: shame is not guilt. Guilt moves a child to
 * repair, shame moves her to hide, and a strategy built for one can make the
 * other worse.
 */

import type { EmotionFamily } from "@/data/emotions";

export type ColouringPath = "strategy" | "moment" | "now";

/** How well supported the page's claim is. Same three levels as the notes. */
export type Evidence = "established" | "reasonable" | "practice";

export interface ColouringPage {
  /** Stable id. Also the artwork filename — named for the drawing, not the feeling. */
  id: string;
  path: ColouringPath;
  /** Line art under /assets/colouring/{path folder}/. */
  src: string;
  /** Descriptive alt text of what the drawing shows. */
  alt: string;
  /**
   * Which emotion families offer this page. Empty is never correct — a page
   * no family links to is unreachable from the activity.
   */
  families: EmotionFamily["id"][];
  /** What the support actually is, and for what claim. Both are required. */
  evidence: { level: Evidence; note: string };
}

/**
 * Angry is authored (D-123). The other six families follow the same shape.
 *
 * Note the evidence notes: not one of them reaches *established*. The base of
 * the first does — young children regulate with an adult, not alone — but no
 * application does. The strongest support in the set points off the screen.
 */
export const COLOURING_PAGES: ColouringPage[] = [
  {
    id: "talking-together",
    path: "strategy",
    src: "/assets/colouring/strategies/talking-together",
    alt: "A child and a grown-up sitting on a bench, talking",
    families: ["angry"],
    evidence: {
      level: "reasonable",
      note: "That young children regulate with an adult rather than alone is well established; that this gesture helps in the moment is reasonable. It teaches that there is always someone to go to — at home or at school — which holds even in a minute when the room is empty.",
    },
  },
  {
    id: "quiet-corner",
    path: "strategy",
    src: "/assets/colouring/strategies/quiet-corner",
    alt: "A quiet corner with soft cushions and a folded blanket",
    families: ["angry"],
    evidence: {
      level: "reasonable",
      note: "Changing the situation rather than enduring inside it.",
    },
  },
  {
    id: "counting-fingers",
    path: "strategy",
    src: "/assets/colouring/strategies/counting-fingers",
    alt: "An open hand with the fingers spread wide",
    families: ["angry"],
    evidence: {
      level: "reasonable",
      note: "Attentional deployment has the best support specifically in young children — the mechanism in the classic delay research. Probably the strongest of this set at four and five. Counting is somewhere to put attention, never an exercise.",
    },
  },
  {
    id: "floating-feather",
    path: "strategy",
    src: "/assets/colouring/strategies/floating-feather",
    alt: "A feather drifting down through the clouds",
    families: ["angry"],
    evidence: {
      level: "practice",
      note: "The most popular strategy in children's products and the evidence is thinner than the popularity implies: the physiological logic and the studies are largely adult. Reasonable in adults, practice in children.",
    },
  },
  {
    id: "jumping",
    path: "strategy",
    src: "/assets/colouring/strategies/jumping",
    alt: "A child jumping with both arms in the air",
    families: ["angry"],
    evidence: {
      level: "practice",
      note: "Moving is not hitting. Discharging anger by striking something is excluded: the catharsis literature points the other way, raising arousal rather than lowering it.",
    },
  },
];

export function pagesForFamily(family: string): ColouringPage[] {
  return COLOURING_PAGES.filter((page) => page.families.includes(family));
}
