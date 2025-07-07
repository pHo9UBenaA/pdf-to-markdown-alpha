# My Python Script Template

## Getting Started

```bash
docker compose up -d
```

## Running Scripts

```
docker compose exec app uv run script.py
```

## Package Management

```bash
docker compose exec -w /app app uv add requests
```

```bash
docker compose exec -w /app app uv remove requests
```
