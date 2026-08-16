"use client";

import Image from "next/image";
import { useState } from "react";
import cn from "clsx";
import {
  BODY_OUTLINE,
  BODY_ZONES,
  EMOTIONS,
  FINE_WORDS,
  bodyZoneShape,
  fineCard,
  type BodyZone,
} from "@/data/emotions";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";
import ColouringCanvas from "@/components/activities/ColouringCanvas";
import { CURRENT_AUDIENCE, can } from "@/data/access";
import { pagesForFamily } from "@/data/colouring";
import SpeakButton from "@/components/ui/SpeakButton";
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

type Stage = "choose" | "body" | "fine" | "strategy" | "colour" | "done";

export default function HowDoIFeel() {
  const { locale } = useLocale();
  const all = strings(locale).feelings;
  // The JSON gives each family its own literal key. Widening to a record keeps
  // the lookup honest — the ids come from EMOTIONS, which is the same list.
  const t = {
    ...all,
    families: all.families as Record<string, string>,
    zones: all.zones as Record<string, string>,
    literacy: all.literacy as Record<string, string>,
    pages: all.pages as Record<string, string>,
    fine: all.fine as Record<string, string>,
  };

  const [stage, setStage] = useState<Stage>("choose");
  const [chosen, setChosen] = useState<string | null>(null);
  const [zone, setZone] = useState<BodyZone | null>(null);
  const [page, setPage] = useState<string | null>(null);

  const family = EMOTIONS.find((e) => e.id === chosen) ?? null;
  // Only angry is authored so far. A family with no pages closes after the
  // body map, which is honest — nothing on screen implies more exists.
  const pages = family ? pagesForFamily(family.id) : [];
  const chosenPage = pages.find((p) => p.id === page) ?? null;

  function reset() {
    setChosen(null);
    setZone(null);
    setPage(null);
    setStage("choose");
  }

  function afterBody() {
    setStage(pages.length ? "strategy" : "done");
  }

  // The fine words are premium and optional. They are reached only by asking
  // for them, never on the way through — the activity has already closed by
  // then (D-100), so a child who does not read loses nothing.
  //
  // `can` is the declared rule, not an enforced one: without accounts (Q-010)
  // every visitor is a free family and this check has nothing to check
  // against. It is wired now so that the account system finds a place to plug
  // into rather than a decision to make.
  const mayOpenFineWords = can(CURRENT_AUDIENCE, "fineWords");
  const fineWords = family ? (FINE_WORDS[family.id] ?? []) : [];

  return (
    <section className="mx-auto w-full max-w-3xl">
      {stage === "choose" ? (
        <>
          <h2 className="flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
            {t.prompt}
            <SpeakButton textKey="feelings.prompt" />
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
          <h2 className="flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
            {t.bodyPrompt}
            <SpeakButton textKey="feelings.bodyPrompt" />
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
              <p className="flex items-center justify-center gap-2 text-center font-display font-700 text-ch-ink">
                {t.families[family.id]}
                <SpeakButton textKey={`feelings.families.${family.id}`} />
              </p>

              <button
                type="button"
                onClick={afterBody}
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

      {stage === "strategy" && family ? (
        <>
          {/*
            Literacy about the feeling in general, never about this child.
            "Sometimes people feel angry when something seems unfair" is
            description; "you are angry because…" is interpretation (D-118).
          */}
          <p className="mx-auto max-w-lg text-center text-lg text-ch-ink/80">
            {t.literacy[family.id]}
          </p>

          {/*
            Offered as a choice. "Which would you like to try?" closes and
            leaves the choice with her; "do this" decides for her, and deciding
            what a child should do next is a person's work.
          */}
          <h2 className="mt-6 flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
            {t.strategyPrompt}
            <SpeakButton textKey="feelings.strategyPrompt" />
          </h2>

          <ul className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3">
            {pages.map((option) => (
              <li key={option.id}>
                <button
                  type="button"
                  onClick={() => {
                    setPage(option.id);
                    setStage("colour");
                  }}
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
                    {t.pages[option.id]}
                  </span>
                </button>
              </li>
            ))}
          </ul>

          <div className="mt-6 text-center">
            <button
              type="button"
              onClick={reset}
              className="min-h-[64px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
            >
              {t.change}
            </button>
          </div>
        </>
      ) : null}

      {stage === "colour" && chosenPage ? (
        <>
          <h2 className="flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
            {t.pages[chosenPage.id]}
            <SpeakButton textKey={`feelings.pages.${chosenPage.id}`} />
          </h2>
          <p className="mt-1 text-center text-ch-ink/70">{t.colourPrompt}</p>

          <div className="mt-5">
            <ColouringCanvas
              src={`${chosenPage.src}.webp`}
              pdf={`${chosenPage.src}.pdf`}
              alt={chosenPage.alt}
            />
          </div>

          <div className="mt-6 flex flex-wrap justify-center gap-3">
            <button
              type="button"
              onClick={() => setStage("strategy")}
              className="min-h-[64px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
            >
              {t.change}
            </button>
            <button
              type="button"
              onClick={() => setStage("done")}
              className="min-h-[64px] rounded-full bg-[--sec-accent] px-8 font-display font-700 text-white"
            >
              {t.bodyDone}
            </button>
          </div>
        </>
      ) : null}

      {stage === "fine" && family ? (
        <>
          <h2 className="flex items-center justify-center gap-3 text-center font-display font-700 text-ch-ink">
            {t.finePrompt}
            <SpeakButton textKey="feelings.finePrompt" />
          </h2>

          <ul className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-4">
            {fineWords.map((word) => (
              <li key={word}>
                {/*
                  Choosing a fine word changes nothing and leads nowhere: it is
                  a better name for what she already said, not a second
                  question. Tapping one simply shows it chosen.
                */}
                <div className="flex w-full flex-col items-center gap-1 rounded-sticker bg-white/60 p-3">
                  <span className="relative block aspect-square w-full">
                    <Image
                      src={asset(fineCard(family.id, word))}
                      alt=""
                      fill
                      sizes="(max-width: 640px) 45vw, 160px"
                      className="object-contain"
                    />
                  </span>
                  <span className="text-center font-display font-700 text-ch-ink">
                    {t.fine[`${family.id}__${word}`] ?? word}
                  </span>
                  <SpeakButton textKey={`feelings.fine.${family.id}__${word}`} />
                </div>
              </li>
            ))}
          </ul>

          <div className="mt-6 text-center">
            <button
              type="button"
              onClick={() => setStage("done")}
              className="min-h-[64px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
            >
              {t.fineBack}
            </button>
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
          <p className="mt-4 flex items-center justify-center gap-3 font-display font-700 text-ch-ink">
            {t.done}
            <SpeakButton textKey="feelings.done" />
          </p>
          <div className="mt-6 flex flex-wrap justify-center gap-3">
            {/*
              The way into the fine words, offered only after the activity has
              closed. An invitation to go deeper, never a wall — she has
              already named what she feels and already been met (D-100).
            */}
            {fineWords.length ? (
              <button
                type="button"
                onClick={() => setStage("fine")}
                className="min-h-[64px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
              >
                {t.finePrompt}
              </button>
            ) : null}
            <button
              type="button"
              onClick={reset}
              className="min-h-[64px] rounded-full bg-[--sec-accent] px-8 font-display font-700 text-white shadow-[0_10px_24px_-14px_rgba(27,42,91,0.8)]"
            >
              {t.doneAgain}
            </button>
          </div>
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
