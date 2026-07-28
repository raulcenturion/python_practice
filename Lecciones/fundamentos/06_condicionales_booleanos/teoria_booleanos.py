#Booleanos
verdadero = True
falso = False
print(verdadero, type(verdadero)) #Muestra: True <class 'bool>
print(falso, type(falso)) #Muestra: False <class 'bool'>
#Operadores booleanos
a = True
b = False
print(a and b) #AND: True si ambos son True, sino False
print(a or b)  #OR: True si al menos uno es True, sino False
print(not a)   #NOT: Invierte el valor de verdad    
print(not b)   #NOT: Invierte el valor de verdad
#Operadores de comparación
x = 10
y = 5
print(x == y)  # Igualdad: False
print(x != y)  # Desigualdad: True
print(x > y)   # Mayor que: True    
print(x < y)   # Menor que: False
print(x >= y)  # Mayor o igual que: True
print(x <= y)  # Menor o igual que: False
#Uso de booleanos en estructuras de control
if a and (x > y):
    print("a es True y x es mayor que y")
else:
    print("Condición no cumplida")
#Ejemplo con listas
lista = [1, 2, 3]
print(2 in lista)  # True, 2 está en la lista
print(5 in lista)  # False, 5 no está en la lista
print(5 not in lista)  # True, 5 no está en la lista
#Conversión a booleano
print(bool(1))      # True, cualquier número distinto de 0 es True
print(bool(0))      # False, 0 es False
print(bool(-1))     # True, cualquier número distinto de 0 es True
print(bool(""))     # False, cadena vacía es False
print(bool("Hola")) # True, cadena no vacía es True
print(bool([]))     # False, lista vacía es False
print(bool([1, 2])) # True, lista no vacía es True
print(bool(None))   # False, None es False  
#Uso en funciones
def es_mayor_de_edad(edad):
    return edad >= 18  # Devuelve True si edad es 18 o más, sino False
print(es_mayor_de_edad(20))  # True
print(es_mayor_de_edad(16))  # False
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
def puede_acceder(rol):
    permisos = {
        "admin": True,
        "usuario": False,
        "invitado": False
    }
    return permisos.get(rol, False)  # Devuelve False si el rol no existe
print(puede_acceder("admin"))   # True
print(puede_acceder("usuario")) # False
print(puede_acceder("invitado")) # False
print(puede_acceder("otro"))    # False, rol no definido
#Ejemplo práctico: Filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)  # Muestra: Números pares: [2, 4, 6]
#Ejemplo práctico: Validar entrada de usuario
def es_numero_valido(valor):
    try:
        num = float(valor)
        return True
    except ValueError:
        return False 
print(es_numero_valido("123.45"))  # True
print(es_numero_valido("abc"))      # False
print(es_numero_valido(""))         # False
#Ejemplo práctico: Uso de booleanos en bucles
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
#Uso de booleanos para controlar el bucle
    if contador == 3:
        print("Contador llegó a 3, saliendo del bucle.")
        break
#Resumen final: Los booleanos son esenciales para la lógica de programación,
#permitiendo tomar decisiones, controlar flujos y validar condiciones.
#Comprender su uso y buenas prácticas es clave para escribir código claro y efectivo.
#Se integran con operadores lógicos y de comparación para formar condiciones complejas.
#Son ampliamente usados en estructuras de control, funciones y validaciones.
#Ejemplos prácticos ayudan a entender su aplicación en escenarios reales.
#Con práctica, el uso de booleanos se vuelve intuitivo y natural en la programación diaria.
#Nota: Este archivo se centra en el uso de booleanos en Python.
#Para más detalles sobre otros tipos de datos y estructuras, revisar archivos relacionados.
#Fin del archivo 07_booleanos.py
#Este archivo complementa los conceptos vistos en:
# 03_cast.py (Casting de tipos de datos)
# 04_variables.py (Variables y tipos de datos)
# 05_input.py (Entrada de datos)
# 06_control_de_flujo.py (Control de flujo)
# Condición ternaria
# Es una forma concisa de asignar un valor basado en una condición
# [valor_si_verdadero] if [condición] else [valor_si_falso]
edad = 20
es_mayor = True if edad >= 18 else False
print(es_mayor)  # True