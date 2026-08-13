# Bucle while
# Repite un bloque mientras se cumpla una condición.

MSG_FIN = "Fin del ejemplo while."
LABEL_VALOR = "valor:"

print("--- Contar del 1 al 5 ---")
contador = 1
while contador <= 5:
    print(LABEL_VALOR, contador)
    contador += 1
print(MSG_FIN)

print("\n--- Sumar hasta superar 20 (input) ---")
suma = 0
while suma <= 20:
    numero = int(input("Ingrese un número para sumar: "))
    suma += numero
    print(f"Suma actual: {suma}")
print("La suma ha superado 20.")

print("\n--- break con input ---")
while True:
    entrada = input("Ingrese 'salir' para terminar el bucle: ")
    if entrada.lower() == "salir":
        print("Salida pedida por el usuario.")
        break
    print(f"Usted ingresó: {entrada}")

print("\n--- continue (saltar pares) ---")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(f"Número impar: {contador}")
print(MSG_FIN)

# else: se ejecuta si el while termina SIN break
print("\n--- else con while (sin break → else corre) ---")
cola = [1, 2, 3, 4, 5]
while cola:
    actual = cola.pop(0)
    print(LABEL_VALOR, actual)
    if actual == 99:
        break
else:
    print("Cola vacía sin break → else del while.")

print("\n--- Condición inicial falsa + else ---")
cola_vacia: list[int] = []
while cola_vacia:
    actual = cola_vacia.pop()
    print(LABEL_VALOR, actual)
    if actual == 99:
        break
else:
    print("No entró al while; igual corre else.")

print("\n--- break (else NO se ejecuta) ---")
contador = 1
while contador <= 5:
    print(LABEL_VALOR, contador)
    if contador == 3:
        print("Contador es 3, salgo con break.")
        break
    contador += 1
else:
    print("Esto no se imprime porque hubo break.")

print("\n--- continue + else (else sí corre) ---")
cola = [1, 2, 3, 4, 5]
while cola:
    actual = cola.pop(0)
    if actual == 3:
        print("Salto el 3 con continue.")
        continue
    print(f"Número: {actual}")
print("Terminó sin break → else del while.")

print("\n--- Contar 1..5 saltando el 3 ---")
contador = 1
while contador <= 5:
    if contador == 3:
        contador += 1
        continue
    print(LABEL_VALOR, contador)
    contador += 1
print(MSG_FIN)

print("\n--- try/except dentro de while (input) ---")
while True:
    try:
        numero = int(input("Ingrese un número entero (o -1 para salir): "))
        if numero == -1:
            print("Salida con -1.")
            break
        print(f"Usted ingresó: {numero}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
print(MSG_FIN)

# Resumen: continue salta iteración; break sale; else corre solo sin break.
