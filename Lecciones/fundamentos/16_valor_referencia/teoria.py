# ============================
# 📘 Valor y referencia (mutabilidad)
# ============================
# En Python las variables NO “guardan el valor”: guardan una REFERENCIA
# (un puntero) a un objeto en memoria.
#
# Tipos INMUTABLES: int, float, str, tuple, frozenset, bool, None...
#   - No se pueden modificar “por dentro”.
#   - Reasignar (a = 20) crea/apunta a OTRO objeto; la otra variable no cambia.
#
# Tipos MUTABLES: list, dict, set, bytearray...
#   - Se pueden modificar in-place (append, update, add...).
#   - Si dos variables apuntan al MISMO objeto, el cambio se ve en ambas.
#
# id(x) → identidad del objeto en memoria (útil para “ver” si es el mismo).

print("--- Lección 16: Valor y referencia ---")

# ============================
# 🔹 Tipos inmutables (int)
# ============================
print("\n--- Tipos inmutables (int) ---")

a = 10
# b = a NO copia el número: b apunta al MISMO objeto int que a.
b = a
print("Antes de cambiar a:")
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))
# Mismos ids → a y b referencian el mismo 10.

# a = 20 no modifica el 10: hace que `a` apunte a un objeto NUEVO (20).
# `b` sigue apuntando al 10 original.
a = 20
print("Después de cambiar a:")
print("a:", a, "id(a):", id(a))  # id distinto (nuevo objeto)
print("b:", b, "id(b):", id(b))  # sigue siendo 10

# ============================
# 🔹 Tipos mutables (list)
# ============================
print("\n--- Tipos mutables (list) ---")

lista1 = [1, 2, 3]
# lista2 apunta a la MISMA lista en memoria (no es una copia).
lista2 = lista1
print("Antes de modificar lista1:")
print("lista1:", lista1, "id(lista1):", id(lista1))
print("lista2:", lista2, "id(lista2):", id(lista2))
# Mismos ids → es un solo objeto lista.

# append modifica la lista IN-PLACE: no crea otra lista.
# Como lista2 apunta al mismo objeto, también “ve” el 4.
lista1.append(4)
print("Después de modificar lista1:")
print("lista1:", lista1, "id(lista1):", id(lista1))  # [1, 2, 3, 4]
print("lista2:", lista2, "id(lista2):", id(lista2))  # ¡también [1, 2, 3, 4]!
# ids iguales: no hubo reasignación, solo mutación.

# ============================
# 🔹 Copia superficial vs profunda
# ============================
# Cuando SÍ querés otra lista independiente, usás copy.
import copy

print("\n--- Copia superficial (shallow copy) ---")

# Lista de listas: contenedor exterior + elementos interiores (también listas).
lista_original = [[1, 2], [3, 4]]
# copy.copy copia el contenedor exterior, pero los interiores se COMPARTEN.
copia_superficial = copy.copy(lista_original)

# Modificamos la primera sublista a través de la copia...
copia_superficial[0].append(5)
print("Después de modificar copia_superficial:")
# ...y el cambio aparece también en lista_original[0] (mismo objeto interno).
print("lista_original:", lista_original)          # [[1, 2, 5], [3, 4]]
print("copia_superficial:", copia_superficial)    # [[1, 2, 5], [3, 4]]

print("\n--- Copia profunda (deep copy) ---")

lista_original = [[1, 2], [3, 4]]
# deepcopy clona TODO el árbol: contenedor e interiores son objetos nuevos.
copia_profunda = copy.deepcopy(lista_original)

copia_profunda[0].append(5)
print("Después de modificar copia_profunda:")
# lista_original NO se ve afectada.
print("lista_original:", lista_original)    # [[1, 2], [3, 4]]
print("copia_profunda:", copia_profunda)    # [[1, 2, 5], [3, 4]]

# ============================
# 🔹 Resumen
# ============================
# - Variables guardan referencias a objetos, no “cajas” con el valor dentro
# - Inmutables (int, float, str, tuple): reasignar → nueva referencia
# - Mutables (list, dict, set): modificar in-place afecta TODAS las referencias
# - copy.copy(): copia superficial (comparte objetos anidados)
# - copy.deepcopy(): copia profunda (totalmente independiente)
# - id() muestra la identidad del objeto en memoria
# 💡 Usá deepcopy con listas/dicts anidados para evitar sorpresas
