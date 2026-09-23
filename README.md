# The Darkwater Project

Detecting anomalous vessel behavior — AIS transmission gaps ("going dark"), loitering, and
at-sea rendezvous — from public U.S. AIS data.

> Status: early setup. Problem statement and findings will be filled in as the project develops.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12.

```bash
make setup   # install deps, pre-commit hooks, notebook output stripping
make test
```

## Layout

```
src/darkwater/    reusable package code (ingestion, features, models)
notebooks/        exploration and analysis
tests/            unit and data tests
docs/decisions/   short records of key project decisions
data/             local only, never committed (raw / interim / processed)
```
