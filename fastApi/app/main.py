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

from dotenv import load_dotenv

load_dotenv()

from app.api.v1.auth.router import router as auth_router
from app.api.v1.posts.router import router as post_router
from app.core.db import Base, engine

from fastapi import FastAPI


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

    return app


# uvicorn y `fastapi dev` buscan esta variable: app.
app = create_app()
