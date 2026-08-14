import cn from "clsx";
import NavBar from "@/components/navigation/NavBar";
import Footer from "@/components/layout/Footer";

/**
 * Page frame for every child-facing surface.
 *
 * `themeClassName` sets the section's --sec-* custom properties, which tint
 * the background wash and the focus ring. The adult area uses its own shell.
 */
export default function ChildShell({
  themeClassName,
  children,
}: {
  themeClassName?: string;
  children: React.ReactNode;
}) {
  return (
    <div className={cn("wash flex min-h-dvh flex-col", themeClassName)}>
      <NavBar />
      <main id="main" className="flex-1 pb-10">
        {children}
      </main>
      <Footer />
    </div>
  );
}
