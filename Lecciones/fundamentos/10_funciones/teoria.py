# Funciones
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se definen usando la palabra clave 'def', seguida del nombre de la función y paréntesis.
# Pueden aceptar parámetros y devolver valores.
# La sintaxis básica es:
# def nombre_funcion(parametros):
#     bloque_de_codigo
#     return valor_de_retorno

# Ejemplo de una función simple que suma dos números
print("--- Función sumar ---")
def sumar(a, b):
    return a + b
resultado = sumar(3, 5)
print("La suma es:", resultado)

# Función con parámetros por defecto
print("\n--- Parámetros por defecto ---")
def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"
print("saludar():", saludar())
print('saludar("Alice"):', saludar("Alice"))

# Función que no devuelve ningún valor (retorna None por defecto)
print("\n--- Función sin return (None) ---")
def imprimir_mensaje(mensaje):
    print(mensaje)
imprimir_mensaje("Este es un mensaje.")

# Función con múltiples valores de retorno
print("\n--- Múltiples valores de retorno ---")
def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta
resultado_suma, resultado_resta = calcular(10, 5)
print("La suma es:", resultado_suma)
print("La resta es:", resultado_resta)

# Función con argumentos arbitrarios
print("\n--- *args ---")
def sumar_todos(*args):
    return sum(args)
print("La suma de todos es:", sumar_todos(1, 2, 3, 4, 5))

# Función con argumentos de palabra clave arbitrarios
print("\n--- **kwargs ---")
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_info(nombre="Alice", edad=30, ciudad="New York")

# Función lambda (función anónima)
print("\n--- lambda ---")
multiplicar = lambda x, y: x * y
print("La multiplicación es:", multiplicar(4, 6))

# Función recursiva (una función que se llama a sí misma)
print("\n--- Función recursiva (factorial) ---")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("El factorial de 5 es:", factorial(5))

# Documentación de funciones
print("\n--- Docstring ---")
def dividir(a, b):
    """Devuelve la división de a entre b. Lanza un error si b es 0."""
    if b == 0:
        raise ValueError("El divisor no puede ser 0.")
    return a / b
print("La división es:", dividir(10, 2))
# Llamada a la función con documentación
print("dividir.__doc__:", dividir.__doc__)

# Funciones anidadas
print("\n--- Funciones anidadas ---")
def externa(x):
    def interna(y):
        return y * 2
    return interna(x) + 3
print("Resultado de la función anidada:", externa(5))

# Uso de funciones como argumentos
print("\n--- Función como argumento ---")
def aplicar_funcion(func, valor):
    return func(valor)
print("Aplicando función lambda:", aplicar_funcion(lambda x: x ** 2, 4))

# Más sobre funciones: posición, clave, *args, **kwargs
print("\n--- Argumentos por posición ---")
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales: el orden importa (nombre, edad, sexo)
describir_persona("midudev", 25, "gato")
describir_persona("madeval", 39, "hombre")
# Tip: si mezclás el orden sin nombres, los datos quedan mal asignados.
# Por eso existen los argumentos por clave (abajo).

# Argumentos por clave (parámetros nombrados)
print("\n--- Argumentos por clave ---")
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21)

# Argumentos de longitud de variable (*args):
print("\n--- *args (sumar_numeros) ---")
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print("sumar_numeros(1..5):", sumar_numeros(1, 2, 3, 4, 5))
print("sumar_numeros(1, 2):", sumar_numeros(1, 2))
print("sumar_numeros(1..10):", sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
print("\n--- **kwargs (mostrar_informacion_de) ---")
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print()
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print()
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print()
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)
