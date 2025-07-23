.PHONY: migrate lint-check lint-fix type-check check-all check-fix up down logs rebuild deploy

migrate:
	uv run alembic upgrade head

lint-check:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

type-check:
	uv run pyright

check-all: lint-check type-check

check-fix: lint-fix type-check

up: 
	docker compose up -d 

down: 
	docker compose down

logs: 
	docker compose logs -f

rebuild: down up

deploy: rebuild
	docker compose exec api make migrate

.DEFAULT_GOAL := check-all
