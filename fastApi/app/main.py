# Arma la aplicación y le engancha las rutas de posts.
#
# La clase importa el engine primero y recién después llama a load_dotenv().
# Eso llega tarde: al importar app.core.db la URL ya se leyó.
# load_dotenv() va primero. core/db.py también lo llama, por si este archivo
# se importa en otro orden.
#
# fastapi.FastAPI          → la aplicación.
# app.core.db.Base/engine  → las tablas y la conexión (SQLAlchemy).
# dotenv.load_dotenv       → paquete python-dotenv. Lee el .env de la raíz del repo.
# app.api.v1.posts.router  → el APIRouter con prefix="/posts".
# app.api.v1.auth.router   → login y /me. Sección 8.
# app.api.v1.uploads.router → subir archivos. Sección 10.
# app.api.v1.tags.router    → CRUD de etiquetas. Sección 11.
# StaticFiles              → publica una carpeta del disco como URL.

import os

from dotenv import load_dotenv

load_dotenv()

from app.api.v1.auth.router import router as auth_router
from app.api.v1.posts.router import router as post_router
from app.api.v1.tags.router import router as tag_router
from app.api.v1.uploads.router import router as upload_router
from app.core.db import Base, engine

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Carpeta donde file_storage.py escribe las imágenes.
# Tiene que existir antes de montarla. exist_ok=True no falla si ya está.
MEDIA_DIR = "app/media"


# create_app deja crear la app en los tests sin ejecutar el archivo como script.
def create_app() -> FastAPI:
    app = FastAPI(title="Mini Blog")
    # Crea las tablas si no existen. La clase lo marca como dev:
    # en un proyecto real las tablas las arma una migración (Alembic), no esto.
    Base.metadata.create_all(bind=engine)

    # Sección 8. El router de auth ya trae prefix="/auth".
    # Este prefix arma /api/v1/auth/login, la misma URL que tokenUrl en security.py.
    # Los posts siguen en /posts: la clase no les agrega /api/v1.
    app.include_router(auth_router, prefix="/api/v1")
    # include_router suma las rutas de posts (/posts, /posts/{id}, ...).
    app.include_router(post_router)
    # Sección 11. El router ya trae prefix="/tags". Queda /tags, sin /api/v1,
    # igual que /posts. La clase lo incluye en el mismo lugar.
    app.include_router(tag_router)
    # Sección 10. /upload/bytes, /upload/file y /upload/save.
    # El router ya trae prefix="/upload", por eso acá no se agrega otro.
    app.include_router(upload_router)

    # Crea app/media y la publica en http://127.0.0.1:8000/media/<archivo>.
    # No es una ruta de router: StaticFiles lee el archivo del disco y lo devuelve.
    os.makedirs(MEDIA_DIR, exist_ok=True)
    app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

    return app


# uvicorn y `fastapi dev` buscan esta variable: app.
app = create_app()
