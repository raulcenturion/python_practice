# ============================
# 01E - Conversiones entre tipos
# ============================

numero_str = "123"
decimal = 3.14
lista = [1, 2, 2, 3]

numero_int = int(numero_str)
decimal_str = str(decimal)
conjunto = set(lista)

print(numero_int, type(numero_int))
print(decimal_str, type(decimal_str))
print(conjunto, type(conjunto))

# ============================
# 📝 EJERCICIOS PARA PRACTICAR:
# ============================

# 1. Convertí el float 9.99 a int. ¿Se redondea o se trunca? Verificalo.

# 2. Convertí la tupla (1, 2, 3, 3) a lista y a set. ¿Qué diferencia hay?

# 3. Convertí el número 255 a binario (bin()), octal (oct()) y hexadecimal (hex())

# 4. Dado un bool True, convertilo a int y a str. ¿Qué valores da?

# 5. Creá un dict a partir de una lista de tuplas:
#    pares = [("nombre", "Raúl"), ("edad", 33)]
#    resultado = dict(pares)
#    Imprimí el resultado y su type()
