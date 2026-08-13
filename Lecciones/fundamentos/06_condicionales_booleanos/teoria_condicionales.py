# Sentencias condicionales if, elif, else
LABEL_NUMERO = "Número:"

print("--- if / elif / else ---")
edad = 20
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes 18 años, eres mayor de edad.")
else:
    print("Eres mayor de edad.")

# Sentencia condicional anidada
print("\n--- Condicionales anidados (nota) ---")
nota = 85
if 0 <= nota <= 100:
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

print("\n--- Bucle while ---")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

print("\n--- Bucle for (lista) ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

print("\n--- Bucle for (range) ---")
for i in range(5):
    print(LABEL_NUMERO, i)

print("\n--- break y continue ---")
for i in range(5):
    if i == 2:
        continue
    print(LABEL_NUMERO, i)
    if i == 3:
        break

# for/else: else corre solo si NO hubo break (uso típico: búsqueda)
print("\n--- else con for (búsqueda; else = no encontrado) ---")
objetivo = 10  # no está en 0..2
for i in range(3):
    print(LABEL_NUMERO, i)
    if i == objetivo:
        print("Encontrado")
        break
else:
    print("No encontrado → se ejecutó el else del for")

print("\n--- else con while (vaciar lista sin break) ---")
pendientes = [1, 2, 3]
while pendientes:
    actual = pendientes.pop()
    print("Procesando:", actual)
    if actual == 99:
        break
else:
    print("Lista vacía sin break → else del while")

print("\n--- else con for (con break → else NO corre) ---")
for i in range(5):
    print(LABEL_NUMERO, i)
    if i == 2:
        print("Salgo con break; el else del for no se ejecuta.")
        break
else:
    print("Esto no se imprime.")

print("\n--- Ejemplo: par o impar ---")
numero = 7
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

print("\n--- Ejemplo: suma de primeros n naturales ---")
n = 10
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma de los primeros {n} números naturales es {suma}.")

print("\n--- Ejemplo: factorial ---")
factorial = 1
for i in range(1, 6):
    factorial *= i
print("El factorial de 5 es", factorial)

print("\n--- Ejemplo: contar pares en lista ---")
numeros = [1, 2, 3, 4, 5, 6]
contador_pares = 0
for num in numeros:
    if num % 2 == 0:
        contador_pares += 1
print("Cantidad de números pares en la lista:", contador_pares)

# Tip: pedir números con input() + while lo practicás en 05_input / 08_while.
