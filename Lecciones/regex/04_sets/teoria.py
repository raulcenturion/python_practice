# ============================
# 📘 Regex 04 — Sets / clases de caracteres
# ============================
# [...] es una clase de caracteres: matchea UN carácter de los listados.
#
#   [abc]     → a, b o c
#   [a-z]     → rango (de a a z)
#   [0-9]     → dígitos (equivale a \d en ASCII básico)
#   [^abc]    → cualquier carácter QUE NO sea a, b ni c
#   [aeiou]   → vocales
#
# Dentro de [] muchos metacaracteres pierden magia (salvo ^ al inicio, -, \).

import re

# ============================
# 🔹 Clase simple [ ]
# ============================
print("--- Clases [ ] ---")

texto = "Hola mundo"
print("vocales:", re.findall(r"[aeiou]", texto))

texto = "man ran fan ñan ban"
print("[mfb]an:", re.findall(r"[mfb]an", texto))
# Tip: "ñan" no entra; "ran" tampoco (r no está en [mfb]).


# ============================
# 🔹 Rangos [a-z] [0-9] [A-Z]
# ============================
print("\n--- Rangos ---")

texto = "22"
print("[4-9] en '22':", re.findall(r"[4-9]", texto))  # [] — 2 no está en 4-9

texto = "RaUl CeNtUrIoN 2026"
print("mayúsculas:", re.findall(r"[A-Z]", texto))
print("dígitos [0-9]:", re.findall(r"[0-9]", texto))

# Tip: el guion - define rango solo entre dos extremos: [a-z].
# Para un guion literal: [-a-z] o [a-z-] (al borde).


# ============================
# 🔹 Negación [^ ]
# ============================
# ^ justo DESPUÉS de [ niega la clase.
print("\n--- Negación [^] ---")

texto = "Hola mundo"
print("no vocales:", re.findall(r"[^aeiou]", texto))
# Incluye espacios, consonantes, etc.

print("no dígitos en abc123xyz:", re.findall(r"[^0-9]", "abc123xyz"))


# ============================
# 🔹 \b + clase — palabras exactas
# ============================
# Sin \b, "man" puede aparecer dentro de "omniman" / "bandana".
print("\n--- \\b + clase ---")

texto = "omniman fanatico man bandana fan ban"
print(r"\b[mfb]an\b:", re.findall(r"\b[mfb]an\b", texto))


# ============================
# 🔹 Demo: username simple
# ============================
# Letras, dígitos, y algunos símbolos comunes: . _ % + -
# ^...$ ancla toda la cadena (debe cumplir el patrón de punta a punta).
print("\n--- Demo username ---")

patron_user = r"^[\w._%+-]+$"
for username in ("raul_69", "rub.$ius+", "invalido!", ""):
    ok = bool(re.search(patron_user, username))
    print(f"  {username!r} →", "válido" if ok else "inválido")


# ============================
# 🔹 Demo: email simple (didáctico, no RFC completo)
# ============================
# Forma aproximada: local@dominio.tld (tld de 2+ letras).
# Casos corner que un patrón naive suele fallar: subdominios, + en local, etc.
print("\n--- Demo email simple ---")

patron_email = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
ejemplos = [
    "raul@mail.com",
    "malo@",
    "ok@ok.py",
    "lo.que+sea@shopping.online",
    "michael@gov.co.uk",
]
for email in ejemplos:
    m = re.search(patron_email, email)
    print(f"  {email!r} →", "OK" if m else "NO")

# Tip: validar emails "de verdad" es más complejo; esto es solo práctica de sets.
# Tip: [a-zA-Z] evita que \w meta dígitos en el TLD si no querés.

# ============================
# 🔹 Resumen
# ============================
# - [abc] un carácter de ese conjunto
# - [a-z0-9] rangos
# - [^...] negación
# - Combiná con ^ $ + cuantificadores para validar strings enteros
# - Username / email simples = demos; no reemplazan librerías de validación
#
# Práctica: practica.py (misma carpeta)
