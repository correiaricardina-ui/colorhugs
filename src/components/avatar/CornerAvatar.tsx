"use client";

import Link from "next/link";
import Avatar from "@/components/avatar/Avatar";
import { useAvatar } from "@/components/avatar/AvatarProvider";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";

/**
 * The avatar in the top corner, on every page below the homepage.
 *
 * Constant presence, and **not as small as it was** (D-213). At 44px it was a
 * speck, and it was also below this project's own 64px tap-target floor
 * (D-013) — for a link shaped like the child herself, which is the one thing
 * on the page she is most likely to reach for. Now 64px, and 80 from the small
 * breakpoint up.
 *
 * The homepage is still where the colour is read properly (D-078). This is
 * presence, not a display.
 *
 * Nothing until she has picked one: an empty frame with a prompt in it would
 * be a nag on every screen, and choosing already has its two proper doors —
 * the homepage and My ColorHugs.
 *
 * It links home rather than to the picker. A child taps the thing that looks
 * like her, and what she wants is to be where she is.
 */
export default function CornerAvatar() {
  const { locale } = useLocale();
  const t = strings(locale).avatar;
  const names = t.names as Record<string, string>;
  const { avatar, painted, ready } = useAvatar();

  if (!ready || !avatar) return null;

  return (
    <Link
      href="/"
      className="tap-target ml-auto flex items-center rounded-2xl p-1"
      aria-label={names[avatar] ?? "Avatar"}
    >
      <Avatar
        id={avatar}
        painted={painted}
        className="h-16 w-auto sm:h-20"
        sizes="80px"
      />
    </Link>
  );
}
