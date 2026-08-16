"use client";

import Image from "next/image";
import { PLAN_BADGES } from "@/data/sections";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";
import { asset } from "@/lib/site";

/**
 * The three ways in, in the adult area.
 *
 * **Not on the child's home page** (D-153). The home page is hers, and a large
 * button reading *Premium* is the nearest thing to a purchase button we could
 * put in front of her — D-036 removed the parents button from the top bar for
 * the same reason, and D-039 keeps price and purchase off every child screen.
 *
 * **The plan names stay in English and are not translated** — they behave as
 * brand, like the section names (D-110). What makes that fair is the line
 * beside each one, which always comes from the language file: nobody has to
 * read English to know what a badge means.
 */
export default function WaysIn() {
  const { locale } = useLocale();
  const t = strings(locale).plans as Record<string, string>;

  const ways = [
    { plan: "free" as const, description: t.free },
    { plan: "premium" as const, description: t.premium },
    { plan: "professional" as const, description: t.professional, branches: [t.professionalHealth, t.professionalEducation] },
  ];

  return (
    <section aria-labelledby="ways-in" className="mt-10">
      <h2 id="ways-in" className="font-display font-700 text-ch-ink">
        {t.heading}
      </h2>

      <ul className="mt-5 grid gap-4 sm:grid-cols-3">
        {ways.map(({ plan, description, branches }) => (
          <li
            key={plan}
            className="flex flex-col items-center rounded-xl border border-ch-ink/10 bg-white p-5 text-center"
          >
            <span className="relative block h-24 w-full">
              <Image
                src={asset(PLAN_BADGES[plan].src)}
                alt={PLAN_BADGES[plan].alt}
                fill
                sizes="220px"
                className="object-contain"
              />
            </span>
            <p className="mt-3 text-sm leading-relaxed text-ch-ink/75">
              {description}
            </p>

            {/*
              The two halves of the professional line, named honestly. A
              psychologist may use material that opens — exploratory questions,
              family dynamics, a clinical sheet. A teacher has thirty children,
              forty-five minutes and no clinical frame, and material that opens
              in a classroom opens and stays open. The education line is a
              separate body of content, not a variant of the clinical one, and
              it is marked as unbuilt rather than pointed at the workbook.
            */}
            {branches ? (
              <ul className="mt-4 w-full space-y-1.5 border-t border-ch-ink/10 pt-3 text-sm text-ch-ink/70">
                {branches.map((branch, index) => (
                  <li key={branch}>
                    {branch}
                    {index === 1 ? (
                      <span className="ml-1 text-ch-ink/40">
                        · {t.notYet}
                      </span>
                    ) : null}
                  </li>
                ))}
              </ul>
            ) : null}
          </li>
        ))}
      </ul>
    </section>
  );
}
