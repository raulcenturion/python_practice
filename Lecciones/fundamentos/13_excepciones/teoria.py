# Excepciones
# Las excepciones son eventos que pueden alterar el flujo normal de un programa. En Python, se pueden manejar utilizando bloques try y except.
# Ejemplo de manejo de excepciones
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción
    print("Error: División por cero no permitida.")
else:
    # Código que se ejecuta si no ocurre ninguna excepción
    print("El resultado es:", resultado)
finally:
    # Código que se ejecuta siempre, ocurra o no una excepción
    print("Bloque finally ejecutado.")
# Tipos comunes de excepciones
# - ZeroDivisionError: División por cero.
# - ValueError: Valor incorrecto.
# - TypeError: Tipo de dato incorrecto.
# - IndexError: Índice fuera de rango.
# - KeyError: Clave no encontrada en un diccionario.
# - FileNotFoundError: Archivo no encontrado.
# Lanzar excepciones
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0.")
    return a / b
try:
    print(dividir(10, 2))
    print(dividir(10, 0))
except ValueError as e:
    print("Excepción capturada:", e)
# Creación de excepciones personalizadas
class MiExcepcionPersonalizada(Exception):
    pass
try:
    raise MiExcepcionPersonalizada("Este es un error personalizado.")
except MiExcepcionPersonalizada as e:
    print("Excepción personalizada capturada:", e)
# Nota: El manejo adecuado de excepciones es crucial para crear programas robustos y evitar fallos inesperados.
# Es recomendable capturar solo las excepciones que se esperan y manejar adecuadamente cada caso.
# El bloque else es opcional y se ejecuta si no se lanza ninguna excepción en el bloque try.
# El bloque finally es opcional y se ejecuta siempre, independientemente de si se lanzó o no una excepción.
# Se pueden capturar múltiples excepciones en un solo bloque except utilizando una tupla.
# Es posible anidar bloques try-except para manejar excepciones en diferentes niveles de un programa.
# Las excepciones personalizadas deben heredar de la clase base Exception.
# Se pueden usar las funciones built-in `assert` para verificar condiciones y lanzar una excepción si la condición es falsa.
# Ejemplo:
def verificar_edad(edad):
    assert edad >= 0, "La edad no puede ser negativa."
    return True
try:
    verificar_edad(25)
    verificar_edad(-5)
except AssertionError as e:
    print("Error de aserción:", e)

# ============================
# 🔹 Resumen
# ============================
# - try: código que puede fallar
# - except: captura el error específico
# - else: se ejecuta si NO hubo error
# - finally: se ejecuta SIEMPRE (ideal para cerrar archivos, conexiones, etc.)
# - raise: lanza una excepción manualmente
# - Se pueden crear excepciones personalizadas heredando de Exception
# - assert: verifica condiciones, lanza AssertionError si es False
