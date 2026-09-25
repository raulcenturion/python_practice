# ============================
# 📝 Práctica: Hola FastAPI
# 📘 Teoría: 00_hola_teoria.py | App: 00_hola_main.py (misma carpeta)
# ============================
#
# Cómo correr SOLO esta práctica:
#   ./r fastapi/00
#   .venv/bin/python fastApi/00_hola_practica.py

import importlib.util
from pathlib import Path

from fastapi.testclient import TestClient

# 00_hola_main.py no se puede importar con `import` porque el nombre empieza con un número.
_main_path = Path(__file__).with_name("00_hola_main.py")
_spec = importlib.util.spec_from_file_location("hola_main", _main_path)
_main = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_main)
app = _main.app

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
    # En 00_hola_main.py agregá @app.get("/hola/{nombre}") que retorne
    # {"saludo": f"Hola, {nombre}!"}.
    # Después probalo acá con TestClient: GET /hola/Raúl
    #
    # Guía:
    # 1) En 00_hola_main.py:
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
