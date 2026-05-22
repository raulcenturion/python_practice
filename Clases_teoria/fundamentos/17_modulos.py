# ============================
# 📘 Módulos y Paquetes en Python
# ============================
# Un módulo es un archivo .py con funciones, clases o variables reutilizables.
# Un paquete es una carpeta con un __init__.py y varios módulos dentro.

# ============================
# 🔹 Crear un módulo
# ============================
# Simplemente creás un archivo .py. Ejemplo: math_utils.py contiene:
#   def addition(num1, num2):
#       return num1 + num2

# ============================
# 🔹 Importar un módulo
# ============================
# import math_utils               → importa todo el módulo
# math_utils.addition(3, 4)       → se accede con el prefijo del módulo

# from math_utils import addition → importa solo la función
# addition(3, 4)                  → se usa directamente

# import math_utils as mu         → alias para el módulo
# mu.addition(3, 4)

# ============================
# 🔹 Importar desde un paquete
# ============================
# Un paquete es una carpeta con __init__.py:
#   my_package/
#   ├── __init__.py      (puede estar vacío)
#   └── messages.py      (contiene funciones)
#
# from my_package import messages
# messages.greet("Raúl")

# ============================
# 🔹 Ejemplo práctico
# ============================
# ⚠️ Estos imports funcionan si ejecutás desde la carpeta fundamentos/
# python 17_modulos.py

import math_utils
from my_package import messages

result = math_utils.addition(3, 4)
print(f"Suma: {result}")  # 7

print(messages.greet("Raúl"))  # Hola, Raúl
print(messages.bye("Raúl"))    # Adiós, Raúl

# ============================
# 🔹 Módulos de la biblioteca estándar
# ============================
# Python viene con módulos muy útiles ya incluidos:

import math
print(f"Pi: {math.pi}")                # 3.14159...
print(f"Raíz de 16: {math.sqrt(16)}")  # 4.0

import datetime
hoy = datetime.date.today()
print(f"Hoy es: {hoy}")

import os
print(f"Directorio actual: {os.getcwd()}")

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
