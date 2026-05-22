###
# Listas metodos
# Los métodos más importantes para listas son:
# append(): Agrega un elemento al final de la lista.
# extend(): Extiende la lista agregando todos los elementos de otra lista.
# insert(): Inserta un elemento en una posición específica.
# remove(): Elimina la primera aparición de un elemento específico.
# pop(): Elimina y devuelve el elemento en una posición específica (por defecto, el último).
# clear(): Elimina todos los elementos de la lista.
# index(): Devuelve el índice de la primera aparición de un elemento específico.
# count(): Cuenta cuántas veces aparece un elemento específico en la lista.
# sort(): Ordena los elementos de la lista en orden ascendente (o según una función personalizada).
# sorted(): Devuelve una nueva lista ordenada sin modificar la original.
# reverse(): Invierte el orden de los elementos en la lista.
# copy(): Devuelve una copia superficial de la lista.
lista = [1,2,3,4,5, 6]
lista.insert(2, "nuevo") # Inserta "nuevo" en la posición 2
print(lista)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False