# ART101: First Sketch with p5.js

## Objective

Create a simple generative sketch using p5.js, then document and audit your work. This is the first step in learning how code can create visual art.

## Background

p5.js is a JavaScript library for creative coding. A p5.js sketch is a single HTML file that draws something on a canvas — shapes, colors, animation.

Read:
- https://p5js.org/get-started/ — understand setup() and draw()
- https://p5js.org/reference/ — shapes (circle, rect, line), colors (fill, stroke), and random()

## Task

1. Write a single HTML file (`ART101-sketch.html`) that uses p5.js to create a generative sketch.
   - Must use at least 2 different shapes
   - Must use `random()` or `noise()` in some way (position, size, or color)
   - Must include at least a splash of color (not grayscale only)

2. Write a short analysis (`ART101-analysis.py`) with:
   - One sentence: what the sketch does
   - One sentence: what element uses randomness or noise
   - The hex code of the main color you chose and why

3. Run `agentrust audit ART101-analysis.py`

4. Save the signed report as `ART101-report.json`

## Pass criteria

- The audit must return CLEAN on your analysis file
- Your analysis shows you understood the p5.js basics: setup, draw, shapes, randomness
