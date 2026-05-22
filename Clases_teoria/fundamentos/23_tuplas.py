# ============================
# 📘 Tuplas en Python
# ============================
# Una tupla es una colección ordenada e INMUTABLE de elementos.
# Se definen con paréntesis () y no se pueden modificar una vez creadas.
# Ideales para datos fijos que no deben cambiar.

# 🔹 Crear tuplas
mi_tupla = (1, 2, 3, 4, 5)
tupla_mixta = (1, "hola", True, 3.14, [1, 2])
tupla_un_elemento = (42,)  # ⚠️ La coma es necesaria, sin ella es solo un número entre paréntesis
no_es_tupla = (42)          # Esto es un int, NO una tupla
print(type(tupla_un_elemento))  # <class 'tuple'>
print(type(no_es_tupla))        # <class 'int'>

# 🔹 Acceder a elementos (igual que listas)
semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(semana[0])    # Lunes (primer elemento)
print(semana[-1])   # Domingo (último elemento)
print(semana[1:4])  # ('Martes', 'Miércoles', 'Jueves') → slicing

# 🔹 Inmutabilidad: NO se pueden modificar
# semana[0] = "Monday"  # ❌ TypeError: 'tuple' object does not support item assignment

# 🔹 Métodos disponibles (solo 2, porque son inmutables)
numeros = (1, 2, 3, 2, 4, 2, 5)
print(numeros.count(2))   # 3 → cuántas veces aparece el 2
print(numeros.index(4))   # 4 → en qué posición está el 4

# 🔹 Desempaquetado de tuplas (tuple unpacking)
# Permite asignar cada elemento de la tupla a una variable
coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}")

# Con * para capturar el resto
primero, *resto = (1, 2, 3, 4, 5)
print(f"Primero: {primero}, Resto: {resto}")  # Primero: 1, Resto: [2, 3, 4, 5]

# 🔹 Tuplas como retorno de funciones
def min_max(lista):
    return (min(lista), max(lista))

resultado = min_max([5, 2, 8, 1, 9])
print(f"Mínimo: {resultado[0]}, Máximo: {resultado[1]}")

# O con desempaquetado directo:
minimo, maximo = min_max([5, 2, 8, 1, 9])
print(f"Min: {minimo}, Max: {maximo}")

# 🔹 Tuplas como claves de diccionario (porque son inmutables)
ubicaciones = {
    (-34.6, -58.4): "Buenos Aires",
    (40.4, -3.7): "Madrid",
}
print(ubicaciones[(-34.6, -58.4)])  # Buenos Aires

# 🔹 Convertir entre tupla y lista
lista = [1, 2, 3]
tupla = tuple(lista)    # Lista → Tupla
lista2 = list(tupla)    # Tupla → Lista
print(tupla, type(tupla))
print(lista2, type(lista2))

# 🔹 Iterar sobre tuplas
for dia in semana:
    print(dia)

# Con enumerate
for i, dia in enumerate(semana):
    print(f"{i}: {dia}")

# 🔹 Tuplas anidadas
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(matriz[1][2])  # 6

# 🔹 ¿Cuándo usar tuplas vs listas?
# ✅ Tuplas: datos que NO deben cambiar (coordenadas, días, constantes, retornos de función)
# ✅ Listas: datos que SÍ pueden cambiar (carrito de compras, tareas, resultados)
# 💡 Las tuplas son más rápidas y usan menos memoria que las listas
