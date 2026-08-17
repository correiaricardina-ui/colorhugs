"use client";

import Link from "next/link";
import Avatar from "@/components/avatar/Avatar";
import { useAvatar } from "@/components/avatar/AvatarProvider";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";

/**
 * The avatar in the top corner, on every page below the homepage.
 *
 * Constant presence, small (D-078). At this size seven colours are not
 * individually legible and are not meant to be — **the homepage is where the
 * colour is actually read**, which is what gives coming back a point.
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
        className="h-11 w-11 sm:h-14 sm:w-14"
        sizes="56px"
      />
    </Link>
  );
}
