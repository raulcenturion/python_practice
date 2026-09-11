# ============================
# 📘 main.py — app mínima FastAPI
# ============================
# Este módulo define la app. Uvicorn la carga así:
#   uvicorn fastApi.00_hola_fastapi.main:app --reload
#
# "main:app" = archivo main.py → variable app

from fastapi import FastAPI

# Creamos la aplicación (como MiniApp de la lección 14, pero real).
app = FastAPI(
    title="welcomePy — Hola FastAPI",
    description="Primera app del curso. Docs en /docs",
    version="0.1.0",
)


@app.get("/")
def home():
    """GET / → JSON de bienvenida."""
    return {"mensaje": "Hola FastAPI", "ok": True}


@app.get("/salud")
def salud():
    """Endpoint simple para chequear que el server vive."""
    return {"status": "ok"}
