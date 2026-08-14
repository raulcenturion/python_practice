# Listas en Python
# Una lista es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos de datos.
# Las listas se definen utilizando corchetes [] y los elementos se separan por comas.

# Ejemplo de creación de una lista
print("--- Crear una lista ---")
mi_lista = [1, 2, 3, "cuatro", "cinco", 6.0]
print("mi_lista:", mi_lista)

print("\n--- Ejemplo: Celsius a Fahrenheit (input) ---")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

# Tipos de datos en listas
# Las listas pueden contener elementos de diferentes tipos de datos, como enteros, flotantes, cadenas, booleanos, etc.
print("\n--- Lista mixta ---")
mi_lista_mixta = [1, "dos", 3.0, True, [5, 6], (7, 8)]
print("mi_lista_mixta:", mi_lista_mixta)

# Acceso a elementos de una lista
# Los elementos de una lista se acceden mediante índices, que comienzan en 0.
print("\n--- Acceso por índice ---")
print("mi_lista[0]:", mi_lista[0])   # Primer elemento
print("mi_lista[3]:", mi_lista[3])   # Cuarto elemento
print("mi_lista[-1]:", mi_lista[-1])  # Último elemento

# Modificación de elementos de una lista
print("\n--- Modificar elementos ---")
mi_lista[1] = "dos_modificado"
print("mi_lista:", mi_lista)

# Agregar elementos a una lista
print("\n--- Agregar elementos (append / insert) ---")
mi_lista.append("nuevo_elemento")
print("después de append:", mi_lista)
mi_lista.insert(2, "elemento_en_posicion_2")
print("después de insert:", mi_lista)

# Eliminar elementos de una lista
# --- Eliminar elementos de una lista ---
# remove(valor) → elimina la primera aparición del valor indicado.
#   Ejemplo: mi_lista.remove("cuatro") borra el elemento "cuatro" si existe.
#
# del lista[indice] → elimina el elemento en la posición indicada.
#   Ejemplo: del mi_lista[0] borra el primer elemento de la lista.
#
# Diferencia clave:
# - remove trabaja por contenido (valor).
# - del trabaja por posición (índice).
print("\n--- Eliminar elementos (remove / del) ---")
mi_lista.remove("cuatro")
print("después de remove:", mi_lista)
del mi_lista[0]
print("después de del:", mi_lista)

# Recorrer una lista
print("\n--- Recorrer una lista ---")
for elemento in mi_lista:
    print("elemento:", elemento)

# Funciones útiles para listas
print("\n--- Funciones útiles (len / count / index) ---")
print("len(mi_lista):", len(mi_lista))            # Longitud de la lista
print("mi_lista.count(2):", mi_lista.count(2))    # Cuenta cuántas veces aparece el elemento 2
print('mi_lista.index("cinco"):', mi_lista.index("cinco"))  # Índice del elemento "cinco"
lista1: list[int|str|float|bool] = [1, "hola", 3.14, True]  # Lista de tipos mixtos
lista_vacia = []  # Lista vacía
print("lista1:", lista1)
print("lista_vacia:", lista_vacia)

# Listas anidadas
print("\n--- Listas anidadas y matrices ---")
lista_anidada = [1, 2, [3, 4], [5, 6]]
print("lista_anidada:", lista_anidada)
# Matrices (listas de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matriz[1][2]:", matriz[1][2])  # Acceder al elemento 6

# Concatenar listas
print("\n--- Concatenar listas ---")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("lista_concatenada:", lista_concatenada)

