"use client";

import { useEffect } from "react";
import AvatarPicker from "@/components/avatar/AvatarPicker";
import { useAvatar } from "@/components/avatar/AvatarProvider";

/**
 * My ColorHugs → the avatar.
 *
 * The homepage carries the *first* choice so that no child reaches an activity
 * without one (D-207). This is where she comes back to change it, and the two
 * are the same picker rather than two screens that can drift.
 *
 * **Being here paints My ColorHugs**, like every other area: colour is for
 * having been somewhere, not for how much was done there (D-067). Changing
 * avatar carries the colour across (D-208), so this screen can never cost her
 * anything.
 */
export default function MyAvatar() {
  const { markVisited } = useAvatar();

  useEffect(() => {
    markVisited("MC");
  }, [markVisited]);

  return <AvatarPicker className="mx-auto w-full max-w-3xl" showPrompt={false} />;
}
