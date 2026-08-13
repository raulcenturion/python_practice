# ============================
# 📝 Ejercicios: Condicionales y Booleanos
# 📘 Teoría: teoria_booleanos.py, teoria_condicionales.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
edad = 20
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# ============================
# Ejercicio 1: Mayor de dos números
# Pedí dos números al usuario y mostrá cuál es el mayor (o si son iguales).
print("Ejercicio 1: Mayor de dos números")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"El número {numero2} es mayor que {numero1}")
else:
    print("Los números son iguales")
print("Fin del ejercicio 1")


# Ejercicio 2: Año bisiesto
# Pedí un año y determiná si es bisiesto.
# Regla: divisible por 4, pero NO por 100, SALVO que sea divisible por 400.
print("Ejercicio 2: Año bisiesto")
anio = int(input("Ingrese el año: "))
if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")
print("Fin del ejercicio 2")


# Ejercicio 3: Clasificación de edades
# Pedí la edad y clasificá en: niño (0-12), adolescente (13-19),
# adulto (20-64), adulto mayor (65+).
print("Ejercicio 3: Clasificación de edades")
edad = int(input("Ingrese la edad: "))
if edad >= 0 and edad <= 12:
    print("Es un niño")
elif edad >= 13 and edad <= 19:
    print("Es un adolescente")
elif edad >= 20 and edad <= 64:
    print("Es un adulto")
else:
    print("Es un adulto mayor")
print("Fin del ejercicio 3")

# Ejercicio 4: Par o impar
# Pedí un número y decí si es par o impar.
print("Ejercicio 4: Par o impar")
numero = int(input("Ingrese el número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
print("Fin del ejercicio 4")

# Ejercicio 5: Calculadora simple
# Pedí dos números y una operación (+, -, *, /)
# Mostrá el resultado. Si dividen por 0, mostrá un error.
print("Ejercicio 5: Calculadora simple")    
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación: ")
if operacion == "+":
    print(f"El resultado de la suma es {numero1 + numero2}")
elif operacion == "-":
    print(f"El resultado de la resta es {numero1 - numero2}")
elif operacion == "*":
    print(f"El resultado de la multiplicación es {numero1 * numero2}")
elif operacion == "/":
    if numero2 == 0:
        print("Error: División por cero")
    else:
        print(f"El resultado de la división es {numero1 / numero2}")
else:
    print("Operación inválida")
print("Fin del ejercicio 5")

# Ejercicio 6: Operadores lógicos
# Pedí edad y si tiene licencia (si/no).
# Imprimí "Puede manejar" solo si edad >= 18 AND tiene licencia.
print("Ejercicio 6: Operadores lógicos")
edad = int(input("Ingrese la edad: "))
licencia = str(input("¿Tiene licencia? (si/no): "))
if edad >= 18 and licencia == "si":
    print("Puede manejar")
else:
    print("No puede manejar")
print("Fin del ejercicio 6")


# Ejercicio 7: IMC
# Pedí peso (kg) y altura (m). Calculá el IMC = peso / altura²
# Clasificá: bajo peso (<18.5), normal (18.5-24.9), sobrepeso (25-29.9), obesidad (30+)
print("Ejercicio 7: IMC")
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en m: "))
imc = peso / altura ** 2
if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")
print("Fin del ejercicio 7")


# Ejercicio 8: Número primo
# Pedí un número y determiná si es primo.
# Pista: un primo solo es divisible por 1 y por sí mismo.
print("Ejercicio 8: Número primo")
numero = int(input("Ingrese el número: "))
if numero % 2 == 0:
    print("El número es primo")
else:
    print("El número no es primo")
print("Fin del ejercicio 8")
