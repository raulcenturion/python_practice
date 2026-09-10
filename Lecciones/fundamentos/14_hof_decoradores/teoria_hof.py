# ============================
# 📘 Higher Order Functions (HOF)
# ============================
# Una HOF es una función que:
#   1) recibe otra función como argumento, y/o
#   2) devuelve una función como resultado.
#
# En Python las funciones son "ciudadanos de primera clase":
# se pueden guardar en variables, pasar como argumento, etc.
#
# HOF built-in más usadas: map(), filter(), sorted()
# reduce() viene de functools (hay que importarlo).

from functools import reduce

# ============================
# 🔹 Funciones como argumentos
# ============================
print("--- Funciones como argumentos ---")


def greet(name):
    # Función normal: recibe un string y arma un saludo.
    return f"Hola, {name}"


def apply_function(func, value):
    """HOF: recibe una función (func) y un valor, y aplica func(value).
    'func' NO se llama con paréntesis al pasarla: se pasa la función en sí."""
    return func(value)


# Pasamos greet (sin paréntesis) + el valor "Raúl".
# apply_function internamente hace: greet("Raúl")
print("apply_function(greet, 'Raúl'):", apply_function(greet, "Raúl"))


# ============================
# 🔹 map() — Aplica una función a cada elemento
# ============================
# Sintaxis: map(función, iterable)
# Devuelve un iterador → casi siempre lo convertimos a list()
print("\n--- map() ---")

numeros = [1, 2, 3, 4, 5]


def cuadrado(x):
    # Función que se aplicará a CADA elemento de la lista.
    return x ** 2


# map(cuadrado, numeros) → aplica cuadrado(1), cuadrado(2), ...
# list(...) materializa el iterador en una lista concreta.
cuadrados = list(map(cuadrado, numeros))
print("map con función:", cuadrados)  # [1, 4, 9, 16, 25]


def al_cubo(x):
    return x ** 3


cubos = list(map(al_cubo, numeros))
print("map con al_cubo:", cubos)  # [1, 8, 27, 64, 125]
# Tip: también podrías escribir map(lambda x: x ** 3, numeros)


# ============================
# 🔹 filter() — Filtra elementos según una condición
# ============================
# Sintaxis: filter(función_que_retorna_bool, iterable)
# Se queda solo con los elementos donde la función da True.
print("\n--- filter() ---")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lambda x: x % 2 == 0 → True si es par.
# filter recorre numeros y deja solo los True.
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("filter pares:", pares)  # [2, 4, 6, 8, 10]

mayores_a_5 = list(filter(lambda x: x > 5, numeros))
print("filter > 5:", mayores_a_5)  # [6, 7, 8, 9, 10]


# ============================
# 🔹 reduce() — Reduce una lista a un solo valor
# ============================
# No es built-in: viene de functools.
# reduce(función, iterable) aplica la función de a pares acumulando.
print("\n--- reduce() ---")

numeros = [1, 2, 3, 4, 5]

# Paso a paso: ((((1+2)+3)+4)+5) = 15
# acc = acumulador (lo que va quedando), x = siguiente elemento.
suma = reduce(lambda acc, x: acc + x, numeros)
print("reduce suma:", suma)  # 15
# Tip práctico: para sumar, sum(numeros) es más claro.

# reduce(max, numeros) compara de a pares y se queda con el mayor.
maximo = reduce(max, numeros)
print("reduce máximo:", maximo)  # 5


# ============================
# 🔹 sorted() con key — Ordenar con función personalizada
# ============================
# sorted(iterable, key=función) → la función decide el criterio de orden.
# No modifica la lista original (devuelve una NUEVA).
print("\n--- sorted() con key ---")

palabras = ["banana", "Manzana", "cereza", "Durazno"]

# key=str.lower → compara todo en minúsculas (ignora mayúsculas).
ordenado = sorted(palabras, key=str.lower)
print("sorted key=lower:", ordenado)

# key=len → ordena por cantidad de caracteres.
por_largo = sorted(palabras, key=len)
print("sorted key=len:", por_largo)

# Ordenar lista de dicts por una clave interna.
personas = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Marta", "edad": 35},
]
# lambda p: p["edad"] → de cada dict toma la edad para comparar.
por_edad = sorted(personas, key=lambda p: p["edad"])
print("sorted por edad:", por_edad)


# ============================
# 🔹 Closures (funciones que retornan funciones)
# ============================
# Una función interna "recuerda" variables de la función externa.
print("\n--- Closures (funciones que retornan funciones) ---")


def multiplicador(factor):
    """Retorna una función que multiplica por 'factor'.
    'factor' queda guardado en la closure de multiplicar."""

    def multiplicar(x):
        # 'factor' NO es parámetro de multiplicar: viene de afuera (closure).
        return x * factor

    return multiplicar  # Devolvemos la función (sin ejecutarla).


# doble "recuerda" factor=2; triple recuerda factor=3.
doble = multiplicador(2)
triple = multiplicador(3)

print("doble(5):", doble(5))    # Ejemplo 5 * 2 = 10
print("triple(5):", triple(5))  # Ejemplo 5 * 3 = 15
# Esto es la base mental de los decoradores.


