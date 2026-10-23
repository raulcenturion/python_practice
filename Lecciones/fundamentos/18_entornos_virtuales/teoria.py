# ============================
# 📘 Entornos virtuales y dependencias
# ============================
# Un entorno virtual (venv) es una carpeta con su propio Python + pip + paquetes.
# Antes de FastAPI (o cualquier proyecto), aislás las dependencias ahí
# para no mezclarlas con las del sistema u otros proyectos.
#
# Idea mental:
#   Sistema:  /usr/bin/python3          (paquetes globales)
#   Proyecto: .venv/bin/python          (solo lo de ESTE repo)

print("--- Lección 18: Entornos virtuales ---")

# ============================
# 🔹 ¿Para qué sirve un venv?
# ============================
# - Cada proyecto puede tener sus propias versiones de paquetes
# - Evitás conflictos (ej: un repo pide requests 2.x y otro 1.x)
# - requirements.txt documenta qué instalar en otra máquina/CI

# ============================
# 🔹 Crear y activar (macOS / Linux / zsh)
# ============================
# Desde la raíz del proyecto:
#
#   python3 -m venv .venv
#   source .venv/bin/activate
#
# Verás el prompt con (.venv). Para salir:
#   deactivate
#
# Windows (PowerShell):
#   python -m venv .venv
#   .venv\Scripts\Activate.ps1

# ============================
# 🔹 pip: instalar y congelar dependencias
# ============================
# Con el venv activo:
#   pip install requests
#   pip install fastapi uvicorn pydantic
#   pip list
#   pip freeze > requirements.txt
#   pip install -r requirements.txt
#
# Buenas prácticas:
# - Nunca instales paquetes del proyecto sin tener el venv activado
# - Commiteá requirements.txt; NO commitees la carpeta .venv/
# - Fijá versiones cuando el proyecto crece (fastapi==0.115.0)
#
# Este repo usa esta opción: .venv en la raíz y requirements.txt.
# .gitignore ya ignora .venv/ y .env. La clase pide no subir el entorno
# ni el .env (ahí van claves y la URL de la base).

# ============================
# 🔹 Otras formas de aislar paquetes (clase)
# ============================
# Las cuatro hacen lo mismo: un Python aparte para el proyecto, la lista de
# paquetes guardada, y poder instalar esa lista en otra máquina.
# No se instala Pipenv, Poetry ni uv acá. El día a día de este repo es
# source .venv/bin/activate y pip install -r requirements.txt.

# --- 2) Pipenv: el venv y el lock en un solo comando ---
# pipenv es un paquete. --user lo instala en el usuario, no en el Python global
# del sistema. pipenv install crea el entorno y dos archivos:
#   Pipfile       lo que pediste (requests, fastapi)
#   Pipfile.lock  las versiones exactas, para repetir el mismo entorno
#   pip install --user pipenv
#   pipenv install requests fastapi
#   pipenv shell                         entra al entorno
#   pipenv run uvicorn app:app           corre un comando adentro, sin entrar
#   pipenv requirements > requirements.txt
#   pipenv install -r requirements.txt   instala desde un requirements.txt

# --- 3) Poetry: pyproject.toml + lock ---
# pipx instala programas de Python aislados (Poetry no queda mezclado con
# los paquetes del proyecto). poetry init pregunta nombre y versión y arma
# pyproject.toml. poetry add declara el paquete y lo instala.
# poetry install lee el lock y deja el entorno igual en otra máquina.
#   pipx install poetry
#   poetry init
#   poetry add requests fastapi
#   poetry install
#   poetry shell
#   poetry run uvicorn app.main:app --reload
#   poetry export -f requirements.txt --output requirements.txt --without-hashes
# --without-hashes saca los hashes: el archivo se puede pasar a pip install -r.
# Con Poetry lo que se comparte es pyproject.toml + poetry.lock y se corre
# poetry install. requirements.txt no hace falta si todo el equipo usa Poetry.
# El export de arriba es solo para alguien que instala con pip.

# --- 4) uv: otro instalador, el mismo .venv ---
# uv arma el entorno y usa pip por debajo, más rápido. Los comandos de activar
# son los de venv. El archivo que queda es el mismo requirements.txt.
#   uv venv
#   source .venv/bin/activate          macOS / Linux
#   .venv\Scripts\Activate.ps1         Windows (PowerShell)
#   uv pip install requests fastapi
#   uv pip freeze > requirements.txt
#   uv pip install -r requirements.txt
# uv también lee pyproject.toml, así que puede usarse al lado de Poetry.
# En este repo no hace falta: pip contra requirements.txt alcanza.

# ============================
# 🔹 Verificar si estás dentro de un venv
# ============================
import sys
from pathlib import Path


def esta_en_venv() -> bool:
    # En un venv, sys.prefix apunta al entorno aislado.
    # base_prefix apunta al Python “base” (el del sistema / instalación real).
    # Si son distintos → estamos corriendo DENTRO del venv.
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


print("\n--- Verificar si estás en un venv ---")
# True si ejecutás con .venv/bin/python (o con el venv activado).
print("¿Corriendo dentro de un venv?:", esta_en_venv())
# sys.executable = ruta exacta del intérprete que está corriendo este script.
print("Python ejecutable:", sys.executable)
# sys.prefix = prefijo de instalación (carpeta del venv o del sistema).
print("Prefijo:", sys.prefix)

# ============================
# 🔹 Leer requirements.txt del proyecto
# ============================
print("\n--- Leer requirements.txt del proyecto ---")

# __file__ → este teoria.py
# .parent × 3 → subimos: 18_entornos... → fundamentos → Lecciones → raíz del repo
req = Path(__file__).resolve().parents[3] / "requirements.txt"

if req.exists():
    # Leemos el archivo, ignoramos líneas vacías y comentarios (# ...).
    lineas = [
        linea.strip()
        for linea in req.read_text(encoding="utf-8").splitlines()
        if linea.strip() and not linea.strip().startswith("#")
    ]
    print("Dependencias en requirements.txt:", len(lineas))
    # Mostramos solo las primeras 5 para no saturar la consola.
    for linea in lineas[:5]:
        print("  -", linea)
    if len(lineas) > 5:
        print("  ...")
else:
    print("aviso:", "No se encontró requirements.txt en la raíz del repo.")

# ============================
# 🔹 Resumen (checklist pre-FastAPI)
# ============================
# 1) python3 -m venv .venv
# 2) source .venv/bin/activate
# 3) pip install -r requirements.txt
# 4) (más adelante) pip install fastapi uvicorn
# 5) pip freeze > requirements.txt cuando agregues paquetes
#
# Extra de esta demo:
# - sys.prefix != base_prefix → estás en un venv
# - Path(__file__).parents[N] sirve para ubicar archivos del repo
# 💡 Activá el venv ANTES de pip install; si no, contaminás el sistema
