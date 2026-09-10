# DESIGN.md — Fish of Fortune UI/UX Reskin Guidelines

Based on the official "Fish of Fortune" references (Whalo Games):
- Behance: *Fish of Fortune (Lands chapter 1)* — level/environment art
- ArtStation: *Boosters / Fish Collection* — in-game UI screens

Recreated UI mockups (HTML sources in `design/screens/`, renders in `design/screenshots/`):

| Screenshot | Source | Shows |
|---|---|---|
| `design/screenshots/01-hud.png` | `design/screens/01-hud.html` | Main gameplay HUD (top bar, level progress, build cards, CTA) |
| `design/screenshots/02-collection.png` | `design/screens/02-collection.html` | Fish Collection screen (boosters, card grid, close button) |
| `design/screenshots/03-elements.png` | `design/screens/03-elements.html` | UI elements sheet (buttons, pills, badges, bars, cards) |

---

## 1. Positioning

Layout is **portrait mobile-first** (reference frame ≈ 390×844), single column, thumb-driven. UI floats over the 3D world, never covering its center.

### Top HUD bar (always visible)
- Full-width row, pinned to the **top edge** with ~10–14 px safe-area inset.
- Order, left → right:
  1. **Level badge** — organic blob shape with level number, anchored top-left.
  2. **Coin pill** (widest currency, takes remaining flex space).
  3. **Gem pill**.
  4. **Energy pill** (narrower, shows `current/max`).
  5. **Hamburger menu button** — rounded square, anchored top-right.
- Currency icons **overlap the left edge** of their white pills (−4…−6 px); a green `+` badge sits on each pill's top-right corner (opens the shop).

### Level progress
- Centered horizontally, directly **below the top bar** (~70 px from top).
- Small all-caps label above the bar; reward (gem amount + chest icon) sits to the **right** of the bar.

### Bottom zone (main screen)
- **Build/shop cards**: row of 3 white cards, centered, ~110 px above the bottom edge.
- **Primary CTA** (big green round "next/play" arrow): bottom-center, ~26 px from bottom. The CTA is the largest tappable element — always bottom-center under the thumb.
- **Close button** on overlay screens (red round X): bottom-center, same slot as the CTA, overlapping panel content.

### Overlay screens (e.g. Fish Collection)
- Content lives on a **colored panel** (sand/yellow) whose top edge is a **wave/scallop shape**, starting ~150 px from the top; the ocean-blue background and top HUD bar stay visible above it.
- **Screen title** is centered on the blue area, overlapping the panel's wave edge.
- **Section headers** ("Boosters", "Collection", "To be collected") are centered brown text flanked by two thin white horizontal rules.
- Boosters: horizontal row of 3 glass bowls, each with a timer pill centered beneath.
- Collection: **3-column card grid**, 10 px gutters, vertically scrollable; locked cards are greyed silhouettes in a separate "To be collected" section.

### Placement rules
- Interactive elements: min ~44 px touch target, ≥7 px gaps.
- Nothing interactive in the vertical middle of the screen — that space belongs to the 3D scene.
- Depth order: 3D world → decorative waves → HUD pills/cards → modal panels → close/CTA buttons.

---

## 2. Coloring

Cheerful tropical palette: **cyan water + sandy yellow + warm accents**, always with white outlines and a darker "3D" bottom edge (fake extrusion via `box-shadow: 0 Npx 0 <darker>`).

### Core palette

| Role | Color | Hex |
|---|---|---|
| Water background (top → bottom) | Sky cyan → ocean blue | `#3FC6F0` → `#25AEE8` → `#1B9CD8` |
| Panel / sand | Cream → sand → gold | `#FFE9A8` → `#FFD86B` → `#FFC93C` |
| Primary action (CTA, confirm, prices) | Leaf green gradient, dark-green base | `#8FE05C` → `#4CAF2E`, base `#37901D` |
| Secondary action (menu, spin) | Orange gradient, burnt base | `#FFB53E` → `#FF8A3D`, base `#D96A1E` |
| Neutral action | Blue gradient | `#5FD3F7` → `#2E9BDF`, base `#1B76B0` |
| Destructive / close | Coral red gradient | `#FF7B7B` → `#E23A3A`, base `#B02020` |
| Accent (titles, shop) | Bubblegum pink | `#FF8FC7` → `#F25CA2`, base `#C93B82` |
| Coins | Gold | `#FFE28A` → `#FFC93C` → `#F0A420`, outline `#E08E00` |
| Gems | Purple | `#E08CFF` → `#B05CE3` → `#7E2FBF` |
| Energy | Orange bolt on amber | `#FFB03A` → `#F08A1D`, outline `#C96A00` |
| Progress track | Deep sea blue | `#1668A8` |
| Progress fill | Yellow gradient | `#FFE066` → `#FFC93C` → `#F5A623` |
| Timer pill | Dark navy | `#3B3B6B` |
| Text on pills/cards | Dark brown | `#4A3B2A` |
| Section headers on sand | Warm brown | `#8A5A1E` |
| Card surface | White | `#FFFFFF` |
| Locked / disabled | Grey | `#8A8F9E`, `#9AA0B0`, `#B9BDC9` |

