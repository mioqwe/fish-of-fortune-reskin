# AGENTS.md — Fish of Fortune Home Assignment

## Project Overview

This project is a two-part home assignment:

1. **Part 1 — HTML Game Reskin:** Reskin a simple HTML game to fit the "Fish of Fortune" aesthetic (colorful, playful fishing/casual-game style). Include custom reskinned backgrounds, sprites, UI components, particle effects, and other visual polish.
2. **Part 2 — 3D Models (GLB):** Three game-ready, low-poly, optimized GLB models: a Fish (Fish of Fortune style), a Farm House (Klondike Adventure commercial style), and a cute humanoid Character with a Mixamo dance animation.

## Hard Technical Rules

- **No build step, no installs.** The game must run by opening `index.html` in a browser from a single folder. No npm, bundlers, or local server requirements.
- **Libraries via CDN only:**
  - **Tailwind CSS** via CDN (`https://cdn.tailwindcss.com`) — used **only** for non-gameplay UI: menus, buttons, HUD, panels, overlays.
  - **Three.js** via CDN (import map / ES modules from unpkg/jsdelivr) — used for **all 3D models, small animations, and effects**.
- **UI vs gameplay split:**
  - Menus, buttons, dialogs, HUD text → plain HTML elements styled with Tailwind classes.
  - Game world, characters, models, particles, animations → Three.js scene.
- **GLB models** are loaded with `GLTFLoader` (Three.js addons via CDN import map); the character GLB must include its Mixamo dance animation clip and play via `AnimationMixer`.

## Project Structure

```
/ (game folder)
  index.html          # single entry point
  js/                 # game logic modules (ES modules, no bundler)
  assets/             # images, audio, glb models (all compressed)
glb/
  fish/               # model + textures + prompts.txt
  farm-house/
  character/
README.txt            # workflow, sources, time log
```

## Coding Conventions

- Plain vanilla JS with ES modules (`<script type="module">`); no frameworks, no TypeScript.
- Keep all DOM-based UI markup in `index.html`; style with Tailwind utility classes inline (no custom CSS unless unavoidable).
- Three.js: one scene/renderer setup; dispose geometries/materials/textures properly; target 60fps on modest hardware.
- Keep assets compressed: images as WebP/small PNG, audio compressed, GLBs low-poly with small textures.
- Never hotlink game assets; CDN links only for libraries (Tailwind, Three.js).

## Workflow & Documentation Requirements

- Document every step of the process (prompts used, tools used, decisions made).
- Export coding-agent task transcripts/prompts into text files.
- Log **human time only** (not computer/processing time) in the README.
- Deliverables: game folder, source files folder, README with creative/technical approach, asset sources, challenges and resolutions.

## Definition of Done

- `index.html` opens locally (double-click / file://) and the game runs with the Fish of Fortune reskin.
- All 3D models render in the Three.js scene; character plays its dance animation.
- All assets compressed; game folder is fully self-contained except the two CDN library imports.
