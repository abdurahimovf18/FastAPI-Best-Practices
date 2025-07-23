.PHONY: 
	# database migrations
	migrate 
	# ruff, pyright commands
	lint-check lint-fix type-check check-all check-fix 
	# pytest commands
	test test-v test-q 
	# docker/docker-compose dommands
	up down logs rebuild deploy

# alembic commands
migrate:
	uv run alembic upgrade head

# ruff commands
lint-check:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

# pyright commands
type-check:
	uv run pyright

# lint commands
check-all: lint-check type-check

check-fix: lint-fix type-check

# test commands
test: 
	uv run pytest 

test-v: 
	uv run pytest -v 

test-q: 
	uv run pytest -q --tb=short --log-level=INFO --maxfail=1

# docker compose commands
up: 
	docker compose up -d 

down: 
	docker compose down

logs: 
	docker compose logs -f

rebuild: down up

deploy: rebuild
	docker compose exec api make migrate

# default command
.DEFAULT_GOAL := check-all
