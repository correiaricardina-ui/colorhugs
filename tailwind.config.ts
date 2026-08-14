import type { Config } from "tailwindcss";

/**
 * Palette sampled directly from the approved ColorHugs artwork so that
 * interface chrome sits harmoniously next to the sticker illustrations.
 * These tokens describe the UI around the artwork — they never recolour it.
 */
const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ch: {
          coral: "#F4696E",
          sun: "#FFC63F",
          mint: "#7BC96F",
          sky: "#4FB3F0",
          grape: "#A98BEE",
          ink: "#1B2A5B",
          cloud: "#FFFDF8",
          cream: "#FFF6E9",
        },
      },
      fontFamily: {
        display: ["var(--font-display)", "system-ui", "sans-serif"],
        body: ["var(--font-body)", "system-ui", "sans-serif"],
      },
      fontWeight: {
        "400": "400",
        "500": "500",
        "600": "600",
        "700": "700",
        "800": "800",
      },
      borderRadius: {
        sticker: "1.75rem",
      },
      boxShadow: {
        sticker: "0 10px 0 -2px rgba(27,42,91,0.10), 0 18px 30px -12px rgba(27,42,91,0.35)",
        "sticker-hover": "0 16px 0 -2px rgba(27,42,91,0.12), 0 26px 40px -14px rgba(27,42,91,0.40)",
        pressed: "0 4px 0 -2px rgba(27,42,91,0.12), 0 8px 16px -8px rgba(27,42,91,0.35)",
      },
      keyframes: {
        "float-soft": {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-6px)" },
        },
        "pop-in": {
          "0%": { opacity: "0", transform: "scale(0.94) translateY(10px)" },
          "100%": { opacity: "1", transform: "scale(1) translateY(0)" },
        },
      },
      animation: {
        "float-soft": "float-soft 6s ease-in-out infinite",
        "pop-in": "pop-in 420ms cubic-bezier(0.22, 1, 0.36, 1) both",
      },
    },
  },
  plugins: [],
};

export default config;
