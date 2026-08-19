# ============================
# 📝 Ejercicios: For y Rangos
# 📘 Teoría: teoria_for.py, teoria_rangos.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
# for con enumerate() para tener índice y valor
colores = ["rojo", "verde", "azul"]
for i, color in enumerate(colores):
    print(f"{i}: {color}")

# range(inicio, fin, paso)
for num in range(2, 11, 2):
    print(num, end=" ")  # 2 4 6 8 10
print()

# ============================
# Ejercicio 1: Números del 1 al 10
# Imprimí los números del 1 al 10 usando for y range().
print("Ejercicio 1: Números del 1 al 10")
for num in range(1, 11):
    print(num, end=" ")
print()


# Ejercicio 2: Impares del 1 al 20
# Imprimí todos los impares entre 1 y 20 usando range() con paso.
print("Ejercicio 2: Impares del 1 al 20")
for num in range(1, 21, 2):
    print(num, end=" ")
print()


# Ejercicio 3: Múltiplos de 5
# Imprimí los múltiplos de 5 desde 5 hasta 50 usando range().
print("Ejercicio 3: Múltiplos de 5")
for num in range(5, 51, 5):
    print(num, end=" ")
print()


# Ejercicio 4: Cuenta atrás
# Imprimí del 10 al 1 usando range() con paso negativo.
print("Ejercicio 4: Cuenta atrás")
for num in range(10, 0, -1):
    print(num, end=" ")
print()


# Ejercicio 5: Suma del 1 al 100
# Calculá la suma de los números del 1 al 100 usando for y range().
print("Ejercicio 5: Suma del 1 al 100")
suma = 0
for num in range(1, 101):
    suma += num
print(suma)
print()


# Ejercicio 6: Tabla de multiplicar
# Pedí un número e imprimí su tabla del 1 al 10 con for.
print("Ejercicio 6: Tabla de multiplicar")
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print()
# --- Ejercicio 6: Tabla de multiplicar con for ---
# numero = int(input(...)) → pide un número y lo guarda en la variable numero.
#
# for i in range(1, 11):
#   → range(1, 11) genera los números del 1 al 10 (el 11 no se incluye).
#   → la variable i toma cada uno de esos valores en cada vuelta del bucle.
#   → i es la "variable de iteración" del for.
#
# print(f"{numero} x {i} = {numero * i}")
#   → imprime la multiplicación del número ingresado por el valor actual de i.
#   → ejemplo: si numero = 7 e i = 3 → imprime "7 x 3 = 21".
#
# Al finalizar el bucle, se imprimen todas las multiplicaciones del 1 al 10.


# Ejercicio 7: Media de una lista
# Dada numeros = [10, 20, 30, 40, 50], calculá la media con for.
print("Ejercicio 7: Media de una lista")
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
media = suma / len(numeros)
print(media)
print()

# Ejercicio 8: Máximo de una lista
# Dada numeros = [15, 5, 25, 10, 20], encontrá el máximo con for (sin usar max()).
# Idea: arrancamos asumiendo que el primero es el máximo;
# después comparamos uno por uno y actualizamos si encontramos uno mayor.
print("Ejercicio 8: Máximo de una lista")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for num in numeros[1:]:  # el [0] ya es el candidato inicial
    if num > maximo:
        maximo = num
print(maximo)
print()

# Ejercicio 9: Filtrar por longitud
# Dada palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Creá una nueva lista solo con palabras de más de 4 letras (list comprehension).
print("Ejercicio 9: Filtrar por longitud")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 4]
print(palabras_largas)
print()


# Ejercicio 10: Contar por letra
# Dada palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pedí una letra y contá cuántas palabras empiezan con esa letra.
print("Ejercicio 10: Contar por letra")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Ingrese una letra: ")
contador = 0
for palabra in palabras:
    if palabra.startswith(letra):
        contador += 1
print(contador)
print()
