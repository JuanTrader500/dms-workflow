
.PHONY: up down logs test lint migrate seed shell

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f backend

migrate:
	docker compose exec backend python manage.py migrate

seed:
	docker compose exec backend python manage.py cargar_semillas

shell:
	docker compose exec backend python manage.py shell

test:
	cd backend && pytest

lint:
	cd backend && ruff check . && black --check .
