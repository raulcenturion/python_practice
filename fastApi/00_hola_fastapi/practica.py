# ============================
# 📝 Práctica: Hola FastAPI
# 📘 Teoría: teoria.py | App: main.py (misma carpeta)
# ============================
#
# Cómo correr SOLO esta práctica:
#   ./r fastapi/00
#   .venv/bin/python fastApi/00_hola_fastapi/practica.py

from pathlib import Path
import sys

from fastapi.testclient import TestClient

# Permite `from main import app` aunque corras el archivo desde la raíz del repo.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from main import app

# 🔸 Ejemplo: TestClient habla con la app SIN levantar uvicorn.
client = TestClient(app)
ejemplo = client.get("/")
print("Ejemplo GET / →", ejemplo.status_code, ejemplo.json())

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_salud() -> None:
    # ENUNCIADO:
    # Con TestClient, hacé GET /salud y verificá:
    # - status_code == 200
    # - json == {"status": "ok"}
    #
    # Guía:
    # 1) client = TestClient(app)  (ya existe arriba)
    # 2) r = client.get("/salud")
    # 3) print / assert
    #
    # TIP / EJEMPLO:
    # r = client.get("/salud")
    # print(r.status_code, r.json())

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1 (GET /salud)")


def ejercicio_2_nueva_ruta() -> None:
    # ENUNCIADO:
    # En main.py agregá @app.get("/hola/{nombre}") que retorne
    # {"saludo": f"Hola, {nombre}!"}.
    # Después probalo acá con TestClient: GET /hola/Raúl
    #
    # Guía:
    # 1) En main.py:
    #    @app.get("/hola/{nombre}")
    #    def hola(nombre: str):
    #        return {"saludo": f"Hola, {nombre}!"}
    # 2) Acá: client.get("/hola/Raúl") y mirá .json()
    #
    # TIP: el path param {nombre} llega como argumento tipado str.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2 (ruta /hola/{nombre})")


if __name__ == "__main__":
    print("--- Práctica 00 Hola FastAPI ---")
    for fn in (ejercicio_1_salud, ejercicio_2_nueva_ruta):
        try:
            fn()
            print(f"✅ {fn.__name__}")
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
