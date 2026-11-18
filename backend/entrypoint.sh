#!/bin/sh
set -e

echo "[entrypoint] Aplicando migraciones..."
python manage.py migrate --noinput

echo "[entrypoint] Cargando semillas (idempotente)..."
python manage.py cargar_semillas

echo "[entrypoint] Recolectando estáticos..."
python manage.py collectstatic --noinput

echo "[entrypoint] Iniciando planificador de alertas en segundo plano..."
python manage.py runscheduler &

echo "[entrypoint] Iniciando gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 60
