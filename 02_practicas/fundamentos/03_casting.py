# ============================
# 📝 Ejercicios: Casting (conversión de tipos)
# 📘 Teoría: Clases_teoria/fundamentos/03_casting.py
# ============================

# 🔸 Ejemplo:
# int() trunca (no redondea), str() convierte cualquier cosa a texto
numero_str = "123"
decimal = 3.14
lista = [1, 2, 2, 3]

numero_int = int(numero_str)
decimal_str = str(decimal)
conjunto = set(lista)

print(numero_int, type(numero_int))
print(decimal_str, type(decimal_str))
print(conjunto, type(conjunto))
print(int(9.99))       # 9 (trunca el decimal)
print(bool(""))        # False (string vacío = False)
print(bool("hola"))    # True (string con contenido = True)

# ============================
# ENUNCIADOS
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


# Ejercicio 7: Casting inválido
# ¿Qué pasa si hacés int("hola")?
# Probalo y después pensá cómo lo resolverías (lo vas a ver en try/except más adelante)
