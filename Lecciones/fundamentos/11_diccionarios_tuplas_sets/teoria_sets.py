# Sets
# Un conjunto es una colección de elementos únicos y no ordenados.
# Se definen utilizando llaves {} o la función set().
# Ejemplo:
mi_conjunto = {1, 2, 3, 4, 5}
otro_conjunto = set([4, 5, 6, 7, 8])
print("Conjunto 1:", mi_conjunto)
print("Conjunto 2:", otro_conjunto)
# Operaciones con conjuntos
# Unión
union = mi_conjunto | otro_conjunto
print("Unión:", union)
# Intersección
interseccion = mi_conjunto & otro_conjunto
print("Intersección:", interseccion)
# Diferencia
diferencia = mi_conjunto - otro_conjunto
print("Diferencia:", diferencia)
# Diferencia simétrica
diferencia_simetrica = mi_conjunto ^ otro_conjunto
print("Diferencia Simétrica:", diferencia_simetrica)
# Métodos útiles
mi_conjunto.add(6)
print("Después de añadir 6:", mi_conjunto)
mi_conjunto.remove(3)
print("Después de eliminar 3:", mi_conjunto)
print("¿4 está en el conjunto?", 4 in mi_conjunto)
print("¿3 está en el conjunto?", 3 in mi_conjunto)
# Longitud del conjunto
print("Longitud del conjunto:", len(mi_conjunto))
# Iterar sobre un conjunto
for elemento in mi_conjunto:
    print("Elemento:", elemento)
# Conjuntos inmutables
conjunto_inmutable = frozenset([1, 2, 3])
print("Conjunto inmutable:", conjunto_inmutable)
# Los conjuntos son útiles para eliminar duplicados y realizar operaciones matemáticas de teoría de conjuntos. 
# Sin embargo, no mantienen el orden de los elementos y no permiten elementos mutables como listas o diccionarios.
# Ejemplo avanzado: Encontrar elementos únicos en una lista
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
conjunto_sin_duplicados = set(lista_con_duplicados)
print("Lista sin duplicados:", conjunto_sin_duplicados)
# Ejemplo avanzado: Verificar si un conjunto es subconjunto de otro
subconjunto = {1, 2}
print("¿subconjunto es parte de mi_conjunto?", subconjunto.issubset(mi_conjunto))
# Ejemplo avanzado: Conjuntos disjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
print("¿conjunto_a y conjunto_b son disjuntos?", conjunto_a.isdisjoint(conjunto_b))
# Ejemplo avanzado: Actualizar un conjunto con otro conjunto
mi_conjunto.update({7, 8, 9})
print("Después de actualizar mi_conjunto:", mi_conjunto)
# Ejemplo avanzado: Limpiar un conjunto
mi_conjunto.clear()
print("Después de limpiar mi_conjunto:", mi_conjunto)
# Nota: Los conjuntos son muy útiles en situaciones donde se necesita garantizar la unicidad de los elementos y realizar operaciones de teoría de conjuntos de manera eficiente.
# set no admite repeticiones y no mantiene el orden de los elementos.
# frozenset es una versión inmutable de set, lo que significa que no se pueden añadir ni eliminar elementos después de su creación.
# Se puede utilizar un len set para obtener el número de elementos únicos en una colección.
# add() añade un elemento a un set.
# remove() elimina un elemento de un set. Si el elemento no existe, lanza un error.
# discard() elimina un elemento de un set. Si el elemento no existe, no hace nada.
# pop() elimina y devuelve un elemento arbitrario de un set. Si el set está vacío, lanza un error.
# clear() elimina todos los elementos de un set.
# union() devuelve un nuevo set con todos los elementos de ambos sets.
# intersection() devuelve un nuevo set con los elementos comunes a ambos sets.
# difference() devuelve un nuevo set con los elementos que están en el primer set pero no en el segundo.
# symmetric_difference() devuelve un nuevo set con los elementos que están en uno de los sets pero no en ambos.
# issubset() devuelve True si todos los elementos del set están en otro set.
# issuperset() devuelve True si todos los elementos de otro set están en el set.
# isdisjoint() devuelve True si no hay elementos comunes entre ambos sets.