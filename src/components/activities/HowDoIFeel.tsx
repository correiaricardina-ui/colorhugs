"use client";

import Image from "next/image";
import { useState } from "react";
import cn from "clsx";
import {
  BODY_OUTLINE,
  BODY_ZONES,
  EMOTIONS,
  bodyZoneShape,
  type BodyZone,
} from "@/data/emotions";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";
import { asset } from "@/lib/site";

/**
 * How Do I Feel? — the first built activity.
 *
 * The child picks one of seven cards, then, if she wants, points to where in
 * her body she feels it. Then it closes. That is the whole activity.
 *
 * What is deliberately absent, and none of it is an omission:
 *
 *  - **No intensity.** No scale, no "how big". A scale produces "my sadness is
 *    a 5" with nothing that follows, and turns a vocabulary tool into
 *    something shaped like a measure (D-096).
 *  - **No why, and nowhere to write.** A material a child uses alone must
 *    close itself; asking why opens something that needs a listener, and a
 *    child writing what happened at home is telling nobody (D-094).
 *  - **Nothing is stored, in this version.** The short trail (D-097) waits on
 *    Q-010, because a trail kept in the browser vanishes when someone clears
 *    history — the child comes back and the product has forgotten her, which
 *    is worse than never having offered.
 *  - **No correct answer, and no interpretation.** Every card is met the same
 *    way. Naming is description; telling a child what it means is a person's
 *    work.
 *  - **The body location is never a record.** The map is the moment; the card
 *    is the record (D-105).
 */

type Stage = "choose" | "body" | "done";

