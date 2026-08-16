"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useLocale } from "@/i18n/LocaleProvider";
import { strings } from "@/i18n/strings";
import { asset } from "@/lib/site";

/**
 * Colouring canvas.
 *
 * **Two modes, both available on every page** (D-130). Tap-and-fill is the
 * accessible one: a four-year-old does not have the finger control for a brush,
 * and going outside the line twenty times is defeating. The brush is the free
 * one, and it is what makes it possible to colour a drawing that cannot obey
 * the six-area rule — every AI-generated page and every child's own drawing.
 * Which mode a child uses is her choice, never a consequence of how the
 * drawing happened to be made.
 *
 * **Undo is not optional.** With fill, a wrong tap is fixed by another tap.
 * With a brush, a wrong stroke crosses the drawing and there is no way back —
 * and a child who ruins her page after ten minutes does not come back.
 *
 * **Nothing is saved, and that is the design** (D-136). The activity happens in
 * the moment and does not stay — the same decision as the activity itself. The
 * download exists so a child can colour *by hand, on paper*, not so a record of
 * what she coloured on screen follows her home; the blank PDF is a different
 * thing for a different place, not an incomplete version of her painting.
 *
 * It also removes a class of problem rather than deferring it: nothing to
 * moderate, nothing to delete, nothing a parent finds.
 *
 * **Undo covers Start again**, deliberately. Ten minutes of painting is lost by
 * one accidental tap, and a confirmation box is tedious and teaches a child to
 * press yes without reading. Do not let a later change break this.
 */

/**
 * Twenty-four colours, in four rows of six.
 *
 * Twelve was too few, and the elephant showed why: a child who wants to colour
 * an elephant reaches for a grey and finds none, so she uses whatever is
 * nearest and the page becomes a colour-matching exercise instead of hers.
 *
 * More colours cost nothing in tap-target size — the grid stays six wide, so
 * the swatches keep their width and only the panel grows taller.
 *
 * The rows are composed rather than gathered:
 *   1  warm     — reds, oranges, yellows
 *   2  cool     — greens, blues, purples
 *   3  skin     — a real range, so a child can colour a person to look like
 *                 someone she knows. Four tones is the least that is honest;
 *                 one "flesh" colour tells most of the world it is not for them.
 *   4  hair, earth and neutrals, ending in white — which doubles as an eraser,
 *      since the paint layer sits on white.
 */
const PALETTE = [
  "#FFCF15", "#FFD84D", "#F2872F", "#E8302C", "#B02A26", "#FC89AE",
  "#A6E5C2", "#4FAE6A", "#2E7D52", "#7DC0F5", "#5B8DEF", "#C9ADE9",
  "#F7D9BE", "#E8B98F", "#C08552", "#8A5A3B", "#5C3A24", "#3A2418",
  "#1F1B18", "#7A6A5A", "#B0A454", "#B9BEC7", "#E4E7EC", "#FFFFFF",
];

const BRUSH_WIDTH = 22;
const MAX_HISTORY = 12;

type Mode = "fill" | "brush";

