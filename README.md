# Asteroids (web build)

A browser-playable version of my Python Asteroids game, packaged with pygbag so it runs without installing anything.

**Play it:** https://jbouchey.github.io/Asteroids-web/

**What it shows:** Python and pygame · packaging a Python game for the browser (WebAssembly via pygbag) · Built without AI (game code); packaged for the browser with pygbag

## Why I built it
The original [Asteroids](https://github.com/jbouchey/Asteroids) project only ran locally. I wanted to see whether I could put it in front of people with a single link.

## What is different from the desktop version
- The game loop is `async` so it can run in the browser.
- The ship, asteroids and shots wrap around the screen edges.
- A background image, a "GAME OVER" screen, and `R` to restart.
- Controls are the same: `A`/`D` rotate, `W`/`S` move, `Space` fires.

## Tech
- Python and pygame, built for the web with [pygbag](https://pypi.org/project/pygbag/)
- Game code in the root (`main.py`, `player.py`, `asteroid.py`, `asteroidfield.py`, `shot.py`, `circleshape.py`, `constants.py`, `logger.py`), assets in `assets/`
- The built output is in `docs/` and served by GitHub Pages from the `main` branch

## Run it locally
```bash
pip install pygame pygbag
pygbag .
```
Then open http://localhost:8000.

## What I learned
- Turning a blocking game loop into an async one
- How a Python game gets compiled and served as a static site

---
Part of [bouchey.dev](https://bouchey.dev).
