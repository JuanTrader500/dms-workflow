# DMS Workflow — Disability Management System Workflow

Sistema de gestión de incapacidades y licencias (Técnicas de Modelado de Software — UTP).
Monolito estructurado: **Django + DRF**, **PostgreSQL**, frontend **HTML/CSS/JS**, **Docker Compose** (3 servicios) y módulo de IA con **Gemini**.

## Arranque rápido

```bash
cp .env.example .env          # editar contraseñas; GEMINI_API_KEY si IA_PROVEEDOR=gemini
docker compose up --build
```

- Aplicación: http://localhost:8080
- Documentación de la API (Swagger): http://localhost:8080/api/docs/
- Usuarios demo (si `SEED_DEMO=1`): uno por rol (`auxiliar_admin_personal`, `colaborador`, `lider`, `cartera`, `juridica`, `contabilidad`, `gestion_documental`) con la clave `DEMO_PASSWORD`.

## Desarrollo local sin Docker

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python manage.py migrate && python manage.py cargar_semillas
python manage.py runserver
pytest
```

Sin `POSTGRES_HOST` se usa SQLite y `IA_PROVEEDOR=fake` (modo desarrollo).

## Estructura

```

backend/     Django (apps por módulo del dominio) + tests
frontend/    HTML/CSS/JS servido por Nginx
docs/        diagramas Mermaid, SRS y API
storage/     volumen de archivos subidos (no versionado)
```

## Nota sobre el stack
El SRS v1.0 y el diagrama de secuencia nombran "Backend FastAPI". El equipo adoptó **Django/DRF**; el modelo de dominio y los requisitos no cambian.

## Seguridad y datos de salud
- La IA nunca extrae ni guarda diagnóstico/CIE (Ley 1581 de 2012).
- Los archivos subidos viven en `storage/` (no versionar). Documentos de ejemplo: solo ficticios.
- Producción: terminar TLS 1.2+ en el proxy y usar volumen cifrado.
