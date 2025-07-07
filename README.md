# pdf-to-markdown

## Overview

This project provides a Dockerized environment for converting PDF files to Markdown using `PyMuPDF` and `markdownify`.

## Getting Started

### Start the Docker Container

```bash
docker compose up -d
```

### Convert PDF to Markdown

To convert a PDF file to Markdown, use the following command:

```
docker compose exec -w /app app uv run scripts/convert_pdf.py docs/input/sample.pdf
```

- To disable image extraction, add the `--disable-image` option:
- The converted Markdown file will be saved in the `docs/output/` directory.

## Code Quality

### Lint and Fix Code Issues

```bash
docker compose exec -w /app app uv run ruff check --fix
```

### Format Code

```bash
docker compose exec -w /app app uv run ruff format
```
