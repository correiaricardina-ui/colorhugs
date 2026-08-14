/**
 * Placeholder body for activity pages.
 *
 * Phase 1 delivers the foundation, not the activities. This states that
 * plainly instead of pretending an experience exists.
 */
export default function ComingSoon({ title }: { title: string }) {
  return (
    <div className="mx-auto max-w-2xl rounded-sticker bg-white/80 p-8 text-center shadow-[0_14px_36px_-24px_rgba(27,42,91,0.5)]">
      <p aria-hidden className="text-5xl">
        🎨
      </p>
      <h2 className="mt-3 font-display font-700 text-ch-ink">
        {title} is being made
      </h2>
      <p className="mt-2 text-base text-ch-ink/70">
        We are still building this one. Come back soon!
      </p>
    </div>
  );
}
