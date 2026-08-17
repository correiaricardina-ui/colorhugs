"use client";

import Image from "next/image";
import cn from "clsx";
import AVATARS from "@/data/avatars.json";
import { AREAS, type Area } from "@/lib/avatar-store";
import { asset } from "@/lib/site";

/**
 * The child on the screen.
 *
 * Line art with one tinted silhouette stacked beneath it per painted area —
 * the same mechanism as the body map (D-107), and it needs no canvas, no
 * script to hold a colour, and no second file per state.
 *
 * **The colour goes underneath the line art, never inside it.** The artwork is
 * transparent everywhere except the line, so using its alpha as a mask over a
 * filled canvas throws the fill away and returns a blank avatar. That mistake
 * was made once and is recorded in `scripts/prepare-avatars.py`.
 *
 * **Each character has its own palette** (D-211), not the section accents. A
 * fox painted in seven section colours is a harlequin, and the avatar's whole
 * job is to be something a child likes looking at.
 *
 * No white die-cut rim: the rim means collectable, and an avatar is not
 * collected (D-077, D-083).
 */

export interface AvatarEntry {
  line: string;
  width: number;
  height: number;
  masks: Record<string, string>;
  /** This character's own colours, one per area (D-211). */
  palette: Record<string, string>;
}

export const AVATAR_DATA = AVATARS as Record<string, AvatarEntry>;
export const AVATAR_IDS = Object.keys(AVATAR_DATA);

export default function Avatar({
  id,
  painted = [],
  className,
  sizes = "200px",
  priority = false,
}: {
  id: string;
  painted?: Area[];
  className?: string;
  sizes?: string;
  priority?: boolean;
}) {
  const entry = AVATAR_DATA[id];
  if (!entry) return null;

  return (
    <span
      className={cn("relative block", className)}
      style={{ aspectRatio: `${entry.width} / ${entry.height}` }}
    >
      {AREAS.map((area) => {
        const mask = entry.masks[area];
        if (!mask || !painted.includes(area)) return null;
        return (
          <span
            key={area}
            aria-hidden
            className="pointer-events-none absolute inset-0 transition-opacity duration-500 motion-reduce:transition-none"
            style={{
              backgroundColor: entry.palette[area],
              WebkitMaskImage: `url(${asset(mask)})`,
              maskImage: `url(${asset(mask)})`,
              WebkitMaskSize: "contain",
              maskSize: "contain",
              WebkitMaskRepeat: "no-repeat",
              maskRepeat: "no-repeat",
              WebkitMaskPosition: "center",
              maskPosition: "center",
            }}
          />
        );
      })}

      <Image
        src={asset(entry.line)}
        alt=""
        fill
        sizes={sizes}
        className="pointer-events-none object-contain"
        priority={priority}
      />
    </span>
  );
}
