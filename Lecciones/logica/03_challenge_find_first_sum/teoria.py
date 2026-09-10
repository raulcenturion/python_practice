# ============================
# 📘 Challenge: Find first sum — primer par que suma goal
# ============================
# Qué hacemos:
#   Dada una lista nums y un goal, encontrar los DOS primeros números
#   que sumen goal y devolver SUS ÍNDICES. Si no hay, None.
#
# Ejemplo:
#   nums = [4, 5, 6, 2], goal = 8
#   → índices [2, 3] porque 6 + 2 = 8
#
# Por qué importa el orden:
#   "Primeros" = el par que aparece antes al recorrer de izquierda a derecha
#   (el segundo índice lo más temprano posible; ante empates, el primero también).
#
# Cómo (recomendado): O(n) con un diccionario de valores ya vistos.
# Alternativa: fuerza bruta O(n²) con doble for (más abajo, comentada).

# ============================
# 🔹 Idea O(n) con dict
# ============================
print("--- Idea O(n) con diccionario ---")
print("Por cada valor, mirá qué 'falta' para llegar al goal:")
print("  missing = goal - value")
print("Si missing ya lo viste → tenés el par.")
print("Si no → guardá value → índice en el dict y seguí.")


# ============================
# 🔹 Solución O(n)
# ============================
print("\n--- Solución O(n) ---")


def find_first_sum(nums: list[int], goal: int):
    """Devuelve [i, j] del primer par que suma goal, o None."""
    seen = {}  # valor → índice donde apareció

    for index, value in enumerate(nums):
        missing = goal - value
        print(f"  i={index}, value={value}, falta={missing}, vistos={seen}")

        # Si el complemento ya está, ese índice + el actual forman el par.
        if missing in seen:
            return [seen[missing], index]

        # Guardamos el valor actual para futuros complementos.
        # (Si el valor se repite, queda el índice más reciente; está bien
        #  mientras busquemos el primer cierre válido de izquierda a derecha.)
        seen[value] = index

    return None


# Tip — fuerza bruta O(n²) (alternativa pedagógica, NO usada abajo):
#   def find_first_sum_brute(nums, goal):
#       for i in range(len(nums)):
#           for j in range(i + 1, len(nums)):
#               if nums[i] + nums[j] == goal:
#                   return [i, j]
#       return None
# Es más fácil de leer, pero compara todos los pares → lento en listas grandes.


# ============================
# 🔹 Demos
# ============================
print("\n--- Demo: [4, 5, 6, 2], goal=8 ---")
nums = [4, 5, 6, 2]
goal = 8
resultado = find_first_sum(nums, goal)
print(f"resultado → {resultado}")  # [2, 3]

print("\n--- Demo: sin solución ---")
print("resultado →", find_first_sum([1, 2, 3], 10))  # None

print("\n--- Demo: el par está al inicio ---")
print("resultado →", find_first_sum([3, 5, 1, 2], 8))  # [0, 1] → 3+5


# ============================
# 🔹 Resumen
# ============================
# - Fuerza bruta: doble for → O(n²), simple.
# - Dict de vistos: por cada n mirás (goal - n) → O(n) tiempo, O(n) memoria.
# - Devolvés índices [i, j], no los valores.
# - Si no hay par → None.
