# Funciones
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se definen usando la palabra clave 'def', seguida del nombre de la función y paréntesis.
# Pueden aceptar parámetros y devolver valores.
# La sintaxis básica es:
# def nombre_funcion(parametros):
#     bloque_de_codigo
#     return valor_de_retorno
# Ejemplo de una función simple que suma dos números
def sumar(a, b):
    return a + b
resultado = sumar(3, 5)
print("La suma es:", resultado)
# Función con parámetros por defecto
def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"
print(saludar())
print(saludar("Alice"))
# Función que no devuelve ningún valor (retorna None por defecto)
def imprimir_mensaje(mensaje):
    print(mensaje)
imprimir_mensaje("Este es un mensaje.")
# Función con múltiples valores de retorno
def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
resultado_suma, resultado_resta = calcular(10, 5)
print("La suma es:", resultado_suma)
print("La resta es:", resultado_resta)
# Función con argumentos arbitrarios
def sumar_todos(*args):
    return sum(args)
print("La suma de todos es:", sumar_todos(1, 2, 3, 4, 5))
# Función con argumentos de palabra clave arbitrarios
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_info(nombre="Alice", edad=30, ciudad="New York")
# Función lambda (función anónima)
multiplicar = lambda x, y: x * y
print("La multiplicación es:", multiplicar(4, 6))
# Función recursiva (una función que se llama a sí misma)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("El factorial de 5 es:", factorial(5))
# Documentación de funciones
def dividir(a, b):
    """Devuelve la división de a entre b. Lanza un error si b es 0."""
    if b == 0:
        raise ValueError("El divisor no puede ser 0.")
    return a / b
print("La división es:", dividir(10, 2))
# Llamada a la función con documentación
print(dividir.__doc__)
# Funciones anidadas
def externa(x):
    def interna(y):
        return y * 2
    return interna(x) + 3
print("Resultado de la función anidada:", externa(5))
# Uso de funciones como argumentos
def aplicar_funcion(func, valor):
    return func(valor)
print("Aplicando función lambda:", aplicar_funcion(lambda x: x ** 2, 4))
# Fin de la clase sobre funciones
## Mas sobre funciones
###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora