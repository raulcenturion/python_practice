# Estructura del blog y de Devinote

Dos apps de FastAPI, las dos en capas. El recorrido es el mismo: la ruta recibe el HTTP, el servicio aplica la regla, el repositorio habla con la base y el modelo es la tabla. Cambian el agrupado de carpetas y el ORM.

El próximo desarrollo sigue el modelo de Devinote. El contrato de capas, qué hace cada módulo y qué prácticas ya están en el código está en [Devinote: capas para el próximo desarrollo](#devinote-capas-para-el-próximo-desarrollo).

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

### Devinote: capas para el próximo desarrollo

El framework HTTP es [FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/). Recibe el request, valida el body y elige el endpoint. Los datos los describe [SQLModel](https://sqlmodel.tiangolo.com/tutorial/fastapi/): por debajo es SQLAlchemy, y la validación del JSON es Pydantic. La configuración es [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) (`BaseSettings`). El esquema de la base lo mueve [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html). Quien escucha el puerto es Uvicorn.

Cada capa existe para que un cambio de regla no toque el SQL, y un cambio de base no toque las rutas.

#### `main.py`

Punto de entrada. Arma la app, el [lifespan](https://fastapi.tiangolo.com/advanced/events/), el middleware de CORS y monta los cuatro routers bajo `/api/v1`.

El lifespan está vacío a propósito: arrancar no crea tablas. Eso lo hace Alembic antes de levantar el proceso. Cerrar tampoco tiene nada que apagar.

No hay lógica de negocio en este archivo. No hay middleware de logging: el blog lo tiene en `fastapi/app/core/middleware.py`. En Devinote el único middleware es CORS, y está escrito en `main.py`.

#### `api/`

Routers y el cable que comparten.

| Módulo | Por qué está |
|---|---|
| `routers/notes_router.py` | `GET/POST /notes`, `PATCH/DELETE /notes/{id}`. Llama a `NoteService` |
| `routers/labels_router.py` | Lista, alta y baja de etiquetas. Llama a `LabelService` |
| `routers/shares_router.py` | Comparte y deja de compartir. Llama a `ShareService` |
| `routers/auth_router.py` | Registro, login y el formulario de Swagger. Llama a `AuthService` |
| `deps.py` | `DBSession` abre la sesión del request. `CurrentUser` lee el Bearer y busca la fila |

Un endpoint declara la URL, el status (201 al crear, 204 al borrar) y delega. Notas, etiquetas y shares no arman SQL ni reglas: `NoteService(db).create(...)`.

`auth_router.py` arma `UserRepository(db)` y se lo pasa a `AuthService`. La consulta sigue en el repositorio. La ruta igual nombra la capa de persistencia. El patrón de notas es el que conviene copiar: el router solo ve el servicio, y el servicio arma sus repositorios.

`deps.py` también llama a `UserRepository` para saber quién es el token. Es infraestructura de cada request, no una regla de negocio. No revisa `User.active`.

#### `core/`

Infraestructura. Si cambia el motor o el secreto, se toca acá.

| Módulo | Por qué está |
|---|---|
| `config.py` | `Settings(BaseSettings)`. URL, JWT, nombre del proyecto, `ENVIRONMENT`. En Pydantic v2 la clase vive en `pydantic-settings`, no en `pydantic` |
| `db.py` | Engine, `get_session`, y `normalize_database_url` (`postgres://` y `postgresql://` pasan a `postgresql+psycopg://`) |
| `security.py` | Hash Argon2 (pwdlib) y el JWT (PyJWT, HS256) |

No hay un `core/middleware.py`. CORS se registra en `main.py`.

#### `models/`

La forma de los datos. Con SQLModel, `table=True` es la tabla y, sin eso, la misma familia de clases valida el JSON.

| Archivo | Tabla | JSON, sin `table=True` |
|---|---|---|
| `user.py` | `User` (`email`, hash, `active`) | `UserCreate` trae `password`. `UserRead` no trae el hash ni `active` |
| `note.py` | `Note` | `NoteCreate`, `NoteUpdate`, `NoteRead`. `label_ids` no es columna |
| `label.py` | `Label`, `NoteLabelLink` | `LabelCreate`, `LabelRead` |
| `share.py` | `NoteShare`, `LabelShare` | `ShareRequest`. `ShareRole` es `read` o `edit` |

El resto del código no inventa columnas: usa estas clases.

#### `repositories/`

El único lugar con `select`, `add`, `delete`, `merge` y `commit`. El servicio pide `get`, `list_owned` o `create`. No escribe SQL.

`session.exec()` ya devuelve las filas cuando el `select` es un modelo. No se encadena `.scalars()`. `NoteRepository.update` hace `merge` y exige que la nota tenga `id`.

El `commit` está en el repositorio. Una regla que escribe en dos repositorios confirma dos veces: crear una nota guarda la fila y, si vienen `label_ids`, el vínculo se confirma en un segundo `commit`.

#### `services/`

La regla de negocio. Usa repositorios y responde 400, 401, 403 o 404. El router no decide eso.

| Servicio | Regla que aplica |
|---|---|
| `AuthService` | Mail repetido → 400. Clave que no cierra → 401. Arma el token con el id |
| `NoteService` | Qué notas ve el usuario (dueño, share directo, share de una etiqueta). Editar pide rol `edit`. Borrar y cambiar etiquetas lo hace el dueño |
| `LabelService` | Nombre repetido del mismo dueño → 400. Borrar una etiqueta ajena → 404 |
| `ShareService` | Solo el dueño comparte o deja de compartir |

`User.active` existe en la tabla y en la migración `fa5e26298a8d`. Ni `AuthService.login` ni `get_current_user` lo leen. Un usuario inactivo hoy entra igual. Esa regla, si hace falta, va en el servicio de auth (y en la dependencia, que es quien deja pasar el request).

#### `alembic/`

Evoluciona el esquema sin borrar la base. `create_all` crea lo que falta y no altera una tabla que ya existe.

| Pieza | Por qué está |
|---|---|
| `alembic.ini` | Configuración del comando. La URL de la base queda comentada: la real la pone `env.py` |
| `env.py` | Importa los modelos, toma `normalize_database_url` y compara ese metadata con la base |
| `versions/0bd823c6c863_init_schema.py` | Crea user, note, label, link y shares |
| `versions/fa5e26298a8d_add_field_active_to_user.py` | Agrega `user.active` con default en el servidor |

Comandos y el cuándo usar Alembic: `devinotes/app/core/db.py`. Desde `devinotes/`, antes de uvicorn: `alembic upgrade head`.

#### Flujo

`PATCH /api/v1/notes/5` recorre las capas así:

1. `main.py` ya montó el router en `/api/v1`.
2. `notes_router.update_note` recibe el JSON. FastAPI lo valida con `NoteUpdate`. `deps.py` abre la sesión y resuelve `CurrentUser`.
3. El router llama a `NoteService.update`.
4. El servicio mira si la nota existe y si ese usuario puede editarla. Si no, 404 o 403, y no hay `UPDATE`.
5. `NoteRepository` hace el `merge` contra el modelo `Note` y confirma.
6. El router devuelve esa fila. FastAPI la serializa como `NoteRead`.

#### Buenas prácticas

| Práctica | En este código |
|---|---|
| Cada capa tiene un rol | Sí. La ruta no arma SQL. El repositorio no decide permisos |
| Probar servicio y repositorio sin HTTP | El constructor recibe la sesión (`NoteService(db)`, `NoteRepository(db)`). Se puede abrir una sesión contra un sqlite de prueba y llamar al método. Este repo no trae esa carpeta de tests |
| Sumar una entidad | Modelo, repositorio, servicio, router, una línea `include_router` en `main.py` y una revisión de Alembic. El resto de las rutas no se toca |
| Cambiar de motor | La URL y el driver están en `core/db.py`. Los repositorios hablan SQLModel, el mismo código para SQLite y Postgres |

Dos costuras, si el próximo desarrollo copia esta app:

- El router de auth construye el repositorio. Notas, etiquetas y shares no lo hacen.
- El `commit` vive en el repositorio. Una operación con dos escrituras no es una sola transacción.

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

## Lectura rápida — capas con SQLModel (Devinote)

Una leída de cómo está armado `devinotes/`, por qué existe cada capa y un ejemplo que ya está en el código. La lógica de negocio es `services/`. No hay otra carpeta de lógica.

```text
main.py          arranca la app y monta los routers
api/             recibe el HTTP y llama al servicio
services/        la regla (permisos, 403, 404)
repositories/    el SQL
models/          la tabla y el JSON
core/            base, secreto, hash
alembic/         cambia el esquema sin borrar la base
```

Un `POST /api/v1/notes` baja así: `main.py` ya incluyó el router → `notes_router.create_note` → `NoteService.create` → `NoteRepository.create` → la fila `Note`.

### main.py — arranque

Solo inicializa. Carga el `.env`, arma `FastAPI` con el lifespan y el CORS, e incluye los cuatro routers bajo `/api/v1`.

Por qué: el proceso tiene un solo lugar que dice qué está publicado. Si la regla de una nota cambiara, este archivo no se toca.

Ejemplo, en `devinotes/app/main.py`: `API_V1 = "/api/v1"` y `app.include_router(notes_router, prefix=API_V1)`. El lifespan no crea tablas. Eso lo hace Alembic antes de levantar uvicorn.

### api/ — rutas

Recibe el HTTP. Declara el método, la URL, el status y el modelo de respuesta. Delega. No arma el `select` ni decide si el usuario puede ver la nota.

Por qué: la ruta es el contrato hacia afuera. Se puede cambiar el SQL sin cambiar la URL.

Ejemplos en `devinotes/app/api/routers/`:

| Archivo | Qué publica | A quién llama |
|---|---|---|
| `notes_router.py` | `GET/POST /notes`, `PATCH/DELETE /notes/{id}` | `NoteService` |
| `labels_router.py` | lista, alta y baja de etiquetas | `LabelService` |
| `shares_router.py` | compartir nota o etiqueta | `ShareService` |
| `auth_router.py` | registro, login y el form de Swagger | `AuthService` |

`create_note` en `notes_router.py` hace esto y nada más: recibe `NoteCreate`, la sesión y el usuario del token, y devuelve `NoteService(db).create(user.id, payload)`. El 201 está en el decorador.

`api/deps.py` es el cable común. `DBSession` abre la sesión del request. `CurrentUser` lee el Bearer, decodifica el JWT y busca la fila. Las cuatro rutas lo usan. No es una regla de negocio: es "quién llama".

### services/ — lógica de negocio

Aplica la regla y traduce el fallo a un status. Usa repositorios. No escribe SQL.

Por qué: la misma regla se prueba sin HTTP. Si mañana el permiso cambia, se cambia el servicio y las rutas siguen iguales.

Ejemplos en `devinotes/app/services/`:

| Servicio | Regla |
|---|---|
| `NoteService.list_visible` | Una nota se ve si sos el dueño, si te la compartieron, o si te compartieron una etiqueta que la nota tiene |
| `NoteService.update` | Sin nota: 404. Sin rol `edit`: 403. Cambiar etiquetas lo hace solo el dueño |
| `NoteService.delete` | Borrar lo hace el dueño. Si no es suya, 404 |
| `AuthService.register` | Mail repetido: 400. La clave se guarda hasheada |
| `AuthService.login` | Clave que no cierra: 401. El token lleva el id en `sub` |
| `LabelService.create` | Nombre repetido del mismo dueño: 400 |
| `ShareService` | Solo el dueño comparte o deja de compartir |

`User.active` está en la tabla y ningún servicio lo mira todavía. Si hiciera falta rechazar a un usuario inactivo, el lugar es `AuthService.login` y `get_current_user`.

### repositories/ — persistencia

El `select`, el `add`, el `delete`, el `merge` y el `commit`. El resto del programa no nombra la base.

Por qué: cambiar de SQLite a Postgres se concentra en `core/` y en Alembic. Las consultas siguen siendo SQLModel.

Ejemplo en `devinotes/app/repositories/note_repository.py`: `create` hace `add`, `commit` y `refresh`. `get` es `session.get(Note, note_id)`. `update` hace `merge` y exige que la nota tenga `id`. `session.exec()` ya devuelve las filas. No se le agrega `.scalars()`.

### models/ — la forma de los datos

Con SQLModel, `table=True` es la tabla. Sin `table=True`, la clase valida el JSON y no crea tabla.

Por qué: `UserCreate` trae `password` y `UserRead` no trae el hash. La fila y la respuesta no son el mismo objeto, aunque vivan en el mismo archivo.

Ejemplos en `devinotes/app/models/`:

| Archivo | Tabla | JSON |
|---|---|---|
| `user.py` | `User` | `UserCreate`, `UserRead` |
| `note.py` | `Note` | `NoteCreate`, `NoteUpdate`, `NoteRead` |
| `label.py` | `Label`, `NoteLabelLink` | `LabelCreate`, `LabelRead` |
| `share.py` | `NoteShare`, `LabelShare` | `ShareRequest` |

`label_ids` está en `NoteCreate` y no es una columna de `note`. El vínculo lo guarda `NoteLabelLink`.

### core/ — infraestructura

Conexión, configuración y criptografía. No sabe qué es una nota.

| Archivo | Para qué |
|---|---|
| `config.py` | `Settings`: URL, JWT, nombre, `ENVIRONMENT` |
| `db.py` | Engine, `get_session`, y la URL `postgresql+psycopg://` |
| `security.py` | Hash Argon2 y el JWT |

### alembic/ — el esquema en el tiempo

`create_all` crea lo que falta y no altera una tabla que ya existe. Alembic sí. `env.py` lee los modelos y la URL. `versions/` guarda cada cambio: `0bd823c6c863` crea el esquema y `fa5e26298a8d` agrega `user.active`.

Por qué: se puede evolucionar `devinotes.db` sin perder las filas.
