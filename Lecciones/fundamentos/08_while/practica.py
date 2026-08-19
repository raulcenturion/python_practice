# ============================
# 📝 Ejercicios: While
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
contador = 5
while contador > 0:
    print(f"Faltan {contador}...")
    contador -= 1
print("¡Despegue! 🚀")

# ============================
# Ejercicio 1: Cuenta atrás
# Imprimí los números del 10 al 1 usando while.
print("Ejercicio 1:")
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("Fin del ejercicio 1")


# Ejercicio 2: Suma de pares
# Calculá la suma de los números pares entre 1 y 20 usando while.
print("Ejercicio 2:")
contador = 1
suma = 0
while contador <= 20:
    if contador % 2 == 0:
        suma += contador
    contador += 1
print(f"La suma de los números pares entre 1 y 20 es: {suma}")
print("Fin del ejercicio 2")
# --- Ejercicio 2: Suma de pares ---
# contador = 1 → inicializa en 1 para recorrer los números del 1 al 20.
# suma = 0 → acumulador que empieza en 0.
#
# while contador <= 20:
#   → el bucle se repite mientras contador sea menor o igual a 20.
#
# if contador % 2 == 0:
#   → el operador % devuelve el resto de la división.
#   → si el resto al dividir por 2 es 0, el número es par.
#
# suma += contador
#   → acumula el número par en la variable suma.
#   → equivale a: suma = suma + contador.
#
# contador += 1
#   → incrementa el contador en 1 para pasar al siguiente número.
#
# Al finalizar el bucle, suma contiene la suma de todos los pares entre 1 y 20.
# Resultado final: 110



# Ejercicio 3: Factorial
# Pedí un número al usuario y calculá su factorial con while.
# Ej: 5! = 5 × 4 × 3 × 2 × 1 = 120
print("Ejercicio 3:")
numero = int(input("Ingrese un número factorial: "))
original = numero  # guardamos el valor porque el while lo va a ir bajando
factorial = 1
while numero > 0:
    factorial *= numero
    numero -= 1  # acá numero termina en 0 → por eso no hay que usarlo en el print final
print(f"El factorial de {original} es: {factorial}")
print("Fin del ejercicio 3")


# Ejercicio 4: Validar contraseña
# Pedí una contraseña. Seguí pidiendo hasta que tenga al menos 8 caracteres.
# Cuando sea válida, imprimí "Contraseña válida".
print("Ejercicio 4:")
contrasenia = input("Ingrese una contraseña: ")
while len(contrasenia) < 8:
    contrasenia = input("La contraseña debe tener al menos 8 caracteres. Ingrese una contraseña: ")
print("Contraseña válida")
print("Fin del ejercicio 4")
# --- Ejercicio 4: Validar contraseña ---
# contrasenia = input(...) → pide la primera contraseña.
#
# while len(contrasenia) < 8:
#   → el bucle se repite mientras la longitud sea menor que 8.
#   → actúa como un "if repetido": verifica la condición en cada vuelta.
#   → si la contraseña es corta, vuelve a pedir otra.
#
# Al salir del while significa que len(contrasenia) >= 8.
# Por eso se imprime directamente "Contraseña válida" sin necesidad de if.
#
# En resumen:
# - El while hace la verificación implícita.
# - Al terminar el bucle, la contraseña ya cumple la condición.


# Ejercicio 5: Tabla de multiplicar
# Pedí un número e imprimí su tabla de multiplicar (del 1 al 10) con while.
print("Ejercicio 5:")
numero = int(input("Ingrese un número: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
print("Fin del ejercicio 5")

# Ejercicio 6: Números primos hasta N
# Pedí un número N e imprimí todos los primos menores o iguales a N.
# (Sin funciones: un while afuera recorre candidatos; uno adentro prueba divisores.)
print("Ejercicio 6:")
numero = int(input("Ingrese un número: "))
candidato = 2
while candidato <= numero:
    # ¿candidato es primo? Probamos divisores desde 2.
    # Si encontramos alguno que lo divida exacto → NO es primo.
    divisor = 2
    es_primo = True  # asumimos que sí, hasta demostrar lo contrario
    while divisor * divisor <= candidato:
        if candidato % divisor == 0:
            es_primo = False
            break  # ya sabemos que no es primo; no hace falta seguir
        divisor += 1
    if es_primo:
        print(candidato)
    candidato += 1
print("Fin del ejercicio 6")
