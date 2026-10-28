# Arranque. Carga el .env, crea la tabla y publica el router.
# Repo: ricardocuellar/Devtalles-Fastapi-Webhooks.
#
# Desde webhooks/:
#   ../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8004
# Swagger: http://127.0.0.1:8004/docs
# El comando y el curl firmado están en el README de la raíz, "Cómo levantar".

from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv

from app.db import init_db

# from fastapi queda después de app. La carpeta fastapi/ del repo hace que
# ruff lo cuente como paquete local.
from fastapi import FastAPI

from .github_webhook import router as github_router

# python-dotenv. load_dotenv mete el archivo en os.environ.
# La clase llama load_dotenv() sin ruta, y después de importar el router.
# Sin ruta lee el .env de la carpeta del comando. Esta ruta es webhooks/.env,
# al lado de app/, aunque el comando salga de otro lado.
# El secreto y la URL de Discord se leen en cada request, no al importar.
# Por eso este llamado puede ir después de los imports y igual los ve.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Crea las tablas al arrancar. Al cerrar, no hay nada que apagar."""
    # Sigue en async aunque init_db() no se espera. FastAPI pide un
    # asynccontextmanager: el yield separa el arranque del cierre.
    # La clase llama al parámetro app y tampoco lo usa. FastAPI lo pasa.
    # Startup
    init_db()
    yield
    # Shutdown


app = FastAPI(lifespan=lifespan, title="Webhooks")

# Sin prefix. Las rutas quedan /webhooks/github y /issues, como en la clase.
app.include_router(github_router)
