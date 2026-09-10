# ============================
# 📝 Challenge: Battle
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo (idea):
# lista_a = [2, 4, 2]
# lista_b = [3, 3, 4]
# # 2vs3 → B+1; 4vs4 empate; 2vs4 → B+2 última → "2b"

# ============================
# ENUNCIADO
# ============================
# lista_a y lista_b tienen la misma longitud.
# Cada índice se enfrenta:
# - si a > b → el SUPERÁVIT (a - b) se suma al siguiente de lista_a
# - si b > a → el SUPERÁVIT (b - a) se suma al siguiente de lista_b
# - si empatan → no afectan al siguiente
#
# Resultado final:
# - queda superávit en a (última ronda) → "Xa"
# - queda superávit en b → "Xb"
# - empate → "x"
#
# Casos esperados:
#   battle([2, 4, 2], [3, 3, 4])  → "2b"
#   battle([4, 4, 4], [2, 8, 2])  → "x"
#   battle([5, 1], [1, 1])        → "4a"

# Guía:
# 1) Copiá las listas (a = lista_a.copy(), b = lista_b.copy())
# 2) Recorré i en range(len(a))
# 3) Compará a[i] y b[i]
# 4) Si hay ganador y existe i+1 → sumá el surplus al siguiente
# 5) Si hay ganador y es la última ronda → return f"{surplus}a" o "...b"
# 6) Si terminás el for sin return → return "x"

# TIP / EJEMPLO (comentado):
#   a, b = lista_a.copy(), lista_b.copy()
#   for i in range(len(a)):
#       if a[i] > b[i]:
#           surplus = a[i] - b[i]
#           if i + 1 < len(a):
#               a[i + 1] += surplus
#           else:
#               return f"{surplus}a"
#       elif b[i] > a[i]:
#           surplus = b[i] - a[i]
#           if i + 1 < len(b):
#               b[i + 1] += surplus
#           else:
#               return f"{surplus}b"
#   return "x"


def battle(lista_a: list[int], lista_b: list[int]) -> str:
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá battle")


if __name__ == "__main__":
    print("Probá tu solución (si aún no está → Pendiente):")
    casos = [
        ([2, 4, 2], [3, 3, 4]),
        ([4, 4, 4], [2, 8, 2]),
        ([5, 1], [1, 1]),
    ]
    for la, lb in casos:
        try:
            print(f"  battle({la}, {lb}) → {battle(la, lb)}")
        except NotImplementedError:
            print(f"  battle({la}, {lb}) → Pendiente")
            break
