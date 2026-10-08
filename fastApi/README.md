# fastapi — curso y clase

Las prácticas `00_*.py` viven en esta raíz. La clase modular vive en `app/`.

| Tipo | Nombre | Ejemplo |
|------|--------|---------|
| Práctica del proyecto | `00_`, `01_`, … | `00_hola_teoria.py`, `00_hola_practica.py`, `00_hola_main.py` |
| Clase, un solo archivo (histórico) | nombre del tema | `blog_api.py` |
| Clase modular | paquete `app/` | `app/main.py` |

## Práctica 00 — Hola FastAPI

```bash
./r fastapi/00 teoria
./r fastapi/00
```

Levantar la app mínima (desde la raíz del repo, con el venv activo):

```bash
fastapi dev fastApi/00_hola_main.py
```

- API: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs
- Salud: http://127.0.0.1:8000/salud

## Clase — blog en un archivo (histórico)

```bash
cd fastApi
fastapi dev blog_api.py
```

## Clase — app modular

La arquitectura por capas (router, schemas, repository, models, core) está
comentada al inicio de `app/__init__.py`, con el recorrido de un `POST /posts`.

Hay que pararse dentro de `fastApi/`. Desde la raíz del repo, Python confunde
esta carpeta con el paquete instalado `fastapi` y `from app...` no resuelve.

```bash
cd fastApi
source ../.venv/bin/activate
fastapi dev app/main.py
```

Rutas: http://127.0.0.1:8000/posts — docs: http://127.0.0.1:8000/docs

Sección 8, con el servidor levantado:

```bash
# Login (formulario, no JSON). Usuarios de práctica en app/api/v1/auth/router.py
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -d "username=ricardo@example.com&password=secret123"
```

Crear, editar y borrar un post pide el header `Authorization: Bearer <access_token>`.
Listar y leer siguen abiertos. El mapa está en `app/__init__.py`.
