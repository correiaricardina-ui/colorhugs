"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import {
  EMPTY,
  load,
  paint,
  save,
  type Area,
  type AvatarState,
} from "@/lib/avatar-store";

/**
 * One avatar state for the whole app.
 *
 * The corner, the home page and every activity read the same thing, so colour
 * earned inside an activity is on the avatar the moment she leaves it.
 *
 * `markVisited` is **the single hook every activity calls when it closes**.
 * That is the entire contract: an activity built next year adds one line and
 * is connected. It was built before the activities rather than after them for
 * exactly this reason — retrofitting it would have meant reopening every one.
 */

interface Ctx extends AvatarState {
  /** True once storage has been read; the prerendered HTML knows nothing. */
  ready: boolean;
  choose: (id: string) => void;
  markVisited: (area: Area) => void;
  /**
   * The one she had before this change, or null. **Held in memory only, never
   * saved** (D-212): this is an immediate undo for a child who tapped to see
   * what would happen, not a history. Coming back tomorrow and being offered
   * yesterday's avatar back would be the product second-guessing her choice.
   */
  previous: string | null;
  undo: () => void;
}

const AvatarContext = createContext<Ctx>({
  ...EMPTY,
  ready: false,
  choose: () => {},
  markVisited: () => {},
  previous: null,
  undo: () => {},
});

export function AvatarProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<AvatarState>(EMPTY);
  const [ready, setReady] = useState(false);
  const [previous, setPrevious] = useState<string | null>(null);

  // Read after mount, not during render: the pages are prerendered as static
  // HTML and reading storage during render would mismatch the markup.
  useEffect(() => {
    setState(load());
    setReady(true);
  }, []);

  const choose = useCallback((id: string) => {
    setState((current) => {
      if (current.avatar === id) return current;
      // Remembered so she can step straight back. Only a real change counts —
      // tapping the one she already has must not offer to undo itself.
      setPrevious(current.avatar);
      // The colour comes with her (D-208). Only the character changes.
      const next = { ...current, avatar: id };
      save(next);
      return next;
    });
  }, []);

  const undo = useCallback(() => {
    setState((current) => {
      if (!previous) return current;
      const next = { ...current, avatar: previous };
      save(next);
      return next;
    });
    setPrevious(null);
  }, [previous]);

  const markVisited = useCallback((area: Area) => {
    setState((current) => {
      const next = paint(current, area);
      if (next !== current) save(next);
      return next;
    });
  }, []);

  return (
    <AvatarContext.Provider
      value={{ ...state, ready, choose, markVisited, previous, undo }}
    >
      {children}
    </AvatarContext.Provider>
  );
}

export function useAvatar(): Ctx {
  return useContext(AvatarContext);
}
