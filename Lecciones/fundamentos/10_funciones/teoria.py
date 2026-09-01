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
# --- *args ---
# def sumar_todos(*args):
#   → define una función que puede recibir cualquier cantidad de argumentos.
#   → el * delante de args significa "empaquetar" todos los valores en una tupla.
#   → ejemplo: sumar_todos(1,2,3) → args = (1,2,3)
#
# return sum(args)
#   → la función sum() suma todos los elementos de la tupla args.
#   → devuelve el resultado al lugar donde se llamó la función.
#
# print("La suma de todos es:", sumar_todos(1, 2, 3, 4, 5))
#   → se llama a la función con 5 números.
#   → internamente: args = (1,2,3,4,5)
#   → sum(args) = 15
#   → imprime: "La suma de todos es: 15"
#
# En resumen:
# - *args permite pasar muchos argumentos sin definirlos uno por uno.
# - Dentro de la función, esos argumentos se guardan en una tupla.
# - Podés recorrerlos con un for, sumarlos, etc.


# Función con argumentos de palabra clave arbitrarios
print("\n--- **kwargs ---")
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_info(nombre="Alice", edad=30, ciudad="New York")
# --- **kwargs ---
# def imprimir_info(**kwargs):
#   → define una función que recibe argumentos nombrados arbitrarios.
#   → kwargs se convierte en un diccionario con pares clave:valor.
#   → ejemplo: {"nombre":"Alice", "edad":30, "ciudad":"New York"}
#
# for clave, valor in kwargs.items():
#   → recorre cada par del diccionario.
#   → imprime la clave y su valor.
#
# imprimir_info(nombre="Alice", edad=30, ciudad="New York")
#   → kwargs = {"nombre":"Alice", "edad":30, "ciudad":"New York"}
#   → imprime:
#       nombre: Alice
#       edad: 30
#       ciudad: New York
#
# En resumen:
# - **kwargs permite pasar muchos argumentos con nombre.
# - Dentro de la función se guardan en un diccionario.
# - Podés recorrerlos con un for y usarlos como clave:valor.


# Función lambda (función anónima)
print("\n--- lambda ---")
multiplicar = lambda x, y: x * y
print("La multiplicación es:", multiplicar(4, 6))

# --- Función lambda ---
# lambda x, y: x * y
#   → define una función anónima (sin nombre) en una sola línea.
#   → recibe dos argumentos (x, y).
#   → devuelve el resultado de x * y.
#
# multiplicar = lambda x, y: x * y
#   → guarda la función en la variable "multiplicar".
#   → equivale a:
#       def multiplicar(x, y):
#           return x * y
#
# multiplicar(4, 6) → devuelve 24.
# print(...) → imprime "La multiplicación es: 24".
#
# En resumen:
# - lambda es una forma corta de definir funciones.
# - Se usa para funciones simples y rápidas.


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
# --- Docstring ---
# def dividir(a, b):
#   """Devuelve la división de a entre b. Lanza un error si b es 0."""
#   → el texto entre triple comillas es el docstring.
#   → sirve como documentación interna de la función.
#   → Python lo guarda en el atributo especial __doc__.
#
# if b == 0: raise ValueError(...)
#   → evita la división por cero lanzando un error.
#
# return a / b
#   → devuelve el resultado de la división.
#
# dividir.__doc__
#   → accede al texto del docstring.
#   → imprime: "Devuelve la división de a entre b. Lanza un error si b es 0."
#
# En resumen:
# - __doc__ contiene la documentación de la función.
# - Es útil para explicar qué hace sin mirar el código.

# Funciones anidadas
print("\n--- Funciones anidadas ---")
def externa(x):
    def interna(y):
        return y * 2
    return interna(x) + 3
print("Resultado de la función anidada:", externa(5))
# --- Funciones anidadas ---
# def externa(x):
#   → define una función externa que recibe un parámetro x.
#   → dentro de ella se define otra función interna(y).
#
# def interna(y):
#   → multiplica el valor recibido por 2 y lo devuelve.
#
# return interna(x) + 3
#   → llama a la función interna con el valor x.
#   → suma 3 al resultado.
#
# externa(5) → interna(5) = 10 → 10 + 3 = 13
# Resultado: "Resultado de la función anidada: 13"


# Uso de funciones como argumentos
print("\n--- Función como argumento ---")
def aplicar_funcion(func, valor):
    return func(valor)
print("Aplicando función lambda:", aplicar_funcion(lambda x: x ** 2, 4))
# --- Función como argumento ---
# def aplicar_funcion(func, valor):
#   → recibe una función y un valor.
#   → devuelve el resultado de aplicar esa función al valor.
#
# aplicar_funcion(lambda x: x ** 2, 4)
#   → se pasa una función lambda que eleva al cuadrado.
#   → valor = 4 → 4 ** 2 = 16
# Resultado: "Aplicando función lambda: 16"


# Más sobre funciones: posición, clave, *args, **kwargs
print("\n--- Argumentos por posición ---")
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")
# --- Argumentos por posición ---
# def describir_persona(nombre, edad, sexo):
#   → recibe tres parámetros en orden: nombre, edad, sexo.
#   → imprime un texto con esos valores.
#
# describir_persona("midudev", 25, "gato")
#   → nombre="midudev", edad=25, sexo="gato"
#   → imprime: "Soy midudev, tengo 25 años y me identifico como gato"
#
# IMPORTANTE: el orden importa. Si se mezclan los valores sin nombres,
# se asignan mal. Por eso existen los argumentos por clave.
# --- Argumentos por clave ---
# describir_persona(sexo="gato", nombre="midudev", edad=25)
#   → se pasan los parámetros nombrados.
#   → el orden ya no importa, porque cada valor se asigna por clave.
#   → imprime: "Soy midudev, tengo 25 años y me identifico como gato"
#
# Ventaja: evita errores de orden y hace el código más legible.


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
# --- *args (sumar_numeros) ---
# def sumar_numeros(*args):
#   → recibe una cantidad variable de argumentos.
#   → args se guarda como una tupla con todos los números.
#
# suma = 0
# for numero in args:
#   → recorre cada número en la tupla y lo acumula en suma.
#
# return suma
#   → devuelve la suma total.
#
# Ejemplos:
# sumar_numeros(1,2,3,4,5) → 15
# sumar_numeros(1,2) → 3
# sumar_numeros(1..10) → 55

print("sumar_numeros(1..5):", sumar_numeros(1, 2, 3, 4, 5))
print("sumar_numeros(1, 2):", sumar_numeros(1, 2))
print("sumar_numeros(1..10):", sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
print("\n--- **kwargs (mostrar_informacion_de) ---")
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")
# --- **kwargs (mostrar_informacion_de) ---
# def mostrar_informacion_de(**kwargs):
#   → recibe una cantidad variable de argumentos nombrados.
#   → kwargs se guarda como un diccionario {clave: valor}.
#
# for clave, valor in kwargs.items():
#   → recorre cada par clave:valor del diccionario.
#   → imprime la información.
#
# Ejemplo:
# mostrar_informacion_de(nombre="Alice", edad=30, ciudad="New York")
#   → kwargs = {"nombre":"Alice", "edad":30, "ciudad":"New York"}
#   → imprime:
#       nombre: Alice
#       edad: 30
#       ciudad: New York
#
# En resumen:
# - **kwargs permite pasar muchos argumentos con nombre.
# - Dentro de la función se guardan en un diccionario.
# - Podés recorrerlos con un for y usarlos como clave:valor.

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print()
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print()
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print()
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)
