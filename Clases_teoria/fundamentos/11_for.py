# Bucles for
# Permiten iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena de texto)
# o cualquier otro objeto iterable.
# La sintaxis básica es:
# for elemento in secuencia:
#     # Hacer algo con elemento
# Ejemplo 1: Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta) 
# Ejemplo 2: Iterar sobre una cadena de texto
for letra in "hola":
    print(letra)
# Ejemplo 3: Usar la función range()
# range(inicio, fin, paso)
for numero in range(1, 11):  # Del 1 al 10
    print(numero)
# Ejemplo 4: Iterar sobre un diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# Ejemplo 5: Anidar bucles for
for i in range(1, 4):  # Filas
    for j in range(1, 4):  # Columnas
        print(f"({i}, {j})")
# Ejemplo 6: Usar break y continue
for numero in range(1, 11):
    if numero == 5:
        break  # Sale del bucle cuando numero es 5
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)  # Imprime solo números impares menores que 5
# Ejemplo 7: Usar else con bucles for
for numero in range(1, 6):
    print(numero)
else:
    print("Bucle terminado")
# El bloque else se ejecuta cuando el bucle termina normalmente (sin break)
# Ejemplo 8: Iterar sobre un conjunto (set)
colores = {"rojo", "verde", "azul"}
for color in colores:
    print(color)
# Ejemplo 9: Iterar sobre una tupla
punto = (10, 20)
for coordenada in punto:
    print(coordenada)
# Ejemplo 10: Usar enumerate() para obtener el índice y el valor
animales = ["perro", "gato", "conejo"]
for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")
# Ejemplo 11: Iterar sobre múltiples listas con zip()
nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
# Ejemplo 12: Listas por comprensión (list comprehensions)
# Crear una nueva lista con los cuadrados de los números del 1 al 10
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)
# Ejemplo 13: Filtrar con listas por comprensión
# Crear una lista con los números pares del 1 al 20
pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)
# Ejemplo 14: Diccionarios por comprensión (dict comprehensions)
# Crear un diccionario con los números del 1 al 5 y sus cuadrados
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(cuadrados_dict)
# Ejemplo 15: Conjuntos por comprensión (set comprehensions)
# Crear un conjunto con los números impares del 1 al 20
impares = {x for x in range(1, 21) if x % 2 != 0}
print(impares)
# Ejemplo 16: Iterar sobre un archivo línea por línea
# with open("archivo.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())
# Ejemplo 17: Usar itertools para combinaciones y permutaciones
import itertools
letras = ['A', 'B', 'C']
combinaciones = itertools.combinations(letras, 2)
for combo in combinaciones:
    print(combo)
permutaciones = itertools.permutations(letras)
for perm in permutaciones:
    print(perm)
# Ejemplo 18: Iterar sobre un rango con pasos negativos
for numero in range(10, 0, -1):  # Del 10 al 1
    print(numero)
# Ejemplo 19: Iterar sobre una lista y modificar sus elementos
numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    numeros[i] *= 2  # Multiplica cada elemento por 2
print(numeros)
# Ejemplo 20: Usar map() para aplicar una función a todos los elementos de una lista
def cuadrado(x):
    return x ** 2
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)
# Ejemplo 21: Usar filter() para filtrar elementos de una lista
def es_par(x):
    return x % 2 == 0
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(es_par, numeros))
print(pares)
# Ejemplo 22: Iterar sobre un rango con números flotantes usando numpy
import numpy as np
for numero in np.arange(0.5, 5.5, 0.5):
    print(numero)

### Enumerate() - Ejemplo extra
# Permite iterar sobre una secuencia y obtener tanto el índice como el valor del elemento
# La sintaxis es:
# for indice, valor in enumerate(secuencia):
#     # Hacer algo con indice y valor
# Ejemplo:
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")
# Esto imprimirá:
# 0: rojo
# 1: verde
# 2: azul
# También se puede especificar un índice inicial:
for indice, color in enumerate(colores, start=1):
    print(f"{indice}: {color}")
# Esto imprimirá:
# 1: rojo
# 2: verde
# 3: azul
# Es útil cuando necesitas el índice de los elementos mientras iteras sobre una lista u otra secuencia.

