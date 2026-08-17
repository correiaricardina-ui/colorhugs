"use client";

import cn from "clsx";
import Avatar, { AVATAR_IDS } from "@/components/avatar/Avatar";
import { useAvatar } from "@/components/avatar/AvatarProvider";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";
import SpeakButton from "@/components/ui/SpeakButton";

/**
 * Where the child picks who comes with her.
 *
 * Ten characters, six creatures and four objects, and **no boys and no girls
 * and no skin tones** (D-071, D-079): a set that has to represent every child
 * either represents them all or leaves some out, and animals and objects avoid
 * having to try.
 *
 * **Every avatar exposes exactly seven paintable areas**, one per section
 * (D-069). That is a fairness rule, not a stylistic one — if one had five and
 * another eight, picking the wrong character would quietly be picking less
 * reward for the same work.
 *
 * Shown here in the colour she has already earned, so choosing is a choice of
 * character and never a choice about starting again (D-208).
 */

export default function AvatarPicker({
  className,
  onPicked,
  showPrompt = true,
}: {
  className?: string;
  /** Optional, for the screens that want to move on after she picks. */
  onPicked?: (id: string) => void;
  /**
   * Off inside the My ColorHugs activity, where the page already carries a
   * title and a line saying the same thing twice over.
   */
  showPrompt?: boolean;
}) {
  const { locale } = useLocale();
  const t = strings(locale).avatar;
  const names = t.names as Record<string, string>;
  const { avatar, painted, choose, previous, undo } = useAvatar();

  return (
    <div className={className}>
      {showPrompt ? (
        <p className="flex items-center justify-center gap-3 text-center font-display text-xl font-700 text-ch-ink sm:text-2xl">
          {t.prompt}
          <SpeakButton textKey="avatar.prompt" />
        </p>
      ) : null}
      <p className="mt-1 text-center text-ch-ink/60">{t.hint}</p>

      {/*
        The way back, and only right after a change (D-212). A small child taps
        to see what happens, and without this the one she liked is simply gone.
        It names the character rather than saying "undo", which is a word for
        someone who knows she made a mistake.
      */}
      {previous ? (
        <div className="mt-4 flex justify-center">
          <button
            type="button"
            onClick={undo}
            className="tap-target inline-flex items-center gap-2 rounded-full bg-white px-5 py-3 font-display font-600 text-ch-ink shadow-[0_6px_0_-2px_rgba(27,42,91,0.18)]"
          >
            <Avatar id={previous} painted={painted} className="h-9 w-auto" sizes="36px" />
            {t.undo} {names[previous] ?? previous}
          </button>
        </div>
      ) : null}

      <ul className="mt-6 grid grid-cols-3 gap-3 sm:grid-cols-5 sm:gap-4">
        {AVATAR_IDS.map((id) => {
          const isChosen = id === avatar;
          return (
            <li key={id}>
              <button
                type="button"
                onClick={() => {
                  choose(id);
                  onPicked?.(id);
                }}
                aria-pressed={isChosen}
                className={cn(
                  "flex w-full flex-col items-center gap-1 rounded-sticker border-2 p-2 transition-transform duration-150 hover:-translate-y-1 focus-visible:-translate-y-1 active:translate-y-0 motion-reduce:transform-none",
                  isChosen
                    ? "border-[--sec-accent] bg-white"
                    : "border-transparent bg-white/60",
                )}
              >
                {/*
                  Already carrying her colour. A picker that shows every
                  character blank would make changing look like starting over.
                */}
                {/*
                  A square box with the character fitted inside it by height.
                  Sized by width, the rocket comes out tall and thin and the
                  house short and wide, the rows go ragged, and some avatars
                  look more important than others — which is the D-069 fairness
                  problem arriving through the layout instead of the artwork.
                */}
                <span className="flex aspect-square w-full items-center justify-center">
                  <Avatar
                    id={id}
                    painted={painted}
                    className="h-full w-auto"
                    sizes="(max-width: 640px) 28vw, 160px"
                  />
                </span>
                <span className="font-display font-700 text-ch-ink">
                  {names[id] ?? id}
                </span>
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
