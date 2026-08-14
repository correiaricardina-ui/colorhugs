import cn from "clsx";

/**
 * Responsive sticker grid.
 *
 * Desktop shows several stickers per row, tablet two to three, mobile one to
 * two with generous spacing — large targets and clear separation matter more
 * than density for the age group.
 */
export default function SectionGrid({
  children,
  columns = "auto",
  className,
}: {
  children: React.ReactNode;
  columns?: "auto" | "wide";
  className?: string;
}) {
  return (
    <div
      className={cn(
        "grid justify-items-center gap-5 sm:gap-7",
        columns === "wide"
          ? "grid-cols-1 md:grid-cols-2"
          : "grid-cols-2 md:grid-cols-3 xl:grid-cols-4",
        className,
      )}
    >
      {children}
    </div>
  );
}
