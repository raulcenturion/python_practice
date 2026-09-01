# ============================
# 📝 Ejercicios: Excepciones
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡No se puede dividir por cero!!")
finally:
    print("Esto se ejecuta siempre!!!.")

# ============================
# Ejercicio 1: Calculadora segura
# Creá una función dividir(a, b) que use try/except para manejar
# ZeroDivisionError y ValueError (si no son números).
print("Ejercicio 1: Calculadora segura")

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    except ValueError:
        print("¡No se puede dividir por cero!")
    finally:
        print("Esto se ejecuta siempre!!.")
# pedir valores al usuario
a = float(input("Ingrese el numerador: "))
b = float(input("Ingrese el denominador: "))

resultado = dividir(a, b)
print("Resultado:", resultado)
# --- Ejercicio 1: Calculadora segura ---
# def dividir(a, b):
#   → intenta dividir a / b.
#   → except ZeroDivisionError: muestra mensaje si el divisor es 0.
#   → finally: se ejecuta siempre, ocurra o no la excepción.
#
# IMPORTANTE:
# - En el código original faltaba el input().
# - Para que el usuario interactúe, hay que pedir los valores:
#     a = float(input("Ingrese el numerador: "))
#     b = float(input("Ingrese el denominador: "))
#     resultado = dividir(a, b)
#     print("Resultado:", resultado)
#
# En resumen:
# - La función maneja la división segura.
# - El input permite que el usuario ingrese los números en tiempo real.


# Ejercicio 2: Conversión segura
# Pedí un número al usuario. Si ingresa texto, capturá el ValueError
# y mostrá "Ingresá un número válido".
print("Ejercicio 2: Conversión segura") 

def convertir_a_numero(texto):
    try:
        return int(texto)
    except ValueError:
        print("Ingresá un número válido.")
    finally:
        print("Esto se ejecuta siempre.")

# pedir al usuario el número
entrada = input("Ingresá un número: ")
convertir_a_numero(entrada)
print(f"El número ingresado es: {convertir_a_numero(entrada)}")
# --- Ejercicio 2: Conversión segura ---
# def convertir_a_numero(texto):
#   → intenta convertir el texto a entero con int(texto).
#   → except ValueError: muestra "Ingresá un número válido." si falla.
#   → finally: se ejecuta siempre, ocurra o no la excepción.
#
# IMPORTANTE:
# - En tu versión, el input() está dentro de la función y se llama de nuevo
#   a convertir_a_numero → eso genera recursión innecesaria.
# - Lo más claro es separar:
#     entrada = input("Ingresá un número: ")
#     convertir_a_numero(entrada)
#
# En resumen:
# - La lógica de la función está bien.
# - Pero conviene dejar el input afuera para que el flujo sea más simple.


# Ejercicio 3: Acceso a lista
# Dada lista = [1, 2, 3], pedí un índice al usuario.
# Capturá IndexError si el índice no existe.
print("Ejercicio 3: Acceso a lista")
lista = [1, 2, 3]
indice = int(input("Ingrese un índice: "))
try:
    print(lista[indice])
except IndexError:
    print("El índice no existe.")
finally:
    print("Esto se ejecuta siempre.")


# Ejercicio 4: Excepción personalizada
# Creá una excepción EdadInvalidaError.
# Creá una función validar_edad(edad) que lance esa excepción si edad < 0.
print("Ejercicio 4: Excepción personalizada")
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    return edad

edad = int(input("Ingrese su edad: "))
validar_edad(edad)
print(f"La edad ingresada es: {validar_edad(edad)}")
