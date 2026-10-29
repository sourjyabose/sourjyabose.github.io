# DESIGN.md

# Visual World: Neo-Brutalist Engineering Terminal & Physical Print

<!-- impeccable:design-schema 1 -->

## Direction
A committed Neo-Brutalist aesthetic tuned for an Embedded Firmware Engineer and Systems Builder. High visual impact with solid tactile physical cues, raw black borders, deliberate high-contrast surfaces, flat zero-blur block shadows, bold mechanical typography, and responsive modular cards.

## Color Palette
- **Canvas Base:** `#FFFDF5` (Warm off-white archival paper)
- **Contrast Black:** `#121212` (Dense pitch black for borders, solid ink, and drop shadows)
- **Primary Accent (High Voltage Yellow):** `#FFE600` (Punchy highlighter yellow for badges, tags, active states)
- **Secondary Accent (Cyber Cyan):** `#00F0FF` (Sharp electric cyan for secondary highlights and metadata)
- **Tertiary Accent (Terminal Lime):** `#22C55E` (High-visibility system status / live signals)
- **Accent Coral / Orange:** `#FF5A36` (Urgent or critical hardware highlights)
- **Surface Cards:** `#FFFFFF` with heavy `3px` solid black borders and `4px 4px 0px #121212` box-shadows.

## Typography
- **Headings & Display:** `Space Grotesk`, `Cabinet Grotesk`, or system geometric sans with tight tracking (`-0.03em`), bold uppercase impact, clean and punchy.
- **Body:** `Inter`, system sans-serif (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`), clear line height `1.6`, readable at 16px.
- **Code & Metadata:** `Space Mono`, `JetBrains Mono`, `Fira Code`, or monospace for memory addresses, commit tags, registers, and technical specs.

## Elevation & Depth (Neo-Brutalist System)
- **Borders:** `3px solid var(--border-color)` across cards, buttons, badges, inputs.
- **Shadows:** Hard offset block shadows with zero blur:
  - Standard Card: `box-shadow: 4px 4px 0px var(--shadow-color);`
  - Large / Hero / Featured: `box-shadow: 6px 6px 0px var(--shadow-color);`
  - Hover State: `transform: translate(-2px, -2px); box-shadow: 6px 6px 0px var(--shadow-color);`
  - Active Press: `transform: translate(2px, 2px); box-shadow: 1px 1px 0px var(--shadow-color);`
  - Night Mode: shadows use deep matte architectural charcoal grey (`#121418`) to preserve high-contrast brutalist depth on dark canvases.

## Theme & Editorial Affordances
- **Day/Night Inversion:** Minimal editorial inversion dot (black square with white center dot in day mode, white square with black center dot in night mode) with static button dimensions and text placement.
- **Footer Surface:** Dark matte charcoal grey (`#14171C`) with architectural borders (`#2D333F`) in night mode.

## Image Handling
- All project and profile images sit inside framed borders with `object-fit: cover` and flexible responsive containers (`aspect-ratio` or adaptive max-heights).
- Graceful fallback: when image URL is empty or fails to load, renders an aesthetic SVG generative schematic or hardware wireframe pattern with title initials and technical metadata.
