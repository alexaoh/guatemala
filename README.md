# Guatemala Travel Website

A simple static website for Guatemala travel guides, with HP theme.

## Setup

Install uv if not already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install dependencies:

```bash
uv sync
```

## Generate HTML

Run the conversion script:

```bash
uv run python convert.py
```

## Serve Locally

Start the local server:

```bash
uv run serve
```

Then open http://localhost:8000 in your browser.

## Deploy to GitHub Pages

1. Push this repository to GitHub (create a new repo if needed)
2. Go to your repo settings > Pages
3. Set Source to "GitHub Actions"
4. Create a feature branch for changes
5. The workflow will validate builds on PRs and branch pushes
6. Merge to `main` - the workflow will automatically deploy to GitHub Pages
7. Your site will be available at `https://<username>.github.io/<repo-name>/` - in this case: `https://alexaoh.github.io/guatemala`

The workflow:
- **Build**: Runs on all PRs, branches, and main to validate and build the site
- **Deploy**: Runs only on `main` pushes to deploy to GitHub Pages (reuses the build artifact)

## Files

- `convert.py`: Converts Markdown and Excel to HTML
- `serve.py`: Starts the HTTP server
- `index.html`: Homepage
- `lodging.html`: Lodging guide
- `itinerary.html`: Itineraries with tabs
- `south_first_itinerary.html`: South First Itinerary Narration