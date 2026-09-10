# ============================
# 📝 Challenge: Jurassic Park
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo (idea):
# egg_list = [3, 4, 7, 5, 8]
# # pares: 4 + 8 = 12

# ============================
# ENUNCIADO
# ============================
# Cada número de la lista = huevos puestos por un dinosaurio.
# Solo los PARES son de carnívoros (T-Rex).
# Devolvé la suma de los números pares.
#
# Casos esperados:
#   count_carnivore_dinosaur_eggs([2, 3, 4, 5, 6])  → 12
#   count_carnivore_dinosaur_eggs([1, 3, 5])        → 0
#   count_carnivore_dinosaur_eggs([3, 4, 7, 5, 8])  → 12

# Guía:
# 1) Inicializá total = 0
# 2) Recorré egg_list
# 3) Si eggs % 2 == 0, sumá al total
# 4) Devolvé total

# TIP / EJEMPLO (comentado):
#   total = 0
#   for eggs in egg_list:
#       if eggs % 2 == 0:
#           total += eggs
#   return total
# # o: return sum(n for n in egg_list if n % 2 == 0)


def count_carnivore_dinosaur_eggs(egg_list: list[int]) -> int:
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá count_carnivore_dinosaur_eggs")


if __name__ == "__main__":
    print("Probá tu solución (si aún no está → Pendiente):")
    for caso in ([2, 3, 4, 5, 6], [1, 3, 5], [3, 4, 7, 5, 8]):
        try:
            print(f"  count_carnivore_dinosaur_eggs({caso}) → {count_carnivore_dinosaur_eggs(caso)}")
        except NotImplementedError:
            print(f"  count_carnivore_dinosaur_eggs({caso}) → Pendiente")
            break
