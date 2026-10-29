# Estructura del blog y de Devinote

Dos apps de FastAPI, las dos en capas. El recorrido es el mismo: la ruta recibe el HTTP, el servicio aplica la regla, el repositorio habla con la base y el modelo es la tabla. Cambian el agrupado de carpetas y el ORM.

| | Blog | Devinote |
|---|---|---|
| Carpeta | `fastapi/` (en git, `fastApi/`) | `devinotes/` |
| Paquete | `app` | `app` |
| Puerto | 8000 | 8001 |
| Base local | `blog.db` | `devinotes.db` |
| ORM | [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) | [SQLModel](https://sqlmodel.tiangolo.com/) (SQLAlchemy por debajo) |
| Tablas | `create_all` al arrancar | [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) (`upgrade head`) |
| Cómo se agrupa | Por recurso (`api/v1/posts/` trae ruta, servicio, esquema y repositorio) | Por capa (`api/`, `services/`, `repositories/`, `models/`) |

Hay que correr cada una desde su carpeta. El paquete se llama `app` en las dos: desde la raíz, Python no sabe cuál abrir. Los comandos están en el README de la raíz, sección **Cómo levantar**.

`websocket/` y `webhooks/` son otras apps. No usan esta división en capas.

La misma idea, escrita al lado del código:

- Blog: `fastapi/app/__init__.py` (el mapa) y `fastapi/app/core/db.py` (SQLAlchemy frente a SQLModel, módulo 16).
- Devinote: `devinotes/app/__init__.py` (cómo se corre) y `devinotes/app/core/db.py` (Alembic y el deploy).

## Cómo viaja un request

1. `main.py` incluye el router. FastAPI elige la función por la URL y el método.
2. [Pydantic](https://docs.pydantic.dev/latest/concepts/models/) valida el JSON. Si no cumple, responde 422 y no llega al servicio.
3. [`Depends`](https://fastapi.tiangolo.com/tutorial/dependencies/) abre una sesión de base para ese request y la cierra al salir.
4. Si la ruta pide usuario, otra dependencia lee `Authorization: Bearer` y resuelve quién es. Sin token válido, 401.
5. El router llama al servicio. El servicio llama al repositorio.
6. El repositorio arma el SQL y devuelve filas.
7. FastAPI convierte la fila al modelo de salida.

En el blog el `commit` y el `rollback` están en el servicio. En Devinote el repositorio hace `commit` él mismo (`self.db.commit()`), y el servicio se queda con los permisos y los 403/404.

## Blog — SQLAlchemy

La tabla y el JSON son clases distintas. La tabla hereda de `Base` ([`DeclarativeBase`](https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#declarative-mapping)). El JSON es un `BaseModel` de Pydantic, en `schemas.py`.

```text
fastapi/
  blog_api.py                 histórico: el mismo blog en un solo archivo
  00_*.py                     prácticas sueltas, fuera de esta arquitectura
  app/
    main.py                   arma la app, create_all, middlewares, routers, /media
    __init__.py               mapa de capas y recorrido de un POST
    core/
      db.py                   engine, SessionLocal, Base, get_db
      config.py               clave, algoritmo y minutos del JWT
      security.py             hash, token, usuario actual, roles
      middleware.py           CORS, tiempo, log, X-Request-ID, bloqueo de IP
    models/                   tablas SQLAlchemy
      user.py                 User
      post.py                 PostORM y la tabla puente post_tags
      tag.py                  TagORM
      category.py             CategoryORM
      author.py               AuthorORM. Quedó en disco. El post apunta a User
    api/v1/
      auth/                   router, service, repository, schemas
      posts/                  router, service, repository, schemas
      tags/                   router, service, repository, schemas
      categories/             router, service, repository, schemas
      uploads/router.py       recibe el archivo. No tiene service ni repository
    services/
      pagination.py           corta un SELECT en páginas. Lo usan los tags
      file_storage.py         guarda la imagen en app/media
    utils/slugify_utils.py    slug único del post
    seeds/                    carga usuarios, categorías y tags de práctica
```

`api/`, `api/v1/`, `posts/` y `core/` no tienen `__init__.py`. Se importa el módulo concreto (`app.core.db`, `app.api.v1.posts.router`). `app/__init__.py` y `app/models/__init__.py` sí: el segundo registra las tablas en `Base` para que `create_all` las vea.

### Qué hace cada capa

| Capa | Dónde | Qué hace |
|---|---|---|
| Router | `api/v1/<recurso>/router.py` | URL, método, status 201/204, `Depends`. No hace SQL |
| Schemas | `schemas.py`, al lado del router | Entrada y salida. No sabe si atrás hay SQLite o Postgres |
| Service | `service.py`, al lado del router | Arma la operación, `commit` o `rollback`, traduce la base a 404/409/500 |
| Repository | `repository.py` | `select`, `add`, relaciones. No hace `commit` |
| Models | `app/models/` | La fila. `Mapped` y `mapped_column` |
| Core | `app/core/` | Conexión, JWT, middlewares |
| Services sueltos | `app/services/` | Ayudas que usan varios recursos: páginas y archivos |

Quién importa a quién: router → schemas, service y `get_db`. Service → repository. Repository → models. Models → `Base` en `core/db.py`. Un schema no importa la base.

`app/services/` no es un bus de eventos. No hay listeners. [SQLAlchemy puede enganchar eventos](https://docs.sqlalchemy.org/en/20/orm/events.html) (`listen`, `before_insert`); este blog no los usa. La lógica de negocio está en el `service.py` de cada recurso.

### Funcionalidades

Auth, prefijo `/api/v1` más el `/auth` del router. Swagger: http://127.0.0.1:8000/docs

| Ruta | Qué hace |
|---|---|
| `POST /api/v1/auth/register` | Alta. La clave se guarda hasheada |
| `POST /api/v1/auth/login` | JSON `{email, password}` y devuelve el token |
| `POST /api/v1/auth/token` | Formulario del botón Authorize de Swagger |
| `GET /api/v1/auth/me` | El usuario del token |
| `PUT /api/v1/auth/role/{id}` | Cambia el rol. Lo pide un admin |

Roles: `user` < `editor` < `admin`. El primer admin sale del seed (`admin@example.com`), porque cambiar un rol pide que ya exista un admin.

Posts en `/posts` (sin `/api/v1`). Listado con páginas, filtro por tags, ficha por slug y por id, alta, edición y borrado. Crear y editar piden token. La imagen del post pasa por `file_storage.py`. El slug lo arma `python-slugify`.

Tags en `/tags`. Listar es público. Crear y editar piden editor. Borrar pide admin. `GET /tags/popular/top` pide un usuario logueado. Los nombres se guardan en minúscula.

Categorías en `/categories`. CRUD público. Un slug repetido responde 400.

Uploads en `/upload/bytes`, `/upload/file` y `/upload/save`. `main.py` publica la carpeta con [StaticFiles](https://fastapi.tiangolo.com/tutorial/static-files/) en `/media`.

`GET /posts/sync` y `GET /posts/async` están comentados. Eran el ejemplo de la sección 9 (`request_test.py`): `time.sleep` frente a `await asyncio.sleep`.

### Librerías de esta app

| Librería | Para qué | Doc |
|---|---|---|
| FastAPI | App, routers, `Depends`, errores HTTP | [tutorial](https://fastapi.tiangolo.com/tutorial/) |
| Starlette | Por debajo de FastAPI: middlewares, archivos estáticos | [middleware](https://www.starlette.io/middleware/) |
| SQLAlchemy | Engine, sesión, tablas, `select` | [sesión](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) |
| Pydantic | Schemas de entrada y salida | [models](https://docs.pydantic.dev/latest/concepts/models/) |
| python-dotenv | Lee `.env` (`DATABASE_URL`, `SECRET_KEY`) | [repo](https://github.com/theskumar/python-dotenv) |
| PyJWT | Firma y verifica el token. El import es `jwt` | [uso](https://pyjwt.readthedocs.io/en/stable/usage.html) |
| pwdlib + argon2 | Hash de la clave. `PasswordHash.recommended()` | [pwdlib](https://github.com/frankie567/pwdlib) |
| python-multipart | Formularios, el login de Swagger y `UploadFile` | [Request files](https://fastapi.tiangolo.com/tutorial/request-files/) |
| email-validator | `EmailStr` en los schemas | [Pydantic email](https://docs.pydantic.dev/latest/api/networks/) |
| python-slugify | El slug del post. El import es `slugify` | [repo](https://github.com/un33k/python-slugify) |
| Typer | `python -m app.seeds` | [Typer](https://typer.tiangolo.com/) |
| Uvicorn | El proceso que escucha en el 8000 | [Uvicorn](https://www.uvicorn.org/) |

La sesión se abre con `sessionmaker` y las consultas con `session.execute(...).scalar_one_or_none()`. `echo=False` desde la sección 15, para que el log del middleware no se mezcle con el SQL.

## Devinote — SQLModel

Una clase con `table=True` es la tabla. Otra clase, en el mismo archivo y sin `table=True`, es el JSON. SQLModel junta [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) y [Pydantic](https://docs.pydantic.dev/latest/concepts/models/). La guía de la clase está en [SQLModel + FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/).

```text
devinotes/
  alembic.ini
  alembic/
    env.py                  toma la URL ya normalizada y el metadata de los modelos
    versions/               0bd823c6c863 crea el esquema; fa5e26298a8d agrega user.active
  app/
    main.py                 lifespan, CORS, incluye los cuatro routers bajo /api/v1
    __main__.py             python -m app. Ya no crea tablas
    __init__.py             secciones 16 a 19 y cómo se corre
    core/
      config.py             Settings: URL, JWT, nombre, ENVIRONMENT
      db.py                 engine, get_session, normalize_database_url, notas de Alembic
      security.py           hash y JWT
    models/
      user.py               User, UserCreate, UserRead
      note.py               Note, NoteCreate, NoteUpdate, NoteRead
      label.py              Label, NoteLabelLink, LabelCreate, LabelRead
      share.py              NoteShare, LabelShare, ShareRole, ShareRequest
    repositories/           user, note, label, share
    services/               auth, note, label, share
    api/
      deps.py               get_db, DBSession, usuario del token
      routers/              auth_router, notes_router, labels_router, shares_router
```

`models/__init__.py` importa las tablas en orden (user, note, label, share) para que las claves foráneas existan cuando Alembic lee el metadata.

### Qué hace cada capa

| Capa | Dónde | Qué hace |
|---|---|---|
| Router | `api/routers/*_router.py` | URL y status. La sesión entra como `DBSession` |
| Deps | `api/deps.py` | Abre la sesión y resuelve el usuario del token. Lo comparten las rutas |
| Service | `app/services/` | Permisos, qué notas se ven, 403 y 404 |
| Repository | `app/repositories/` | SQL y `commit`. `update` de notas hace `merge` y pide que la nota tenga id |
| Models | `app/models/` | Tabla (`table=True`) y DTO (sin `table=True`) en el mismo archivo |
| Core | `app/core/` | Settings, engine, hash y token |

El árbol que pedía la diapositiva es este: `api/` rutas, `services/` reglas, `repositories/` base, `models/` tabla y JSON, `core/` configuración. No hay carpeta `listeners`.

### Funcionalidades

Todo cuelga de `/api/v1`. Swagger: http://127.0.0.1:8001/docs

| Ruta | Qué hace |
|---|---|
| `POST /api/v1/auth/register` | Alta |
| `POST /api/v1/auth/login` | Token |
| `POST /api/v1/auth/token` | Formulario de Swagger |
| `GET/POST /api/v1/notes` | Notas visibles y alta |
| `PATCH/DELETE /api/v1/notes/{id}` | Editar y borrar |
| `GET/POST /api/v1/labels` | Etiquetas del usuario |
| `DELETE /api/v1/labels/{id}` | Borrar una etiqueta |
| `POST/DELETE /api/v1/shares/notes/{id}` | Compartir una nota |
| `POST/DELETE /api/v1/shares/labels/{id}` | Compartir una etiqueta |

Una nota se ve si sos el dueño, si te la compartieron, o si te compartieron una etiqueta que esa nota tiene. Editar pide rol `edit` en ese share. Borrar lo hace el dueño. `ShareRole` vale `read` o `edit`; en SQLite la columna guarda `READ` o `EDIT`.

`UserRead` no expone `active` ni la clave. La columna `active` entra en la segunda migración, con default en el servidor.

Las tablas no las crea el proceso de uvicorn. Antes de levantarlo: `alembic upgrade head`, desde `devinotes/`. El deploy (URL `postgresql+psycopg://`, `pool_pre_ping`, gunicorn) está comentado en `devinotes/app/core/db.py`.

### Librerías de esta app

| Librería | Para qué | Doc |
|---|---|---|
| FastAPI | App, routers, lifespan, CORS | [bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/), [lifespan](https://fastapi.tiangolo.com/advanced/events/) |
| SQLModel | Tabla y DTO, `Session.exec` | [select](https://sqlmodel.tiangolo.com/tutorial/select/) |
| SQLAlchemy | El motor que SQLModel usa, y Alembic | [engine](https://docs.sqlalchemy.org/en/20/core/engines.html) |
| Pydantic | Va dentro de SQLModel. Settings es Pydantic v2 | [settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| pydantic-settings | `BaseSettings` lee el `.env` | [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| Alembic | Migraciones. Plantillas con Mako | [tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) |
| python-dotenv | `load_dotenv()` en `main.py` | [repo](https://github.com/theskumar/python-dotenv) |
| PyJWT | El token. El import es `jwt` | [uso](https://pyjwt.readthedocs.io/en/stable/usage.html) |
| pwdlib + argon2 | El mismo hash que el blog | [pwdlib](https://github.com/frankie567/pwdlib) |
| psycopg | Postgres en el deploy. La URL queda `postgresql+psycopg://` | [psycopg 3](https://www.psycopg.org/psycopg3/docs/) |
| Gunicorn + Uvicorn | Proceso del servidor. En local alcanza Uvicorn | [gunicorn](https://docs.gunicorn.org/en/stable/), [worker de Uvicorn](https://www.uvicorn.org/deployment/) |

`session.exec()` de SQLModel, cuando el `select` es un modelo o una columna, ya devuelve las filas. Encadenar `.scalars()` otra vez revienta. En el blog, con SQLAlchemy, el método es `execute()` y ahí sí hace falta `scalar_one_or_none()` o `.scalars()`. La nota del profesor está en los repositorios de Devinote.

## La misma pieza, en otro cajón

| Idea | Blog | Devinote |
|---|---|---|
| Rutas | `api/v1/<recurso>/router.py` | `api/routers/<recurso>_router.py` |
| Reglas | `service.py` al lado de la ruta | `services/<recurso>_service.py` |
| SQL | `repository.py` al lado de la ruta | `repositories/<recurso>_repository.py` |
| Tabla | `models/*.py`, clase `(Base)` | `models/*.py`, clase `(SQLModel, table=True)` |
| JSON | `schemas.py` con `BaseModel` | clase SQLModel sin `table=True`, en el archivo de la tabla |
| Sesión por request | `core/db.py` → `get_db` | `core/db.py` → `get_session`, y `api/deps.py` → `get_db` |
| Usuario del token | `core/security.py` | `api/deps.py`, que llama a `core/security.py` |
| Config | clase `settings` y `os.getenv` | `Settings(BaseSettings)` |

## En qué se parecen

- FastAPI, `APIRouter`, `Depends`, `HTTPException` y el botón Authorize contra `POST .../auth/token`.
- Capas: la ruta no arma el SQL.
- `core/` guarda la conexión y la seguridad.
- JWT con PyJWT, algoritmo HS256. La clave sale del entorno, con un default solo para practicar.
- La clave de usuario se hashea con pwdlib (Argon2), no se guarda en claro.
- SQLite en la máquina de estudio. La URL puede apuntar a Postgres.
- Cada una es un proceso distinto. No comparten el engine ni el archivo `.db`.

## En qué se diferencian

| | Blog | Devinote |
|---|---|---|
| ORM | SQLAlchemy 2. La tabla no valida el JSON | SQLModel. La tabla y el DTO son primos, en el mismo archivo |
| Carpetas | Un recurso = una carpeta con sus cuatro archivos | Una capa = una carpeta, todos los recursos adentro |
| Consulta | `session.execute` | `session.exec` |
| Guardar | `commit` en el servicio | `commit` en el repositorio |
| Crear tablas | `Base.metadata.create_all` en `main.py` | Alembic. `init_db` quedó en `pass` |
| Versión de la API | `/api/v1` solo en auth. Posts, tags y categorías cuelgan de la raíz | Los cuatro routers cuelgan de `/api/v1` |
| Extra de HTTP | CORS, log, tiempo, id de request, bloqueo de IP, archivos estáticos | CORS con orígenes concretos. `lifespan` vacío |
| Datos de práctica | `python -m app.seeds` | No hay seed |
| Permisos | Rol del usuario: user, editor, admin | Dueño de la nota, o un share `read` / `edit` |
| Cuándo crece | El módulo 16 lo deja como default de un FastAPI que va a crecer, porque el JSON ya no coincide con la fila | El mismo módulo lo recomienda para un CRUD chico. Acá el DTO igual está separado (`UserRead` no lleva la clave) |

Pueden convivir en un mismo proceso: SQLModel usa el engine de SQLAlchemy. Lo que no conviene es declarar la misma tabla dos veces. En este repo no conviven: son dos carpetas y dos servidores. El detalle está en `fastapi/app/core/db.py`, después de `class Base`.
