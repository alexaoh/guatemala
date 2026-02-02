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
uv run convert
```

## Serve Locally

Start the local server (serves from `dist/`):

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

- `src/convert.py`: Converts Markdown files to HTML using Jinja2 templating and processes Excel data for itineraries
- `src/serve.py`: Starts the HTTP server for local development, serving from dist/
- `src/templates/base.html`: Jinja2 template providing consistent HTML structure and styling for all pages
- `content/`: Directory containing source files
  - `content/lodging.md`: Lodging guide source
  - `content/south_first_itinerary.md`: South First Itinerary Narration source
  - `content/Guatemala.xlsx`: Excel file with itinerary data
- `dist/`: Directory containing generated HTML files for deployment
  - `dist/index.html`: Homepage
  - `dist/lodging.html`: Lodging guide (generated from content/lodging.md)
  - `dist/itinerary.html`: Itineraries with tabs (generated from content/Guatemala.xlsx)
  - `dist/south_first_itinerary.html`: South First Itinerary Narration (generated from content/south_first_itinerary.md)
- `config.json`: Configuration file containing theme settings, colors, fonts, and navigation structure

## Further Work

See [further_work.md](further_work.md) for planned improvements and migration suggestions.
