install:
	uv sync
brain-games:
	uv run brain-games

brain_even:
	uv brain_even

brain_calc:
	uv brain_calc

brain_gcd:
	uv brain_gcd
	
build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain-games