# ============================
# 📘 Regex 01 — Módulo re
# ============================
# Una expresión regular (regex) es un patrón que describe texto.
# En Python vivimos en el módulo `re`: search, findall, finditer, sub, flags…
#
# ¿Para qué sirve?
# - Buscar patrones en textos grandes
# - Validar formatos (email, teléfono, códigos)
# - Extraer y reemplazar partes de un string
#
# ⚠️ Preferí raw strings: r"..."
# En raw strings la barra \ no se "come" el siguiente carácter.
# Tip: r"\d" es el patrón "dígito"; "\\d" es lo mismo pero más feo de leer.

import re

# ============================
# 🔹 re.search — primera coincidencia
# ============================
# search(patrón, texto) → Match o None.
# No exige que el patrón esté al inicio (eso es más bien re.match).
print("--- re.search ---")

patron = r"Hola"  # raw string: buena costumbre desde el día 1
texto = "Hola mundo"
resultado = re.search(patron, texto)

if resultado:
    print("Encontré el patrón")
    # .group() → el texto que coincidió
    print("group():", resultado.group())
    # .start() / .end() → índices [inicio, fin) en el string original
    print("start():", resultado.start(), "| end():", resultado.end())
else:
    print("No encontré el patrón")

# Tip (SOLVED mini-demo): buscar "IA" y mostrar posición
# texto_ia = "Todo el mundo dice que la IA nos va a quitar el trabajo."
# m = re.search(r"IA", texto_ia)
# print(m.start(), m.end())  # 28 30


# ============================
# 🔹 re.findall — todas las coincidencias (lista)
# ============================
# findall → lista de strings (o tuplas si hay grupos).
# Útil cuando solo te importa QUÉ encontró, no dónde.
print("\n--- re.findall ---")

texto = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
patron = r"Python"
coincidencias = re.findall(patron, texto)
print("findall:", coincidencias)
print("cantidad:", len(coincidencias))


# ============================
# 🔹 re.finditer — todas con posición
# ============================
# finditer → iterador de objetos Match (group, start, end en cada uno).
# Ideal cuando necesitás el texto Y la posición.
print("\n--- re.finditer ---")

for match in re.finditer(r"Python", texto):
    print(match.group(), "→", match.start(), match.end())

# Tip: list(re.finditer(...)) materializa todos los Match si los querés en memoria.


# ============================
# 🔹 re.IGNORECASE — mayúsculas / minúsculas
# ============================
# Flags cambian el comportamiento del patrón sin reescribirlo.
# IGNORECASE (o re.I) hace que "IA" también matchee "ia" e "Ia".
print("\n--- re.IGNORECASE ---")

texto = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
encontradas = re.findall(r"IA", texto, flags=re.IGNORECASE)
print("findall IGNORECASE:", encontradas)

# Tip: también podés pasar flags a search/sub/finditer.


# ============================
# 🔹 re.sub — reemplazar coincidencias
# ============================
# sub(patrón, reemplazo, texto, flags=...) → nuevo string.
# Reemplaza TODAS las coincidencias (salvo que uses count=).
print("\n--- re.sub ---")

texto = "Hola, mundo! Hola de nuevo. Hola otra vez."
nuevo = re.sub(r"hola", "Adiós", texto, flags=re.IGNORECASE)
print("sub:", nuevo)

# Tip: re.sub(r"\d", "*", "abc123") → "abc***"


# ============================
# 🔹 Match: group / start / end (repaso)
# ============================
print("\n--- Match.group / start / end ---")

m = re.search(r"mundo", "Hola mundo cruel")
if m:
    print(f"'{m.group()}' va de {m.start()} a {m.end()}")

# ============================
# 🔹 Resumen
# ============================
# - import re + patrones en r"..."
# - search → primer Match | None
# - findall → lista de coincidencias
# - finditer → Matches con posición
# - IGNORECASE → no distingue mayúsculas
# - sub → reemplaza
# - Match: .group(), .start(), .end()
#
# Práctica: practica.py (misma carpeta)
