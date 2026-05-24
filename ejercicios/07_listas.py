# ============================
# 📝 Ejercicios: Listas y sus métodos
# 📘 Teoría: fundamentos/08_listas.py + 09_metodos_listas.py
# ============================

# 🔸 Ejemplo:
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")       # Agrega al final
frutas.insert(1, "kiwi")       # Inserta en posición 1
print(frutas)                  # ['manzana', 'kiwi', 'banana', 'cereza', 'naranja']
print(frutas[1:3])             # ['kiwi', 'banana'] → slicing

# ============================
# Ejercicio 1: Mensaje secreto
# Dada la lista:
#   mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Usando slicing, extraé solo la palabra "secreto".


# Ejercicio 2: Intercambio de posiciones
# Dada: numeros = [10, 20, 30, 40, 50]
# Intercambiá la primera y última posición usando asignación por índice.


# Ejercicio 3: Sándwich de listas
# Dadas:
#   pan = ["pan arriba"]
#   ingredientes = ["jamón", "queso", "tomate"]
#   pan_abajo = ["pan abajo"]
# Creá una lista "sandwich" concatenando las tres.


# Ejercicio 4: Duplicar lista
# Dada lista = [1, 2, 3], creá una nueva con los elementos duplicados.
# Resultado: [1, 2, 3, 1, 2, 3]


# Ejercicio 5: Centro de la lista
# Dada una lista impar, extraé el elemento central usando slicing.
# Ej: [10, 20, 30, 40, 50] → 30


# Ejercicio 6: Reversa parcial
# Invertí solo la primera mitad.
# Ej: [1, 2, 3, 4, 5, 6] → [3, 2, 1, 4, 5, 6]


# Ejercicio 7: Añadir y modificar
# Creá una lista del 1 al 5. Agregá 6 con append(). Insertá 10 en posición 2.
# Modificá el primer elemento a 0.


# Ejercicio 8: Combinar y limpiar
# lista_a = [1, 2, 3] y lista_b = [4, 5, 6, 1, 2]
# Extendé lista_a con lista_b. Eliminá la primera aparición del 1.
# Eliminá el elemento en índice 3 con pop(). Limpiá lista_b con clear().


# Ejercicio 9: Ordenar y contar
# Dada: [5, 2, 8, 1, 9, 4, 2]
# Ordená con sort(). Contá cuántas veces aparece el 2. Verificá si 7 está en la lista.


# Ejercicio 10: Copia vs Referencia
# Creá original = [1, 2, 3]
# Hacé copia_1 con slicing [:], copia_2 con .copy(), y referencia = original
# Modificá referencia[0] = 10. ¿Qué pasó con cada una? Imprimí las 4.

