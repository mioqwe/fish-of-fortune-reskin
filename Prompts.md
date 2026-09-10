# Prompts.md — coding-agent session summary

Full verbatim prompt log: `docs/session-export.txt` (exported via `opencode export`).
Step-by-step agent actions: `docs/agent-transcript.txt`.
This file is the short, reviewer-friendly version.

## 1. Initial game setup
> "start implementing this game. @AGENTS.md @Game.html @DESIGN.md"

Lane-runner rebuilt as a Three.js underwater scene + Tailwind HUD per DESIGN.md.
Single inline `<script type="module">` chosen so the game runs by double-clicking
`index.html` (file:// blocks ES-module file imports via CORS). Icons generated
locally with a Python/Pillow script (supersampled WebP), Fredoka font bundled.

## 2. Economy & upgrades
> "we should collect coins, death should decrease coins counter by exponent —
> each game should take 20 coins, initially 100; buyable shield (metal armor,
> +1 health for next mine, then breaks); ask to use energy when not enough coins"

> "energy is just currency to buy new runs — set initial health to 3 per run"

> "shop: shield / grow fish 1.1x (shield grows too, +1 health, cost x2) /
> baby fish swarm that catches coins/diamonds but not bombs"

> "red level too fast; hearts UI not updating; cheaper play-again tax;
> shield x2; swarm = 15s ability with timer ring, x2 per use"

Wallet persists in localStorage. Energy regen 1/45s. Hearts bug root-caused to a
misplaced boot block re-rendering hearts on every hit — fixed and verified with
headless screenshots.

## 3. Portals & levels
> "add portals that look like an oxygen explosion under water, at the edges of
> the screen, sliding top-to-bottom — entering teleports to another location
> (change background color + slide effect)"

> "3 portal types: purple (coins→diamonds), red (3x speed bombs, exit restores
> energy), golden (only coins, forced out by a top waterfall after N coins)"

> "all portals are the same blue bubbles" / "fix the waterfall (looks like 3
> lines)" / "portal bubbles should hug the screen edge"

Additive bubble plumes per type, camera slide + wipe transition, per-level spawn
tables, waterfall = wavy vertex-animated curtain + foam crest + foam rain.

## 4. Fish types & shop
> "generate 6 fish types; replace collection with a gem-priced fish shop; same
> size as main fish so the shield fits all; god (golden), devil, purple diamond
> + 3 of your choice"

One base model with palette/extras (halo, horns, sparkles); `applyFish()` hot-swaps
materials on the live rig; ownership/selection persisted.

## 5. UI/UX polish
> "make all text and UI elements bigger; fix title outline; keycap buttons for
> A/D/arrows; colored + outlined currency pills" / "change energy icon" /
> "remove double-tap zoom" / "add pause button" / "background music, low volume"

## 6. Backgrounds & lighting (branch try/bg-image, later merged)
> "use assets/images/background.jpeg as background; change only the top lighting
> per level" → file:// blocks WebGL image textures, solved with data-URI assets
> loaded via a classic script tag (assets/bg.js).
> "remove the 3D floor props; make the background full-screen"
> "volumetric diffuse sunbeams + caustics + per-level tint (red/yellow/white/purple)"
> "apply red-bg/yellow-bg/purp-bg images per level, preload them"
> "tint background fish silhouettes per level"

## 7. CTA end card
> "end card with animated green download button, blurred background, FoF logo,
> fish swimming around (not on top), light rays layer on top of blur; triggers:
> death, gold rush end, fish purchase"

## 8. Docs & release
> "export agent tasks via opencode export, summarize into Prompts.md; create
> README.md; zip; GitHub repo + Pages; keep loaded payload under 5 MB"

Human time on the project: **1 h 30 min**.
