# Number Storage App

A simple website built with **Datastar** (frontend), **FastAPI** (backend), and **SQLite** (database).

## Features

- Stores two numbers:
  1. A **7-digit number**
  2. A **10–14 digit number**
- Real-time DOM updates via Datastar SSE
- Validation on both client and server side
- Local SQLite database for persistent storage
- Works without JavaScript (form fallback)

## Tech Stack

- **Frontend**: [Datastar](https://data-star.dev/) — hypermedia framework using Server-Sent Events
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite (standard library `sqlite3`)

## Running Locally

```bash
# Install dependencies
uv sync

# Run the server
uv run python main.py
```

The app will be available at [http://localhost:8000](http://localhost:8000).

## Running with Docker

Build and run the application in a Docker container:

```bash
# Build the image
docker build -t datastar-zd .

# Run the container
docker run -p 8000:8000 datastar-zd
```

The app will be available at [http://localhost:8000](http://localhost:8000).

## Project Structure

```
.
├── main.py              # FastAPI application
├── db.py                # Database setup and queries (SQLite)
├── Dockerfile           # Docker build configuration
├── .dockerignore        # Docker ignore rules
├── static/
│   └── datastar.js      # Local Datastar bundle
├── templates/
│   └── index.html       # Datastar frontend
├── pyproject.toml       # Python dependencies
└── README.md            # This file
```

## License

MIT