# slices (rebanadas) de listas
print("\n--- Slicing (rebanadas) ---")
sub_lista = lista_concatenada[1:4]  # Elementos desde el índice 1 hasta el 3
print("sub_lista [1:4]:", sub_lista)
lista = [1, 2, 3, 4, 5]
print("lista[::2]:", lista[::2])    # Elementos en posiciones pares
print("lista[::-1]:", lista[::-1])  # Lista invertida
print("lista[:3]:", lista[:3])      # Primeros tres elementos
print("lista[3:]:", lista[3:])      # Desde el cuarto elemento hasta el final
print("lista[:]:", lista[:])        # Toda la lista
print("lista[1:-1]:", lista[1:-1])  # Desde el segundo elemento hasta el penúltimo
print("lista[1:4]:", lista[1:4])    # Desde el segundo elemento hasta el cuarto (sin incluirlo)
# Desde, hasta, paso
print("lista[::2]:", lista[::2])    # Desde el inicio hasta el final, con paso 2
print("lista[1::2]:", lista[1::2])  # Desde el segundo elemento hasta el final, con paso 2
print("lista[:4:2]:", lista[:4:2])  # Desde el inicio hasta el cuarto elemento (sin incluirlo), con paso 2
print("lista[::-1]:", lista[::-1])  # Lista invertida

# Añadir elementos a una lista
print("\n--- Añadir con + / append / += ---")
lista3 = [1, 2, 3]
# Forma larga y menos eficiente
lista3 = lista3 + [4]
print("lista3 + [4]:", lista3)
# Forma eficiente
lista3.append(5)
print("después de append(5):", lista3)
lista3 += [6, 7, 8, 9]
print("después de += [6,7,8,9]:", lista3)

# Ejercicios prácticos con listas y condicionales
###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("--- Ejercicio 1: El mensaje secreto ---Utilizando slicing y concatenación---")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = mensaje[7:]
print("mensaje_secreto:", mensaje_secreto)
# En esta linea lo que se hace es convertir la lista en una cadena de caracteres y el join es para unir los elementos de la lista en una cadena de caracteres
mensaje_secreto = "".join(mensaje[7:])
print("mensaje_secreto:", mensaje_secreto)


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("--- Ejercicio 2: Intercambio de posiciones ---")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
# La línea numeros[0], numeros[-1] = numeros[-1], numeros[0]
# funciona como un "swap" (intercambio) en una sola instrucción.
# Paso 1: Python evalúa la parte derecha → (numeros[-1], numeros[0])
#         que es una tupla con los valores actuales (último, primero).
# Paso 2: Asigna esos valores en orden a la izquierda:
#         numeros[0] = último valor
#         numeros[-1] = primer valor
# Resultado: se intercambian el primer y el último elemento de la lista.
print("numeros:", numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("--- Ejercicio 3: El sándwich de listas ---")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print("sandwich:", sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("--- Ejercicio 4: Duplicando la lista ---")
lista = [1, 2, 3]
lista_duplicada = lista * 2
print("lista_duplicada:", lista_duplicada)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("--- Ejercicio 5: Extrayendo el centro ---")
lista = [10, 20, 30, 40, 50]
centro = lista[len(lista) // 2]
print("centro:", centro)
# --- Formas de obtener el elemento central de una lista ---
# Método clásico con len() y división entera:
# centro = lista[len(lista)//2]
#   → Usa la longitud de la lista y devuelve el índice central.
#   → En listas pares devuelve el "central derecho".

# Usando slicing:
# medio = len(lista)//2
# centro = lista[medio:medio+1]
#   → Devuelve una sublista con el elemento central.

# Usando statistics.median:
# import statistics
# centro = statistics.median(lista)
#   → Devuelve la mediana matemática.
#   → En listas impares coincide con el elemento central.
#   → En listas pares devuelve el promedio de los dos centrales.

# Usando math.floor y math.ceil (para listas pares):
# import math
# centro_izq = lista[math.floor(len(lista)/2) - 1]
# centro_der = lista[math.ceil(len(lista)/2)]
#   → Permite elegir entre el central izquierdo o derecho.


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("--- Ejercicio 6: Reversa parcial ---")
lista = [1, 2, 3, 4, 5, 6]
lista_reversa_parcial = lista[2::-1] + lista[3:]
print("lista_reversa_parcial:", lista_reversa_parcial)