"use client";

import ComingSoon from "@/components/ui/ComingSoon";
import { activityComponent } from "@/components/activities/registry";
import { useLocale } from "@/i18n/LocaleProvider";
import { activityStrings, strings } from "@/i18n/strings";

/**
 * Everything on an activity page below the artwork.
 *
 * Client-side because the words depend on the chosen locale, which is a device
 * setting and cannot be known when the page is prerendered. The artwork, the
 * chrome and the route stay server-rendered.
 */
export default function ActivityBody({
  section,
  activity,
  fallback,
  premium,
}: {
  section: string;
  activity: string;
  fallback: { title: string; tagline: string };
  premium: boolean;
}) {
  const { locale } = useLocale();
  const t = strings(locale);
  const { title, tagline } = activityStrings(locale, section, activity, fallback);
  const Activity = activityComponent(section, activity);

  return (
    <>
      <h1 className="mt-5 font-display font-700 text-ch-ink">{title}</h1>
      <p className="mt-1 text-lg text-ch-ink/70">{tagline}</p>

      {/*
        The only plan message a child ever sees, and only where an activity
        genuinely cannot be opened. It points at a grown-up rather than at a
        price, and there is no purchase button on any child-facing screen
        (D-039).
      */}
      {premium ? (
        <p className="mt-4 font-display font-600 text-ch-ink/70">
          {t.ui.askAGrownUp}
        </p>
      ) : null}

      <div className="mt-8 text-left">
        {Activity ? (
          <Activity />
        ) : (
          <ComingSoon
            title={title}
            heading={t.ui.comingSoonTitle}
            body={t.ui.comingSoonBody}
          />
        )}
      </div>
    </>
  );
}
