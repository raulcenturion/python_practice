# ============================
# 📝 Ejercicios: Casting (conversión de tipos)
# 📘 Teoría: fundamentos/03_casting.py
# ============================

# 🔸 Ejemplo:
# int() trunca (no redondea), str() convierte cualquier cosa a texto
print(int(9.99))       # 9 (trunca el decimal)
print(str(100))        # "100" (ahora es texto)
print(bool(""))        # False (string vacío = False)
print(bool("hola"))    # True (string con contenido = True)

# ============================
# Ejercicio 1: Float a int
# Convertí el float 9.99 a int. ¿Se redondea o se trunca? Verificalo.


# Ejercicio 2: Tupla a lista y set
# Convertí la tupla (1, 2, 3, 3) a lista y a set. ¿Qué diferencia hay?


# Ejercicio 3: Decimal a binario, octal y hexadecimal
# Convertí el número 255 a binario (bin()), octal (oct()) y hexadecimal (hex())


# Ejercicio 4: Bool a otros tipos
# Dado un bool True, convertilo a int y a str. ¿Qué valores da?


# Ejercicio 5: Lista de tuplas a diccionario
# Creá un dict a partir de una lista de tuplas:
#   pares = [("nombre", "Raúl"), ("edad", 33)]
#   resultado = dict(pares)
# Imprimí el resultado y su type()


# Ejercicio 6: Valores falsy
# ¿Cuáles de estos dan False al convertir con bool()?
# Probá: 0, "", [], {}, None, 0.0, (), set()

