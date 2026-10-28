# welcomePy

Repo de estudio de Python: cada lección junta **teoría + práctica** (checklist hacia FastAPI).

## Cómo estudiar

Abrí una carpeta de lección (ej. `Lecciones/fundamentos/01_print_comentarios/`):

1. Leé `teoria.py` (o `teoria_*.py` si hay más de una)
2. Resolvé `practica.py` en la misma carpeta
3. Pasá a la lección siguiente (`02_...`, `03_...`)

## Estructura

```text
Lecciones/
  fundamentos/     → base Python (orden 01 → 20)
  fechas/
  logica/
  regex/
  scraping/
  integradores/    → repaso + proyectos de cierre
fastApi/           → teorías y prácticas de FastAPI (siguiente etapa)
devinotes/         → secciones 16 a 19, app nueva con SQLModel, Alembic y deploy
websocket/         → sección 21, chat por WebSocket (proyecto aparte)
webhooks/          → GitHub avisa por POST y se puede reenviar a Discord (proyecto aparte)
```

Cada lección:

```text
01_print_comentarios/
  teoria.py
  practica.py
```

Si el tema necesita más de un archivo de teoría:

```text
07_listas/
  teoria_listas.py
  teoria_metodos.py
  practica.py
```

## Fundamentos (checklist)

| # | Lección | Contenido |
|---|---------|-----------|
| 01 | `print_comentarios` | print, comentarios |
| 02 | `tipos_de_datos` | str, int, float, bool, … |
| 03 | `casting` | conversiones |
| 04 | `variables` | variables + `practica_operaciones.py` |
| 05 | `input` | input y strings |
| 06 | `condicionales_booleanos` | if/else, bool |
| 07 | `listas` | listas y métodos |
| 08 | `while` | while |
| 09 | `for_rangos` | for y range |
| 10 | `funciones` | def, params, return |
| 11 | `diccionarios_tuplas_sets` | dict, tuple, set |
| 12 | `clases_poo` | clases y herencia |
| 13 | `excepciones` | try/except/finally |
| 14 | `hof_decoradores` | HOF y `@` (estilo FastAPI) |
| 15 | `modulos_ficheros_json` | módulos, archivos, JSON |
| 16 | `valor_referencia` | teoría |
| 17 | `librerias` | pip / paquetes (teoría) |
| 18 | `entornos_virtuales` | venv + requirements |
| 19 | `async_await` | async / await |
| 20 | `modelos_datos_pydantic` | dataclasses → Pydantic |

## Checklist pre-FastAPI

| Tema | Lección |
|------|---------|
| Variables y tipos | 01–05 |
| Listas / dict / tuplas / sets | 07, 11 |
| if / for / while | 06, 08, 09 |
| Funciones y módulos | 10, 15 |
| Errores | 13 |
| POO | 12 |
| Archivos y JSON | 15 |
| venv + pip | 18 (+ 17) |
| Decoradores | 14 |
| async / await | 19 |
| Pydantic | 20 |

## Integradores

| # | Proyecto | Nivel | Qué integra |
|---|----------|-------|-------------|
| 00 | `integradores/00_repaso_presupuesto_cli` | Repaso | lecciones 01→10 + 13 (CLI con input) |
| 01 | `integradores/01_agenda_contactos` | Fácil | menú, dict/list, JSON, funciones, try/except |
| 02 | `integradores/02_gestor_tareas` | Medio | POO, módulos, excepción propia, decorador |
| 03 | `integradores/03_mini_api_biblioteca` | Difícil | rutas con `@`, Pydantic, async (+ `tips.md`) |

Detalle en `Lecciones/integradores/README.md`.

## Cómo levantar

El entorno es el `.venv` de la raíz. Los comandos de abajo usan esa ruta y hay que correrlos **dentro de la carpeta de cada app**. Desde la raíz, `app` puede ser el blog o Devinote, y uvicorn no sabe cuál abrir.

Cada servidor tiene su puerto. Se pueden tener abiertos a la vez.

| App | Puerto | Para qué |
|-----|--------|----------|
| Blog (`fastapi/`) | 8000 | API del curso, secciones 11 a 15. Swagger: http://127.0.0.1:8000/docs |
| Devinote (`devinotes/`) | 8001 | SQLModel, secciones 16 a 19. Swagger: http://127.0.0.1:8001/docs |
| Chat WebSocket (`websocket/`) | 8002 | Sección 21. Página: http://127.0.0.1:8002/ |
| Eco WebSocket (`websocket/echo.py`) | 8003 | El mismo curso, el ejemplo corto. Socket: `ws://127.0.0.1:8003/ws/echo` |
| Webhooks (`webhooks/`) | 8004 | GitHub avisa un issue nuevo. Swagger: http://127.0.0.1:8004/docs |
| Front de CORS (`cors-demo/`) | 3000 | Prueba el middleware del blog |