export default function ColouringCanvas({
  src,
  pdf,
  alt,
}: {
  /** Line art, transparent PNG/WebP. */
  src: string;
  /** A4 PDF of the same page. */
  pdf: string;
  alt: string;
}) {
  const { locale } = useLocale();
  const t = strings(locale).feelings;

  const paintRef = useRef<HTMLCanvasElement | null>(null);
  const lineRef = useRef<HTMLImageElement | null>(null);
  const historyRef = useRef<ImageData[]>([]);
  const drawingRef = useRef(false);
  const lastRef = useRef<{ x: number; y: number } | null>(null);

  const [ready, setReady] = useState(false);
  const [mode, setMode] = useState<Mode>("fill");
  const [colour, setColour] = useState(PALETTE[0]);
  const [canUndo, setCanUndo] = useState(false);

  // The line art is drawn on top by a separate <img>, so the paint layer never
  // has to preserve it — which keeps flood fill simple and undo cheap.
  useEffect(() => {
    const image = new Image();
    image.onload = () => {
      const canvas = paintRef.current;
      if (!canvas) return;
      canvas.width = image.naturalWidth;
      canvas.height = image.naturalHeight;
      setReady(true);
    };
    image.src = asset(src);
  }, [src]);

  const snapshot = useCallback(() => {
    const canvas = paintRef.current;
    const ctx = canvas?.getContext("2d", { willReadFrequently: true });
    if (!canvas || !ctx) return;
    historyRef.current.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
    if (historyRef.current.length > MAX_HISTORY) historyRef.current.shift();
    setCanUndo(true);
  }, []);

  function pointOn(event: React.PointerEvent<HTMLCanvasElement>) {
    const canvas = paintRef.current;
    if (!canvas) return null;
    const rect = canvas.getBoundingClientRect();
    return {
      x: Math.round(((event.clientX - rect.left) / rect.width) * canvas.width),
      y: Math.round(((event.clientY - rect.top) / rect.height) * canvas.height),
    };
  }

  /**
   * Flood fill bounded by the line art.
   *
   * The paint layer is empty where nothing has been painted, so the boundary
   * cannot come from it — it comes from the line drawing, read once into an
   * offscreen canvas. A pixel is a wall if the line art is dark there. This is
   * why every region must be sealed (D-129): an unclosed line is not a wall,
   * and the colour runs across the whole page.
   */
  function fill(x: number, y: number) {
    const canvas = paintRef.current;
    const line = lineRef.current;
    const ctx = canvas?.getContext("2d", { willReadFrequently: true });
    if (!canvas || !ctx || !line) return;

    const w = canvas.width;
    const h = canvas.height;
    if (x < 0 || y < 0 || x >= w || y >= h) return;

    const off = document.createElement("canvas");
    off.width = w;
    off.height = h;
    const offCtx = off.getContext("2d", { willReadFrequently: true });
    if (!offCtx) return;
    offCtx.drawImage(line, 0, 0, w, h);
    const lineData = offCtx.getImageData(0, 0, w, h).data;

    const target = ctx.getImageData(0, 0, w, h);
    const paint = target.data;

    const rgb = [
      parseInt(colour.slice(1, 3), 16),
      parseInt(colour.slice(3, 5), 16),
      parseInt(colour.slice(5, 7), 16),
    ];

    const isWall = (i: number) => lineData[i * 4 + 3] > 90;
    const seen = new Uint8Array(w * h);
    const stack = [y * w + x];
    if (isWall(stack[0])) return;

    while (stack.length) {
      const index = stack.pop() as number;
      if (seen[index] || isWall(index)) continue;
      seen[index] = 1;

      const p = index * 4;
      paint[p] = rgb[0];
      paint[p + 1] = rgb[1];
      paint[p + 2] = rgb[2];
      paint[p + 3] = 255;

      const px = index % w;
      if (px > 0) stack.push(index - 1);
      if (px < w - 1) stack.push(index + 1);
      if (index >= w) stack.push(index - w);
      if (index < w * h - w) stack.push(index + w);
    }

    ctx.putImageData(target, 0, 0);
  }

  function stroke(from: { x: number; y: number }, to: { x: number; y: number }) {
    const ctx = paintRef.current?.getContext("2d");
    if (!ctx) return;
    ctx.strokeStyle = colour;
    ctx.lineWidth = BRUSH_WIDTH;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.beginPath();
    ctx.moveTo(from.x, from.y);
    ctx.lineTo(to.x, to.y);
    ctx.stroke();
  }

  function onPointerDown(event: React.PointerEvent<HTMLCanvasElement>) {
    const point = pointOn(event);
    if (!point) return;
    snapshot();
    if (mode === "fill") {
      fill(point.x, point.y);
      return;
    }
    drawingRef.current = true;
    lastRef.current = point;
    event.currentTarget.setPointerCapture(event.pointerId);
    stroke(point, point);
  }

  function onPointerMove(event: React.PointerEvent<HTMLCanvasElement>) {
    if (mode !== "brush" || !drawingRef.current) return;
    const point = pointOn(event);
    const last = lastRef.current;
    if (!point || !last) return;
    stroke(last, point);
    lastRef.current = point;
  }

  function onPointerUp() {
    drawingRef.current = false;
    lastRef.current = null;
  }

  function undo() {
    const ctx = paintRef.current?.getContext("2d");
    const previous = historyRef.current.pop();
    if (!ctx || !previous) return;
    ctx.putImageData(previous, 0, 0);
    setCanUndo(historyRef.current.length > 0);
  }

  function clear() {
    const canvas = paintRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;
    snapshot();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  return (
    <div className="mx-auto w-full max-w-md">
      <div className="relative mx-auto aspect-square w-full overflow-hidden rounded-sticker bg-white">
        <canvas
          ref={paintRef}
          onPointerDown={onPointerDown}
          onPointerMove={onPointerMove}
          onPointerUp={onPointerUp}
          onPointerCancel={onPointerUp}
          className="absolute inset-0 h-full w-full touch-none"
          aria-label={alt}
        />
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          ref={lineRef}
          src={asset(src)}
          alt={alt}
          className="pointer-events-none absolute inset-0 h-full w-full select-none"
        />
      </div>

      <div className="mt-4 flex justify-center gap-2">
        {(["fill", "brush"] as Mode[]).map((option) => (
          <button
            key={option}
            type="button"
            onClick={() => setMode(option)}
            aria-pressed={mode === option}
            className={
              mode === option
                ? "min-h-[52px] rounded-full bg-ch-ink px-6 font-display font-700 text-white"
                : "min-h-[52px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/70"
            }
          >
            {option === "fill" ? t.fillMode : t.brushMode}
          </button>
        ))}
      </div>

      <ul className="mt-4 grid grid-cols-6 gap-2">
        {PALETTE.map((swatch) => (
          <li key={swatch}>
            <button
              type="button"
              onClick={() => setColour(swatch)}
              aria-pressed={colour === swatch}
              aria-label={swatch}
              style={{ backgroundColor: swatch }}
              className={
                colour === swatch
                  ? "h-14 w-full rounded-full ring-4 ring-ch-ink/70"
                  : "h-14 w-full rounded-full ring-1 ring-ch-ink/25"
              }
            />
          </li>
        ))}
      </ul>

      <div className="mt-4 flex flex-wrap justify-center gap-2">
        <button
          type="button"
          onClick={undo}
          disabled={!canUndo || !ready}
          className="min-h-[52px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80 disabled:opacity-40"
        >
          {t.undo}
        </button>
        <button
          type="button"
          onClick={clear}
          className="min-h-[52px] rounded-full bg-white/80 px-6 font-display font-600 text-ch-ink/80"
        >
          {t.clear}
        </button>
        {/*
          The other route, always offered (D-131). Some children have a printer
          and crayons and no patience for a screen, and some have the opposite.
        */}
        <a
          href={asset(pdf)}
          download
          className="inline-flex min-h-[52px] items-center rounded-full bg-[--sec-accent] px-6 font-display font-700 text-white"
        >
          {t.download}
        </a>
      </div>
    </div>
  );
}
