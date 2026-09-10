================================================================================
FISH OF FORTUNE — HOME ASSIGNMENT README
================================================================================

PART 1 — HTML GAME RESKIN ("Lucky Catch" lane runner)
-----------------------------------------------------

HOW TO RUN
  Double-click index.html (works over file://) — no build step, no installs,
  no local server. Internet is needed only for the two allowed CDN libraries
  (Tailwind CSS, Three.js). Everything else is local and self-contained.

GAMEPLAY
  Reskin of the provided "Lane Runner" (original kept as Game.html):
  - INFINITE mode (no levels): score = coins collected this run; difficulty
    ramps forever (spawn rate + fall speed scale with run time).
  - You are a cute orange fish swimming between 5 current lanes.
  - Catch gold coins (+1) and purple gems (+10 coins, +1 gem).
  - Dodge the sea urchins — each hit costs 1 heart (3 per run).
  - PORTALS: churning "oxygen explosion" bubble plumes slide top-to-bottom
    along the left/right screen edges. Dodge them, or swim in to WARP:
    camera slide-out + bubble wipe + palette swap, then slide back in with
    a fresh field and brief invulnerability. Three colored portal types:
      * PURPLE portal -> purple level: coins replaced by diamonds (gems).
      * RED portal -> red level: 3x fall speed, no coins/gems, only bombs
        (urchins) at an increased rate. Exiting the red level restores ALL
        energy (3/3).
      * GOLD portal -> golden level: only coins spawn. After collecting
        15 coins a waterfall flushes from the top and force-warps you out.
    Inside special levels a white "home" portal returns to the base ocean.
  - Controls: Arrow keys / A,D / tap left-right half of the screen (touch).
  - FIRST-RUN GUIDE (in-memory flags, reset on page reload):
    a) tap-hand animation floats over the playfield for ~4 s at the start
       of the first run (mobile players learn tap-to-move);
    b) the first portal spawn pauses the game and shows the PORTALS modal
       (3 real screenshots, rounded corners: Diamond rush / Die or refresh /
       Gold rush) with a PLAY button to resume.

  ECONOMY (persistent wallet, saved to localStorage):
  - Player starts with 100 coins; every game costs 10 coins to play.
  - Energy is a META CURRENCY for buying runs only (not health). Not enough
    coins? A dialog offers to pay 1 energy instead. Out of both -> wait for
    energy regen (1 energy / 45 s, max 3). Energy pill "+" buys 1 energy for
    10 gems; the dialog also has a small green +1 energy top-up button.
  - HEALTH is per-run: the fish starts every run with 3 + growLevel hearts
    (heart row under the top bar, hearts grey out on hits). 0 = game over.
  - Urchin hits tax your coins per run: 2, 4, 8 (2*2^n),
    shown as floating red "-N" under the coin pill; total shown on the
    game-over panel as "Urchin tax".
  - SHOP (build cards, bought with wallet coins):
      * SHIELD (25, x2 per purchase, persisted): metal armor (helmet dome +
        bands + rivets). The next urchin hit breaks the shield (clang, grey
        burst) instead of costing health/coins. Re-buyable. Armor is a child
        of the player rig, so it scales with growth.
      * GROW (30, x2 per level, max 5, persisted): fish grows 1.1x per
        level, max health +1 per level; buying mid-run heals +1; catch
        radius +0.05/level.
      * BABY SWARM (50, x2 per use, persisted): ACTIVE ABILITY — 3 baby fish
        orbit the main fish for 15 SECONDS (countdown ring + seconds shown
        on the card) and auto-collect coins/gems they touch — never bombs.
  - FISH SHOP (hamburger): 6 fish types priced in GEMS — Lucky (free
    starter), Bubble 20, Toxic 35, Diamond 60 (sparkles), Devil 80 (horns),
    God 150 (golden, halo). All fish are recolors/extras of the SAME base
    model/size, so the shield armor fits every fish. Buying selects the
    fish; owned fish can be re-selected. Owned/selection persist.
  - Green "+" badges on coin/gem pills give small top-ups.

