"use client";

import { LOCALES, LOCALE_NAMES, strings } from "@/i18n/strings";
import { useLocale } from "@/i18n/LocaleProvider";

/**
 * Language control.
 *
 * In the footer, never in the child's top bar (D-111). A child who taps it
 * lands in a language she may not read, and the way back is now in that
 * language too — and the top bar is the one piece of chrome that follows her
 * everywhere. Language is a household setting, so it sits with the other adult
 * controls, where D-036 already put the adult door.
 *
 * Each language names itself. No flags: PT-PT and PT-BR share a language and
 * not a flag, and a flag names a country rather than a language.
 */
export default function LanguageSwitcher() {
  const { locale, setLocale } = useLocale();
  const t = strings(locale).ui;

  return (
    <div className="flex flex-wrap items-center gap-2">
      <span className="text-ch-ink/60">{t.languageLabel}</span>
      <div className="flex gap-1" role="group" aria-label={t.languageLabel}>
        {LOCALES.map((option) => (
          <button
            key={option}
            type="button"
            onClick={() => setLocale(option)}
            aria-pressed={locale === option}
            lang={option}
            className={
              locale === option
                ? "rounded-full bg-ch-ink px-3 py-1.5 font-600 text-white"
                : "rounded-full px-3 py-1.5 font-600 text-ch-ink/70 underline decoration-ch-ink/25 underline-offset-2 hover:decoration-ch-ink/60"
            }
          >
            {LOCALE_NAMES[option]}
          </button>
        ))}
      </div>
    </div>
  );
}
