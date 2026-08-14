import Image from "next/image";
import type { Metadata } from "next";
import AdultShell from "@/components/layout/AdultShell";
import { PLAN_BADGES, SECTIONS } from "@/data/sections";
import { asset } from "@/lib/site";

export const metadata: Metadata = {
  title: "Parents & Safety",
  description:
    "How ColorHugs protects children: account model, moderation, privacy and subscription.",
};

/**
 * Adult entry point.
 *
 * Everything below describes commitments already agreed for ColorHugs. Where
 * a control is not built yet, it says so rather than implying protection that
 * does not exist. Authentication, consent capture and parental controls are
 * scheduled for a later phase and must be validated legally before launch.
 */

const COMMITMENTS = [
  {
    title: "An adult account owns everything",
    body: "Children use a profile inside a verified adult account. Consent, subscription and safety settings stay with the grown-up, and adult account details are never shown to the child.",
  },
  {
    title: "No child uses ColorHugs anonymously",
    body: "Free is a subscription level, not anonymity. Interactive features always require an authorised child profile.",
  },
  {
    title: "No child-to-child messaging",
    body: "There are no private messages, no open chat, no contact exchange and no unmoderated comments anywhere in ColorHugs.",
  },
  {
    title: "Nothing is published without review",
    body: "Drawings submitted by children pass automated checks and human review before anyone else can see them. Publishing artwork never publishes a child's identity.",
  },
  {
    title: "Recognition, not competition",
    body: "Community Favorite celebrates a drawing each week. There are no public leaderboards, no punitive streaks, and no achievement is ever taken away.",
  },
  {
    title: "Psychology-informed, not clinical",
    body: "My Inner World offers psychoeducation drawn from developmental psychology, SEL, CBT and ACT. ColorHugs does not diagnose, assess or replace a psychologist.",
  },
] as const;

const parents = SECTIONS.find((s) => s.slug === "parents")!;

const PENDING = [
  "Adult account creation, verification and sign-in",
  "Verifiable parental consent, validated per jurisdiction",
  "Child profile creation, avatars and pseudonyms",
  "Parental controls, activity visibility and time settings",
  "Subscription management",
  "Data access, export and deletion requests",
] as const;

export default function ParentsPage() {
  return (
    <AdultShell>
      <div className="mx-auto w-full max-w-4xl px-4 py-10">
        {/*
          The approved section banner. It is deliberately capped in width and
          kept above quiet, dense type — the adult area borrows the brand mark,
          not the child interface.
        */}
        <div className="overflow-hidden rounded-xl border border-ch-ink/10 bg-white">
          <div className="relative aspect-[1568/644] w-full">
            <Image
              src={asset(parents.banner.src!)}
              alt={parents.banner.alt}
              fill
              sizes="(max-width: 896px) 100vw, 896px"
              className="object-cover"
              priority
            />
          </div>
        </div>

        <h1 className="mt-8 font-display font-700 text-ch-ink">Parents &amp; Safety</h1>
        <p className="mt-3 max-w-2xl text-lg leading-relaxed text-ch-ink/75">
          ColorHugs is built so that children want to use it and parents can
          trust it. This page explains how that works and what is still being
          built.
        </p>

        <section aria-labelledby="commitments" className="mt-10">
          <h2 id="commitments" className="font-display font-700 text-ch-ink">
            Our safety commitments
          </h2>
          <dl className="mt-5 grid gap-4 sm:grid-cols-2">
            {COMMITMENTS.map((item) => (
              <div
                key={item.title}
                className="rounded-xl border border-ch-ink/10 bg-white p-5"
              >
                <dt className="font-display text-lg font-600 text-ch-ink">
                  {item.title}
                </dt>
                <dd className="mt-1.5 text-[0.95rem] leading-relaxed text-ch-ink/75">
                  {item.body}
                </dd>
              </div>
            ))}
          </dl>
        </section>

        <section aria-labelledby="plans" className="mt-12">
          <h2 id="plans" className="font-display font-700 text-ch-ink">
            Free and Premium
          </h2>
          <p className="mt-2 max-w-2xl text-[0.95rem] leading-relaxed text-ch-ink/75">
            <strong className="font-700">Nothing is locked shut on Free.</strong>{" "}
            Your child opens every activity and plays; most hold their first
            three items free, and the rest need Premium. They never meet a
            closed door on the way in, and they never see a price or a payment
            button — when a set runs out, ColorHugs asks them to talk to you.
          </p>
          <p className="mt-2 max-w-2xl text-[0.95rem] leading-relaxed text-ch-ink/75">
            Uncapped on Free: the whole Color &amp; Create colouring library,
            drawing and sharing in Kids Draw for Kids, and all of My ColorHugs.
            Progress, stickers and trophies are always free — what your child
            earned is theirs, whatever plan you are on.
          </p>
          <p className="mt-2 max-w-2xl text-[0.95rem] leading-relaxed text-ch-ink/75">
            Premium will be offered monthly or yearly, with a weekly option, and
            every price will show what it works out to per month. Prices are not
            yet set.
          </p>
          <div className="mt-5 grid gap-4 sm:grid-cols-2">
            {(["free", "premium"] as const).map((plan) => (
              <div
                key={plan}
                className="overflow-hidden rounded-xl border border-ch-ink/10 bg-white"
              >
                <div className="relative aspect-[1568/644] w-full bg-ch-cream">
                  <Image
                    src={asset(PLAN_BADGES[plan].banner)}
                    alt={`${plan === "free" ? "Free" : "Premium"} plan banner`}
                    fill
                    sizes="(max-width: 640px) 100vw, 400px"
                    className="object-cover"
                  />
                </div>
                <p className="p-4 text-sm text-ch-ink/70">
                  {plan === "free"
                    ? "Every activity opens. The whole colouring library, drawing and sharing, and the first three items of most activities."
                    : "Everything in ColorHugs, including Imagine & Create and the full Drawing Missions progression."}
                </p>
              </div>
            ))}
          </div>
        </section>

        <section aria-labelledby="pending" className="mt-12">
          <h2 id="pending" className="font-display font-700 text-ch-ink">
            Not built yet
          </h2>
          <p className="mt-2 text-[0.95rem] text-ch-ink/75">
            This release is the foundation of the ColorHugs website. The
            following are planned and must pass legal and privacy validation
            before launch:
          </p>
          <ul className="mt-4 space-y-2">
            {PENDING.map((item) => (
              <li
                key={item}
                className="flex items-start gap-2.5 text-[0.95rem] text-ch-ink/75"
              >
                <span aria-hidden className="mt-1 text-ch-ink/35">
                  &#9723;
                </span>
                {item}
              </li>
            ))}
          </ul>
        </section>
      </div>
    </AdultShell>
  );
}
