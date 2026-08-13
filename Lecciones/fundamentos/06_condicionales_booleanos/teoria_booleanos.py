#Booleanos
print("--- Valores booleanos ---")
verdadero = True
falso = False
print("verdadero:", verdadero, type(verdadero))  # True <class 'bool'>
print("falso:", falso, type(falso))              # False <class 'bool'>

#Operadores booleanos
print("\n--- Operadores booleanos (and / or / not) ---")
a = True
b = False
print("a and b:", a and b)  # AND: True si ambos son True
print("a or b:", a or b)    # OR: True si al menos uno es True
print("not a:", not a)      # NOT: invierte el valor
print("not b:", not b)

#Operadores de comparación
print("\n--- Operadores de comparación ---")
x = 10
y = 5
print("x == y:", x == y)  # Igualdad: False
print("x != y:", x != y)  # Desigualdad: True
print("x > y:", x > y)    # Mayor que: True
print("x < y:", x < y)    # Menor que: False
print("x >= y:", x >= y)  # Mayor o igual: True
print("x <= y:", x <= y)  # Menor o igual: False

#Uso de booleanos en estructuras de control
print("\n--- Booleanos en if/else ---")
if a and (x > y):
    print("a es True y x es mayor que y")
else:
    print("Condición no cumplida")

#Ejemplo con listas
print("\n--- Operador in / not in (listas) ---")
lista = [1, 2, 3]
print("2 in lista:", 2 in lista)          # True
print("5 in lista:", 5 in lista)          # False
print("5 not in lista:", 5 not in lista)  # True

#Conversión a booleano
print("\n--- Conversión a bool() ---")
print("bool(1):", bool(1))          # True
print("bool(0):", bool(0))          # False
print("bool(-1):", bool(-1))        # True
print('bool(""):', bool(""))        # False
print('bool("Hola"):', bool("Hola"))  # True
print("bool([]):", bool([]))        # False
print("bool([1, 2]):", bool([1, 2]))  # True
print("bool(None):", bool(None))    # False

#Uso en funciones
print("\n--- Función es_mayor_de_edad ---")
def es_mayor_de_edad(edad):
    return edad >= 18  # Devuelve True si edad es 18 o más
print("edad 20:", es_mayor_de_edad(20))  # True
print("edad 16:", es_mayor_de_edad(16))  # False

#Resumen: Los booleanos son fundamentales en la lógica de programación,
#permitiendo tomar decisiones y controlar el flujo del programa.
#Se usan en condiciones, comparaciones y conversiones de tipos.
#Operadores booleanos: and, or, not
#Operadores de comparación: ==, !=, >, <, >=, <=
#Valores que se evalúan como False: False, None, 0, "", [], {}, ()
#Todos los demás valores se evalúan como True
#Buenas prácticas: Usar paréntesis para clarificar condiciones complejas
#Evitar comparaciones redundantes (ej. if x == True es mejor if x)
#Usar funciones para encapsular lógica booleana reutilizable

#Ejemplo práctico: Validar acceso basado en permisos
print("\n--- Ejemplo: puede_acceder (permisos por rol) ---")
def puede_acceder(rol):
    permisos = {
        "admin": True,
        "usuario": False,
        "invitado": False
    }
    return permisos.get(rol, False)  # Devuelve False si el rol no existe
print("admin:", puede_acceder("admin"))       # True
print("usuario:", puede_acceder("usuario"))   # False
print("invitado:", puede_acceder("invitado")) # False
print("otro:", puede_acceder("otro"))        # False, rol no definido

#Ejemplo práctico: Filtrar números pares de una lista
print("\n--- Ejemplo: filtrar números pares ---")
numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)  # Muestra: Números pares: [2, 4, 6]

#Ejemplo práctico: Validar entrada de usuario
print("\n--- Ejemplo: es_numero_valido ---")
def es_numero_valido(valor):
    try:
        _ = float(valor)  # si convierte bien, es número válido
        return True
    except ValueError:
        return False
print('"123.45":', es_numero_valido("123.45"))  # True
print('"abc":', es_numero_valido("abc"))        # False
print('"":', es_numero_valido(""))              # False

#Ejemplo práctico: Uso de booleanos en bucles
print("\n--- Ejemplo: while + break con booleanos ---")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
#Uso de booleanos para controlar el bucle
    if contador == 3:
        print("Contador llegó a 3, saliendo del bucle.")
        break

# Condición ternaria / comparación que ya da bool
print("\n--- Ejemplo: comparación que da bool ---")
# [valor_si_verdadero] if [condición] else [valor_si_falso]
edad = 20
es_mayor = edad >= 18  # la comparación ya da True/False (no hace falta el if/else)
print("es_mayor:", es_mayor)  # True