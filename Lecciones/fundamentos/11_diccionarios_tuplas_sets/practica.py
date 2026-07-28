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

numeros = {1, 2, 2, 3, 3}
print(numeros)  # {1, 2, 3} → sin duplicados

# ============================
# DICCIONARIOS
# ============================

# Ejercicio 1: CRUD de diccionario
# Creá un dict con nombre, edad y email. Agregá "país". Modificá "edad".
# Eliminá "email" con pop(). Imprimí el resultado.


# Ejercicio 2: Recorrer diccionario
# Dado usuario = {"nombre": "Ana", "edad": 28, "rol": "dev"}
# Recorrelo con .items() e imprimí "clave → valor" para cada par.


# Ejercicio 3: Diccionario anidado
# Creá un dict con 2 productos, cada uno con nombre y precio.
# Accedé al precio del segundo producto e imprimilo.


# ============================
# TUPLAS
# ============================

# Ejercicio 4: Desempaquetado
# Dada datos = ("Raúl", 33, "Argentina"), desempaquetá en nombre, edad, pais.


# Ejercicio 5: Función con retorno múltiple
# Creá una función que reciba una lista y retorne (min, max) como tupla.


# ============================
# SETS
# ============================

# Ejercicio 6: Eliminar duplicados
# Dada lista = [1, 2, 2, 3, 4, 4, 5], convertila a set para eliminar duplicados.


# Ejercicio 7: Operaciones de conjuntos
# Dados: a = {1, 2, 3, 4} y b = {3, 4, 5, 6}
# Calculá e imprimí: unión (|), intersección (&), diferencia (-)

