install:
	uv sync

brain-games:
	uv run python -m brain_games.scripts.brain_games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games

format:
	uv run ruff format brain_games

test: lint brain-games

.PHONY: install brain-games build package-install lint lint-fix format test