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

## Serve the Website

Start the local server:

```bash
uv run python serve.py
```

Or directly:

```bash
python serve.py
```

Then open http://localhost:8000 in your browser.

## Files

- `convert.py`: Converts Markdown and Excel to HTML
- `serve.py`: Starts the HTTP server
- `index.html`: Homepage
- `lodging.html`: Lodging guide
- `itinerary.html`: Itineraries with tabs
- `south_first_itinerary.html`: South First Itinerary Narration