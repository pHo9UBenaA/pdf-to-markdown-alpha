# pdf-to-markdown

## Overview

This project provides a Dockerized environment for converting PDF files to Markdown using `PyMuPDF` and `markdownify`.

## Quick Run with uvx (Without Installation)

```bash
# Basic usage
uvx --from git+https://github.com/pHo9UBenaA/pdf-to-markdown-on-container pdf-to-markdown input.pdf

# With custom output path
uvx --from git+https://github.com/pHo9UBenaA/pdf-to-markdown-on-container pdf-to-markdown input.pdf -o output.md

# Disable image extraction
uvx --from git+https://github.com/pHo9UBenaA/pdf-to-markdown-on-container pdf-to-markdown input.pdf --disable-image
```

## Development

### Start the Docker Container

```bash
docker compose up -d
```

### Convert PDF to Markdown

To convert a PDF file to Markdown, use the following command:

```
docker compose exec -w /app app uv run src/convert_pdf.py docs/input/sample.pdf
```

- To disable image extraction, add the `--disable-image` option:
- The converted Markdown file will be saved in the `docs/output/` directory.

## Lint & Format

```bash
uv run ruff check --fix;
uv run ruff format;
uv run mypy ./src/;
```
