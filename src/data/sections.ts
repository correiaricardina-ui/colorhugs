import type { Section } from "./types";

/**
 * The ColorHugs universe, expressed as data.
 *
 * Rules encoded here:
 *  - every child-facing label is English (see brief §15);
 *  - section taglines are transcribed from each sticker's own ribbon, never
 *    written for the interface;
 *  - `access` follows the approved split: nothing is locked shut. Color &
 *    Create's library and My ColorHugs are uncapped, most activities open with
 *    their first three items Free, and Premium unlocks the rest;
 *  - `sticker.src: null` marks approved-but-missing artwork, so the interface
 *    degrades honestly instead of inventing a substitute graphic;
 *  - `status` is truthful: Phase 1 ships navigation, not activities.
 */
export const SECTIONS: Section[] = [
  // ────────────────────────────────────────────────────────────── Learning Hub
  {
    slug: "learning-hub",
    title: "Learning Hub",
    tagline: "Read • Count • Discover",
    audience: "child",
    theme: { className: "theme-learning-hub" },
    purpose:
      "Literacy and numeracy activities grounded in the science of reading and numeracy research.",
    sticker: {
      src: "/assets/stickers/sections/learning-hub.webp",
      alt: "Learning Hub: a friendly owl in a graduation cap reading a book",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/learning-hub.webp",
      alt: "Learning Hub banner",
      ratio: "wide",
    },
    activities: [
      {
        slug: "word-explorer",
        title: "Word Explorer",
        tagline: "Discover words and build vocabulary",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/learning-hub/word-explorer.webp",
          alt: "Word Explorer: an owl with a magnifying glass and alphabet letters",
          ratio: "square",
        },
      },
      {
        slug: "number-adventure",
        title: "Number Adventure",
        tagline: "Play with numbers and counting",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/learning-hub/number-adventure.webp",
          alt: "Number Adventure: colourful numbers and counting shapes",
          ratio: "square",
        },
      },
      {
        slug: "story-time",
        title: "Story Time",
        tagline: "Listen, read and imagine",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/learning-hub/story-time.webp",
          alt: "Story Time: an open storybook with friendly characters",
          ratio: "square",
        },
      },
      {
        slug: "school-challenge",
        title: "School Challenge",
        tagline: "Practise what you learn at school",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/learning-hub/school-challenge.webp",
          alt: "School Challenge: a school desk with pencils and a bright star",
          ratio: "square",
        },
      },
    ],
  },

  // ───────────────────────────────────────────────────────────────── Brain Gym
  {
    slug: "brain-gym",
    title: "Brain Gym",
    tagline: "Focus • Think • Solve",
    audience: "child",
    theme: { className: "theme-brain-gym" },
    purpose:
      "Playful cognitive training for attention, working memory, reasoning and processing speed.",
    sticker: {
      src: "/assets/stickers/sections/brain-gym.webp",
      alt: "Brain Gym: a cheerful brain character lifting weights",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/brain-gym.webp",
      alt: "Brain Gym banner",
      ratio: "wide",
    },
    activities: [
      {
        slug: "focus-mission",
        title: "Focus Mission",
        tagline: "Train your attention",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/brain-gym/focus-mission.webp",
          alt: "Focus Mission: a target and a concentrating brain character",
          ratio: "square",
        },
      },
      {
        slug: "memory-challenge",
        title: "Memory Challenge",
        tagline: "Remember more, step by step",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/brain-gym/memory-challenge.webp",
          alt: "Memory Challenge: a brain character matching picture cards",
          ratio: "square",
        },
      },
      {
        slug: "think-and-solve",
        title: "Think & Solve",
        tagline: "Puzzles that make you think",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/brain-gym/think-and-solve.webp",
          alt: "Think & Solve: puzzle pieces and a thoughtful brain character",
          ratio: "wide",
        },
      },
      {
        slug: "speedy-brain",
        title: "Speedy Brain",
        tagline: "Think fast and have fun",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/brain-gym/speedy-brain.webp",
          alt: "Speedy Brain: a brain character racing with a stopwatch",
          ratio: "square",
        },
      },
    ],
  },

  // ─────────────────────────────────────────────────────────── My Inner World
  {
    slug: "my-inner-world",
    title: "My Inner World",
    tagline: "Discover • Grow • Shine",
    audience: "child",
    theme: { className: "theme-my-inner-world" },
    purpose:
      "Psychology-informed emotional tools drawing on SEL, CBT and ACT. Psychoeducation, never therapy or diagnosis.",
    sticker: {
      src: "/assets/stickers/sections/my-inner-world.webp",
      alt: "My Inner World: a gentle character holding a glowing heart",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/my-inner-world.webp",
      alt: "My Inner World banner",
      ratio: "wide",
    },
    activities: [
      {
        slug: "how-do-i-feel",
        // Title and tagline are the English fallback; the shown text comes
        // from the language file (D-110). See src/i18n/strings.ts.
        title: "How Do I Feel?",
        tagline: "Name what you are feeling today",
        // Free with no limit (D-099). Under the sample rule the fourth time a
        // child wanted to say how she felt, the product would have told her
        // the set was finished — and an activity for naming what you feel
        // cannot cap how many times you may feel.
        access: { kind: "free" },
        status: "live",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-inner-world/how-do-i-feel.webp",
          alt: "How Do I Feel: friendly faces showing different emotions",
          ratio: "wide",
        },
      },
      {
        slug: "calm-my-body",
        title: "Calm My Body",
        tagline: "Breathe slowly and feel calmer",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-inner-world/calm-my-body.webp",
          alt: "Calm My Body: a child breathing calmly among soft clouds",
          ratio: "square",
        },
      },
      {
        slug: "my-worries",
        title: "My Worries",
        tagline: "Make big worries feel smaller",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-inner-world/my-worries.webp",
          alt: "My Worries: a child putting a worry into a friendly worry box",
          ratio: "square",
        },
      },
      {
        slug: "my-superpowers",
        title: "My Superpowers",
        tagline: "Find the strengths you already have",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-inner-world/my-superpowers.webp",
          alt: "My Superpowers: a confident child wearing a cape with stars",
          ratio: "square",
        },
      },
    ],
  },

  // ──────────────────────────────────────────────────── Kids Draw for Kids
  {
    slug: "kids-draw",
    title: "Kids Draw for Kids",
    tagline: "Drawn by Kids • Colored by Kids",
    audience: "child",
    theme: { className: "theme-kids-draw" },
    purpose:
      "Genuine child-created artwork. The system may set the mission, but the child always makes the drawing. No submission is published without review.",
    sticker: {
      src: "/assets/stickers/sections/kids-draw.webp",
      alt: "Kids Draw for Kids: children drawing together with crayons",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/kids-draw.webp",
      alt: "Kids Draw for Kids banner",
      ratio: "wide",
    },
    groups: [
      {
        id: "routes",
        title: "Start Drawing",
        description:
          "The two approved creation routes. In both, the child draws.",
      },
      {
        id: "missions",
        title: "Drawing Missions",
        description:
          "Approved progression, ordered fun-first: humour and low failure risk before instructional load.",
      },
      {
        id: "gallery",
        title: "Kids' Gallery",
        description:
          "Viewing and submitting artwork. Every submission passes automated and human review before publication.",
      },
    ],
    activities: [
      // Creating, viewing and sharing stay Free so the gallery keeps filling.
      {
        slug: "draw-your-own-idea",
        title: "Draw Your Own Idea",
        tagline: "Grab your pencils and imagine anything",
        access: { kind: "free" },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "routes",
        sticker: {
          src: "/assets/stickers/kids-draw/draw-your-own-idea.webp",
          alt: "Draw Your Own Idea: a girl drawing happily with pencils",
          ratio: "wide",
        },
      },
      {
        slug: "drawing-missions",
        title: "Drawing Missions",
        tagline: "Get a mission and draw it your way",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "routes",
        sticker: {
          src: "/assets/stickers/kids-draw/drawing-missions.webp",
          alt: "Drawing Missions: a mission card with drawing tools",
          ratio: "wide",
        },
      },
      {
        slug: "silly-and-creative",
        title: "Silly & Creative",
        tagline: "Level 1 — draw something wonderfully silly",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/silly-and-creative.webp",
          alt: "Silly and Creative: a funny mixed-up creature drawing",
          ratio: "wide",
        },
      },
      {
        slug: "add-something",
        title: "Add Something",
        tagline: "Level 2 — finish the picture your way",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/add-something.webp",
          alt: "Add Something: a half-finished drawing waiting to be completed",
          ratio: "wide",
        },
      },
      {
        slug: "follow-the-clues",
        title: "Follow the Clues",
        tagline: "Level 3 — clue by clue, build the drawing",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/follow-the-clues.webp",
          alt: "Follow the Clues: clue cards leading to a drawing",
          ratio: "wide",
        },
      },
      {
        slug: "where-does-it-go",
        title: "Where Does It Go?",
        tagline: "Level 4 — put everything in the right place",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/where-does-it-go.webp",
          alt: "Where Does It Go: objects being placed around a scene",
          ratio: "wide",
        },
      },
      {
        slug: "listen-and-draw",
        title: "Listen & Draw",
        tagline: "Level 5 — listen carefully, then draw",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/listen-and-draw.webp",
          alt: "Listen and Draw: a child listening to a mission and drawing",
          ratio: "wide",
        },
      },
      {
        slug: "memory-mission",
        title: "Memory Mission",
        tagline: "Level 6 — look, remember, draw from memory",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/memory-mission.webp",
          alt: "Memory Mission: a boy remembering a picture and drawing it",
          ratio: "wide",
        },
      },
      {
        slug: "surprise-mission",
        title: "Surprise Mission",
        tagline: "Let ColorHugs pick a mission for you",
        access: { kind: "sample", freeItems: 3 },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "missions",
        sticker: {
          src: "/assets/stickers/kids-draw/surprise-mission.webp",
          alt: "Surprise Mission: a surprise gift box full of drawing ideas",
          ratio: "wide",
        },
      },
      {
        slug: "see-kids-drawings",
        title: "See Kids' Drawings",
        tagline: "Look at drawings made by other children",
        access: { kind: "free" },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "gallery",
        sticker: {
          src: "/assets/stickers/kids-draw/see-kids-drawings.webp",
          alt: "See Kids' Drawings: a gallery wall of children's artwork",
          ratio: "square",
        },
      },
      {
        slug: "submit-my-drawing",
        title: "Submit My Drawing",
        tagline: "Send your drawing to be checked and shared",
        access: { kind: "free" },
        status: "planned",
        origin: "kids-draw-for-kids",
        group: "gallery",
        sticker: {
          src: "/assets/stickers/kids-draw/submit-my-drawing.webp",
          alt: "Submit My Drawing: a drawing being posted into a friendly mailbox",
          ratio: "wide",
        },
      },
    ],
  },

  // ─────────────────────────────────────────────────────────── Color & Create
  {
    slug: "color-and-create",
    title: "Color & Create",
    tagline: "Draw • Color • Imagine",
    audience: "child",
    theme: { className: "theme-color-and-create" },
    purpose:
      "The full colouring library is Free. Imagine & Create, the AI colouring-page tool with input and output moderation, is Premium.",
    sticker: {
      src: "/assets/stickers/sections/color-and-create.webp",
      alt: "Color & Create: crayons and a colourful drawing being coloured in",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/color-and-create.webp",
      alt: "Color & Create banner",
      ratio: "wide",
    },
    activities: [
      {
        slug: "explore-and-color",
        title: "Explore & Color",
        // Free in full: every folder of colouring pages, not a sample.
        tagline: "Pick a picture and colour it in",
        access: { kind: "free" },
        status: "live",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/color-and-create/explore-and-color.webp",
          alt: "Explore & Color: a colouring page being filled with bright colours",
          ratio: "wide",
        },
      },
      {
        slug: "imagine-and-create",
        title: "Imagine & Create",
        tagline: "Describe your idea and bring it to life",
        access: {
          kind: "premium",
          reason:
            "Every use costs money and must pass input and output moderation, so it cannot be sampled the way a fixed set of items can.",
        },
        status: "planned",
        origin: "imagine-and-create",
        sticker: {
          src: "/assets/stickers/color-and-create/imagine-and-create.webp",
          alt: "Imagine & Create: a bunny imagining a unicorn colouring page",
          ratio: "wide",
        },
      },
    ],
  },

  // ─────────────────────────────────────────────────────────── My ColorHugs
  {
    slug: "my-colorhugs",
    title: "My ColorHugs",
    tagline: "Small Steps, Big Achievements!",
    audience: "child",
    theme: { className: "theme-my-colorhugs" },
    purpose:
      "Private, positive progress. Effort and participation are rewarded; nothing is ranked publicly and nothing is ever taken away.",
    sticker: {
      src: "/assets/stickers/sections/my-colorhugs.webp",
      alt: "My ColorHugs: a personal sticker album full of rewards",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/my-colorhugs.webp",
      alt: "My ColorHugs banner",
      ratio: "wide",
    },
    activities: [
      {
        // First in the section on purpose: it is the only one of the four that
        // does something today, and it is where the child comes back to change
        // who goes with her (D-207).
        slug: "my-avatar",
        title: "Who Comes With Me",
        tagline: "Pick who goes with you around ColorHugs",
        access: { kind: "free" },
        status: "live",
        origin: "official-library",
        sticker: {
          // Artwork pending. Missing artwork is flagged, never invented
          // (D-004, rule 6): a substitute graphic quietly becomes a brand asset.
          src: null,
          alt: "Who Comes With Me",
          ratio: "square",
        },
      },
      {
        slug: "my-sticker-book",
        title: "My Sticker Book",
        tagline: "All the stickers you have collected",
        access: { kind: "free" },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-colorhugs/my-sticker-book.webp",
          alt: "My Sticker Book: an open album filled with colourful stickers",
          ratio: "wide",
        },
      },
      {
        slug: "my-progress",
        title: "My Progress",
        tagline: "See how far you have come",
        access: { kind: "free" },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-colorhugs/my-progress.webp",
          alt: "My Progress: a smiling star on a path of steps towards a flag",
          ratio: "square",
        },
      },
      {
        slug: "next-goal",
        title: "Next Goal",
        tagline: "Your next little step",
        access: { kind: "free" },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-colorhugs/next-goal.webp",
          alt: "Next Goal: a signpost pointing towards a friendly goal star",
          ratio: "square",
        },
      },
      {
        slug: "my-trophy-shelf",
        title: "My Trophy Shelf",
        tagline: "Every trophy you have earned",
        access: { kind: "free" },
        status: "planned",
        origin: "official-library",
        sticker: {
          src: "/assets/stickers/my-colorhugs/my-trophy-shelf.webp",
          alt: "My Trophy Shelf: a shelf of golden trophies and medals",
          ratio: "wide",
        },
      },
    ],
  },

  // ────────────────────────────────────────────────────────────── Community
  {
    slug: "community",
    title: "Community",
    // Taken from the artwork's own ribbon, not written for the interface.
    tagline: "Together we share, together we grow",
    audience: "child",
    theme: { className: "theme-community" },
    purpose:
      "Recognition, not competition. No leaderboards, no child-to-child messaging, no public identities.",
    sticker: {
      src: "/assets/stickers/sections/community.webp",
      alt: "Community: three cheerful children together under a Community banner",
      // Landscape artwork, declared square so the seven homepage tiles keep
      // identical dimensions. object-contain letterboxes it; nothing is cropped.
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/community.webp",
      alt: "Community banner",
      ratio: "wide",
    },
    activities: [
      {
        slug: "community-favorite",
        title: "Community Favorite",
        tagline: "This week's celebrated drawing",
        access: { kind: "free" },
        status: "planned",
        origin: "kids-draw-for-kids",
        sticker: {
          src: "/assets/stickers/community/community-favorite.webp",
          alt: "Community Favorite: a celebrated drawing surrounded by hearts and stars",
          ratio: "square",
        },
      },
    ],
  },

  // ────────────────────────────────────────────────────── Parents & Safety
  {
    slug: "parents",
    title: "Parents & Safety",
    tagline: "For grown-ups",
    audience: "adult",
    theme: { className: "theme-parents" },
    purpose:
      "The adult entry point: consent, child profiles, subscription and safety controls. Deliberately styled differently from the child environment.",
    sticker: {
      src: "/assets/stickers/sections/parents-safety.webp",
      alt: "Parents & Safety: a protective shield with a family and a padlock",
      ratio: "square",
    },
    banner: {
      src: "/assets/banners/parents-safety.webp",
      alt: "Parents & Safety banner",
      ratio: "wide",
    },
    activities: [],
  },
];

/** Sections shown on the child homepage grid, in display order. */
export const CHILD_SECTIONS = SECTIONS.filter((s) => s.audience === "child");

export const PLAN_BADGES = {
  free: {
    src: "/assets/stickers/plans/free.webp",
    alt: "Free plan badge",
    banner: "/assets/banners/free.webp",
  },
  premium: {
    src: "/assets/stickers/plans/premium.webp",
    alt: "Premium plan badge",
    banner: "/assets/banners/premium.webp",
  },
  professional: {
    src: "/assets/stickers/plans/professional.webp",
    alt: "Professional badge",
    banner: null,
  },
} as const;

export const BRAND = {
  logo: {
    src: "/assets/branding/colorhugs-logo.webp",
    alt: "ColorHugs — Create, Learn, Grow, Together",
  },
  homeBanner: {
    src: "/assets/banners/home.webp",
    alt: "ColorHugs — Create, Learn, Grow, Together",
  },
} as const;
