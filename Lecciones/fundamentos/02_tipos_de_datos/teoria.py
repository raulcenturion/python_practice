# Tipos de datos en Python
# type() te dice la clase de un valor en runtime.

entero = 10
decimal = 10.5
texto = "Hello"
lista = [1, 2, 3]

print("int:", type(entero))
print("float:", type(decimal))
print("str:", type(texto))
print("list:", type(lista))

# 🔹 Diccionario (dict)
persona = {"key": "value"}
print("dict:", type(persona))
# 👉 Estructura clave-valor. Permite acceder rápidamente a datos por una "clave".
# Ejemplo: persona = {"nombre": "Raúl", "edad": 33}
# Acceso: persona["nombre"] → "Raúl"
# Mutable (puede cambiarse en tiempo de ejecución).
# Muy usado para representar configuraciones, JSON o respuestas de APIs.

# 🔹 Tupla (tuple)
coordenadas = (1, 2, 3)
print("tuple:", type(coordenadas))
# 👉 Secuencia ordenada e inmutable de elementos.
# Ejemplo: coordenadas = (10, 20)
# No se puede modificar una vez creada.
# Ideal para datos fijos o retornos múltiples en funciones.

# 🔹 Conjunto (set)
numeros = {1, 2, 3}
print("set:", type(numeros))
# 👉 Colección no ordenada y sin duplicados.
# Ejemplo: numeros = {1, 2, 2, 3} → {1, 2, 3}
# Útil para eliminar duplicados o hacer operaciones de conjuntos (union, intersección, diferencia).
# Mutable.

# 🔹 Booleano (bool)
activo = True
print("bool:", type(activo))
# 👉 Representa valores lógicos: True o False.
# Ejemplo: activo = True
# Usado en condiciones, comparaciones, control de flujo (if, while).

# 🔹 NoneType (None)
resultado = None
print("NoneType:", type(resultado))
# 👉 Representa la ausencia de valor o "nada".
# Ejemplo: resultado = None
# Usado para indicar que una variable o función no tiene resultado definido.

# 🔹 Números complejos (complex)
complejo = 1 + 2j
print("complex:", type(complejo))
# 👉 Números con parte real e imaginaria.
# Ejemplo: z = 3 + 4j → z.real = 3, z.imag = 4
# Se usa poco fuera del ámbito científico o matemático.

# 🔹 Bytes (bytes)
datos_bytes = b"byte string"
print("bytes:", type(datos_bytes))
# 👉 Secuencia inmutable de datos binarios.
# Ejemplo: data = b"hola"
# Muy usado al trabajar con archivos binarios, redes, o criptografía.
# Inmutable.

# 🔹 Bytearray (bytearray)
datos_bytearray = bytearray(b"byte array")
print("bytearray:", type(datos_bytearray))
# 👉 Similar a bytes pero mutable.
# Ejemplo: data = bytearray(b"hola") → data[0] = 72 (modifica el valor).
# Útil cuando necesitás manipular datos binarios directamente.

# 🔹 Frozenset (frozenset)
conjunto_fijo = frozenset([1, 2, 3])
print("frozenset:", type(conjunto_fijo))
# 👉 Versión inmutable de un set.
# Ejemplo: fs = frozenset([1, 2, 3])
# No se puede modificar, ideal para usar como clave de diccionario o en operaciones seguras.

# 🔹 Range (range)
rango = range(5)
print("range:", type(rango))
# 👉 Secuencia de números generada en rango.
# Ejemplo: range(5) → [0, 1, 2, 3, 4]
# Usado comúnmente en bucles for.
# No genera una lista completa en memoria (eficiente).

# 🔹 Memoria vista (memoryview)
vista = memoryview(b"hola")
print("memoryview:", type(vista))
# 👉 Permite acceder a los datos de un objeto de bytes sin copiarlos.
# Ejemplo: mv = memoryview(b"hola")
# mv[0] → 104 (código ASCII de 'h')
# Útil para manipular grandes cantidades de datos binarios de manera eficiente.
