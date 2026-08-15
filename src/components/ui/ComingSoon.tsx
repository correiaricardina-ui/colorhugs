/**
 * Placeholder body for activity pages that are not built yet.
 *
 * States that plainly instead of pretending an experience exists (D-010).
 * The wording comes from the language file so the placeholder is honest in
 * every locale, not only in English.
 */
export default function ComingSoon({
  title,
  heading,
  body,
}: {
  title: string;
  heading: string;
  body: string;
}) {
  return (
    <div className="mx-auto max-w-2xl rounded-sticker bg-white/80 p-8 text-center shadow-[0_14px_36px_-24px_rgba(27,42,91,0.5)]">
      <p aria-hidden className="text-5xl">
        🎨
      </p>
      <h2 className="mt-3 font-display font-700 text-ch-ink">
        {title} {heading}
      </h2>
      <p className="mt-2 text-base text-ch-ink/70">{body}</p>
    </div>
  );
}
