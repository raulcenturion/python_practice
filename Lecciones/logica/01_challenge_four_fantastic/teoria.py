# ============================
# 📘 Challenge: Four Fantastic — equilibrio R / J
# ============================
# Historia: en los 4 Fantásticos, Reed Richards (R) y Johnny Storm (J)
# deben estar en equilibrio de poder.
#
# Qué hacemos:
#   Contar cuántas R y cuántas J hay en un texto (sin importar mayúsculas)
#   y devolver True si las cantidades son iguales (incluye 0 = 0).
#
# Por qué:
#   Es un ejercicio clásico de conteo + comparación booleana.
#
# Cómo:
#   1) Normalizar el texto a mayúsculas (o minúsculas).
#   2) Contar "R" y "J" con .count() o un bucle.
#   3) Comparar: return count_r == count_j

# ============================
# 🔹 El problema
# ============================
print("--- El problema ---")
print("Reed = R, Johnny = J. ¿Misma cantidad? → True / False")
print("Sin ninguna letra: 0 == 0 → True")


# ============================
# 🔹 Solución paso a paso
# ============================
print("\n--- Solución paso a paso ---")


def check_is_balanced(text: str) -> bool:
    """Devuelve True si hay la misma cantidad de R y J (case-insensitive)."""
    # Qué: unificar mayúsculas/minúsculas para no distinguir "r" de "R".
    normalizado = text.upper()

    # Cómo: .count() recorre el string y cuenta ocurrencias exactas.
    count_r = normalizado.count("R")  # Reed Richards
    count_j = normalizado.count("J")  # Johnny Storm

    print(f"  texto={text!r} → R={count_r}, J={count_j}")

    # Por qué == alcanza: True si iguales (también cuando ambos son 0).
    return count_r == count_j


# Tip: también podrías contar a mano:
#   count_r = 0
#   count_j = 0
#   for ch in text.upper():
#       if ch == "R":
#           count_r += 1
#       elif ch == "J":
#           count_j += 1
#   return count_r == count_j


# ============================
# 🔹 Demos
# ============================
print("\n--- Demos ---")
casos = [
    "RRJJ",           # 2 y 2 → True
    "RRRRJJ",         # 4 y 2 → False
    "RRJJJJJJ",       # 2 y 6 → False
    "RRRJJJjjjrrr",   # 6 y 6 → True (mezcla mayúsculas/minúsculas)
    "awwwaqAQAQA",    # 0 y 0 → True
    "",               # vacío → True
]

for caso in casos:
    resultado = check_is_balanced(caso)
    print(f"check_is_balanced({caso!r}) → {resultado}")


# ============================
# 🔹 Resumen
# ============================
# - upper()/lower() unifica el case antes de contar.
# - str.count("R") cuenta ocurrencias.
# - Equilibrio = (count_r == count_j), incluyendo 0 == 0.
# - No hace falta if/else: la comparación ya es un bool.
