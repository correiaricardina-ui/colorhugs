"use client";

import Image from "next/image";
import { useState } from "react";
import ColouringCanvas from "@/components/activities/ColouringCanvas";
import { COLOURING_PAGES, LIBRARY_PAGES } from "@/data/colouring";
import SpeakButton from "@/components/ui/SpeakButton";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";
import { asset } from "@/lib/site";

/**
 * Explore & Color — the whole colouring library, free in full.
 *
 * Every page in the product appears here, including the ones a strategy leads
 * to (D-119). Hidden, the choice inside How Do I Feel? would become a reward to
 * unlock, and a child would start choosing the feeling that yields the drawing
 * she wants — destroying the only honest thing that activity records.
 *
 * The names here describe the picture, never the strategy: the bench page is
 * "On the bench", not "Go and tell someone". A child browsing the library has
 * no reason to meet a feeling she did not choose, and a page that named its
 * strategy would carry the feeling with it (D-120).
 */
export default function ExploreAndColor() {
  const { locale } = useLocale();
  const t = strings(locale).library as {
    pick: string;
    back: string;
    pages: Record<string, string>;
  };

  const [chosen, setChosen] = useState<string | null>(null);
  const pages = [...LIBRARY_PAGES, ...COLOURING_PAGES];
  const page = pages.find((p) => p.id === chosen) ?? null;

  if (page) {
    return (
      <section className="mx-auto w-full max-w-3xl">
        <h2 className="flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
          {t.pages[page.id] ?? page.id}
        </h2>
        <div className="mt-5">
          <ColouringCanvas
            src={`${page.src}.webp`}
            pdf={`${page.src}.pdf`}
            alt={page.alt}
          />
        </div>
        <div className="mt-6 text-center">
          <button
            type="button"
            onClick={() => setChosen(null)}
            className="min-h-[64px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
          >
            {t.back}
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="mx-auto w-full max-w-3xl">
      <h2 className="flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
        {t.pick}
        <SpeakButton textKey="library.pick" />
      </h2>
      <ul className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-3">
        {pages.map((option) => (
          <li key={option.id}>
            <button
              type="button"
              onClick={() => setChosen(option.id)}
              className="flex w-full flex-col items-center gap-1 rounded-sticker bg-white/70 p-3 transition-transform duration-150 hover:-translate-y-1 motion-reduce:transform-none"
            >
              <span className="relative block aspect-square w-full">
                <Image
                  src={asset(`${option.src}.webp`)}
                  alt=""
                  fill
                  sizes="(max-width: 640px) 45vw, 200px"
                  className="object-contain"
                />
              </span>
              <span className="text-center font-display font-700 text-ch-ink">
                {t.pages[option.id] ?? option.id}
              </span>
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}
