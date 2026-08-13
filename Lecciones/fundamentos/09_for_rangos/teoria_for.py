# Bucles for
# Permiten iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena de texto)
# o cualquier otro objeto iterable.
# La sintaxis básica es:
# for elemento in secuencia:
#     # Hacer algo con elemento

import itertools

import numpy as np

LABEL_NUMERO = "numero:"

# Ejemplo 1: Iterar sobre una lista
print("--- for sobre una lista ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("fruta:", fruta)

# Ejemplo 2: Iterar sobre una cadena de texto
print("\n--- for sobre una cadena ---")
for letra in "hola":
    print("letra:", letra)

# Ejemplo 3: Usar la función range()
# range(inicio, fin, paso)
print("\n--- for con range(1, 11) ---")
for numero in range(1, 11):  # Del 1 al 10
    print(LABEL_NUMERO, numero)

# Ejemplo 4: Iterar sobre un diccionario
print("\n--- for sobre un diccionario (.items) ---")
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Ejemplo 5: Anidar bucles for
print("\n--- Bucles for anidados ---")
for i in range(1, 4):  # Filas
    for j in range(1, 4):  # Columnas
        print(f"({i}, {j})")

# Ejemplo 6: Usar break y continue
print("\n--- break y continue ---")
for numero in range(1, 11):
    if numero == 5:
        break  # Sale del bucle cuando numero es 5
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(LABEL_NUMERO, numero)  # Imprime solo números impares menores que 5

# Ejemplo 7: else con for (uso típico: búsqueda)
print("\n--- else con for (búsqueda) ---")
objetivo = 10  # no está en 1..5
for numero in range(1, 6):
    print(LABEL_NUMERO, numero)
    if numero == objetivo:
        print("Encontrado")
        break
else:
    print("No encontrado → else del for")
# El else corre solo si el for terminó sin break

# Ejemplo 8: Iterar sobre un conjunto (set)
print("\n--- for sobre un set ---")
colores = {"rojo", "verde", "azul"}
for color in colores:
    print("color:", color)

# Ejemplo 9: Iterar sobre una tupla
print("\n--- for sobre una tupla ---")
punto = (10, 20)
for coordenada in punto:
    print("coordenada:", coordenada)

# Ejemplo 10: Usar enumerate() para obtener el índice y el valor
print("\n--- enumerate() ---")
animales = ["perro", "gato", "conejo"]
for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")

# Ejemplo 11: Iterar sobre múltiples listas con zip()
print("\n--- zip() ---")
nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Ejemplo 12: Listas por comprensión (list comprehensions)
# Crear una nueva lista con los cuadrados de los números del 1 al 10
print("\n--- List comprehension (cuadrados) ---")
cuadrados = [x**2 for x in range(1, 11)]
print("cuadrados:", cuadrados)

# Ejemplo 13: Filtrar con listas por comprensión
# Crear una lista con los números pares del 1 al 20
print("\n--- List comprehension (pares) ---")
pares = [x for x in range(1, 21) if x % 2 == 0]
print("pares:", pares)

# Ejemplo 14: Diccionarios por comprensión (dict comprehensions)
# Crear un diccionario con los números del 1 al 5 y sus cuadrados
print("\n--- Dict comprehension ---")
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print("cuadrados_dict:", cuadrados_dict)

# Ejemplo 15: Conjuntos por comprensión (set comprehensions)
# Crear un conjunto con los números impares del 1 al 20
print("\n--- Set comprehension (impares) ---")
impares = {x for x in range(1, 21) if x % 2 != 0}
print("impares:", impares)

# Ejemplo 16: Iterar sobre un archivo línea por línea
# Tip: with open("archivo.txt") as f: for linea in f: ...

# Ejemplo 17: Usar itertools para combinaciones y permutaciones
print("\n--- itertools.combinations ---")
letras = ['A', 'B', 'C']
combinaciones = itertools.combinations(letras, 2)
for combo in combinaciones:
    print("combo:", combo)

print("\n--- itertools.permutations ---")
permutaciones = itertools.permutations(letras)
for perm in permutaciones:
    print("perm:", perm)

# Ejemplo 18: Iterar sobre un rango con pasos negativos
print("\n--- range con paso negativo ---")
for numero in range(10, 0, -1):  # Del 10 al 1
    print(LABEL_NUMERO, numero)

# Ejemplo 19: Iterar sobre una lista y modificar sus elementos
print("\n--- Modificar lista mientras se itera ---")
numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    numeros[i] *= 2  # Multiplica cada elemento por 2
print("numeros:", numeros)

# Ejemplo 20: Usar map() para aplicar una función a todos los elementos de una lista
print("\n--- map() ---")
def cuadrado(x):
    return x ** 2
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print("cuadrados:", cuadrados)

# Ejemplo 21: Usar filter() para filtrar elementos de una lista
print("\n--- filter() ---")
def es_par(x):
    return x % 2 == 0
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(es_par, numeros))
print("pares:", pares)

# Ejemplo 22: Iterar sobre un rango con números flotantes usando numpy
print("\n--- numpy.arange (flotantes) ---")
for numero in np.arange(0.5, 5.5, 0.5):
    print(LABEL_NUMERO, numero)

### Enumerate() - Ejemplo extra
# Permite iterar sobre una secuencia y obtener tanto el índice como el valor del elemento
# La sintaxis es:
# for indice, valor in enumerate(secuencia):
#     # Hacer algo con indice y valor
print("\n--- enumerate() (extra) ---")
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")
# Esto imprimirá:
# 0: rojo
# 1: verde
# 2: azul
# También se puede especificar un índice inicial:
print("\n--- enumerate(start=1) ---")
for indice, color in enumerate(colores, start=1):
    print(f"{indice}: {color}")
# Esto imprimirá:
# 1: rojo
# 2: verde
# 3: azul
# Es útil cuando necesitas el índice de los elementos mientras iteras sobre una lista u otra secuencia.
