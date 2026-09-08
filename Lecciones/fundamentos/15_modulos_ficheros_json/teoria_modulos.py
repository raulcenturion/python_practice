# ============================
# 📘 Módulos y Paquetes en Python
# ============================
# Un módulo es un archivo .py con funciones, clases o variables reutilizables.
# Un paquete es una carpeta con un __init__.py y varios módulos dentro.
#
# Idea mental:
#   math_utils.py          → módulo (un archivo)
#   my_package/            → paquete (carpeta)
#   ├── __init__.py
#   └── messages.py        → módulo dentro del paquete
#
# ⚠️ Ejecutá desde esta carpeta de lección:
#    python teoria_modulos.py
# (así Python encuentra math_utils y my_package en el mismo directorio)

# ============================
# 🔹 Crear un módulo
# ============================
# Simplemente creás un archivo .py. En esta lección ya existe math_utils.py:
#   def addition(num1, num2):
#       return num1 + num2
# Cualquier .py del directorio (o en el PYTHONPATH) puede importarse.

# ============================
# 🔹 Formas de importar un módulo
# ============================
# import math_utils               → importa TODO el módulo
# math_utils.addition(3, 4)       → se accede con el prefijo del módulo
#
# from math_utils import addition → importa solo la función
# addition(3, 4)                  → se usa directamente (sin prefijo)
#
# import math_utils as mu         → alias corto para el módulo
# mu.addition(3, 4)

# ============================
# 🔹 Importar desde un paquete
# ============================
# Un paquete es una carpeta con __init__.py (puede estar vacío):
#   my_package/
#   ├── __init__.py
#   └── messages.py      (contiene greet / bye)
#
# from my_package import messages
# messages.greet("Raúl")

# ============================
# 🔹 Ejemplo práctico (módulo + paquete locales)
# ============================
print("--- Importar módulo y paquete local ---")

# math_utils.py está en la MISMA carpeta que este archivo.
# Al hacer import, Python busca en sys.path (incluye el dir actual).
import math_utils

# my_package es una carpeta; messages es el módulo messages.py dentro.
from my_package import messages

# Llamamos addition del módulo: num1=3, num2=4 → 7.
result = math_utils.addition(3, 4)
print("Suma:", result)  # 7

# greet / bye vienen de my_package/messages.py; el nombre va interpolado en el f-string.
print("greet:", messages.greet("Raúl"))  # Hola, Raúl
print("bye:", messages.bye("Raúl"))    # Adiós, Raúl

# ============================
# 🔹 Módulos de la biblioteca estándar (stdlib)
# ============================
# Python trae muchos módulos ya incluidos: no hace falta pip install.
print("\n--- Biblioteca estándar (math / datetime / os) ---")

import math

# math.pi es una constante del módulo; math.sqrt calcula la raíz cuadrada.
print("Pi:", math.pi)                # 3.14159...
print("Raíz de 16:", math.sqrt(16))  # 4.0

import datetime

# datetime.now(UTC) → momento actual en UTC; .date() deja solo año-mes-día.
hoy = datetime.datetime.now(datetime.UTC).date()
print("Hoy es:", hoy)

import os

# getcwd() = get current working directory (desde dónde se ejecutó el script).
print("Directorio actual:", os.getcwd())

# Otros módulos útiles de la stdlib:
# sys      → argumentos de línea de comandos, info del sistema
# json     → leer/escribir JSON
# random   → números aleatorios
# re       → expresiones regulares
# pathlib  → manejo moderno de rutas de archivos

# ============================
# 🔹 Buenas prácticas
# ============================
# ✅ Usá nombres descriptivos para módulos y funciones
# ✅ Mantené cada módulo enfocado en una sola responsabilidad
# ✅ Documentá funciones con docstrings
# ✅ Evitá imports circulares (A importa B y B importa A)
# ✅ Usá entornos virtuales (venv) para manejar dependencias

# ============================
# 🔹 Resumen
# ============================
# - Módulo: archivo .py reutilizable (import nombre_modulo)
# - Paquete: carpeta con __init__.py + módulos (from paquete import modulo)
# - import X / from X import Y / import X as alias → tres formas habituales
# - Stdlib: math, datetime, os, json, pathlib, etc. (vienen con Python)
# - Para módulos locales: ejecutá el script desde la carpeta que los contiene
# 💡 Separá código en módulos cuando crezca: más claro y reutilizable
