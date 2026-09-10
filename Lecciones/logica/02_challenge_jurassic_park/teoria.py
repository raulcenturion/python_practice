# ============================
# 📘 Challenge: Jurassic Park — huevos de carnívoros
# ============================
# Historia: en Jurassic Park, los dinosaurios carnívoros (T-Rex)
# depositan un número PAR de huevos. Cada número de la lista es
# la cantidad de huevos que puso un dinosaurio.
#
# Qué hacemos:
#   Sumar solo los números pares de una lista.
#
# Por qué:
#   Práctica de filtro + acumulación (bucles, % 2, sum/filter).
#
# Cómo:
#   Recorrer la lista; si n % 2 == 0, sumar n al total.

# ============================
# 🔹 Recordatorio: ¿par o impar?
# ============================
print("--- Recordatorio: módulo % ---")
print("n % 2 == 0 → par")
print("n % 2 == 1 → impar")
print("Ejemplo: 4 % 2 =", 4 % 2, "| 7 % 2 =", 7 % 2)


# ============================
# 🔹 Solución con bucle
# ============================
print("\n--- Solución con bucle ---")


def count_carnivore_dinosaur_eggs(egg_list: list[int]) -> int:
    """Suma solo los números pares (huevos de carnívoros)."""
    total = 0
    for eggs in egg_list:
        # Qué: ¿este dinosaurio es carnívoro? → cantidad par.
        if eggs % 2 == 0:
            total += eggs
            print(f"  + {eggs} (par) → total parcial = {total}")
        else:
            print(f"  se ignora {eggs} (impar)")
    return total


# Tip (forma corta con filter + sum):
#   return sum(filter(lambda x: x % 2 == 0, egg_list))
# Tip (comprensión):
#   return sum(n for n in egg_list if n % 2 == 0)


# ============================
# 🔹 Demos
# ============================
print("\n--- Demo 1: [3, 4, 7, 5, 8] ---")
egg_list = [3, 4, 7, 5, 8]
resultado = count_carnivore_dinosaur_eggs(egg_list)
print(f"Suma de pares = {resultado}")  # 4 + 8 = 12

print("\n--- Demo 2: solo impares ---")
print("resultado:", count_carnivore_dinosaur_eggs([1, 3, 5]))  # 0

print("\n--- Demo 3: [2, 3, 4, 5, 6] ---")
print("resultado:", count_carnivore_dinosaur_eggs([2, 3, 4, 5, 6]))  # 12


# ============================
# 🔹 Resumen
# ============================
# - Par: n % 2 == 0
# - Acumulá en un total solo los pares.
# - Alternativas: sum(filter(...)) o sum(... for ... if ...)
# - Lista vacía o sin pares → 0
