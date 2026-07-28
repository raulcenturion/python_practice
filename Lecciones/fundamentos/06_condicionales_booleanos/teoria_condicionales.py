# Sentencias condicionales if, elif, else
edad = 20
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes 18 años, eres mayor de edad.")
else:
    print("Eres mayor de edad.")    
# Sentencia condicional anidada
nota = 85
if nota >= 0 and nota <= 100:
    if nota >= 90:
        print("Excelente")
    elif nota >= 80:
        print("Muy bien")
    elif nota >= 70:
        print("Bien")
    elif nota >= 60:
        print("Suficiente")
    else:
        print("Insuficiente")
else:
    print("Nota inválida")
# Bucles while y for
# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1
# Bucle for
# Itera sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)
# Itera sobre un rango de números
for i in range(5):  # Desde 0 hasta 4
    print("Número:", i)
# Uso de break y continue
for i in range(5):
    if i == 2:
        continue  # Salta el número 2
    print("Número:", i) 
    if i == 3:
        break  # Sale del bucle cuando i es 3
# Uso de else con bucles
for i in range(3):
    print("Número:", i)
else:
    print("Bucle for terminado sin interrupciones.")
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("Bucle while terminado sin interrupciones.")
# Nota: El bloque else se ejecuta si el bucle termina normalmente,
# pero no si se interrumpe con break.   
# Resumen: Las estructuras de control de flujo permiten dirigir la ejecución del código
# según condiciones y repetir bloques de código. Son fundamentales para la lógica de programación.
# Sentencias condicionales permiten ejecutar código basado en condiciones (if, elif, else).
# Bucles permiten repetir código múltiples veces (while, for).  
# Palabras clave break y continue controlan el flujo dentro de los bucles.
# El bloque else en bucles se ejecuta si el bucle termina sin interrupciones.
# Es importante entender y usar correctamente estas estructuras para escribir programas efectivos.
# Ejemplos prácticos
# Verificar si un número es par o impar
numero = 7
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
# Calcular la suma de los primeros n números naturales
n = 10
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma de los primeros {n} números naturales es {suma}.")
# Encontrar el factorial de un número
factorial = 1
for i in range(1, 6):  # Factorial de 5
    factorial *= i
print("El factorial de 5 es", factorial)
# Contar cuántos números pares hay en una lista
numeros = [1, 2, 3, 4, 5, 6]
contador_pares = 0
for num in numeros:
    if num % 2 == 0:
        contador_pares += 1
print("Cantidad de números pares en la lista:", contador_pares)
# Uso de while para pedir un número positivo al usuario
# (Descomentar para usar)
# numero = -1
# while numero < 0:
#     numero = int(input("Ingrese un número positivo: "))
# print(f"Número positivo ingresado: {numero}")
# Nota: La sección de entrada de datos está comentada para evitar interrupciones en la ejecución
# durante pruebas automáticas. Descomentar para usar en un entorno interactivo. 
# Ejemplo de uso combinado
# Calcular la suma de números pares hasta un límite dado por el usuario
# (Descomentar para usar)
# limite = int(input("Ingrese un número límite: "))
# suma_pares = 0
# for i in range(limite + 1):
#     if i % 2 == 0:
#         suma_pares += i
# print(f"La suma de los números pares hasta {limite} es {suma_pares}.")
# Nota: La sección de entrada de datos está comentada para evitar interrupciones en la ejecución
# durante pruebas automáticas. Descomentar para usar en un entorno interactivo.
# Resumen final: El control de flujo es esencial para crear programas dinámicos y funcionales.
# Permite tomar decisiones y repetir acciones según sea necesario. Con práctica, se vuelve una herramienta poderosa en la programación.
