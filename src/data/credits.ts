/**
 * Authorship and clinical credit.
 *
 * Kept as data so the same wording appears everywhere and is changed in one
 * place. The wording states what was done — design and clinical review — and
 * deliberately stops short of implying that ColorHugs is a clinical service.
 */
export const CREDIT = {
  name: "Ricardina Correia",
  role: "Paediatric Psychology",
  url: "https://ricardinacorreia.pt",
  logo: {
    src: "/assets/branding/ricardina-correia.webp",
    alt: "Ricardina Correia — Psicologia Pediátrica",
  },
  /** One line, used in footers and on the holding page. */
  short: "Created and clinically reviewed by Ricardina Correia",
  /** Fuller version for the Parents & Safety page. */
  long: "ColorHugs is created and clinically reviewed by Ricardina Correia, a paediatric psychologist. Its activities draw on developmental psychology, social and emotional learning, and the learning sciences, shaped by clinical practice with children and families.",
  /** The boundary, restated where the credential is claimed. */
  boundary:
    "ColorHugs offers psychoeducational tools. It does not diagnose, assess or replace psychological care.",
} as const;