### Coloring rules
- **Every button/panel has a white 3–4 px border** and a solid darker bottom edge (4–6 px) for the squishy toy look.
- Gradients run **light at top → saturated at bottom** (lit from above).
- Text is white with a soft dark shadow (`0 2px 0 rgba(...)`) on colored surfaces; dark brown on white surfaces.
- Screen titles: pink fill, **white stroke**, darker pink drop shadow.
- Locked content is fully desaturated greyscale — color = affordance.
- Gold stars `#FFC93C` with `#E08E00` shadow; currency green `+` badges always with white ring.

---

## 3. UI Elements

All elements are rounded, chunky, outlined — "inflatable toy" styling. Font: rounded geometric bold (reference uses a Baloo/Fredoka-style face).

### Buttons
- **Rectangular button**: `border-radius` 16–18 px, white 3 px border, colored gradient, 5 px darker base shadow, white bold uppercase label with drop shadow. Variants: green (primary), orange (secondary), blue (neutral), pink (shop/promo).
- **Circle icon buttons** (Ø 56–74 px): same treatment, single white glyph (▶ play/next, ✕ close).
- **Hamburger menu**: orange rounded square, three white bars.
- **Green `+` badge**: 19–22 px circle on currency pills — opens purchase flow.

### Pills & badges
- **Currency pill**: white capsule (h 34 px, radius 20 px), currency icon overlapping left edge, brown semibold number, green `+` top-right.
- **Level badge**: irregular blob (asymmetric border-radius), blue fill, white border, rotated −6°, white level number.
- **Timer pill**: dark navy capsule, white monospace-ish `HH:MM:SS`, sits under booster bowls.
- **"NEW" ribbon**: red gradient tag on card's top-right corner, slightly rotated, notched corner.

### Progress
- **Level progress bar**: deep-blue track with white 3 px border, yellow gradient fill, centered white % label; reward preview (gem + chest) to its right.
- **Card progress**: split capsule — white segment with brown `current/max` text + solid orange segment; blue circle level badge on its left.

### Cards
- **Build card (HUD)**: white rounded card (radius 20 px) with item thumbnail on light-blue tile + green price tag (coin icon + amount); purchased state swaps price for a white checkmark on green.
- **Collection card**: white card → blue-gradient image tile → gold star rating (1–3) → footer with level badge + split progress capsule. States: normal, **NEW** (red ribbon), **locked** (grey silhouette, `?` badge).

### Panels & structure
- **Overlay panel**: solid warm-yellow sheet with scalloped/wave top edge separating it from the blue header zone.
- **Section header**: centered brown bold text + thin white rules on both sides.
- **Booster bowl**: white/glass dome with purple liquid at the bottom, character inside, timer pill below.

### Feedback & motion (for implementation)
- Buttons squish on press (scale 0.92–0.95 + base shadow collapse).
- Rewards: particle burst (coins/gems), card flip on unlock.
- Booster receive/expire: pop-in scale animation, dissolve on use.
- Waves/water idle animation behind HUD; CTA gentle idle pulse.

---

## Asset / implementation notes for this project
- These mockups are static HTML+CSS (`design/screens/*.html`) rendered at 390×844 with headless Chrome — they are **design targets**, not game code.
- In the game, rebuild these as Tailwind-styled DOM overlays (per AGENTS.md: DOM for UI, Three.js for world); replace emoji placeholders with compressed WebP sprite icons in `assets/`.
- Reference palette hexes above are the source of truth for Tailwind config / inline classes.
