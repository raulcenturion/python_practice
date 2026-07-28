# ============================
# 📝 Ejercicios: Requests / APIs
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo (descomentá para probar; requiere red):
# import urllib.request
# import json
#
# url = "https://jsonplaceholder.typicode.com/posts/1"
# with urllib.request.urlopen(url) as response:
#     data = json.loads(response.read().decode("utf-8"))
#     print(data["title"])

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: GET sin dependencias
# Usá urllib.request para obtener https://jsonplaceholder.typicode.com/posts/1
# Parseá el JSON e imprimí el title.


# Ejercicio 2: GET con requests
# Instalá requests si hace falta. Pedí la misma URL e imprimí status_code y el body.


# Ejercicio 3: Lista de posts
# Pedí https://jsonplaceholder.typicode.com/posts y mostrá los títulos de los 3 primeros.


# Ejercicio 4: Manejo de errores
# Intentá una URL inválida y capturá el error (URLError o RequestException).
# Imprimí un mensaje claro.