# ============================
# 🔹 Lambda — Funciones anónimas
# ============================
# Sintaxis: lambda parámetros: expresión
# Función de UNA sola expresión, sin nombre (salvo que la asignes).
print("\n--- Lambda ---")

sumar = lambda a, b: a + b
print("sumar(3, 4):", sumar(3, 4))  # 7

# Se usan mucho como argumento corto de map/filter/sorted.
# ⚠️ Si la lógica es compleja, preferí def (más legible).

# Nivel Fácil – Funciones como argumentos:
# Un HOF es una función que recibe otra función como parámetro o devuelve una función.
def aplicar(funcion, valor):
    return funcion(valor)

print(aplicar(len, "Raúl"))   # → 4
print(aplicar(str.upper, "hola"))  # → "HOLA"
# 👉 Concepto: aplicar recibe otra función (len, upper) y la ejecuta sobre el valor.
# Esto muestra que en Python las funciones son ciudadanos de primera clase.
# 📌 Nivel Medio – Uso con map, filter, reduce
# map(f, lista): transforma cada elemento con f
# filter(f, lista): deja solo donde f da True
# reduce(f, lista): acumula hasta un solo valor (functools)
# sorted(..., key=f): ordena según el criterio de f
# Los HOF se usan mucho con colecciones.
numeros = [1, 2, 3, 4, 5]

# map → aplica una función a cada elemento
# Con map sería: list(map(lambda x: x**2, numeros))
# Sonar/Ruff prefieren list comprehension (misma idea, más clara):
cuadrados = [x**2 for x in numeros]  # [1, 4, 9, 16, 25]

# filter → selecciona elementos que cumplen condición
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]

# reduce → acumula valores (functools.reduce ya importado arriba)
suma = reduce(lambda acc, x: acc + x, numeros)  # 15
# 👉 reduce acumula (acc) los valores de la lista (x) hasta un solo valor.
# 👉 Concepto: map, filter, reduce son HOF porque reciben funciones como argumento.
#📌 Nivel Avanzado – Funciones que devuelven funciones (decoradores)
# Los HOF también pueden crear funciones nuevas.
def decorador_mayusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper()
    return wrapper

@decorador_mayusculas
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Raúl"))  # → "HOLA RAÚL"

print("\n--- Funciones que devuelven funciones ---")
def crear_multiplicador(factor):
    return lambda x: x * factor
multiplicar_por_2 = crear_multiplicador(2)
print(multiplicar_por_2(5))  # → 10
# 👉 Concepto: crear_multiplicador es una función que retorna otra función.
# Esto es la base mental de los decoradores.
# 📌 Nivel Experto – Decoradores (funciones que decoran funciones)
# Los decoradores son funciones que:
#   1) reciben una función,
#   2) la decoran (la modifican),
#   3) retornan la función decorada.
# Ejemplo:
def decorar_saludo(funcion):
    def wrapper(nombre):
        return f"¡Hola, {nombre}!"
    return wrapper

@decorar_saludo
def saludar(nombre):
    return f"Hola, {nombre}"
print(saludar("Juan"))  # → "¡Hola, Juan!"
# 👉 Concepto: decorar_saludo recibe saludar y retorna wrapper.
# wrapper es la función decorada.
# 👉 Concepto: decorar_saludo recibe saludar y retorna wrapper.
# 👉 Concepto: decorador_mayusculas recibe saludar y retorna wrapper.
# wrapper es la función decorada.
# 👉 Concepto: decorador_mayusculas recibe saludar y retorna wrapper.

# --- Higher-Order Functions (HOF) en Python ---
#
# Nivel Fácil:
# - Una HOF recibe otra función como argumento.
# - Ejemplo:
#   def aplicar(funcion, valor): return funcion(valor)
#   aplicar(len, "Raúl") → 4
#
# Nivel Medio:
# - HOF aplicadas a colecciones: map, filter, reduce.
# - map(lambda x: x**2, numeros) → aplica función a cada elemento.
# - filter(lambda x: x%2==0, numeros) → selecciona pares.
# - reduce(lambda acc,x: acc+x, numeros) → acumula suma.
#
# Nivel Avanzado:
# - HOF que devuelven funciones → decoradores.
# - Ejemplo:
#   def decorador(func): def wrapper(...): return func(...).upper()
#   @decorador → modifica comportamiento de la función original.
#
# --- Buenas prácticas ---
# - Usar HOF para evitar duplicar lógica.
# - Preferir funciones puras (sin efectos secundarios).
# - Decoradores: útiles para validación, logging, autenticación.
# - map/filter → más expresivos que bucles manuales en algunos casos.

# ============================
# 🔹 Resumen
# ============================
# - HOF: recibe y/o devuelve funciones
# - map(f, lista): transforma cada elemento con f
# - filter(f, lista): deja solo donde f da True
# - reduce(f, lista): acumula hasta un solo valor (functools)
# - sorted(..., key=f): ordena según el criterio de f
# - closure: función interna que recuerda variables externas
# - lambda: función corta de una expresión
# - Los decoradores (@) se apoyan en estos mismos conceptos
