# Quantum Mechanics From Scratch

An interactive research atlas for reconstructing quantum mechanics from its foundational papers.

## What is included

- 41 historically ordered papers and milestones, from Planck (1900) to Bell (1964)
- direct DOI, publisher, archive, or open-translation links
- original abstract summaries and central equations
- full-text search, era filters, an Essential 20 path, and chronological sorting
- a browser-local reading-progress tracker and light/dark themes
- responsive layouts for desktop and mobile

The corpus is a curated foundational route, not a claim to include every paper that influenced quantum mechanics. Publisher pages may require institutional access. Abstract overviews are original educational summaries rather than copied publisher text.

## Run locally

No build step is required:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## GitHub Pages

The included workflow deploys the static site after changes reach `main`. In the repository settings, choose **Pages → Source → GitHub Actions** once if Pages is not already enabled.

## Research method

For each paper:

1. Identify the classical problem or conceptual gap.
2. Reconstruct the central derivation in modern notation.
3. Reproduce one result analytically or computationally.
4. Separate the formal result from its physical interpretation.

Curated for the **Quantum Mechanics From Scratch** research initiative by Kumar Azad.
