# Number Storage App

A simple website built with **Datastar** (frontend), **FastAPI** (backend), and **Turso** (database).

## Features

- Stores two numbers:
  1. A **7-digit number**
  2. A **10-14 digit number**
- Real-time DOM updates via Datastar SSE
- Validation on both client and server side
- Turso/libSQL database for persistent storage

## Tech Stack

- **Frontend**: [Datastar](https://data-star.dev/) — hypermedia framework using Server-Sent Events
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [Turso](https://turso.tech/) (libSQL)

## Running Locally

```bash
# Install dependencies
uv sync

# Run the server
uv run python main.py
```

The app will be available at [http://localhost:8000](http://localhost:8000).

## Turso Configuration

By default, the app uses a local SQLite database (`numbers.db`).

To use Turso cloud:

1. Create a database at [Turso](https://turso.tech/)
2. Copy `.env.example` to `.env` and fill in your credentials:

```bash
DATABASE_URL=libsql://your-db-name-your-username.turso.io
DATABASE_AUTH_TOKEN=your-auth-token-here
```

3. The app will automatically use Turso when `DATABASE_AUTH_TOKEN` is set.

## Project Structure

```
.
├── main.py              # FastAPI application
├── db.py                # Database setup and queries
├── templates/
│   └── index.html       # Datastar frontend
├── pyproject.toml       # Python dependencies
└── README.md            # This file
```

## License

MIT
