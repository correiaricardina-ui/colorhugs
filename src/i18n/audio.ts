import manifest from "@/i18n/audio-manifest.json";
import type { Locale } from "@/i18n/strings";

/**
 * Which spoken lines exist.
 *
 * The site is statically exported, so nothing can check the filesystem at
 * runtime. `scripts/prepare-audio.py` writes this manifest listing only the
 * files that are actually there, and the Listen button uses it to decide
 * whether to appear at all.
 *
 * The manifest stores the real filename, extension included, because a line
 * recorded later in a real voice may be an .m4a where the generated one was an
 * .mp3 — and swapping it in must not require touching code. That is the whole
 * point of deriving the name from the string key.
 */

const AVAILABLE = manifest as Record<string, Record<string, string>>;

export function audioFor(locale: Locale, textKey: string): string | null {
  const file = AVAILABLE[locale]?.[textKey];
  return file ? `/assets/audio/${locale}/${file}` : null;
}
