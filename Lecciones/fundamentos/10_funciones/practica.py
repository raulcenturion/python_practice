# ============================
# 📝 Ejercicios: Funciones
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
def saludar(nombre="Mundo"):
    """Saluda a alguien por su nombre."""
    return f"¡Hola, {nombre}!"

print(saludar())          # ¡Hola, Mundo!
print(saludar("Raúl"))    # ¡Hola, Raúl!

# ============================
# Ejercicio 1: Función sumar
# Creá una función que reciba dos números y devuelva la suma.
print("Ejercicio 1: Función sumar")
def sumar(a, b):
    return a + b
print(sumar(1, 2))
print()


# Ejercicio 2: Par o impar
# Creá una función es_par(n) que devuelva True si n es par, False si no.
print("Ejercicio 2: Par o impar")
def es_par(n):
    return n % 2 == 0
print(es_par(2))
print(es_par(3))
print()

# Ejercicio 3: Factorial
# Creá una función factorial(n) que calcule el factorial de forma recursiva.
# Ej: factorial(5) → 120
print("Ejercicio 3: Factorial")
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
print()

# Ejercicio 4: Múltiples retornos
# Creá una función estadisticas(lista) que devuelva una tupla con
# (mínimo, máximo, promedio) de una lista de números.

print("Ejercicio 4: Múltiples retornos")
def estadisticas(lista):
    return min(lista), max(lista), sum(lista) / len(lista)
print(estadisticas([1, 2, 3, 4, 5]))
print()
# Ejercicio 5: *args
# Creá una función sumar_todos(*args) que sume todos los argumentos recibidos.
# Ej: sumar_todos(1, 2, 3, 4) → 10
print("Ejercicio 5: *args")
def sumar_todos(*args):
    return sum(args)
print(sumar_todos(1, 2, 3, 4))
print()

# Ejercicio 6: **kwargs
# Creá una función ficha(**kwargs) que imprima cada clave-valor recibido.
# Ej: ficha(nombre="Raúl", edad=33) → nombre: Raúl \n edad: 33
print("Ejercicio 6: **kwargs")
def ficha(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
ficha(nombre="Raúl", edad=33)
print()

# Ejercicio 7: Lambda
# Creá una lambda que reciba un número y devuelva su cuadrado.
# Aplicá esa lambda a [1, 2, 3, 4, 5] (estilo moderno: list comprehension).
# Nota: map(cuadrado, lista) también funciona, pero Sonar/Ruff prefieren
# [cuadrado(x) for x in lista] porque es más claro en Python.
print("Ejercicio 7: Lambda")
cuadrado = lambda x: x ** 2
print([cuadrado(x) for x in [1, 2, 3, 4, 5]])
print()

# Ejercicio 8: Función con docstring
# Creá una función convertir_celsius(c) que convierta Celsius a Fahrenheit.
# Agregale un docstring y probá accederlo con print(convertir_celsius.__doc__)
print("Ejercicio 8: Función con docstring")
def convertir_celsius(c):
    """Convierte Celsius a Fahrenheit."""
    return (c * 9/5) + 32
print(convertir_celsius(100))
print(convertir_celsius.__doc__)
print()

# Ejercicio 9: Función anidada
# Creá una función externa que imprima un mensaje y una función interna que imprima otro mensaje.
print("Ejercicio 9: Función anidada")
def externa():
    print("Mensaje externo")
    def interna():
        print("Mensaje interno")
    interna()
externa()
print()

# Ejercicio 10: Función + input (interactivo)
# Creá una función calcular_potencia(base, exponente) que devuelva base ** exponente.
# Pedí base y exponente por terminal, llamá a la función e imprimí el resultado.
print("Ejercicio 10: Función + input")
def calcular_potencia(base: float, exponente: float) -> float:
    """Devuelve base elevada a exponente."""
    return base ** exponente
base = float(input("Ingrese la base: "))
exponente = float(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"{base} elevado a {exponente} = {resultado}")
print()
# --- Ejercicio 10: Función + input ---
# def calcular_potencia(base: float, exponente: float) -> float:
#   → define una función con anotaciones de tipo.
#   → base: float y exponente: float → se espera que sean números decimales.
#   → -> float → indica que la función devuelve un valor de tipo float.
#   → estas anotaciones son solo documentación/pistas, no obligan al intérprete.
#
# """Devuelve base elevada a exponente.""" → docstring de la función.
# return base ** exponente → calcula la potencia.
#
# base = float(input(...)) → pide la base al usuario y la convierte a float.
# exponente = float(input(...)) → pide el exponente y lo convierte a float.
# resultado = calcular_potencia(base, exponente) → llama a la función.
# print(...) → muestra el resultado en pantalla.
#
# En resumen:
# - Los dos puntos (:) y la flecha (->) son anotaciones de tipo (type hints).
# - Sirven para documentar qué tipo de datos espera y devuelve la función.
# - No cambian el comportamiento, pero ayudan a leer y mantener el código.
