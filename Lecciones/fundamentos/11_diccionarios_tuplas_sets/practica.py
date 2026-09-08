# ============================
# 📝 Ejercicios: Diccionarios, Tuplas y Sets
# 📘 Teoría: teoria_diccionarios.py, teoria_sets.py, teoria_tuplas.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
persona = {"nombre": "Raúl", "edad": 33}
print(persona.get("nombre"))      # Raúl
print(persona.get("phone", "—"))  # — (valor por defecto si no existe)

coordenadas = (10, 20)
x, y = coordenadas  # Desempaquetado

numeros = {1, 2, 3}
print(numeros)  # {1, 2, 3} → sin duplicados

# ============================
# DICCIONARIOS
# ============================

# Ejercicio 1: CRUD de diccionario
# Creá un dict con nombre, edad y email. Agregá "país". Modificá "edad".
# Eliminá "email" con pop(). Imprimí el resultado.
print("Ejercicio 1:")

persona = {"nombre": "Raúl", "edad": 33, "email": "raul@gmail.com"}
persona["país"] = "Argentina"
persona["edad"] = 34
persona.pop("email")
print(persona)

# Ejercicio 2: Recorrer diccionario
# Dado usuario = {"nombre": "Ana", "edad": 28, "rol": "dev"}
# Recorrelo con .items() e imprimí "clave → valor" para cada par.
print("Ejercicio 2:")
usuario = {"nombre": "Ana", "edad": 28, "rol": "dev"}
for clave, valor in usuario.items():
    print(f"{clave} → {valor}")

# Ejercicio 3: Diccionario anidado
# Creá un dict con 2 productos, cada uno con nombre y precio.
# Accedé al precio del segundo producto e imprimilo.
print("Ejercicio 3:")
productos = [
    {"nombre": "Producto 1", "precio": 100},
    {"nombre": "Producto 2", "precio": 200},
]
print(productos[1]["precio"])

# ============================
# TUPLAS
# ============================

# Ejercicio 4: Desempaquetado
# Dada datos = ("Raúl", 33, "Argentina"), desempaquetá en nombre, edad, pais.
print("Ejercicio 4:")
datos = ("Raúl", 33, "Argentina")
nombre, edad, pais = datos
print(nombre, edad, pais)
# --- Ejercicio 4: Desempaquetado ---
# datos = ("Raúl", 33, "Argentina")
#   → tupla con 3 elementos.
#
# nombre, edad, pais = datos
#   → desempaquetado de tupla:
#       nombre = "Raúl"   (primer valor)
#       edad   = 33       (segundo valor)
#       pais   = "Argentina" (tercer valor)
#
# print(nombre, edad, pais)
#   → imprime: Raúl 33 Argentina
#
# IMPORTANTE:
# - Python no interpreta el significado de los nombres de las variables.
# - Solo asigna valores por posición en la tupla.


# Ejercicio 5: Función con retorno múltiple
# Creá una función que reciba una lista y retorne (min, max) como tupla.
print("Ejercicio 5:")
def min_max(lista):
    return min(lista), max(lista)
print(min_max([1, 2, 3, 4, 5]))

# ============================
# SETS
# ============================

# Ejercicio 6: Eliminar duplicados
# Dada lista = [1, 2, 2, 3, 4, 4, 5], convertila a set para eliminar duplicados.
print("Ejercicio 6:")
lista = [1, 2, 2, 3, 4, 4, 5]
print(set(lista))

# Ejercicio 7: Operaciones de conjuntos
# Dados: a = {1, 2, 3, 4} y b = {3, 4, 5, 6}
# Calculá e imprimí: unión (|), intersección (&), diferencia (-)
print("Ejercicio 7:")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a & b)
print(a - b)
