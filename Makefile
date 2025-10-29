update: install build force


install:
	uv sync


start:
	uv run start


brain-games:
	uv run brain-games


build:
	uv build


package-install:
	uv tool install dist/*.whl


force:
	uv tool install --force dist/*.whl


lint:
	uv run ruff check brain_games


fix:
	uv run ruff check --fix
