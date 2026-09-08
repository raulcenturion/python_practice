# ============================
# 📘 Librerías externas en Python
# ============================
# Python tiene una enorme comunidad que crea paquetes/librerías de terceros.
# Se instalan con pip (el gestor de paquetes de Python).
#
# Idea mental:
#   stdlib     → viene con Python (math, os, json...) → import directo
#   externa    → se instala con pip (requests, pydantic...) → luego import
#
# Siempre preferí instalar dentro de un venv (ver lección 18).

print("--- Lección 17: Librerías externas ---")

# ============================
# 🔹 Instalar una librería (comandos de terminal)
# ============================
# Desde la terminal (con el venv activado):
#   pip install nombre_paquete
#   pip install cowpy requests flask
#
# Ver librerías instaladas:
#   pip list
#   pip freeze
#
# Guardar dependencias en un archivo:
#   pip freeze > requirements.txt
#
# Instalar desde requirements.txt (otra máquina / CI):
#   pip install -r requirements.txt

# ============================
# 🔹 Ejemplo con cowpy (librería divertida)
# ============================
# cowpy dibuja un “ASCII cow” hablando el mensaje que le pases.
# Primero: pip install cowpy
print("\n--- Ejemplo: cowpy ---")
try:
    # Importamos solo si está instalada; si no, avisamos sin romper la lección.
    from cowpy import cow  # type: ignore[import-not-found]

    # Cowacter() crea el “personaje”; milk(texto) genera el dibujo con el mensaje.
    my_cow = cow.Cowacter()
    print("cowpy milk:", my_cow.milk("I love Python"))
except ImportError:
    print("aviso:", "⚠️ cowpy no está instalada. Ejecutá: pip install cowpy")

# ============================
# 🔹 Ejemplo con requests (HTTP)
# ============================
# requests simplifica llamadas HTTP (GET/POST...) frente a urllib de la stdlib.
# Primero: pip install requests
print("\n--- Ejemplo: requests ---")
try:
    import requests

    # GET a una API de prueba pública. La URL devuelve un todo de ejemplo en JSON.
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    # .json() parsea el body JSON → dict de Python.
    print("response.json():", response.json())
except ImportError:
    print("aviso:", "⚠️ requests no está instalada. Ejecutá: pip install requests")

# ============================
# 🔹 Diferencia entre módulo, paquete y librería
# ============================
# Módulo:   un archivo .py con funciones/clases (tuyo o de la stdlib)
# Paquete:  una carpeta con __init__.py y varios módulos
# Librería: un paquete de terceros que se instala con pip
# Stdlib:   la biblioteca estándar de Python (math, os, sys, json, datetime...)

# ============================
# 🔹 Librerías populares por categoría
# ============================
# 🌐 Web:        requests, flask, django, fastapi
# 📊 Datos:      pandas, numpy, matplotlib
# 🧪 Testing:    pytest, unittest
# 🤖 ML/AI:      scikit-learn, tensorflow, pytorch
# 🕷️ Scraping:   beautifulsoup4, scrapy, playwright
# 📝 Utilidades: rich, click, pydantic

# ============================
# 🔹 Resumen
# ============================
# - pip install nombre → descarga e instala una librería externa
# - pip freeze > requirements.txt documenta dependencias del proyecto
# - try/except ImportError permite demos que no rompen si falta el paquete
# - requests: HTTP sencillo; response.json() → dict
# - Instalá siempre dentro de un venv para no mezclar con el sistema
# 💡 Leé el README del paquete: casi siempre muestra el import exacto
