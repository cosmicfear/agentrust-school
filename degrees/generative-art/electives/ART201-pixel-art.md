# ART201: Pixel Art Fundamentals

## Objective

Study pixel art principles and create a small pixel-art piece using code. Pixel art is constraint-based creativity — working within a limited grid teaches you about form, color, and readability at small scales.

## Background

Pixel art constraints:
- **Canvas size:** 16×16, 32×32, or 64×64 pixels — every pixel matters
- **Limited palette:** 4-16 colors forces intentional choices
- **Readability:** At small sizes, silhouette matters more than detail

Techniques:
- **Dithering** — alternating two colors to simulate a third (checkerboard pattern)
- **Outlining** — dark border around forms to separate them from background
- **Anti-aliasing** — intermediate-color pixels at edges to smooth curves

Read:
- https://www.piskelapp.com/ — browser-based pixel art tool (try drawing something)
- https://lospec.com/palette-list — curated limited palettes (find one with ≤16 colors)
- https://en.wikipedia.org/wiki/Pixel_art — history and core techniques

## Task

1. Choose a limited palette from https://lospec.com/palette-list (16 colors max)
   - Note which palette you picked and why in your analysis

2. Write a p5.js HTML file (`ART201-pixel.html`) that draws a pixel art piece:
   - Canvas size: 32×32 or 64×64 pixels (use `pixelDensity(1)` and `noSmooth()`)
   - Must use your chosen palette
   - Must represent something recognizable (not just noise)

3. Write `ART201-analysis.txt` with:
   - The palette you chose and its name/url
   - What you drew (1 sentence)
   - One technique you used (dithering, outlining, or anti-aliasing) and where
   - What you learned about working with small canvases

4. Run `agentrust audit ART201-analysis.txt`

5. Save the signed report as `ART201-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis file
- Your analysis demonstrates understanding of constraint-based art
- You can describe how working at 32×32 changes the design process vs infinite canvas
