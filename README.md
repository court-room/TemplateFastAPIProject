# TemplatePythonProject

This repository holds code for the `TemplatePythonProject`.

## Development

### Clone the repo

```
git clone https://github.com/court-room/TemplatePythonProject.git
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
