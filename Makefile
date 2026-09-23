.PHONY: setup test lint fmt notebook

setup:
	uv sync
	uv run pre-commit install
	uv run nbstripout --install

test:
	uv run pytest -q

lint:
	uv run ruff check .
	uv run ruff format --check .

fmt:
	uv run ruff check --fix .
	uv run ruff format .

notebook:
	uv run jupyter lab
