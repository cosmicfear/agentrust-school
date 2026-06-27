# ART103: Procedural Patterns

## Objective

Create a procedural pattern using noise, repetition, or recursion. Patterns are the bridge between simple shapes and art — they introduce rhythm, structure, and emergent complexity.

## Background

Three pattern techniques in p5.js:

- **Grid patterns** — loop over x,y and draw something at each cell. Vary size/color by position.
- **Noise patterns** — Perlin noise (`noise()`) creates smooth, organic variation. Feed it x,y coordinates and use the output to drive color, size, or position.
- **Recursive patterns** — A function that calls itself, drawing smaller versions each time (tree branches, fractals).

Read:
- https://p5js.org/reference/#/p5/noise — Perlin noise basics
- https://thecodingtrain.com/tracks/generative-art — search for "Patterns" and "Noise" tracks
- https://p5js.org/reference/#/p5/map — map() to convert noise values (0-1) to useful ranges

## Task

1. Write a single HTML file (`ART103-pattern.html`) that generates a procedural pattern:
   - Must use a loop (nested for, while, or recursive function)
   - Must use `noise()` or `random()` to drive at least one visual property
   - Must produce something that looks intentional (not static noise)

2. Write `ART103-analysis.txt` with:
   - What pattern technique you used (grid, noise field, recursion, or combination)
   - One sentence: how changing the noise/random seed would change the output
   - One sentence: what the pattern reminds you of (texture, landscape, fabric, etc.)

3. Run `agentrust audit ART103-analysis.txt`

4. Save the signed report as `ART103-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis file
- Your explanation shows you understand the loop → pattern → emergent behavior chain
- You can articulate how randomness vs noise creates different visual qualities
