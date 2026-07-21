up:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose down
	docker compose up --build

logs:
	docker compose logs -f

backend:
	docker compose exec backend bash

worker:
	docker compose exec worker bash

db:
	docker compose exec postgres psql -U astra

redis:
	docker compose exec redis redis-cli

lint:
	ruff check backend

format:
	black backend
	isort backend

test:
	pytest backend/app/tests