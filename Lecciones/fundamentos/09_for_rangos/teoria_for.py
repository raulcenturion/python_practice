# ============================
# 📘 Bucles for
# ============================
# Idea clave: for recorre UNA VEZ cada elemento de un iterable
# (lista, string, range, tupla, set, dict, etc.).
#
#   for elemento in secuencia:
#       # usar elemento
#
# Diferencia rápida con while:
#   while → repetís mientras una condición sea True (vos controlás el contador)
#   for   → Python te da cada elemento de la secuencia

# ---------------------------
# Imports (¿para qué están acá?)
# ---------------------------
# La mayoría de ejemplos de este archivo usan solo Python "puro"
# (listas, strings, range, dict, etc.) y NO necesitan import.
#
# Estos dos módulos se usan más abajo en secciones EXTRA:
#
# itertools  → herramientas para trabajar con iterables.
#              Acá lo usamos para combinations (parejas sin importar orden)
#              y permutations (todos los órdenes posibles).
#              Ver secciones: "itertools.combinations" y "itertools.permutations".
#
# numpy      → librería de números/arrays (hay que tenerla instalada).
#              Acá solo usamos np.arange(...): como range(), pero con decimales
#              (range normal solo acepta enteros).
#              Ver sección: "numpy.arange (flotantes)".
#              "as np" es un alias corto: escribís np.arange en vez de numpy.arange.
#
# Si todavía no viste módulos/librerías, podés saltear esas secciones extra
# y seguir con el resto del archivo sin problema.
import itertools

import numpy as np

LABEL_NUMERO = "numero:"

# ---------------------------
# for sobre una lista
# ---------------------------
# Meta: imprimir cada fruta. En cada vuelta, 'fruta' vale el elemento actual.
print("--- for sobre una lista ---")
print("Idea: una vuelta por cada elemento de la lista")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("fruta:", fruta)

# ---------------------------
# for sobre un string
# ---------------------------
# Meta: un string también es iterable → recorre letra por letra.
print("\n--- for sobre una cadena ---")
print("Idea: 'hola' se recorre como ['h','o','l','a']")
for letra in "hola":
    print("letra:", letra)

# ---------------------------
# for + range
# ---------------------------
# Meta: números del 1 al 10. range(1, 11) → 1..10 (el 11 no entra).
print("\n--- for con range(1, 11) ---")
print("Idea: range genera los números; for los recorre")
for numero in range(1, 11):
    print(LABEL_NUMERO, numero)

# ---------------------------
# for sobre un diccionario
# ---------------------------
# Meta: ver clave y valor juntos con .items().
# Sin .items() el for solo daría las claves.
print("\n--- for sobre un diccionario (.items) ---")
print("Idea: .items() entrega pares (clave, valor)")
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ---------------------------
# for anidados
# ---------------------------
# Meta: todas las combinaciones (i, j) con i y j de 1 a 3.
# El for de adentro da una vuelta completa por cada vuelta del de afuera.
print("\n--- Bucles for anidados ---")
print("Idea: for interno se ejecuta entero en cada paso del externo")
for i in range(1, 4):  # filas
    for j in range(1, 4):  # columnas
        print(f"({i}, {j})")

# ---------------------------
# break y continue
# ---------------------------
# break    → corta el for YA
# continue → salta al próximo elemento (no ejecuta lo de abajo)
# Meta: imprimir impares menores que 5 (1 y 3). Al llegar a 5, break.
print("\n--- break y continue ---")
print("Idea: continue salta pares; break corta al llegar a 5")
for numero in range(1, 11):
    if numero == 5:
        break
    if numero % 2 == 0:
        continue
    print(LABEL_NUMERO, numero)

# ---------------------------
# else con for (búsqueda)
# ---------------------------
# else corre solo si el for terminó SIN break.
# Uso típico: "recorrí todo y no encontré el objetivo".
print("\n--- else con for (búsqueda) ---")
print("Idea: else = 'terminé el recorrido sin encontrar / sin break'")
objetivo = 10  # no está en 1..5
for numero in range(1, 6):
    print(LABEL_NUMERO, numero)
    if numero == objetivo:
        print("Encontrado")
        break
else:
    print("No encontrado → else del for")

# ---------------------------
# for sobre un set
# ---------------------------
# Meta: recorrer un conjunto. Ojo: el orden NO está garantizado.
print("\n--- for sobre un set ---")
print("Idea: set = elementos únicos, sin orden fijo")
colores = {"rojo", "verde", "azul"}
for color in colores:
    print("color:", color)

# ---------------------------
# for sobre una tupla
# ---------------------------
# Meta: igual que lista, pero la tupla no se puede modificar.
print("\n--- for sobre una tupla ---")
print("Idea: misma forma de recorrer; la tupla es inmutable")
punto = (10, 20)
for coordenada in punto:
    print("coordenada:", coordenada)

# ---------------------------
# enumerate() — índice + valor
# ---------------------------
# Meta: además del elemento, necesitamos su posición (0, 1, 2...).
print("\n--- enumerate() ---")
print("Idea: enumerate(lista) → (índice, valor) en cada vuelta")
animales = ["perro", "gato", "conejo"]
for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")

