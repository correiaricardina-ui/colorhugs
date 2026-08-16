/**
 * The language file.
 *
 * Every child-facing word lives here, never inside artwork (D-081, D-110) and
 * never hard-coded in a component. Artwork is drawn once and captioned in as
 * many languages as we support; a sticker that reads "Explorer" would need
 * seven regenerations for ever.
 *
 * Section names are the exception: they behave as wordmarks, like "ColorHugs"
 * itself, and are not translated (D-110). The app writes the local name
 * beneath the tile; the artwork keeps its own.
 *
 * Priority locales are EN, FR, ES, PT-PT, PT-BR, ZH and HI (rule 10). Two are
 * written; the rest fall back to English until they are authored — and
 * authored is the right word: the emotion vocabulary is written per language,
 * not translated (D-101).
 *
 * **The text itself lives in JSON, one file per locale**, so a translator edits
 * `pt-PT.json` and never opens a TypeScript file. It is also what lets the
 * audio script read the strings directly: every spoken line is generated from
 * the same source the screen reads, so the two cannot drift apart.
 */

import enJson from "@/i18n/en.json";
import ptPTJson from "@/i18n/pt-PT.json";

export const LOCALES = ["en", "pt-PT"] as const;
export type Locale = (typeof LOCALES)[number];

export const DEFAULT_LOCALE: Locale = "en";

/** Shown in the switcher. Each language names itself — never a flag (D-111). */
export const LOCALE_NAMES: Record<Locale, string> = {
  en: "English",
  "pt-PT": "Português",
};

/** BCP-47 value for the <html lang> attribute. */
export const LOCALE_TAGS: Record<Locale, string> = {
  en: "en",
  "pt-PT": "pt-PT",
};

type Dictionary = typeof enJson;

const DICTIONARIES: Record<Locale, Dictionary> = {
  en: enJson,
  "pt-PT": ptPTJson as Dictionary,
};

export function strings(locale: Locale): Dictionary {
  return DICTIONARIES[locale] ?? DICTIONARIES[DEFAULT_LOCALE];
}

/**
 * Activity title and tagline for a locale, falling back to the value in
 * `sections.ts` while a locale is still being authored. The fallback is
 * deliberate: an untranslated English line is honest, an empty one is a bug.
 */
export function activityStrings(
  locale: Locale,
  section: string,
  activity: string,
  fallback: { title: string; tagline: string },
): { title: string; tagline: string } {
  const found = (strings(locale).activities as Record<string, { title: string; tagline: string }>)[
    `${section}/${activity}`
  ];
  return found ?? fallback;
}
