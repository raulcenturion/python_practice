# ============================
# 📘 Higher Order Functions (HOF)
# ============================
# Una HOF es una función que recibe otra función como argumento
# o que devuelve una función como resultado.
# Python tiene varias HOF built-in: map(), filter(), reduce(), sorted()

from functools import reduce

# ============================
# 🔹 Funciones como argumentos
# ============================
# En Python las funciones son "ciudadanos de primera clase" (first-class citizens),
# es decir, se pueden guardar en variables, pasar como argumento, etc.

print("--- Funciones como argumentos ---")
def greet(name):
    return f"Hola, {name}"

def apply_function(func, value):
    """Recibe una función y un valor, y aplica la función al valor."""
    return func(value)

print("apply_function(greet, 'Raúl'):", apply_function(greet, "Raúl"))  # Hola, Raúl

# ============================
# 🔹 map() — Aplica una función a cada elemento
# ============================
# Sintaxis: map(función, iterable)
# Devuelve un iterador, se suele convertir a list()

print("\n--- map() ---")
numeros = [1, 2, 3, 4, 5]

# Con función normal
def cuadrado(x):
    return x ** 2

cuadrados = list(map(cuadrado, numeros))
print("map con función:", cuadrados)  # [1, 4, 9, 16, 25]

# Con función corta (equivalente a lo que harías con lambda en map)
def al_cubo(x):
    return x ** 3


cubos = list(map(al_cubo, numeros))
print("map con al_cubo:", cubos)  # [1, 8, 27, 64, 125]
# Tip: también podrías escribir map(lambda x: x ** 3, numeros)

# ============================
# 🔹 filter() — Filtra elementos según una condición
# ============================
# Sintaxis: filter(función_que_retorna_bool, iterable)

print("\n--- filter() ---")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("filter pares:", pares)  # [2, 4, 6, 8, 10]

mayores_a_5 = list(filter(lambda x: x > 5, numeros))
print("filter > 5:", mayores_a_5)  # [6, 7, 8, 9, 10]

# ============================
# 🔹 reduce() — Reduce una lista a un solo valor
# ============================
# No es built-in, hay que importarlo de functools
print("\n--- reduce() ---")

numeros = [1, 2, 3, 4, 5]

# Suma acumulada: ((((1+2)+3)+4)+5) = 15
suma = reduce(lambda acc, x: acc + x, numeros)
print("reduce suma:", suma)  # 15
# Tip: para sumar una lista, en la práctica suele bastar sum(numeros)

# Encontrar el máximo
maximo = reduce(max, numeros)
print("reduce máximo:", maximo)  # 5

# ============================
# 🔹 sorted() con key — Ordenar con función personalizada
# ============================
print("\n--- sorted() con key ---")
palabras = ["banana", "Manzana", "cereza", "Durazno"]

# Ordenar ignorando mayúsculas
ordenado = sorted(palabras, key=str.lower)
print("sorted key=lower:", ordenado)

# Ordenar por longitud
por_largo = sorted(palabras, key=len)
print("sorted key=len:", por_largo)

# Ordenar lista de dicts por una clave
personas = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Marta", "edad": 35},
]
por_edad = sorted(personas, key=lambda p: p["edad"])
print("sorted por edad:", por_edad)

# ============================
# 🔹 Funciones que retornan funciones (closures)
# ============================
print("\n--- Closures (funciones que retornan funciones) ---")
def multiplicador(factor):
    """Retorna una función que multiplica por 'factor'."""
    def multiplicar(x):
        return x * factor
    return multiplicar

doble = multiplicador(2)
triple = multiplicador(3)

print("doble(5):", doble(5))   # 10
print("triple(5):", triple(5))  # 15

# ============================
# 🔹 Lambda — Funciones anónimas
# ============================
# Sintaxis: lambda parámetros: expresión
# Son funciones de una sola línea, sin nombre

print("\n--- Lambda ---")
sumar = lambda a, b: a + b
print("sumar(3, 4):", sumar(3, 4))  # 7

# Se usan mucho como argumento de HOFs (map, filter, sorted)
# ⚠️ No abuses de lambda para lógica compleja, usá def para eso
