"use client";

import Link from "next/link";
import Avatar from "@/components/avatar/Avatar";
import AvatarPicker from "@/components/avatar/AvatarPicker";
import { useAvatar } from "@/components/avatar/AvatarProvider";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";

/**
 * The homepage's avatar block, and the first thing a child meets.
 *
 * **The first choice happens here, and it is not a wall** (D-207). The section
 * grid renders below this whether or not she has chosen, so nobody is stopped
 * on the way in — which is D-048's rule, that the gate sits on the action and
 * never on the door. What this does is make sure the choice is *in front of*
 * every child rather than hidden inside a section she may never open, so no
 * child spends her first activity with an empty corner.
 *
 * Once she has chosen, this is where the colour is read. It is large here and
 * small everywhere else (D-078), because at 44px seven colours are one muddle
 * — and because returning home is then where the colour lands.
 */
export default function HomeAvatar() {
  const { locale } = useLocale();
  const t = strings(locale).avatar;
  const names = t.names as Record<string, string>;
  const { avatar, painted, ready } = useAvatar();

  // Nothing is rendered from the prerendered HTML: it cannot know whether she
  // has an avatar, and guessing wrong would flash the picker at a child who
  // already chose one.
  if (!ready) return <div className="min-h-[12rem]" aria-hidden />;

  if (!avatar) {
    return (
      <section
        aria-label="Choose your avatar"
        className="mx-auto mt-8 w-full max-w-3xl px-4"
      >
        <AvatarPicker />
      </section>
    );
  }

  return (
    <section className="mx-auto mt-8 flex w-full max-w-6xl flex-col items-center px-4">
      {/* By height, so all ten stand the same size (see the picker). */}
      <Avatar
        id={avatar}
        painted={painted}
        className="h-40 w-auto sm:h-52"
        sizes="(max-width: 640px) 160px, 208px"
        priority
      />
      <p className="mt-2 font-display text-lg font-700 text-ch-ink">
        {names[avatar] ?? avatar}
      </p>
      {/*
        The way to change, small and beside her — not a call to action. She
        should be able to change her mind without being invited to every day.
      */}
      <Link
        href="/my-colorhugs/my-avatar"
        className="tap-target mt-1 inline-flex items-center rounded-full px-4 text-sm font-600 text-ch-ink/60 underline decoration-ch-ink/20 underline-offset-4"
      >
        {t.change}
      </Link>
    </section>
  );
}
