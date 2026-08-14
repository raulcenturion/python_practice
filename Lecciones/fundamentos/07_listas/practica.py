# ============================
# 📝 Ejercicios: Listas y sus métodos
# 📘 Teoría: teoria_listas.py, teoria_metodos.py (misma carpeta)
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
print("--- Ejercicio 1: Mensaje secreto ---")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
palabra_secreto = mensaje[11:17]
print("palabra_secreto:", palabra_secreto)


# Ejercicio 2: Intercambio de posiciones
# Dada: numeros = [10, 20, 30, 40, 50]
# Intercambiá la primera y última posición usando asignación por índice.
print("--- Ejercicio 2: Intercambio de posiciones ---")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print("numeros:", numeros)

# Ejercicio 3: Sándwich de listas
# Dadas:
#   pan = ["pan arriba"]
#   ingredientes = ["jamón", "queso", "tomate"]
#   pan_abajo = ["pan abajo"]
# Creá una lista "sandwich" concatenando las tres.
print("--- Ejercicio 3: Sándwich de listas ---")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print("sandwich:", sandwich)    

# Ejercicio 4: Duplicar lista
# Dada lista = [1, 2, 3], creá una nueva con los elementos duplicados.
# Resultado: [1, 2, 3, 1, 2, 3]
print("--- Ejercicio 4: Duplicar lista ---")
lista = [1, 2, 3]
lista_duplicada = lista * 2
print("lista_duplicada:", lista_duplicada)

# Ejercicio 5: Centro de la lista
# Dada una lista impar, extraé el elemento central usando slicing.
# Ej: [10, 20, 30, 40, 50] → 30
print("--- Ejercicio 5: Centro de la lista ---")
lista = [10, 20, 30, 40, 50]
centro = lista[len(lista) // 2]
print("centro:", centro)

# Ejercicio 6: Reversa parcial
# Invertí solo la primera mitad.
# Ej: [1, 2, 3, 4, 5, 6] → [3, 2, 1, 4, 5, 6]
print("--- Ejercicio 6: Reversa parcial ---")
lista = [1, 2, 3, 4, 5, 6]
lista_reversa_parcial = lista[2::-1] + lista[3:]
print("lista_reversa_parcial:", lista_reversa_parcial)  

# Ejercicio 7: Añadir y modificar
# Creá una lista del 1 al 5. Agregá 6 con append(). Insertá 10 en posición 2.
# Modificá el primer elemento a 0.
print("--- Ejercicio 7: Añadir y modificar ---")
lista = [1, 2, 3, 4, 5]
lista.append(6)
print("lista-append(6):", lista)
lista.insert(2, 10)
print("lista-insert(2, 10):", lista)
lista[0] = 0
print("lista-modificar(0):", lista)

# Ejercicio 8: Combinar y limpiar
# lista_a = [1, 2, 3] y lista_b = [4, 5, 6, 1, 2]
# Extendé lista_a con lista_b. Eliminá la primera aparición del 1.
# Eliminá el elemento en índice 3 con pop(). Limpiá lista_b con clear().
print("--- Ejercicio 8: Combinar y limpiar ---")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print("lista_a-extend(lista_b):", lista_a)
lista_a.remove(1)
print("lista_a-remove(1):", lista_a)
lista_b.pop(3)
print("lista_b-pop(3):", lista_b)
lista_b.clear()
print("lista_b-clear():", lista_b)
# --- Diferencia entre append y extend ---
# append(x) → agrega un solo elemento al final de la lista.
#   Ejemplo: [1,2,3].append([4,5]) → [1,2,3,[4,5]]
#   (mete la lista como un bloque dentro de la otra).
#
# extend(lista) → agrega cada elemento de la otra lista por separado.
#   Ejemplo: [1,2,3].extend([4,5]) → [1,2,3,4,5]
#   (combina las listas en una sola).
#
# En resumen:
# - append → añade un único objeto (puede ser número, string o incluso otra lista).
# - extend → recorre el iterable y añade cada elemento individualmente.


# Ejercicio 9: Ordenar y contar
# Dada: [5, 2, 8, 1, 9, 4, 2]
# Ordená con sort(). Contá cuántas veces aparece el 2. Verificá si 7 está en la lista.
print("--- Ejercicio 9: Ordenar y contar ---")
lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
print("lista-sort():", lista)
print("lista.count(2):", lista.count(2))
print("7 in lista:", 7 in lista)

# Ejercicio 10: Copia vs Referencia
# Creá original = [1, 2, 3]
# Hacé copia_1 con slicing [:], copia_2 con .copy(), y referencia = original
# Modificá referencia[0] = 10. ¿Qué pasó con cada una? Imprimí las 4.
print("--- Ejercicio 10: Copia vs Referencia ---")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print("original:", original)
print("copia_1:", copia_1)
print("copia_2:", copia_2)
print("referencia:", referencia)
