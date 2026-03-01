install:
uv sync
brain-games:
uv run brain_games

build:
uv build

package-install:
uv tool install dist/*.whl