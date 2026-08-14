import Link from "next/link";

/**
 * Explicit "go back one level" control.
 *
 * It is a real link to a known destination rather than a history-based
 * `router.back()`, so where it leads is predictable for a child every time.
 */
export default function BackButton({
  href,
  label,
}: {
  href: string;
  label: string;
}) {
  return (
    <Link
      href={href}
      className="tap-target inline-flex items-center gap-2 rounded-full bg-white/85 px-5 py-3 font-display text-base font-600 text-ch-ink shadow-[0_6px_0_-2px_rgba(27,42,91,0.12)] transition hover:-translate-y-0.5 hover:bg-white active:translate-y-0.5"
    >
      <span aria-hidden className="text-xl leading-none">
        ←
      </span>
      Back to {label}
    </Link>
  );
}
