# Design Tokens

Source of truth: `site/src/app/site.css`.

- Canvas #0c0f10; surface #131819; raised #1a2022; line #2c3637.
- Text #f2f5f3; muted #a3afae; cyan signal #83ece4.
- Pass #bfdea1; fail #ffa18b. Status also has text/icons.
- Evidence paper #eef1ed; paper ink #142124.
- Geist variable for copy; JetBrains Mono variable for data. Local WOFF2 through next/font.
- Spacing tokens 8,16,24,32,48,64,96px; max content 1296px.
- Desktop H1 90px, wide 104px, tablet 76px, mobile 58px. Section H2 48px / mobile 35px. Use responsive breakpoints, not viewport-proportional fonts.
- No negative tracking. Buttons radius 3px, dialogs 6px. Page sections are unframed bands.
- Interaction 200ms; section reveals use the chosen cubic-bezier(.22,1,.36,1). Reduced motion removes travel and autoplay.

These are implementation tokens, not copied reference values. Future refinements must update this document.