# ============================
# 📝 Challenge: Find first sum
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo (idea):
# nums = [4, 5, 6, 2]
# goal = 8
# # 6 + 2 = 8 → índices [2, 3]

# ============================
# ENUNCIADO
# ============================
# Dado nums y goal, encontrá los dos primeros números que sumen goal
# y devolvé sus índices [i, j]. Si no hay combinación, None.
#
# Preferí O(n) con un diccionario de valores ya vistos.
#
# Casos esperados:
#   find_first_sum([4, 5, 6, 2], 8)  → [2, 3]
#   find_first_sum([1, 2, 3], 10)    → None
#   find_first_sum([3, 5, 1, 2], 8)  → [0, 1]

# Guía:
# 1) Creá seen = {}  # valor → índice
# 2) Recorré con enumerate(nums)
# 3) missing = goal - value
# 4) Si missing in seen → return [seen[missing], index]
# 5) Si no → seen[value] = index
# 6) Al terminar → None

# TIP / EJEMPLO (comentado):
#   seen = {}
#   for index, value in enumerate(nums):
#       missing = goal - value
#       if missing in seen:
#           return [seen[missing], index]
#       seen[value] = index
#   return None


def find_first_sum(nums: list[int], goal: int):
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá find_first_sum")


if __name__ == "__main__":
    print("Probá tu solución (si aún no está → Pendiente):")
    casos = [
        ([4, 5, 6, 2], 8),
        ([1, 2, 3], 10),
        ([3, 5, 1, 2], 8),
    ]
    for nums, goal in casos:
        try:
            print(f"  find_first_sum({nums}, {goal}) → {find_first_sum(nums, goal)}")
        except NotImplementedError:
            print(f"  find_first_sum({nums}, {goal}) → Pendiente")
            break
