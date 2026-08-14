import Link from "next/link";
import ChildShell from "@/components/layout/ChildShell";

export default function NotFound() {
  return (
    <ChildShell>
      <div className="mx-auto max-w-xl px-4 py-16 text-center">
        <p aria-hidden className="text-6xl">
          🧭
        </p>
        <h1 className="mt-4 font-display font-700 text-ch-ink">
          This page went for a walk
        </h1>
        <p className="mt-2 text-lg text-ch-ink/70">
          Let&apos;s go back to the start.
        </p>
        <Link
          href="/"
          className="tap-target mt-8 inline-flex items-center gap-2 rounded-full bg-ch-ink px-7 py-4 font-display text-lg font-600 text-white shadow-[0_6px_0_-2px_rgba(27,42,91,0.25)] transition hover:-translate-y-0.5"
        >
          Take me home
        </Link>
      </div>
    </ChildShell>
  );
}
