import type { ColouringPage } from "@/data/colouring";

/**
 * Subjects for the Explore & Color library, **deduced from what each page
 * shows** (D-377).
 *
 * ## Why not by feeling
 *
 * The library must never be arranged by emotion. `colouring.ts` already fixes
 * the rule for filenames: **a page is named for what it shows, never for the
 * feeling**, because a parent finding `angry/breathing.pdf` learns what the
 * child chose, and the product promised not to report. **A shelf labelled
 * "When I am angry" would do exactly that, on screen, where anyone can see
 * it.**
 *
 * Two more reasons, both practical. **One page serves several families** — the
 * quiet corner serves anger and sadness and does a different job in each — so
 * an arrangement by feeling would either repeat it or pick a family for it. And
 * **a child who comes to colour comes to choose a drawing, not a feeling**: a
 * menu of feelings turns colouring into emotional homework.
 *
 * ## How the deduction works, and what it costs
 *
 * The only field describing the picture is `alt`. `path` and `families` are
 * about emotion and are exactly the ones that may not become shelves.
 *
 * So the subject comes from **ordered keyword rules over `alt`**, and the order
 * is the whole design: *stepping-stones* is a child crossing stones **towards a
 * cat**, so it matches both moving and animals. **First rule wins**, which
 * means the order is an editorial decision written as code rather than as a
 * field.
 *
 * Two things keep that honest. `subjectReport()` prints every page and its
 * shelf, so a wrong one is visible rather than buried. And **a page matching no
 * rule throws** instead of landing quietly in an "Other" shelf, which is how a
 * library slowly stops being arranged at all.
 *
 * `override` exists for the case the rules get wrong. **Using it is a decision
 * and should be rare**; if it stops being rare, the rules are the wrong shape.
 */
export type Subject =
  | "with-someone"
  | "animals"
  | "moving"
  | "quiet"
  | "things";

export const SUBJECT_ORDER: Subject[] = [
  "with-someone",
  "quiet",
  "animals",
  "moving",
  "things",
];

export const SUBJECT_LABEL: Record<Subject, { en: string; "pt-PT": string }> = {
  "with-someone": { en: "With someone", "pt-PT": "Com alguém" },
  animals: { en: "Animals", "pt-PT": "Animais" },
  moving: { en: "Moving about", "pt-PT": "A mexer" },
  quiet: { en: "Quiet places", "pt-PT": "Sítios sossegados" },
  things: { en: "Things and hands", "pt-PT": "Coisas e mãos" },
};

/**
 * Ordered. **First match wins**, and the order is the editorial call.
 *
 * *With someone* comes first because a page with two people in it is about the
 * two people, whatever else is in the picture.
 *
 * ***Quiet* comes before *animals*, and that ordering is a correction.** With
 * animals first, the folded blanket shelved under animals because of the plush
 * bear on it, and the bedroom corner because of the plush rabbit — **a plush toy
 * is a thing, not an animal.** Putting quiet first fixes all three without a
 * single exception: the blanket has *blanket*, the bedroom has *bedroom*, the
 * lying-and-clouds page has both, and the dog, the cat at the end of the stones
 * and the elephant have no quiet word at all.
 *
 * *Animals* then comes before *moving*, so the stones-and-cat page shelves with
 * the cat: a child looking for animals finds it, and a child looking for
 * movement has three others.
 */
const RULES: { subject: Subject; words: RegExp }[] = [
  { subject: "with-someone", words: /grown-up|two children|facing each other/i },
  { subject: "quiet", words: /quiet corner|cushions|blanket|lying|bedroom|clouds/i },
  { subject: "animals", words: /\b(dog|cat|elephant|rabbit|bear)\b/i },
  { subject: "moving", words: /jumping|running|crossing|on grass|football/i },
  { subject: "things", words: /shelf|frame|hand|fingers|feather|table|plush toys/i },
];

export function subjectFor(page: ColouringPage & { override?: Subject }): Subject {
  if (page.override) return page.override;
  const hit = RULES.find((rule) => rule.words.test(page.alt));
  if (!hit) {
    throw new Error(
      `Colouring page "${page.id}" matches no subject rule. Its alt text is ` +
        `"${page.alt}". Add a word to a rule or set an override — do not let ` +
        `it fall into a catch-all shelf.`,
    );
  }
  return hit.subject;
}

export function groupBySubject<T extends ColouringPage>(
  pages: T[],
): { subject: Subject; pages: T[] }[] {
  return SUBJECT_ORDER.map((subject) => ({
    subject,
    pages: pages.filter((page) => subjectFor(page) === subject),
  })).filter((shelf) => shelf.pages.length > 0);
}

/** Prints every page and the shelf it landed on, so it can be checked. */
export function subjectReport(pages: ColouringPage[]): string {
  return pages
    .map((page) => `${subjectFor(page).padEnd(13)} ${page.id.padEnd(20)} ${page.alt}`)
    .join("\n");
}
