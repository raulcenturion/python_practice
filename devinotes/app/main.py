# Arranque HTTP de Devinote. Sección 17.
# Se corre desde la carpeta devinotes, para que `app` sea este paquete
# y no el del blog:
#   ../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8001
# El blog sigue en el 8000.
#
# asynccontextmanager → biblioteca estándar. lifespan es el arranque de la API.
# load_dotenv         → python-dotenv. Carga devinotes/.env si existe.
# FastAPI             → la app.
# CORSMiddleware      → starlette, reexportado por FastAPI. El front puede llamar.
# settings            → título, de core/config.py.
# init_db             → sección 17 lo llamaba acá y creaba tablas.
#   Sección 18: las tablas las arma Alembic antes de levantar el servidor.

from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.auth_router import router as auth_router
from app.api.routers.labels_router import router as labels_router
from app.api.routers.notes_router import router as notes_router
from app.api.routers.shares_router import router as shares_router
from app.core.config import settings
from fastapi import FastAPI

# from app.core.db import init_db

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async porque asynccontextmanager lo pide. No hay await.
    # Sección 17:
    #     init_db()
    # Sección 18, la clase deja comentado también el if de entorno:
    #     if settings.ENVIRONMENT == "DEV":
    #         init_db()
    # Antes de este proceso: alembic upgrade head (comandos en core/db.py).
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    swagger_ui_parameters={"persistAuthorization": True},
)

# La clase abre el origen a "*" y a la vez allow_credentials=True.
# El navegador no acepta esa pareja: con credenciales el origen tiene que ser
# uno concreto. Estos son los que ya usa el front del curso.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5555",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# La clase repite prefix="/api/v1" cuatro veces. Sonar mira el texto entre comillas,
# no el nombre de una variable. prefix="PF_RUTAS " (con comillas y un espacio)
# sigue siendo el mismo literal cuatro veces: la variable no se usa.
# prefix espera un solo string. Cada router ya trae el suyo
# (/auth, /notes, /labels, /shares). El común es /api/v1.
API_V1 = "/api/v1"
app.include_router(auth_router, prefix=API_V1)
app.include_router(notes_router, prefix=API_V1)
app.include_router(labels_router, prefix=API_V1)
app.include_router(shares_router, prefix=API_V1)
