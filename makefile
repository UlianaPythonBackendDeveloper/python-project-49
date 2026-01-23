install:
	uv sync

brain-games:
	uv run python -m brain_games.scripts.brain_games
build:
	uv build

package-install:
	uv tool install dist/*.whl

.PHONY: install brain-games build package-install