# Ejercicios propuestos
###
# 1. Determinar el mayor de dos números ingresados por el usuario.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Ambos números son iguales.")
###
# 2. Calculadora simple: Pedir dos números y una operación (suma, resta, multiplicación, división) y mostrar el resultado.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero."
else:
    resultado = "Operación no válida."
print(f"El resultado es: {resultado}")
###
# 3. Año bisiesto: Pedir al usuario que ingrese un año y determinar si es bisiesto o no.
# Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
###
# 4. Clasificación de edades: Pedir al usuario su edad y clasificarlo en niño (0-12), adolescente (13-19), adulto (20-64) o anciano (65+).
edad = int(input("Ingrese su edad: "))
if 0 <= edad <= 12:
    categoria = "niño"
elif 13 <= edad <= 19:
    categoria = "adolescente"
elif 20 <= edad <= 64:
    categoria = "adulto"
elif edad >= 65:
    categoria = "anciano"
else:
    categoria = "edad no válida"
print(f"Usted es un {categoria}.")
###
# 5. Número par o impar: Pedir al usuario un número entero y determinar si es par o impar.
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
###
# 6. Conversión de temperaturas: Pedir al usuario una temperatura en grados Celsius y convertirla a Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
###
# 7. Validación de contraseña: Pedir al usuario que ingrese una contraseña y verificar si cumple con ciertos criterios (mínimo 8 caracteres, al menos una letra mayúscula, una letra minúscula y un número).
import re
contraseña = input("Ingrese una contraseña: ")
if (len(contraseña) >= 8 and
    re.search(r"[A-Z]", contraseña) and
    re.search(r"[a-z]", contraseña) and
    re.search(r"[0-9]", contraseña)):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los criterios.")
###
# 8. Cálculo del IMC: Pedir al usuario su peso (en kg) y su altura (en metros) y calcular su Índice de Masa Corporal (IMC). Clasificar el resultado según las categorías estándar (bajo peso, peso normal, sobrepeso, obesidad).
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    categoria = "bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "peso normal"
elif 25 <= imc < 29.9:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"
print(f"Su IMC es {imc:.2f}, lo que indica {categoria}.")
### 9. Número primo: Pedir al usuario un número entero y determinar si es un número primo o no.
numero = int(input("Ingrese un número entero: "))
if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"El número {numero} no es primo.")
            break
    else:
        print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
### 10. Menú de opciones: Crear un menú simple que permita al usuario elegir entre varias opciones (por ejemplo, saludar, despedirse, mostrar la fecha actual) y ejecutar la acción correspondiente.
import datetime

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Mostrar la fecha actual")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("¡Adiós!")
    elif opcion == "3":
        fecha_actual = datetime.datetime.now()
        print(f"La fecha y hora actual es: {fecha_actual}")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
