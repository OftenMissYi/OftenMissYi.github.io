# Jiayi Zhao — Robotics portfolio

Live site: https://oftenmissyi.github.io/

A static portfolio covering robotics, motion planning, embedded systems,
signal processing and mechanical engineering.

## Edit and preview

The homepage and four case studies are generated from `tools/build.py`.
Edit content there, then run:

```sh
python tools/build.py
python -m http.server 8765
```

Open http://localhost:8765. Commit the generated HTML together with source changes;
GitHub Pages serves the static files without a build dependency.

- `assets/site.css`: shared design system and responsive layouts.
- `assets/site.js`: mobile navigation and case-study section highlighting.
- `images/`: original project imagery.
- `DESIGN.md`: design direction and content principles.

Every detail page uses the same template. Main content remains readable without
JavaScript. Space Grotesk is locally hosted under the SIL Open Font License;
see `assets/space-grotesk-OFL.txt`.
