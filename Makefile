install:
	uv sync
brain-games:
	uv run brain-games

brain_even:
	uv  run brain_even

brain_calc:
	uv run  brain_calc

brain_gcd:
	uv run brain_gcd

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain-games