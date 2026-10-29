# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML5, Modern CSS (Custom Properties, Grid & Flexbox, Neo-Brutalism design system), Vanilla JavaScript (Zero build step, 100% GitHub Pages native with dynamic `details.json` state engine)

## Users

Prospective engineering recruiters, technical hiring managers, hardware/firmware teams, open-source collaborators, and peers evaluating Sourjya Basu's firmware development, embedded systems engineering, computer networking protocols, and technical background.

## Product Purpose

A distinct Neo-Brutalist personal portfolio and technical showcase highlighting low-level firmware engineering (ESP32/ESP-IDF, FreeRTOS, display drivers, AVR emulator), network protocol design (CloudVPN+ raw sockets), education, certifications, and leadership. Every text string and state is dynamically data-driven via `details.json` with zero server dependencies.

## Positioning

An authentic, crafted systems engineering portfolio that merges raw hardware-level technical depth with high-impact Neo-Brutalist visual design, completely configurable via a single JSON file without needing rebuilds.

## Operating Context

Viewed across mobile, foldable (folded and unfolded states), and desktop devices.
- On mobile portrait: cards feature collapsible accordions with left-aligned headers and right-side toggle buttons, single-column profile layout, and inline read-more bio expansion.
- On mobile landscape & unfolded foldables: profile section renders in two-column grid matching desktop aesthetics while preserving read-more functionality.
- On desktop: cards render as full, structured technical sheets with two-column split layouts.
- Fast loading, responsive, zero-build vanilla stack, and fully keyboard/screen-reader accessible.

## Capabilities and Constraints

- 100% data-driven presentation via `details.json` (titles, badges, descriptions, custom tags, header strips, and button labels).
- Mobile-specific collapsible accordions for Education, Certifications, and Achievements with clean left-aligned text and right-aligned indicators.
- Device & mode detection driven by User-Agent inspection with dimensions fallback (no CSS media query decision hacks).
- Foldable detection supporting unfolded tablet-like postures for responsive layout matching.
- High-contrast day/night mode with editorial inversion switch, automated time-window switching (desktop: 11PM-5:30AM; mobile: dark system theme + 6PM-7:30AM), and dark-matte charcoal/grey accents.
- Zero npm/webpack/vite build step; deployed directly via GitHub Pages.

## Product Principles

1. **Artifact Leads First:** The technical work (firmware stacks, protocol architecture, emulators) takes center stage with tactile Neo-Brutalist presentation.
2. **Total JSON Controllability:** All copy, section titles, accordion labels, and summary tags are controlled in `details.json` without modifying markup.
3. **Responsive Separation of Concerns:** Tailored mobile touch interactions (accordions, compact badges, read-more toggles) without degrading desktop layout integrity.
4. **Precision and Accessibility:** High-contrast text, full keyboard navigation (`Tab` + `Enter`/`Space`), and screen-reader accessible attributes (`aria-expanded`, `aria-controls`).
