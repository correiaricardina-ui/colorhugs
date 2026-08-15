import Image from "next/image";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import ChildShell from "@/components/layout/ChildShell";
import BackButton from "@/components/navigation/BackButton";
import HomeButton from "@/components/navigation/HomeButton";
import ActivityBody from "@/components/activities/ActivityBody";
import MissingArtwork from "@/components/stickers/MissingArtwork";
import { allActivityParams, getActivity } from "@/lib/sections";
import { asset } from "@/lib/site";

/**
 * Activity page.
 *
 * The route, the chrome and the way back are the same for every activity. What
 * sits below the artwork is either a built activity from the registry or the
 * honest "not made yet" placeholder — never something that implies an
 * experience exists before it does (D-010).
 */

type Params = { params: { section: string; activity: string } };

export function generateStaticParams() {
  return allActivityParams();
}

export function generateMetadata({ params }: Params): Metadata {
  const found = getActivity(params.section, params.activity);
  return found
    ? { title: `${found.activity.title} · ${found.section.title}` }
    : { title: "Not found" };
}

export default function ActivityPage({ params }: Params) {
  const found = getActivity(params.section, params.activity);
  if (!found) notFound();
  const { section, activity } = found;

  return (
    <ChildShell themeClassName={section.theme.className}>
      <div className="mx-auto w-full max-w-4xl px-4 pt-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <BackButton href={`/${section.slug}`} label={section.title} />
          <HomeButton compact />
        </div>

        <article className="mt-8 text-center">
          <div className="relative mx-auto aspect-[3/2] w-full max-w-lg">
            {activity.sticker.src ? (
              <Image
                src={asset(activity.sticker.src)}
                alt={activity.sticker.alt}
                fill
                sizes="(max-width: 640px) 90vw, 512px"
                className="object-contain"
                priority
              />
            ) : (
              <MissingArtwork label={activity.title} />
            )}
          </div>

          <ActivityBody
            section={section.slug}
            activity={activity.slug}
            fallback={{ title: activity.title, tagline: activity.tagline }}
            premium={activity.access.kind === "premium"}
          />
        </article>

        <div className="mt-10 flex flex-wrap justify-center gap-3">
          <BackButton href={`/${section.slug}`} label={section.title} />
          <HomeButton />
        </div>
      </div>
    </ChildShell>
  );
}
