# ============================
# 📝 Ejercicios: Tipos de Datos
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
# type() te dice el tipo de dato de cualquier valor

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Todos los tipos
# Creá una variable de cada tipo: str, int, float, bool, list, tuple, dict, set
# Imprimí el type() de cada una.
print("Ejercicio 1:")
texto = "Hola mundo"
numero = 10
decimal = 3.14
activo = True
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
diccionario = {"nombre": "Juan", "edad": 20}
conjunto = {1, 2, 3, 4}

print(numero, type(numero))
print(decimal, type(decimal))
print(texto, type(texto))
print(activo, type(activo))
print(lista, type(lista))
print(tupla, type(tupla))
print(diccionario, type(diccionario))
print(conjunto, type(conjunto))

# Ejercicio 2: Suma mixta
# ¿Qué tipo da si sumás un int + float? Probalo:
#   resultado = 10 + 3.14
#   print(type(resultado))
print("Ejercicio 2:")
resultado = 10 + 3.14
print(resultado, type(resultado))

# Ejercicio 3: Multiplicar strings
# ¿Qué pasa si multiplicás un string por un número? Probá: "ja" * 3
print("Ejercicio 3:")
resultado = "ja" * 3
print(resultado, type(resultado))

# Ejercicio 4: Booleanos como números
# ¿True + True cuánto da? ¿Y True + False? ¿Qué tipo es? Verificalo.
print("Ejercicio 4:")
resultado = True + True
print(resultado, type(resultado))
resultado = True + False
print(resultado, type(resultado))

# Ejercicio 5: Diccionario personal
# Creá un diccionario con tus datos (nombre, edad, hobbies como lista)
# Imprimí su type() y el type() de cada valor.
print("Ejercicio 5:")
diccionario = {"nombre": "Juan", "edad": 20, "hobbies": ["programar", "leer", "viajar"]}
print(diccionario, type(diccionario))
print(diccionario["nombre"], type(diccionario["nombre"]))
print(diccionario["edad"], type(diccionario["edad"]))
print(diccionario["hobbies"], type(diccionario["hobbies"]))