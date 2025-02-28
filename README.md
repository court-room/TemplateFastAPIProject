# TemplateFastAPIProject

This repository holds code for the `TemplateFastAPIProject`.
It comes with a working health check API as a minimal web server.

## Development

### Clone the repo

```
git clone https://github.com/court-room/TemplateFastAPIProject.git
```

### Install dependencies

I use [poetry](https://python-poetry.org/docs/) to manage the project.
Install the dependencies using

```
poetry install --with dev
```

### Run linters

```
poetry run ruff check
```

### Run formatters

```
poetry run ruff format
```

### Run type checkers

```
poetry run mypy
```

### Run tests

```
poetry run pytest
```

### Set environment variables

```
export $(cat .env | xargs)
```

### Run server

```
poetry run fastapi dev --app app --host 0.0.0.0 --port 8000
```
