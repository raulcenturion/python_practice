# Listas en Python 
# Una lista es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos de datos.
# Las listas se definen utilizando corchetes [] y los elementos se separan por comas.
# Ejemplo de creación de una lista
mi_lista = [1, 2, 3, "cuatro", "cinco", 6.0]
print(mi_lista)
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
# Tipos de datos en listas
# Las listas pueden contener elementos de diferentes tipos de datos, como enteros, flotantes, cadenas, booleanos, etc.
mi_lista_mixta = [1, "dos", 3.0, True, [5, 6], (7, 8)]
print(mi_lista_mixta)
# Acceso a elementos de una lista
# Los elementos de una lista se acceden mediante índices, que comienzan en 0.
print(mi_lista[0])  # Primer elemento
print(mi_lista[3])  # Cuarto elemento
print(mi_lista[-1]) # Último elemento
# Modificación de elementos de una lista
mi_lista[1] = "dos_modificado"
print(mi_lista)
# Agregar elementos a una lista
mi_lista.append("nuevo_elemento")
print(mi_lista)
mi_lista.insert(2, "elemento_en_posicion_2")
print(mi_lista)
# Eliminar elementos de una lista
mi_lista.remove("cuatro")
print(mi_lista)
del mi_lista[0]
print(mi_lista)
# Recorrer una lista
for elemento in mi_lista:
    print(elemento)
# Funciones útiles para listas
print(len(mi_lista))          # Longitud de la lista
print(mi_lista.count(2))      # Cuenta cuántas veces aparece el elemento 2
print(mi_lista.index("cinco")) # Índice del elemento "cinco"
lista1: list[int|str|float|bool] = [1, "hola", 3.14, True] # Lista de tipos mixtos
lista_vacia = []  # Lista vacía
# Listas anidadas
lista_anidada = [1, 2, [3, 4], [5, 6]]
# Matrices (listas de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][2])  # Acceder al elemento 6

# Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)
# slices (rebanadas) de listas
sub_lista = lista_concatenada[1:4]  # Elementos desde el índice 1 hasta el 3
print(sub_lista)
lista = [1,2,3,4,5]
print(lista[::2])  # Elementos en posiciones pares
print(lista[::-1]) # Lista invertida
print(lista[:3])  # Primeros tres elementos
print(lista[3:])  # Desde el cuarto elemento hasta el final
print(lista[:])  # Toda la lista
print(lista[1:-1])  # Desde el segundo elemento hasta el penúltimo
print(lista[1:4])  # Desde el segundo elemento hasta el cuarto (sin incluirlo)
# Desde, hasta, paso
print(lista[::2])  # Desde el inicio hasta el final, con paso 2
print(lista[1::2]) # Desde el segundo elemento hasta el final, con paso 2
print(lista[:4:2]) # Desde el inicio hasta el cuarto elemento (sin incluirlo), con paso 2
print(lista[::-1]) # Lista invertida
# Añadir elementos a una lista
lista3 = [1, 2, 3]
# Forma larga y menos eficiente
lista3 = lista3 + [4]
print(lista3)
# Forma eficiente
lista3.append(5)
print(lista3)
lista3 += [6,7,8,9]
print(lista3)
# Ejercicios prácticos con listas y condicionales
###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]