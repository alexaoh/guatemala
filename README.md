# Guatemala Travel Website

A simple static website for Guatemala travel guides, with Harry Potter theme.

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
4. Push any change to the `main` branch - the workflow will automatically build and deploy
5. Your site will be available at `https://<username>.github.io/<repo-name>/`

The GitHub Action will:
- Install dependencies with uv
- Generate HTML from Markdown
- Deploy the static files to GitHub Pages

## Files

- `convert.py`: Converts Markdown and Excel to HTML
- `serve.py`: Starts the HTTP server
- `index.html`: Homepage
- `lodging.html`: Lodging guide
- `itinerary.html`: Itineraries with tabs
- `south_first_itinerary.html`: South First Itinerary Narration