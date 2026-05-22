## Variables
# Las variables son contenedores que almacenan datos.
# En Python, no es necesario declarar el tipo de dato de una variable.
# El tipo de dato se asigna automáticamente según el valor que se le asigne a la variable.
# Se pueden reasignar valores de diferentes tipos a la misma variable.
# Las variables deben comenzar con una letra o un guion bajo (_),
# y pueden contener letras, números y guiones bajos.
# No pueden contener espacios ni caracteres especiales.
# Las variables son sensibles a mayúsculas y minúsculas (case-sensitive).
# Ejemplos de variables
nombre = "Juan"  # string
edad = 30        # int
altura = 1.75    # float
es_estudiante = True  # bool
# Reasignación de variables
nombre = "Maria"  # ahora nombre es "Maria"
edad = 25         # ahora edad es 25
# Mostrar el valor y tipo de dato de las variables
print(nombre, type(nombre))  # Muestra: Maria <class 'str'>
print(edad, type(edad))      # Muestra: 25 <class 'int'>
print(altura, type(altura))  # Muestra: 1.75 <class 'float'>
print(es_estudiante, type(es_estudiante))  # Muestra: True <class 'bool'>
# Variables con diferentes tipos de datos
lista = [1, 2, 3]  # lista
tupla = (1, 2, 3)  # tuple
conjunto = {1, 2, 3}  # set
diccionario = {"a": 1, "b": 2}  # dict
print(lista, type(lista))          # Muestra: [1, 2, 3] <class 'list'>
print(tupla, type(tupla))          # Muestra: (1, 2, 3) <class 'tuple'>
print(conjunto, type(conjunto))      # Muestra: {1, 2, 3} <class 'set'>
print(diccionario, type(diccionario))  # Muestra: {'a': 1, 'b': 2} <class 'dict'>
# Variables con nombres válidos e inválidos
_valido = "válido"  # válido
valido2 = "válido"  # válido
# 2invalido = "inválido"  # inválido, no puede comenzar con número
# invalido-3 = "inválido"  # inválido, no puede contener guion
# invalido espacio = "inválido"  # inválido, no puede contener espacios
# print(2invalido)  # Esto generaría un error
# print(invalido-3)  # Esto generaría un error
# print(invalido espacio)  # Esto generaría un error
# Nota: Las líneas comentadas con errores no deben descomentarse, ya que generarán errores de sintaxis.
# Buenas prácticas para nombres de variables
# Usar nombres descriptivos y en minúsculas, separando palabras con guiones bajos
nombre_completo = "Ana Perez"
edad_usuario = 28
es_mayor_de_edad = True
print(nombre_completo, edad_usuario, es_mayor_de_edad)
# Evitar usar palabras reservadas del lenguaje como nombres de variables
# Ejemplos de palabras reservadas: if, else, while, for, def, return, import, etc.
# if = 10  # inválido, 'if' es una palabra reservada
# print(if)  # Esto generaría un error
# Nota: La línea comentada con error no debe descomentarse, ya que generará un error de sintaxis.
# Se puede usar la función type() para verificar el tipo de dato de una variable
print(type(nombre_completo))  # Muestra: <class 'str'>
print(type(edad_usuario))     # Muestra: <class 'int'>
print(type(es_mayor_de_edad))  # Muestra: <class 'bool'>
# Las variables pueden ser usadas en operaciones según su tipo de dato
suma_edades = edad + edad_usuario  # suma de enteros
print(suma_edades)  # Muestra: 55
nombre_completo_mayus = nombre_completo.upper()  # método de string
print(nombre_completo_mayus)  # Muestra: ANA PEREZ
# Las variables pueden ser eliminadas con la palabra clave delete
del es_estudiante
# print(es_estudiante)  # Esto generaría un error, ya que la variable ha sido eliminada
# Nota: La línea comentada con error no debe descomentarse, ya que generará un error de nombre no definido.
# Resumen: Las variables son fundamentales en la programación para almacenar y manipular datos.
# En Python, son flexibles y fáciles de usar, pero es importante seguir buenas prácticas para mantener el código claro y legible.
# Tipado dinámico: una variable puede cambiar de tipo al reasignarle un valor de diferente tipo
var = 10          # var es un int
print(var, type(var))  # Muestra: 10 <class 'int'>
var = "Hola"     # var ahora es un str
print(var, type(var))  # Muestra: Hola <class 'str'>
# Tipado fuerte: no se pueden realizar operaciones entre diferentes tipos de datos sin conversión explícita
num = 5          # int
texto = "10"     # str
# suma = num + texto  # Esto generaría un error de tipo
# print(suma)  # Esto generaría un error
edad = 25
nombre = "Carlos"
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Usando f-string
# F-strings permiten incluir expresiones dentro de las llaves {}
print(f"El próximo año tendré {edad + 1} años.")  # Evalua la expresión edad + 1
# También se pueden usar métodos dentro de las llaves
print(f"Mi nombre en mayúsculas es {nombre.upper()}.")  # Usa el método upper() de str
# Las f-strings son una forma eficiente y legible de formatear cadenas en Python
# Nota: Las f-strings están disponibles a partir de Python 3.6
# Convensiones de nombres de variables
# snake_case: palabras separadas por guiones bajos (recomendado en Python)
mi_variable = 10
otra_variable = "Hola"
# camelCase: palabras unidas, cada palabra (excepto la primera) comienza con mayúscula
miVariable = 20
otraVariable = "Mundo"
# PascalCase: palabras unidas, cada palabra comienza con mayúscula (usado en clases)
MiClase = 30
OtraClase = "Python"
# kebab-case: palabras separadas por guiones (no válido en Python para variables)
# mi-variable = 40  # Esto generaría un error
# print(mi-variable)  # Esto generaría un error
# Cuando se hace una declaración en mayúsculas, se suele reservar para constantes
PI = 3.1416
GRAVEDAD = 9.81
# Nota: Aunque Python no tiene constantes reales, esta es una convención para indicar que el valor no debe cambiarse

