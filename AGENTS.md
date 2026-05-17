# Agent Notes

## Environment

- **Package manager**: `uv` — never `pip install`. Use `uv sync` after changing `pyproject.toml`.
- **Python**: 3.14 (set in `.python-version` and `pyproject.toml`). If unavailable, this repo cannot run.
- **Auto-activation**: `.envrc` runs `uv sync` then sources `.venv/bin/activate` for direnv users.

## Running

```bash
uv run python main.py   # starts on http://localhost:8000
```

## Architecture

- **Backend**: Single-file FastAPI (`main.py`). No Jinja2 — serves raw HTML via `open("templates/index.html")`.
- **Frontend**: Datastar v1.0.0-beta.11 loaded from CDN. Pure HTML + `data-*` attributes; zero custom JS.
- **Communication**: Backend pushes DOM updates via SSE using `datastar_py`. Endpoints that mutate UI return `DatastarResponse` with `ServerSentEventGenerator.patch_elements(...)`.
- **Form submissions**: Datastar handles these, not standard HTML forms. The form uses `data-on:submit="@post('/api/numbers', {contentType: 'form'})"`. Do not add `action` or `method` to the `<form>`.
- **Database**: Turso/libSQL via `pyturso` (PyPI name) which imports as `turso`. Defaults to local SQLite (`numbers.db`). Switches to Turso cloud only when `DATABASE_AUTH_TOKEN` env var is present (`DATABASE_URL` also required then).
- **DB init**: `init_db()` runs automatically inside the FastAPI `lifespan` on every startup — no separate migration command.

## Validation

- **Seven-digit number**: exactly 7 digits, validated client-side (`pattern="[0-9]{7}"`) and server-side.
- **Long number**: 10–14 digits, validated client-side (`minlength="10" maxlength="14" pattern="[0-9]{10,14}"`) and server-side.

## Lint / Format

```bash
uv run ruff check .
uv run ruff format .
```

## Testing

No test suite exists yet. `pytest` is not in dependencies.