CREATIVE APPROACH
  Rebuilt the flat 2D canvas game as a 3D underwater diorama that follows
  DESIGN.md (recreated from the official Fish of Fortune references):
  - Portrait mobile-first frame (~390x844), thumb-driven layout.
  - DOM/Tailwind for all UI: top HUD bar (level blob, coin/gem/energy pills
    with overlapping icons and green + badges, orange hamburger), level
    progress bar with gem+chest reward, 3 build/shop cards, big green CTA,
    Fish Collection overlay with scalloped wave panel edge, booster bowls
    with timer pills, 3-column collection grid, locked "To be collected"
    cards, red round close button.
  - Three.js for the whole game world: gradient water, light rays, drifting
    fish silhouettes, swaying seaweed, corals, rocks, bubbles, a farm house
    on a floating sand island and a dancing character on a floating rock.
  - Palette, squishy "inflatable toy" styling (white 3px borders, darker
    solid bottom edge, light-to-saturated gradients) per DESIGN.md.
  - Feedback: collect particle bursts, damage red flash + screen shake +
    i-frames blink, button squish, CTA idle pulse, pop-in panels.
  - Audio: zero-asset WebAudio — synth SFX (coin, gem, hit, clang, warp,
    click) + generative background music (slow pentatonic arpeggio over a
    soft bass progression, ~92 BPM, master gain 0.05 = low volume,
    starts on first user gesture per browser autoplay rules).

TECHNICAL APPROACH
  - Single index.html, one inline <script type="module">.
    DECISION: AGENTS.md asks for js/ ES-module files AND for the game to run
    by double-click (file://). Browsers block file:// module imports and
    fetch() of local files (CORS), so the module was inlined into index.html
    to satisfy the Definition of Done. Code is organized in labeled sections.
  - Import map pins three@0.160.0 (jsdelivr); GLTFLoader via three/addons.
  - GLB integration: the loader tries glb/fish/fish.glb,
    glb/farm-house/farm-house.glb, glb/character/character.glb. On file://
    (or while the Part-2 GLBs don't exist yet) loading fails gracefully and
    procedural low-poly fallbacks are used, so the game always runs. When the
    GLBs exist (served over http), they replace the fallbacks; the character's
    Mixamo clip plays via AnimationMixer (animations[0]).
  - Performance: shared/cached geometries & materials, object pools for
    falling items, one ambient-bubble Points system, pooled particle bursts
    with proper dispose(), DPR capped at 2.

ASSETS & SOURCES (all local, compressed)
  - assets/icons/*.webp — 21 icons (coin, gem, bolt, chest, stars, lock,
    6 collection creatures, 3 boosters, 3 build items, locked silhouette),
    generated programmatically with a Python/Pillow script (4x supersampled,
    96px WebP q82) — ~44 KB total. No external art, no hotlinks.
  - assets/fonts/fredoka.woff2 — Fredoka variable font (Google Fonts,
    OFL license), 30 KB, bundled locally per the no-hotlink rule.
  - Libraries via CDN (allowed): Tailwind (cdn.tailwindcss.com),
    Three.js 0.160.0 (cdn.jsdelivr.net).
  - Design targets: design/screens/*.html + design/screenshots/*.png.

CHALLENGES & RESOLUTIONS
  1. file:// CORS blocks ES-module files and GLB fetch -> inlined the module;
     GLTFLoader wrapped with procedural fallbacks.
  2. Player fish was occluded by the bottom build cards -> raised the catch
     line and verified layout iteratively with headless-Chrome screenshots
     at 390x844 (hash test hooks: index.html#play / #collection / #win / #over).
  3. Fredoka has no arrow glyphs -> rewrote the controls hint in words.
  4. Farm house/character were buried behind UI -> placed them on cartoon
     floating islands in the mid-background (on-brand for Fish of Fortune).

WORKFLOW / TOOLS
  - VS Code + opencode coding agent (model: kimi-for-coding/k3) for all code.
  - Python 3 + Pillow for icon generation.
  - Headless Chrome (google-chrome-stable --headless=new --screenshot) for
    visual verification of every screen.
  - Agent task transcript: docs/agent-transcript.txt

HUMAN TIME LOG (human time only, not computer/processing time)
  - Art direction & DESIGN.md study ............ ~20 min
  - Icon generator script & icon review ........ ~25 min
  - Game/HUD implementation guidance & review .. ~45 min
  - Visual QA iterations (screenshots, fixes) .. ~25 min
  - Documentation .............................. ~15 min
  Total human time: ~2 h 10 min

PART 2 — 3D MODELS (GLB)
------------------------
  Placeholder scaffolding prepared: glb/fish, glb/farm-house, glb/character,
  each with prompts.txt containing the exact gen-AI prompts, conversion and
  optimization specs, and integration notes. The game already consumes these
  paths and hot-swaps the procedural placeholders when the GLBs are present.

FOLDER STRUCTURE
  index.html            reskinned game (single entry point)
  Game.html             original provided game (untouched, source reference)
  assets/icons/*.webp   generated UI sprites
  assets/fonts/         bundled Fredoka font
  design/               UI mockups + screenshots (design targets)
  glb/<model>/          Part-2 model folders + prompts.txt
  docs/                 agent transcript
  AGENTS.md / DESIGN.md project rules and design guidelines
================================================================================
