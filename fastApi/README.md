# fastapi — curso y clase

Todo vive en esta raíz. No hay subcarpetas de lección.

| Tipo | Nombre | Ejemplo |
|------|--------|---------|
| Práctica del proyecto | `00_`, `01_`, … | `00_hola_teoria.py`, `00_hola_practica.py`, `00_hola_main.py` |
| Clase | nombre del tema | `blog_api.py` |

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

## Clase — blog

```bash
cd fastApi
fastapi dev blog_api.py
```

Docs: http://127.0.0.1:8000/docs
