# ============================
# 📘 Métodos de listas
# ============================
# Objetivo de este archivo: ver los métodos más usados para
# agregar, borrar, ordenar y consultar elementos de una lista.
#
# Idea clave: la lista es MUTABLE (se puede cambiar).
# Algunos métodos modifican la lista "en el lugar"
# (ej. sort, insert). Otros NO la tocan y devuelven otra cosa
# (ej. sorted → nueva lista; count → un número).

DOG = "🐶"
PANDA = "🐼"
KOALA = "🐨"
NUMBERS = [3, 10, 2, 8, 99, 101]
FRUTAS_BASE = ["manzana", "pera", "manzana", "pera", "limón"]
LABEL_ANTES = "antes :"
LABEL_DESPUES = "después:"

# ---------------------------
# insert(posición, valor)
# ---------------------------
# ¿Para qué? Meter un elemento en un índice concreto.
# Los que estaban desde esa posición se corren a la derecha.
# Índices: 0 = primero, 1 = segundo, etc.
print("--- insert() — meter un elemento en una posición ---")
print("Meta: en [1, 2, 3, 4, 5, 6] insertar 'nuevo' en el índice 2")
lista = [1, 2, 3, 4, 5, 6]
print(LABEL_ANTES, lista)
lista.insert(2, "nuevo")
print(LABEL_DESPUES, lista)
print("Lectura: quedó [1, 2, 'nuevo', 3, 4, 5, 6]")

# ---------------------------
# del lista[inicio:fin]
# ---------------------------
# ¿Para qué? Borrar un rango de índices (slice).
# Ojo: el fin NO se incluye. [1:3] borra índices 1 y 2.
print("\n--- del con rango — borrar varios de una vez ---")
print("Meta: de [🐼, 🐨, 🐶, 😿, 🐹] borrar índices 1 y 2 (🐨 y 🐶)")
lista1 = [PANDA, KOALA, DOG, "😿", "🐹"]
print(LABEL_ANTES, lista1)
del lista1[1:3]
print(LABEL_DESPUES, lista1)
print("Lectura: quedan 🐼, 😿 y 🐹")

# ---------------------------
# sort()  → modifica la lista original
# ---------------------------
# ¿Para qué? Ordenar la MISMA lista (de menor a mayor por defecto).
# No crea otra lista: cambia la que ya tenés.
print("\n--- sort() — ordena la lista original ---")
print("Meta: ordenar números y ver que NUMBERS original no se toca")
numbers = list(NUMBERS)  # copia, para no pisar NUMBERS
print(LABEL_ANTES, numbers)
numbers.sort()
print(LABEL_DESPUES, numbers)
print("NUMBERS (original):", NUMBERS)
print("Lectura: sort() cambió 'numbers'; NUMBERS sigue igual")

# ---------------------------
# sorted(lista)  → nueva lista ordenada
# ---------------------------
# ¿Para qué? Querés una versión ordenada SIN tocar la original.
# Devuelve otra lista; la de entrada queda igual.
print("\n--- sorted() — nueva lista ordenada (no modifica la original) ---")
print("Meta: obtener una copia ordenada de NUMBERS")
sorted_numbers = sorted(NUMBERS)
print("original NUMBERS :", NUMBERS)
print("nueva sorted_... :", sorted_numbers)
print("Lectura: usá sorted() si necesitás conservar el orden original")

# ---------------------------
# sorted() con strings
# ---------------------------
# Ordena alfabéticamente (según Unicode/orden del sistema).
print("\n--- sorted() con cadenas ---")
print("Meta: ordenar frutas alfabéticamente")
sorted_frutas = sorted(FRUTAS_BASE)
print("original:", FRUTAS_BASE)
print("ordenado:", sorted_frutas)
print("Lectura: 'limón' va antes que 'manzana' y 'pera'")

# ---------------------------
# sort(key=...) — orden personalizado
# ---------------------------
# Sin key, "Pera" y "pera" se ordenan distinto (mayúsculas vs minúsculas).
# key=str.lower compara todo en minúsculas → orden más natural.
print("\n--- sort(key=str.lower) — ignorar mayúsculas al ordenar ---")
print("Meta: ordenar frutas sin que la mayúscula altere el orden")
frutas = ["manzana", "Pera", "Limón", "manzana", "pera", "limón"]
print(LABEL_ANTES, frutas)
frutas.sort(key=str.lower)
print(LABEL_DESPUES, frutas)
print("Lectura: 'Limón'/'limón' y 'Pera'/'pera' quedan juntos lógicamente")

# ---------------------------
# len / count / in
# ---------------------------
# len(lista)     → cuántos elementos hay
# lista.count(x) → cuántas veces aparece x
# x in lista     → True/False (¿está o no?)
print("\n--- len / count / in — consultar la lista ---")
print("Meta: tamaño, repeticiones y pertenencia")
animals = [DOG, PANDA, KOALA, DOG]
print("lista :", animals)
print("len(animals):", len(animals), "→ hay 4 elementos")
print("count DOG:", animals.count(DOG), "→ el perro aparece 2 veces")
print("PANDA in animals:", PANDA in animals, "→ True, está")
print("hamster in animals:", "🐹" in animals, "→ False, no está")

# ---------------------------
# Mini mapa mental
# ---------------------------
# insert(i, x)  → agregar en posición i
# del lista[a:b]→ borrar rango
# sort()        → ordenar EN la lista
# sorted(lista) → devolver OTRA lista ordenada
# len / count / in → preguntar (no modifican)