```bash
# Blog
cd fastapi
../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000

# Datos de práctica del blog (usuarios, categorías, tags). También desde fastapi/
../.venv/bin/python -m app.seeds all

# Devinote. Primero las tablas, después la API.
cd devinotes
../.venv/bin/python -m alembic upgrade head
../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8001

# Chat. El front lo sirve esta misma app.
cd websocket
../.venv/bin/python -m uvicorn main:app --host 127.0.0.1 --port 8002

# Eco, en otra terminal, también desde websocket/
../.venv/bin/python -m uvicorn echo:app --host 127.0.0.1 --port 8003

# Webhooks. GitHub hace POST /webhooks/github. GET /issues lista lo guardado.
# Sin .env usa el secreto de práctica de app/github_webhook.py.
# Para un webhook real, el mismo secreto va en GitHub (campo Secret) y en webhooks/.env.
# Discord es opcional: sin DISCORD_WEBHOOK_URL el issue se guarda igual.
cd webhooks
../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8004

# Front que pega al blog para probar CORS. Pide Node 22 (hay .nvmrc).
cd cors-demo
nvm use
npm run dev
```

Sin `?username=` el chat pide el nombre con un cuadro. Con `http://127.0.0.1:8002/?username=Ana` entra directo. Dos pestañas con dos nombres se ven entre sí.

GitHub no puede llamar a `127.0.0.1`. El curl de abajo firma el body como lo hace GitHub y pega al 8004 ya levantado. Un issue con el mismo `id` responde ok y no se duplica. Sin el header de la firma, la respuesta es 401.

```bash
# Firma inválida, con el servidor del 8004 ya levantado.
curl -i -X POST http://127.0.0.1:8004/webhooks/github \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: issues" \
  -d '{"action":"opened"}'

# Issue firmado. El secreto lo lee el propio módulo.
cd webhooks
../.venv/bin/python - <<'PY'
import hashlib, hmac, json, urllib.request
from app.github_webhook import github_secret

payload = {
    "action": "opened",
    "issue": {
        "id": 1,
        "title": "Hola",
        "html_url": "https://github.com/ejemplo/repo/issues/1",
        "state": "open",
        "created_at": "2026-01-20T10:00:00Z",
    },
}
body = json.dumps(payload).encode()
sig = hmac.new(github_secret().encode(), body, hashlib.sha256).hexdigest()
req = urllib.request.Request(
    "http://127.0.0.1:8004/webhooks/github",
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-Hub-Signature-256": f"sha256={sig}",
        "X-GitHub-Event": "issues",
    },
    method="POST",
)
print(urllib.request.urlopen(req).read().decode())
PY

curl http://127.0.0.1:8004/issues
```

```bash
# Devinote. python -m app ya no crea tablas: init_db quedó en pass.
cd devinotes
../.venv/bin/python -m app

# Alembic, también desde devinotes/. El init ya está hecho en este repo.
../.venv/bin/python -m alembic init alembic
../.venv/bin/python -m alembic revision --autogenerate -m "mensaje"
../.venv/bin/python -m alembic upgrade +1
../.venv/bin/python -m alembic downgrade -1
../.venv/bin/python -m alembic downgrade base
../.venv/bin/python -m alembic current
../.venv/bin/python -m alembic history
../.venv/bin/python -m alembic upgrade head --sql

# Deploy de Devinote. En local no hace falta: sigue uvicorn en el 8001.
# El detalle está en devinotes/app/core/db.py.
cd devinotes
../.venv/bin/python -m alembic upgrade head
gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT

# Seed de una sola lista, desde fastapi/. all carga las tres.
../.venv/bin/python -m app.seeds users
../.venv/bin/python -m app.seeds categories
../.venv/bin/python -m app.seeds tags

# Login del blog, con el servidor del 8000 ya levantado.
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"Admin123!"}'
```

El alta y el login de la sección 12, con el usuario de la clase, están en `fastapi/README.md`.

## Entorno y lecciones

Desde la raíz del repo. El script `r` usa el `.venv` solo.

```bash
source .venv/bin/activate
pip install -r requirements.txt

# Práctica y teoría. 16 y 17 no tienen practica.py: ahí va teoria.
./r 01
./r 01 teoria
./r 04 practica_operaciones
./r 16 teoria
./r integradores/01
./r integradores/00 presupuesto --list
./r integradores/00 presupuesto 01
./r logica/01
./r regex/02 teoria
./r scraping/01
./r fastapi/00
./r fastapi/00 teoria

# Lo mismo, sin el atajo
python Lecciones/fundamentos/01_print_comentarios/practica.py
```

Los `pip install` de cada clase (`pwdlib[argon2]`, `passlib`, `sqlmodel`, `alembic`, `gunicorn`, `psycopg`) ya están pinneados en `requirements.txt` y en la tabla de `fastapi/README.md`. No hace falta correrlos sueltos. La clase de webhooks no agrega paquetes: su `requirements.txt` bajaría fastapi y sqlmodel, y no se instala.

## FastAPI

Carpeta en la raíz: `fastApi/` (venv del repo ya tiene FastAPI + Uvicorn). El servidor de la app modular es el de la tabla de arriba, puerto 8000. `fastapi dev app/main.py` desde `fastapi/` no sirve: esa carpeta tapa al paquete `fastapi`.

```bash
# App mínima y el blog de un solo archivo. Desde la raíz, con el venv activo.
fastapi dev fastApi/00_hola_main.py
fastapi dev fastApi/blog_api.py
```

La app modular no se levanta con `fastapi dev app/main.py`. Ese es el comando de la clase y, desde `fastapi/`, la carpeta tapa al paquete. El que funciona es el uvicorn del puerto 8000, más arriba.

Docs: http://127.0.0.1:8000/docs — detalle en `fastApi/README.md`.
