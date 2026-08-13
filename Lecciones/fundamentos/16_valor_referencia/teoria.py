# Valor y referencia
# En Python, los tipos de datos se dividen en dos categorías principales: tipos mutables e inmutables.
# Los tipos inmutables incluyen: int, float, str, tuple, frozenset, etc.
# Los tipos mutables incluyen: list, dict, set, bytearray, etc.
# Cuando se asigna un valor a una variable, Python maneja la memoria de manera diferente según el tipo de dato.

print("--- Lección 16: Valor y referencia ---")

# Ejemplo con tipos inmutables
print("\n--- Tipos inmutables (int) ---")
a = 10
b = a  # b apunta a la misma dirección de memoria que a
print("Antes de cambiar a:")
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))
a = 20  # a ahora apunta a una nueva dirección de memoria
print("Después de cambiar a:")
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))

# Ejemplo con tipos mutables
print("\n--- Tipos mutables (list) ---")
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 apunta a la misma dirección de memoria que lista1
print("Antes de modificar lista1:")
print("lista1:", lista1, "id(lista1):", id(lista1))
print("lista2:", lista2, "id(lista2):", id(lista2))
lista1.append(4)  # Modificar lista1 afecta a lista2
print("Después de modificar lista1:")
print("lista1:", lista1, "id(lista1):", id(lista1))
print("lista2:", lista2, "id(lista2):", id(lista2))

# Copias superficiales y profundas
import copy

print("\n--- Copia superficial (shallow copy) ---")
lista_original = [[1, 2], [3, 4]]
copia_superficial = copy.copy(lista_original)
copia_superficial[0].append(5)  # Modificar un elemento interno
print("Después de modificar copia_superficial:")
print("lista_original:", lista_original)
print("copia_superficial:", copia_superficial)

print("\n--- Copia profunda (deep copy) ---")
lista_original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(lista_original)
copia_profunda[0].append(5)  # Modificar un elemento interno
print("Después de modificar copia_profunda:")
print("lista_original:", lista_original)
print("copia_profunda:", copia_profunda)

# ============================
# 🔹 Resumen
# ============================
# - Tipos inmutables (int, float, str, tuple): reasignar crea nueva referencia
# - Tipos mutables (list, dict, set): modificar afecta TODAS las referencias
# - copy.copy(): copia superficial (copia el contenedor, pero comparte los internos)
# - copy.deepcopy(): copia profunda (copia todo, totalmente independiente)
# - id() muestra la dirección de memoria de un objeto
# 💡 Usá deepcopy cuando trabajes con listas/dicts anidados para evitar sorpresas
