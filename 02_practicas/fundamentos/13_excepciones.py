# ============================
# 📝 Ejercicios: Excepciones
# 📘 Teoría: Clases_teoria/fundamentos/16_excepciones.py
# ============================

# 🔸 Ejemplo:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")
finally:
    print("Esto se ejecuta siempre.")

# ============================
# Ejercicio 1: Calculadora segura
# Creá una función dividir(a, b) que use try/except para manejar
# ZeroDivisionError y ValueError (si no son números).


# Ejercicio 2: Conversión segura
# Pedí un número al usuario. Si ingresa texto, capturá el ValueError
# y mostrá "Ingresá un número válido".


# Ejercicio 3: Acceso a lista
# Dada lista = [1, 2, 3], pedí un índice al usuario.
# Capturá IndexError si el índice no existe.


# Ejercicio 4: Excepción personalizada
# Creá una excepción EdadInvalidaError.
# Creá una función validar_edad(edad) que lance esa excepción si edad < 0.

