"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import {
  DEFAULT_LOCALE,
  LOCALES,
  LOCALE_TAGS,
  type Locale,
} from "@/i18n/strings";

/**
 * Locale state for the whole app.
 *
 * Chosen by an adult in the footer, not by the child in the top bar (D-111):
 * a child who taps a language control lands somewhere she cannot read, and the
 * way back is now in that language too.
 *
 * The choice is remembered on the device because language is a household
 * setting, not a session choice. **It never touches anything the child made** —
 * not the avatar, not the stickers, not what she chose in an activity. Worst
 * case is a strange page for a minute, never a loss.
 */

const STORAGE_KEY = "colorhugs.locale";

type Ctx = { locale: Locale; setLocale: (next: Locale) => void };

const LocaleContext = createContext<Ctx>({
  locale: DEFAULT_LOCALE,
  setLocale: () => {},
});

function isLocale(value: unknown): value is Locale {
  return typeof value === "string" && (LOCALES as readonly string[]).includes(value);
}

export function LocaleProvider({ children }: { children: React.ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>(DEFAULT_LOCALE);

  // Read after mount rather than during render: the pages are prerendered as
  // static HTML, so reading storage during render would mismatch the markup.
  useEffect(() => {
    try {
      const saved = window.localStorage.getItem(STORAGE_KEY);
      if (isLocale(saved)) setLocaleState(saved);
    } catch {
      // Storage can be unavailable (private mode, blocked cookies). The
      // default locale is a perfectly good answer; nothing else depends on it.
    }
  }, []);

  useEffect(() => {
    document.documentElement.lang = LOCALE_TAGS[locale];
  }, [locale]);

  const setLocale = useCallback((next: Locale) => {
    setLocaleState(next);
    try {
      window.localStorage.setItem(STORAGE_KEY, next);
    } catch {
      // Not remembering the choice is a small loss; failing is not acceptable.
    }
  }, []);

  return (
    <LocaleContext.Provider value={{ locale, setLocale }}>
      {children}
    </LocaleContext.Provider>
  );
}

export function useLocale(): Ctx {
  return useContext(LocaleContext);
}
