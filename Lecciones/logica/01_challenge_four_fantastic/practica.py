# ============================
# 📝 Challenge: Four Fantastic
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo (idea):
# text = "RrJj"
# # upper → "RRJJ" → R=2, J=2 → True

# ============================
# ENUNCIADO
# ============================
# Reed Richards = R, Johnny Storm = J.
# Creá check_is_balanced(text) que:
# - cuente R y J sin importar mayúsculas/minúsculas
# - retorne True si hay la misma cantidad (incluye 0 = 0)
# - retorne False si no
#
# Casos esperados:
#   check_is_balanced("RRRJJJjjjrrr")  → True   # 6R y 6J
#   check_is_balanced("RRRJ")          → False
#   check_is_balanced("")              → True
#   check_is_balanced("abc")           → True

# Guía:
# 1) Convertí el texto a mayúsculas: text.upper()
# 2) Contá "R" y "J" con .count()
# 3) Devolvé count_r == count_j

# TIP / EJEMPLO (comentado):
#   normalizado = text.upper()
#   return normalizado.count("R") == normalizado.count("J")


def check_is_balanced(text: str) -> bool:
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá check_is_balanced")


if __name__ == "__main__":
    print("Probá tu solución (si aún no está → Pendiente):")
    for caso in ("RRRJJJjjjrrr", "RRRJ", "", "abc"):
        try:
            print(f"  check_is_balanced({caso!r}) → {check_is_balanced(caso)}")
        except NotImplementedError:
            print(f"  check_is_balanced({caso!r}) → Pendiente")
            break
