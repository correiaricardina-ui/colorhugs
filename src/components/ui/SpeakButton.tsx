"use client";

import { useEffect, useRef, useState } from "react";
import { useLocale } from "@/i18n/LocaleProvider";
import { audioFor } from "@/i18n/audio";
import { strings } from "@/i18n/strings";
import { asset } from "@/lib/site";

/**
 * Listen button.
 *
 * Two rules, fixed early because otherwise they erode:
 *
 *  1. **Nothing ever plays by itself.** A child presses to hear. Sound that
 *     starts on its own startles, and starting it for her is a way of deciding
 *     what she needs.
 *  2. **The button appears wherever there is text**, not only where we judge
 *     it necessary — otherwise we are deciding which children can read.
 *
 * If no recording exists for a line, the button is absent rather than broken.
 * A control that fails when pressed teaches a child not to press anything.
 */
export default function SpeakButton({
  textKey,
  className,
}: {
  textKey: string;
  className?: string;
}) {
  const { locale } = useLocale();
  const [playing, setPlaying] = useState(false);
  const ref = useRef<HTMLAudioElement | null>(null);
  const src = audioFor(locale, textKey);

  useEffect(() => {
    const audio = ref.current;
    return () => {
      audio?.pause();
    };
  }, []);

  if (!src) return null;

  const label = strings(locale).ui.listen;

  function toggle() {
    const audio = ref.current;
    if (!audio) return;
    if (playing) {
      audio.pause();
      audio.currentTime = 0;
      setPlaying(false);
      return;
    }
    void audio.play();
    setPlaying(true);
  }

  return (
    <>
      <button
        type="button"
        onClick={toggle}
        aria-label={label}
        className={
          className ??
          "inline-flex h-11 w-11 items-center justify-center rounded-full bg-white/80 text-ch-ink/70 shadow-[0_6px_16px_-10px_rgba(27,42,91,0.8)]"
        }
      >
        <span aria-hidden className="text-xl">
          {playing ? "◼" : "▶"}
        </span>
      </button>
      <audio
        ref={ref}
        src={asset(src)}
        preload="none"
        onEnded={() => setPlaying(false)}
      />
    </>
  );
}
