# ART102: Color Theory & Palettes

## Objective

Study color theory and build a cohesive palette. Great generative art starts with intentional color choices, not random hex codes.

## Background

Color theory governs how colors interact. Three core concepts:

- **Hue** — the color itself (red, blue, 270° on the wheel)
- **Saturation** — intensity (pure vs muted)
- **Value/Brightness** — lightness to darkness

Common palette types:
- **Complementary** — opposite on the wheel (blue/orange) → high contrast
- **Analogous** — adjacent on the wheel (blue/teal/green) → harmonious
- **Triadic** — evenly spaced (red/yellow/blue) → vibrant but balanced

Read:
- https://coolors.co/ — explore palettes (hunt for "generate" button)
- https://p5js.org/reference/#/p5/color — p5.js color functions (color(), lerpColor(), colorMode(HSB))

HSB mode is better than RGB for art because it lets you vary hue in a way that stays vibrant.

## Task

1. Use a palette tool (https://coolors.co/ or similar) to create a 5-color palette
   - Must have a clear dominant color and an accent
   - Paste the palette hex codes into your analysis

2. Write `ART102-analysis.txt` with:
   - List your 5 hex codes
   - Name the palette type (complementary, analogous, triadic, or custom)
   - One sentence: what mood or feeling this palette creates
   - One sentence: where you'd use the accent color (background, highlights, lines)

3. Run `agentrust audit ART102-analysis.txt`

4. Save the signed report as `ART102-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis file
- Your palette type identification is valid (not calling random colors "complementary")
- Mood/feeling description is genuine, not generic
