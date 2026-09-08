# ============================
# 📘 Tuplas en Python
# ============================
# Una tupla es una colección ordenada e INMUTABLE de elementos.
# Se definen con paréntesis () y no se pueden modificar una vez creadas.
# Ideales para datos fijos que no deben cambiar.

# 🔹 Crear tuplas
print("--- Crear tuplas ---")
mi_tupla = (1, 2, 3, 4, 5)
tupla_mixta = (1, "hola", True, 3.14, [1, 2])
tupla_un_elemento = (42,)  # ⚠️ La coma es necesaria, sin ella es solo un número entre paréntesis
no_es_tupla = (42)          # Esto es un int, NO una tupla
print("type(tupla_un_elemento):", type(tupla_un_elemento))  # <class 'tuple'>
print("type(no_es_tupla):", type(no_es_tupla))        # <class 'int'>

# 🔹 Acceder a elementos (igual que listas)
print("\n--- Acceder a elementos ---")
semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print("semana[0]:", semana[0])    # Lunes (primer elemento)
print("semana[-1]:", semana[-1])   # Domingo (último elemento)
print("semana[1:4]:", semana[1:4])  # ('Martes', 'Miércoles', 'Jueves') → slicing

# 🔹 Inmutabilidad: NO se pueden modificar
# semana[0] = "Monday"  # ❌ TypeError: 'tuple' object does not support item assignment

# 🔹 Métodos disponibles (solo 2, porque son inmutables)
print("\n--- Métodos count / index ---")
numeros = (1, 2, 3, 2, 4, 2, 5)
print("numeros.count(2):", numeros.count(2))   # 3 → cuántas veces aparece el 2
print("numeros.index(4):", numeros.index(4))   # 4 → en qué posición está el 4

# 🔹 Desempaquetado de tuplas (tuple unpacking)
print("\n--- Desempaquetado de tuplas ---")
# Permite asignar cada elemento de la tupla a una variable
coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")

# Con * para capturar el resto
primero, *resto = (1, 2, 3, 4, 5)
print(f"Primero: {primero}, Resto: {resto}")  # Primero: 1, Resto: [2, 3, 4, 5]

# 🔹 Tuplas como retorno de funciones
print("\n--- Tuplas como retorno de funciones ---")
def min_max(lista):
    return (min(lista), max(lista))

resultado = min_max([5, 2, 8, 1, 9])
print(f"Mínimo: {resultado[0]}, Máximo: {resultado[1]}")

# O con desempaquetado directo:
minimo, maximo = min_max([5, 2, 8, 1, 9])
print(f"Min: {minimo}, Max: {maximo}")
# --- Tuplas como retorno ---
# def min_max(lista):
#   → devuelve una tupla con (min(lista), max(lista)).
#   → min() y max() son funciones internas de Python:
#       min() → recorre la lista y devuelve el menor valor.
#       max() → recorre la lista y devuelve el mayor valor.
#
# resultado = min_max([5,2,8,1,9]) → (1, 9)
# resultado[0] → 1 (mínimo)
# resultado[1] → 9 (máximo)
#
# También se puede desempaquetar:
# minimo, maximo = min_max([5,2,8,1,9])
# → minimo = 1, maximo = 9
# --- Desempaquetado de tuplas ---
# min_max([5,2,8,1,9]) devuelve (1, 9).
# minimo, maximo = min_max(...) → asigna:
#   minimo = 1 (primer valor de la tupla)
#   maximo = 9 (segundo valor de la tupla)
#
# IMPORTANTE:
# - Python no "sabe" que son mínimo y máximo por el nombre.
# - Solo asigna valores por posición:
#   primera variable ← primer valor
#   segunda variable ← segundo valor
#
# Ejemplo:
# abc, dce = min_max([5,2,8,1,9])
# abc = 1, dce = 9


# 🔹 Tuplas como claves de diccionario (porque son inmutables)
print("\n--- Tuplas como claves de diccionario ---")
ubicaciones = {
    (-34.6, -58.4): "Buenos Aires",
    (40.4, -3.7): "Madrid",
}
print("ubicaciones[(-34.6, -58.4)]:", ubicaciones[(-34.6, -58.4)])  # Buenos Aires

# 🔹 Convertir entre tupla y lista
print("\n--- Convertir entre tupla y lista ---")
lista = [1, 2, 3]
tupla = tuple(lista)    # Lista → Tupla
lista2 = list(tupla)    # Tupla → Lista
print("tupla:", tupla, type(tupla))
print("lista2:", lista2, type(lista2))

# 🔹 Iterar sobre tuplas
print("\n--- Iterar sobre tuplas ---")
for dia in semana:
    print(dia)

print("\n--- Iterar con enumerate ---")
for i, dia in enumerate(semana):
    print(f"{i}: {dia}")

# 🔹 Tuplas anidadas
print("\n--- Tuplas anidadas ---")
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("matriz[1][2]:", matriz[1][2])  # 6

# 🔹 ¿Cuándo usar tuplas vs listas?
# ✅ Tuplas: datos que NO deben cambiar (coordenadas, días, constantes, retornos de función)
# ✅ Listas: datos que SÍ pueden cambiar (carrito de compras, tareas, resultados)
# 💡 Las tuplas son más rápidas y usan menos memoria que las listas
