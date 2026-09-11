# fastApi — curso FastAPI (welcomePy)

Acá van las **teorías, prácticas y ejercicios** de FastAPI.
El venv del repo (`.venv` en la raíz) ya tiene las dependencias.

## Dependencias instaladas (relevantes)

| Paquete | Para qué |
|---------|----------|
| `fastapi` | Framework de la API |
| `uvicorn[standard]` | Servidor ASGI (desarrollo con `--reload`) |
| `pydantic` + `email-validator` | Modelos / validación (lección 20) |
| `python-multipart` | Forms y uploads |
| `httpx` | Cliente HTTP + `TestClient` |

Reinstalar todo (máquina nueva):

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Cómo estudiar

Cada lección (ej. `00_hola_fastapi/`):

1. Leé `teoria.py`
2. Mirá / corré `main.py` con uvicorn
3. Resolvé `practica.py`

## Cómo levantar el server (lección 00)

Desde la **raíz** del repo:

```bash
source .venv/bin/activate
uvicorn fastApi.00_hola_fastapi.main:app --reload
```

Abrí:
- API: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs
- Salud: http://127.0.0.1:8000/salud

## Cómo correr teoría / práctica

```bash
./r fastapi/00 teoria
./r fastapi/00
# o
.venv/bin/python fastApi/00_hola_fastapi/teoria.py
.venv/bin/python fastApi/00_hola_fastapi/practica.py
```

## Lecciones

| # | Carpeta | Tema |
|---|---------|------|
| 00 | `00_hola_fastapi` | App mínima + TestClient + /docs |

(Se irán sumando `01_…`, `02_…` a medida que avance el curso.)

## Requisitos previos del repo

Ya vistos en `Lecciones/fundamentos/`:
decoradores (14), JSON (15), venv (18), async (19), Pydantic (20).