# --- enumerate() ---
# enumerate(lista) → devuelve pares (índice, valor).
#   Ejemplo: enumerate(["perro","gato","conejo"])
#   genera: (0,"perro"), (1,"gato"), (2,"conejo")
#
# En el for:
# for indice, animal in enumerate(animales):
#   → en cada vuelta desempaqueta el par:
#      - indice → posición del elemento (0,1,2,...)
#      - animal → el valor de la lista en esa posición
#
# Resultado:
# 0: perro
# 1: gato
# 2: conejo
#
# En resumen:
# - enumerate() te da índice + valor en cada iteración.
# - Es más práctico que usar range(len(lista)), porque
#   directamente entrega el elemento junto con su posición.


# ---------------------------
# zip() — recorrer dos listas a la vez
# ---------------------------
# Meta: emparejar nombres con edades. Se corta con la lista más corta.
print("\n--- zip() ---")
print("Idea: zip(a, b) entrega pares (a[i], b[i])")
nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# ---------------------------
# List comprehension
# ---------------------------
# Forma corta de crear una lista nueva con un for.
# Meta: cuadrados de 1..10 → [1, 4, 9, ..., 100]
print("\n--- List comprehension (cuadrados) ---")
print("Idea: [expresión for x in ...] arma una lista nueva")
cuadrados = [x**2 for x in range(1, 11)]
print("cuadrados:", cuadrados)

# Meta: solo pares del 1 al 20 (filtro con if)
print("\n--- List comprehension (pares) ---")
print("Idea: [x for x in ... if condición] filtra")
pares = [x for x in range(1, 21) if x % 2 == 0]
print("pares:", pares)

# ---------------------------
# Dict / set comprehension
# ---------------------------
print("\n--- Dict comprehension ---")
print("Idea: {clave: valor for x in ...}")
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print("cuadrados_dict:", cuadrados_dict)

print("\n--- Set comprehension (impares) ---")
print("Idea: {x for x in ... if ...} → conjunto (sin duplicados)")
impares = {x for x in range(1, 21) if x % 2 != 0}
print("impares:", impares)

# Tip: también podés hacer for linea in archivo abierto con with open(...).

# ---------------------------
# itertools (extra)
# ---------------------------
# Combinaciones: grupos sin importar el orden (AB = BA, no se repite).
print("\n--- itertools.combinations ---")
print("Idea: todas las parejas posibles de A,B,C sin repetir orden")
letras = ["A", "B", "C"]
combinaciones = itertools.combinations(letras, 2)
for combo in combinaciones:
    print("combo:", combo)

# Permutaciones: el orden SÍ importa (AB ≠ BA).
print("\n--- itertools.permutations ---")
print("Idea: todos los órdenes posibles de A,B,C")
permutaciones = itertools.permutations(letras)
for perm in permutaciones:
    print("perm:", perm)

# ---------------------------
# range con paso negativo
# ---------------------------
print("\n--- range con paso negativo ---")
print("Idea: countdown del 10 al 1")
for numero in range(10, 0, -1):
    print(LABEL_NUMERO, numero)

# ---------------------------
# Modificar lista por índice
# ---------------------------
# Si necesitás CAMBIAR elementos, conviene for i in range(len(lista)).
# (Recorrer solo con for x in lista no te deja escribir lista[i] fácil.)
print("\n--- Modificar lista mientras se itera ---")
print("Idea: usamos el índice para hacer numeros[i] *= 2")
numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    numeros[i] *= 2
print("numeros:", numeros)

# ---------------------------
# map / filter (extra; se profundiza en HOF)
# ---------------------------
# map: aplica una función a cada elemento.
print("\n--- map() ---")
print("Idea: list(map(funcion, lista)) transforma cada ítem")


def cuadrado(x):
    return x ** 2


numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print("cuadrados:", cuadrados)

# filter: deja pasar solo los que cumplen la condición.
print("\n--- filter() ---")
print("Idea: list(filter(funcion_bool, lista)) filtra")


def es_par(x):
    return x % 2 == 0


numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(es_par, numeros))
print("pares:", pares)

# ---------------------------
# numpy.arange (extra: pasos con decimales)
# ---------------------------
# range() solo maneja enteros. Para 0.5, 1.0, 1.5... usamos numpy.
print("\n--- numpy.arange (flotantes) ---")
print("Idea: como range, pero admite floats")
for numero in np.arange(0.5, 5.5, 0.5):
    print(LABEL_NUMERO, numero)

# ---------------------------
# enumerate extra (start=1)
# ---------------------------
# Por defecto el índice empieza en 0. Con start=1 numerás desde 1.
print("\n--- enumerate() (extra) ---")
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")

print("\n--- enumerate(start=1) ---")
print("Idea: start=1 → primera posición vale 1 (útil para menús/listados)")
for indice, color in enumerate(colores, start=1):
    print(f"{indice}: {color}")

# ---------------------------
# Mini mapa mental
# ---------------------------
# for x in lista/str/range/... → recorrer
# break / continue / else     → igual idea que en while
# enumerate → índice + valor
# zip       → varias secuencias a la vez
# [x for x in ...] → crear lista nueva en una línea
