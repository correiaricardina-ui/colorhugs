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
 */

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

type Dictionary = {
  /** Interface furniture. */
  ui: {
    languageLabel: string;
    home: string;
    back: string;
    askAGrownUp: string;
    comingSoonTitle: string;
    comingSoonBody: string;
  };
  /** Activity titles and taglines, keyed `section/activity`. */
  activities: Record<string, { title: string; tagline: string }>;
  /** The How Do I Feel? activity. */
  feelings: {
    prompt: string;
    bodyPrompt: string;
    bodySkip: string;
    bodyDone: string;
    done: string;
    doneAgain: string;
    change: string;
    /** One per emotion family, in the fixed order of D-104. */
    families: Record<string, string>;
    /** One per body zone. */
    zones: Record<string, string>;
  };
};

const en: Dictionary = {
  ui: {
    languageLabel: "Language",
    home: "Home",
    back: "Back",
    askAGrownUp: "Ask a grown-up to unlock this one",
    comingSoonTitle: "is being made",
    comingSoonBody: "We are still building this one. Come back soon!",
  },
  activities: {
    "my-inner-world/how-do-i-feel": {
      title: "How Do I Feel?",
      tagline: "Name what you are feeling today",
    },
  },
  feelings: {
    prompt: "How do you feel today?",
    bodyPrompt: "Where do you feel it?",
    bodySkip: "I would rather not say",
    bodyDone: "Done",
    done: "Thank you for telling me.",
    doneAgain: "Choose again",
    change: "Pick a different feeling",
    families: {
      happy: "Happy",
      calm: "Calm",
      sad: "Sad",
      scared: "Scared",
      angry: "Angry",
      ashamed: "Ashamed",
      bored: "Bored",
    },
    zones: {
      head: "Head",
      chest: "Chest",
      stomach: "Tummy",
      arms: "Arms and hands",
      legs: "Legs and feet",
    },
  },
};

const ptPT: Dictionary = {
  ui: {
    languageLabel: "Língua",
    home: "Início",
    back: "Voltar",
    askAGrownUp: "Pede a um adulto para abrir esta",
    comingSoonTitle: "está a ser feita",
    comingSoonBody: "Ainda estamos a construir esta. Volta em breve!",
  },
  activities: {
    "my-inner-world/how-do-i-feel": {
      title: "Como Me Sinto?",
      tagline: "Diz o que estás a sentir hoje",
    },
  },
  feelings: {
    prompt: "Como te sentes hoje?",
    bodyPrompt: "Onde é que sentes isso?",
    bodySkip: "Prefiro não dizer",
    bodyDone: "Pronto",
    done: "Obrigada por me contares.",
    doneAgain: "Escolher outra vez",
    change: "Escolher outro sentimento",
    families: {
      happy: "Feliz",
      calm: "Calmo",
      sad: "Triste",
      scared: "Assustado",
      angry: "Zangado",
      // The family is Tédio in the documentation; the child sees the word she
      // actually says, and the drawing beside it removes the ambiguity (D-103).
      ashamed: "Envergonhado",
      bored: "Aborrecido",
    },
    zones: {
      head: "Cabeça",
      chest: "Peito",
      stomach: "Barriga",
      arms: "Braços e mãos",
      legs: "Pernas e pés",
    },
  },
};

const DICTIONARIES: Record<Locale, Dictionary> = { en, "pt-PT": ptPT };

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
  return strings(locale).activities[`${section}/${activity}`] ?? fallback;
}
