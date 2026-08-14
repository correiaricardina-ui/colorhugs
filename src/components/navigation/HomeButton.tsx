import Link from "next/link";

/** Always-available route home. Present on every child-facing page. */
export default function HomeButton({ compact = false }: { compact?: boolean }) {
  return (
    <Link
      href="/"
      className="tap-target inline-flex items-center gap-2 rounded-full bg-ch-ink px-5 py-3 font-display text-base font-600 text-white shadow-[0_6px_0_-2px_rgba(27,42,91,0.25)] transition hover:-translate-y-0.5 hover:bg-ch-ink/90 active:translate-y-0.5"
    >
      <span aria-hidden className="text-xl leading-none">
        ⌂
      </span>
      <span className={compact ? "sr-only sm:not-sr-only" : undefined}>
        Home
      </span>
    </Link>
  );
}
