# Tipos de datos en Python

print("int:", type(10))
print("float:", type(10.5))
print("str:", type("Hello"))
print("list:", type([1, 2, 3]))
# 🔹 Diccionario (dict)
print("dict:", type({"key": "value"}))
# 👉 Estructura clave-valor. Permite acceder rápidamente a datos por una "clave".
# Ejemplo: persona = {"nombre": "Raúl", "edad": 33}
# Acceso: persona["nombre"] → "Raúl"
# Mutable (puede cambiarse en tiempo de ejecución).
# Muy usado para representar configuraciones, JSON o respuestas de APIs.

# 🔹 Tupla (tuple)
print("tuple:", type((1, 2, 3)))
# 👉 Secuencia ordenada e inmutable de elementos.
# Ejemplo: coordenadas = (10, 20)
# No se puede modificar una vez creada.
# Ideal para datos fijos o retornos múltiples en funciones.

# 🔹 Conjunto (set)
print("set:", type({1, 2, 3}))
# 👉 Colección no ordenada y sin duplicados.
# Ejemplo: numeros = {1, 2, 2, 3} → {1, 2, 3}
# Útil para eliminar duplicados o hacer operaciones de conjuntos (union, intersección, diferencia).
# Mutable.

# 🔹 Booleano (bool)
print("bool:", type(True))
# 👉 Representa valores lógicos: True o False.
# Ejemplo: activo = True
# Usado en condiciones, comparaciones, control de flujo (if, while).

# 🔹 NoneType (None)
print("NoneType:", type(None))
# 👉 Representa la ausencia de valor o "nada".
# Ejemplo: resultado = None
# Usado para indicar que una variable o función no tiene resultado definido.

# 🔹 Números complejos (complex)
print("complex:", type(1 + 2j))
# 👉 Números con parte real e imaginaria.
# Ejemplo: z = 3 + 4j → z.real = 3, z.imag = 4
# Se usa poco fuera del ámbito científico o matemático.

# 🔹 Bytes (bytes)
print("bytes:", type(b"byte string"))
# 👉 Secuencia inmutable de datos binarios.
# Ejemplo: data = b"hola"
# Muy usado al trabajar con archivos binarios, redes, o criptografía.
# Inmutable.

# 🔹 Bytearray (bytearray)
print("bytearray:", type(bytearray(b"byte array")))
# 👉 Similar a bytes pero mutable.
# Ejemplo: data = bytearray(b"hola") → data[0] = 72 (modifica el valor).
# Útil cuando necesitás manipular datos binarios directamente.

# 🔹 Frozenset (frozenset)
print("frozenset:", type(frozenset([1, 2, 3])))
# 👉 Versión inmutable de un set.
# Ejemplo: fs = frozenset([1, 2, 3])
# No se puede modificar, ideal para usar como clave de diccionario o en operaciones seguras.

# 🔹 Range (range)
print("range:", type(range(5)))
# 👉 Secuencia de números generada en rango.
# Ejemplo: range(5) → [0, 1, 2, 3, 4]
# Usado comúnmente en bucles for.
# No genera una lista completa en memoria (eficiente).
# 🔹 Memoria vista (memoryview)
print("memoryview:", type(memoryview(b"hola")))
# 👉 Permite acceder a los datos de un objeto de bytes sin copiarlos.
# Ejemplo: mv = memoryview(b"hola")
# mv[0] → 104 (código ASCII de 'h')
# Útil para manipular grandes cantidades de datos binarios de manera eficiente.
