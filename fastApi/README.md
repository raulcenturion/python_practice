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

Sección 12, con el servidor levantado. El usuario se crea en la tabla `users`.
El rol inicial es `user`. Cambiar roles (`PUT /api/v1/auth/role/{id}`) pide un admin.

```bash
# Alta. JSON, no formulario.
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"ricardo@example.com","password":"secret123","full_name":"Ricardo"}'

# Login. Devuelve access_token y el usuario.
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"ricardo@example.com","password":"secret123"}'
```

El botón Authorize de `/docs` no usa ese JSON: manda el formulario a
`POST /api/v1/auth/token`. En el campo username va el email.

Crear, editar y borrar un post pide el header `Authorization: Bearer <access_token>`.
Listar y leer posts siguen abiertos. Crear o editar un tag pide rol editor.
Borrar un tag pide admin. El mapa está en `app/__init__.py`.

## Paquetes que hay que instalar

La lista completa, con versiones, está en `requirements.txt` de la raíz del repo.
Estos los pide la clase y no vienen con Python:

| Paquete | Para qué | Sección |
|---------|----------|---------|
| `fastapi` | La aplicación y las rutas | base |
| `python-dotenv` | Lee el `.env` (`DATABASE_URL`, `SECRET_KEY`) | 6 |
| `sqlalchemy` | Tablas y consultas | 6 |
| `PyJWT` | Firma y verifica el token. El import es `jwt` | 8 |
| `python-multipart` | Formularios y archivos (`UploadFile`, login) | 8 y 10 |
| `email-validator` | `EmailStr` en los schemas | 6 |
| `pwdlib[argon2]` | Hashea la clave. `PasswordHash` en `app/core/security.py` | 11 |
| `passlib` | Otra librería para hashear claves (`CryptContext`). No es `pwdlib` | 11 |

`pwdlib` y `passlib` son dos paquetes distintos. El código de la clase importa
`pwdlib`. `passlib` queda instalado para tenerlo en el proyecto.

`pwdlib` solo no alcanza: `PasswordHash.recommended()` usa Argon2, y ese algoritmo
viene en el extra `[argon2]` (`argon2-cffi`). La clase escribe `pip install pwdlib`.
En este proyecto el comando es el de abajo.

Con el venv del repo activo, desde la raíz:

```bash
source .venv/bin/activate
pip install "pwdlib[argon2]"
pip install passlib
```
