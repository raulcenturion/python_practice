# ============================
# 📝 Ejercicios: Scraping básico
# 📘 Teoría: Clases_teoria/scraping/01_basic.py
# ============================

# 🔸 Ejemplo (requiere: pip install requests):
# import requests
# import re
#
# url = "https://example.com"
# response = requests.get(url)
# if response.status_code == 200:
#     title = re.search(r"<title>(.*?)</title>", response.text)
#     print(title.group(1) if title else "Sin título")

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Status code
# Hacé un GET a https://example.com e imprimí status_code.


# Ejercicio 2: Extraer title con regex
# Del HTML de example.com, extráé el contenido de <title> con re.search.


# Ejercicio 3: Contar links
# Contá cuántas veces aparece "<a " (o href=) en el HTML de example.com.
