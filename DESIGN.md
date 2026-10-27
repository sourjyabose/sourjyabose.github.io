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
- **Borders:** `3px solid #121212` across cards, buttons, badges, inputs.
- **Shadows:** Hard offset block shadows with zero blur:
  - Standard Card: `box-shadow: 4px 4px 0px #121212;`
  - Large / Hero / Featured: `box-shadow: 6px 6px 0px #121212;`
  - Hover State: `transform: translate(-2px, -2px); box-shadow: 6px 6px 0px #121212;`
  - Active Press: `transform: translate(2px, 2px); box-shadow: 1px 1px 0px #121212;`

## Image Handling
- All project and profile images sit inside framed borders with `object-fit: cover` and flexible responsive containers (`aspect-ratio` or adaptive max-heights).
- Graceful fallback: when image URL is empty or fails to load, renders an aesthetic SVG generative schematic or hardware wireframe pattern with title initials and technical metadata.
