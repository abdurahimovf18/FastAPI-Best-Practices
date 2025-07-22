.PHONY: lint-check lint-fix type-check check-all check-fix

lint-check:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

type-check:
	uv run pyright

check-all: lint-check type-check

check-fix: lint-fix type-check


.DEFAULT_GOAL := check-all