export default function HowDoIFeel() {
  const { locale } = useLocale();
  const t = strings(locale).feelings;

  const [stage, setStage] = useState<Stage>("choose");
  const [chosen, setChosen] = useState<string | null>(null);
  const [zone, setZone] = useState<BodyZone | null>(null);

  const family = EMOTIONS.find((e) => e.id === chosen) ?? null;

  function reset() {
    setChosen(null);
    setZone(null);
    setStage("choose");
  }

  return (
    <section className="mx-auto w-full max-w-3xl">
      {stage === "choose" ? (
        <>
          <h2 className="text-center font-display font-700 text-ch-ink">
            {t.prompt}
          </h2>

          {/*
            Three columns with the last row centred. Seven in a plain grid
            leaves one card alone with an emphasis it has not earned (D-104).
            The label always sits beneath the card, never inside it — text
            inside artwork is the mistake that costs seven regenerations.
          */}
          <ul className="mt-6 grid grid-cols-3 gap-3 sm:gap-4">
            {EMOTIONS.map((emotion, index) => (
              <li
                key={emotion.id}
                className={cn(
                  index === EMOTIONS.length - 1 && "col-start-2",
                )}
              >
                <button
                  type="button"
                  onClick={() => {
                    setChosen(emotion.id);
                    setStage("body");
                  }}
                  className="group flex w-full flex-col items-center gap-1 rounded-sticker p-2 transition-transform duration-150 hover:-translate-y-1 focus-visible:-translate-y-1 active:translate-y-0 motion-reduce:transform-none"
                >
                  <span className="relative block aspect-square w-full">
                    <Image
                      src={asset(emotion.src)}
                      alt=""
                      fill
                      sizes="(max-width: 640px) 30vw, 200px"
                      className="object-contain"
                    />
                  </span>
                  <span className="font-display font-700 text-ch-ink">
                    {t.families[emotion.id]}
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </>
      ) : null}

      {stage === "body" && family ? (
        <>
          <h2 className="text-center font-display font-700 text-ch-ink">
            {t.bodyPrompt}
          </h2>

          <div className="mt-6 flex flex-col items-center gap-6 sm:flex-row sm:items-start sm:justify-center">
            <BodyMap
              tint={family.tint}
              selected={zone}
              onSelect={setZone}
              labels={t.zones}
            />

            <div className="flex w-full max-w-xs flex-col gap-3">
              <span className="relative mx-auto block h-28 w-28">
                <Image
                  src={asset(family.src)}
                  alt=""
                  fill
                  sizes="112px"
                  className="object-contain"
                />
              </span>
              <p className="text-center font-display font-700 text-ch-ink">
                {t.families[family.id]}
              </p>

              <button
                type="button"
                onClick={() => setStage("done")}
                className="min-h-[64px] rounded-full bg-[--sec-accent] px-6 font-display font-700 text-white shadow-[0_10px_24px_-14px_rgba(27,42,91,0.8)]"
              >
                {/*
                  The primary action names what it does. Before a zone is
                  chosen it is a way out — the child never has to point at her
                  body. After one is chosen it is "done", because a skip button
                  offered as the only way forward reads as the app asking her
                  to give up.
                */}
                {zone ? t.bodyDone : t.bodySkip}
              </button>
              <button
                type="button"
                onClick={reset}
                className="min-h-[64px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
              >
                {t.change}
              </button>
            </div>
          </div>
        </>
      ) : null}

      {stage === "done" && family ? (
        <div className="mx-auto max-w-md text-center">
          <span className="relative mx-auto block aspect-square w-48">
            <Image
              src={asset(family.src)}
              alt=""
              fill
              sizes="192px"
              className="object-contain"
              priority
            />
          </span>
          {/*
            Every feeling is met identically. "Furious" is thanked exactly as
            "calm" is — the moment one answer gets a warmer reply than another,
            the child learns which one to give.
          */}
          <p className="mt-4 font-display font-700 text-ch-ink">{t.done}</p>
          <button
            type="button"
            onClick={reset}
            className="mt-6 min-h-[64px] rounded-full bg-[--sec-accent] px-8 font-display font-700 text-white shadow-[0_10px_24px_-14px_rgba(27,42,91,0.8)]"
          >
            {t.doneAgain}
          </button>
        </div>
      ) : null}
    </section>
  );
}

/**
 * The neutral outline figure.
 *
 * No face, no hair, no clothing, no gender, no skin tone — the same reasoning
 * that gave the avatars animals and objects rather than boys and girls
 * (D-071): a figure that represents nobody in particular leaves no child out.
 *
 * Colour is applied by stacking one tinted silhouette per zone beneath the
 * outline, rather than flood-filling a canvas. Five shapes and one outline
 * cover every state, and it works with no script on a static host.
 */
function BodyMap({
  tint,
  selected,
  onSelect,
  labels,
}: {
  tint: string;
  selected: BodyZone | null;
  onSelect: (zone: BodyZone) => void;
  labels: Record<string, string>;
}) {
  return (
    <div className="relative aspect-[589/900] w-56 shrink-0 sm:w-64">
      {BODY_ZONES.map((zone) => (
        <span
          key={zone}
          aria-hidden
          className="pointer-events-none absolute inset-0 transition-opacity duration-200 motion-reduce:transition-none"
          style={{
            opacity: selected === zone ? 1 : 0,
            backgroundColor: tint,
            WebkitMaskImage: `url(${asset(bodyZoneShape(zone))})`,
            maskImage: `url(${asset(bodyZoneShape(zone))})`,
            WebkitMaskSize: "contain",
            maskSize: "contain",
            WebkitMaskRepeat: "no-repeat",
            maskRepeat: "no-repeat",
          }}
        />
      ))}

      <Image
        src={asset(BODY_OUTLINE)}
        alt=""
        fill
        sizes="256px"
        className="pointer-events-none object-contain"
      />

      {/*
        Hit areas, not drawn shapes. Each is a generous rectangle over its part
        of the figure, comfortably above the 64px floor (D-013) — a zone that
        misses a child's finger reads as the app not listening.
      */}
      {ZONE_HITS.map(({ zone, style }, index) => (
        <button
          key={`${zone}-${index}`}
          type="button"
          onClick={() => onSelect(zone)}
          aria-pressed={selected === zone}
          className="absolute rounded-2xl focus-visible:ring-4 focus-visible:ring-[--sec-accent]"
          style={style}
        >
          <span className="sr-only">{labels[zone]}</span>
        </button>
      ))}
    </div>
  );
}

/** Percentages measured from the prepared artwork, not guessed. */
const ZONE_HITS: { zone: BodyZone; style: React.CSSProperties }[] = [
  { zone: "head", style: { left: "28%", top: "0%", width: "44%", height: "34%" } },
  { zone: "chest", style: { left: "30%", top: "34%", width: "40%", height: "20%" } },
  { zone: "stomach", style: { left: "30%", top: "54%", width: "40%", height: "16%" } },
  { zone: "arms", style: { left: "0%", top: "36%", width: "28%", height: "30%" } },
  { zone: "arms", style: { left: "72%", top: "36%", width: "28%", height: "30%" } },
  { zone: "legs", style: { left: "22%", top: "70%", width: "56%", height: "30%" } },
];
