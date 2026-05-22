# Bucle while
# El bucle while se utiliza para repetir un bloque de código mientras se cumpla una condición.
# Sintaxis:
# while condición:
#     # bloque de código

# Ejemplo: Contar del 1 al 5
contador = 1
while contador <= 5:
    print(contador)
    contador += 1   # Incrementar el contador en 1
print("Bucle terminado")
# Ejemplo: Sumar números hasta que la suma sea mayor a 20
suma = 0
while suma <= 20:
    numero = int(input("Ingrese un número para sumar: "))
    suma += numero
    print(f"Suma actual: {suma}")
print("La suma ha superado 20, bucle terminado.")
# Ejemplo: Bucle infinito (usa Ctrl+C para detenerlo)
# while True:
#     print("Este bucle nunca termina.")
# Ejemplo: Uso de break para salir del bucle
while True:
    entrada = input("Ingrese 'salir' para terminar el bucle: ")
    if entrada.lower() == 'salir':
        print("Saliendo del bucle.")
        break
    print(f"Usted ingresó: {entrada}")
# Ejemplo: Uso de continue para saltar a la siguiente iteración
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Saltar los números pares
    print(f"Número impar: {contador}")
print("Bucle terminado.")
# Ejemplo: Uso de else con while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
else:
    print("El bucle while ha terminado normalmente.")
# Nota: El bloque else se ejecuta cuando la condición del while se vuelve falsa.
# Si el bucle se termina con break, el bloque else no se ejecuta.
# Ejemplo: Bucle con condición inicial falsa
contador = 10
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle while no se ejecutó, condición inicial falsa.")
# Ejemplo: Bucle con condición verdadera y break
contador = 1
while contador <= 5:   
    print(contador)
    if contador == 3:
        print("Contador es 3, saliendo del bucle.")
        break
    contador += 1
else:
    print("El bucle while ha terminado normalmente.")
# En este caso, el bloque else no se ejecuta porque el bucle se terminó con break.
# Ejemplo: Bucle con continue y else
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print("Contador es 3, saltando esta iteración.")
        continue
    print(f"Número: {contador}")
else:
    print("El bucle while ha terminado normalmente.")
# En este caso, el bloque else se ejecuta porque el bucle terminó normalmente.
# Ejemplo: Bucle con condición inicial falsa y else
contador = 10
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle while no se ejecutó, condición inicial falsa.")
# En este caso, el bloque else se ejecuta porque el bucle no se ejecutó.
# Ejemplo: Bucle con break y else
contador = 1
while contador <= 5:   
    print(contador)
    if contador == 3:
        print("Contador es 3, saliendo del bucle.")
        break
    contador += 1
else:
    print("El bucle while ha terminado normalmente.")
# En este caso, el bloque else no se ejecuta porque el bucle se terminó con break.
# Ejemplo: Bucle con continue y else
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print("Contador es 3, saltando esta iteración.")
        continue
    print(f"Número: {contador}")
else:
    print("El bucle while ha terminado normalmente.")
# En este caso, el bloque else se ejecuta porque el bucle terminó normalmente.
# Ejemplo: Bucle con condición inicial falsa y else
contador = 10
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle while no se ejecutó, condición inicial falsa.")
# En este caso, el bloque else se ejecuta porque el bucle no se ejecutó.
# Continue: Salta a la siguiente iteración del bucle
# Break: Sale completamente del bucle
# Else: Se ejecuta si el bucle termina normalmente (sin break)
# Ejemplo: Contar del 1 al 5, pero saltando el 3
contador = 1
while contador <= 5:
    if contador == 3:
        contador += 1
        continue  # Saltar el número 3
    print(contador)
    contador += 1
print("Bucle terminado")
# try/except dentro de un bucle while
while True:
    try:
        numero = int(input("Ingrese un número entero (o -1 para salir): "))
        if numero == -1:
            print("Saliendo del bucle.")
            break
        print(f"Usted ingresó: {numero}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
print("Bucle terminado.")
