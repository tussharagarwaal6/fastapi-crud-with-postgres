# FastAPI CRUD with PostgreSQL

A FastAPI application with PostgreSQL, JWT authentication, and SQLAlchemy ORM.

## Prerequisites

- Python 3.13+
- PostgreSQL running locally or via Docker

## Setup

### Option 1: Using Poetry (recommended)

```bash
pip install poetry
poetry install
poetry run uvicorn app.main:app --reload
```

### Option 2: Using pip

```bash
pip install .
uvicorn app.main:app --reload
```

### Option 3: Using Docker Compose (PostgreSQL only)

```bash
docker-compose up -d   # starts PostgreSQL
pip install .
uvicorn app.main:app --reload
```

## Environment Variables

Create `app/.env` with:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Database Migrations

```bash
alembic upgrade head
```

## API Docs

Once running, visit: http://localhost:8000/docs
