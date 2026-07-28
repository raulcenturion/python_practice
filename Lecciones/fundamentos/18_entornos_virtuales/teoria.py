# ============================
# 📘 Entornos virtuales y dependencias
# ============================
# Antes de FastAPI (o cualquier proyecto), aislás las dependencias
# en un entorno virtual para no mezclar paquetes del sistema.

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

# Buenas prácticas:
# - Nunca instales paquetes del proyecto sin tener el venv activado
# - Commiteá requirements.txt; NO commitees la carpeta .venv/
# - Fijá versiones cuando el proyecto crece (fastapi==0.115.0)

# ============================
# 🔹 Verificar si estás dentro de un venv
# ============================
import sys
from pathlib import Path


def esta_en_venv() -> bool:
    # En un venv, sys.prefix apunta al entorno; base_prefix al Python del sistema
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


print(f"¿Corriendo dentro de un venv?: {esta_en_venv()}")
print(f"Python ejecutable: {sys.executable}")
print(f"Prefijo: {sys.prefix}")

# ============================
# 🔹 Leer requirements.txt del proyecto
# ============================
req = Path(__file__).resolve().parents[3] / "requirements.txt"
if req.exists():
    lineas = [
        linea.strip()
        for linea in req.read_text(encoding="utf-8").splitlines()
        if linea.strip() and not linea.strip().startswith("#")
    ]
    print(f"\nDependencias en requirements.txt ({len(lineas)}):")
    for linea in lineas[:5]:
        print(f"  - {linea}")
    if len(lineas) > 5:
        print("  ...")
else:
    print("\nNo se encontró requirements.txt en la raíz del repo.")

# ============================
# 🔹 Resumen (checklist pre-FastAPI)
# ============================
# 1) python3 -m venv .venv
# 2) source .venv/bin/activate
# 3) pip install -r requirements.txt
# 4) (más adelante) pip install fastapi uvicorn
# 5) pip freeze > requirements.txt cuando agregues paquetes
