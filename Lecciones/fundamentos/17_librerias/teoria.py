# ============================
# 📘 Librerías externas en Python
# ============================
# Python tiene una enorme comunidad que crea paquetes/librerías de terceros.
# Se instalan con pip (el gestor de paquetes de Python).

# ============================
# 🔹 Instalar una librería
# ============================
# Desde la terminal:
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
# Instalar desde requirements.txt:
#   pip install -r requirements.txt

# ============================
# 🔹 Ejemplo con cowpy (librería divertida)
# ============================
# Primero instalar: pip install cowpy
try:
    from cowpy import cow
    my_cow = cow.Cowacter()
    print(my_cow.milk("I love Python"))
except ImportError:
    print("⚠️ cowpy no está instalada. Ejecutá: pip install cowpy")

# ============================
# 🔹 Ejemplo con requests (HTTP)
# ============================
# Primero instalar: pip install requests
try:
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.json())
except ImportError:
    print("⚠️ requests no está instalada. Ejecutá: pip install requests")

# ============================
# 🔹 Diferencia entre módulo y librería
# ============================
# Módulo: un archivo .py con funciones/clases (puede ser tuyo o de la stdlib)
# Paquete: una carpeta con __init__.py y varios módulos
# Librería: un paquete de terceros que se instala con pip
# Stdlib: la biblioteca estándar de Python (math, os, sys, json, datetime, etc.)

# ============================
# 🔹 Librerías populares por categoría
# ============================
# 🌐 Web:        requests, flask, django, fastapi
# 📊 Datos:      pandas, numpy, matplotlib
# 🧪 Testing:    pytest, unittest
# 🤖 ML/AI:      scikit-learn, tensorflow, pytorch
# 🕷️ Scraping:   beautifulsoup4, scrapy, playwright
# 📝 Utilidades: rich, click, pydantic
