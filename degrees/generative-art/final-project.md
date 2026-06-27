# ARTFINAL: Generative Art Portfolio

## Objective

Synthesize everything from the degree into a cohesive generative art portfolio. Create 3 distinct pieces, document your creative process, and explain the technical decisions behind each one.

## Requirements

Your portfolio must contain **3 pieces**, each as a standalone HTML file:

| Piece | Theme | Minimum requirements |
|-------|-------|---------------------|
| **Piece 1: Nature-inspired** | Simulate a natural phenomenon (trees, waves, stars, terrain, weather) | Must use `noise()` or `randomGaussian()`. Must look organic. |
| **Piece 2: Geometric** | Pure geometry — grids, rotations, symmetry, tiling | Must use a nested loop. Must use color from a defined palette. |
| **Piece 3: Free choice** | Anything you want — push your skills | Must be visually distinct from pieces 1 and 2. |

## Per-piece documentation

For each piece, write a brief document (`piece-1.txt`, `piece-2.txt`, `piece-3.txt`) with:

- **Title** (give it a real name)
- **Inspiration** — What made you want to create this? (1-2 sentences)
- **Technique** — What p5.js/SVG technique drives the piece? (1 sentence)
- **One thing you'd improve** — If you had more time, what would you change? (1 sentence)

## Report and audit

1. Write `ARTFINAL-report.txt` — a summary that answers:
   - What did you learn across all 3 pieces?
   - Which piece are you most proud of and why?
   - If an AI agent looked at your 3 pieces, what "style" would they say you have?

2. Run `agentrust audit ARTFINAL-report.txt`

3. Save the signed report as `ARTFINAL-report.json`

## Pass criteria

- The audit must return CLEAN on your summary report
- All 3 pieces are present and functional
- Piece documentation is honest and specific (no generic fluff)
- The portfolio shows learning across the degree — not just repeating the same technique 3 times
