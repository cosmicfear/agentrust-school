# ART202: Generative SVG

## Objective

Create a generative artwork in pure SVG format. SVG is vector-based — scalable, lightweight, and mathematically elegant. Understanding SVG generation is the foundation for generative design in any context (web, print, motion).

## Background

SVG basics:
- Elements: `<rect>`, `<circle>`, `<path>`, `<g>` (group)
- Attributes: `fill`, `stroke`, `stroke-width`, `opacity`, `transform`
- Coordinates: 0,0 is top-left, x goes right, y goes down

Generative SVG strategies:
- Build an SVG string in JavaScript and inject it into the DOM
- Use `<path d="M... L... C...">` for curves and organic shapes
- Layer translucent shapes to create depth (multiple `<circle>` with low opacity)
- Use `<g transform="translate(x,y) rotate(a)">` to place repeated elements

Read:
- https://developer.mozilla.org/en-US/docs/Web/SVG/Element — SVG element reference
- https://p5js.org/reference/#/p5/createGraphics — create an off-screen canvas and export as SVG

## Task

1. Write an HTML file (`ART202-svg.html`) that generates an SVG using JavaScript:
   - Must contain at least 3 different SVG element types
   - Must use a loop to generate repeating elements (not hand-coded)
   - Must have a clear visual composition (not random scatter)

2. Write `ART202-analysis.py` with:
   - What the piece is (abstract, landscape, pattern, etc.)
   - What SVG elements you used and why
   - One thing about vector vs raster art that surprised you
   - The viewBox attribute of your SVG and why you chose that aspect ratio

3. Run `agentrust audit ART202-analysis.py`

4. Save the signed report as `ART202-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis file
- Your analysis shows understanding of vector vs bitmap differences
- The composition is intentional, not accidental
