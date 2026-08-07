# ============================
# 📝 Ejercicios: Casting (conversión de tipos)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Datos para los ejemplos y ejercicios (declarados una sola vez)
numero_str = "123"
decimal = 3.14
lista = [1, 2, 2, 3]
texto_vacio = ""
texto_hola = "hola"

# Ejercicio 1
numero_decimal = 9.99

# Ejercicio 2
tupla_nums = (1, 2, 3, 3)

# Ejercicio 3
numero = 255

# Ejercicio 4
verdadero = True

# Ejercicio 5
pares = [("nombre", "Raúl"), ("edad", 33)]

# Ejercicio 6 (valores falsy para probar con bool())
cero = 0
lista_vacia = []
dict_vacio = {}
nada = None
cero_decimal = 0.0
tupla_vacia = ()
set_vacio = set()

# Ejercicio 7
texto_invalido = "hola"

# 🔸 Ejemplo:
# int() trunca (no redondea), str() convierte cualquier cosa a texto
numero_int = int(numero_str)
decimal_str = str(decimal)
conjunto = set(lista)

print(numero_int, type(numero_int))
print(decimal_str, type(decimal_str))
print(conjunto, type(conjunto))
print(int(numero_decimal), "→ trunca el decimal")
print(bool(texto_vacio), "False (string vacío = False)")
print(bool(texto_hola), "True (string con contenido = True)")

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Float a int
# Convertí el float 9.99 a int. ¿Se redondea o se trunca? Verificalo.
print(f"Ejercicio 1  {'=' * 50}")
print("int(numero_decimal) →", int(numero_decimal))
print("Se trunca el decimal")

# Ejercicio 2: Tupla a lista y set
# Convertí la tupla (1, 2, 3, 3) a lista y a set. ¿Qué diferencia hay?
print(f"Ejercicio 2  {'=' * 50}")
lista_desde_tupla = list(tupla_nums)
set_desde_tupla = set(tupla_nums)
print("tupla original →", tupla_nums)
print("list(tupla_nums) →", lista_desde_tupla)
print("set(tupla_nums)  →", set_desde_tupla)
print("Diferencia: la lista mantiene orden y duplicados; el set elimina duplicados")

# Ejercicio 3: Decimal a binario, octal y hexadecimal
# Convertí el número 255 a binario (bin()), octal (oct()) y hexadecimal (hex())
print(f"Ejercicio 3  {'=' * 50}")
print("Numero original →", numero)

# Forma 1: castear, guardar en variable e imprimir la variable
bin_numero = bin(numero)  # 0b11111111
print("bin(numero) →", bin_numero)

# Forma 2: casting directo en el print (sin variable intermedia)
print("bin(numero) →", bin(numero))  # casting directo
print("oct(numero) →", oct(numero))  # casting directo
print("hex(numero) →", hex(numero))  # casting directo


# Ejercicio 4: Bool a otros tipos
# Dado un bool True, convertilo a int y a str. ¿Qué valores da?
print(f"Ejercicio 4  {'=' * 50}")
print("int(True) →", int(True))
print("str(True) →", str(True))
print("True se convierte a 1 y 'True'")


# Ejercicio 5: Lista de tuplas a diccionario
# Creá un dict a partir de una lista de tuplas:
#   pares = [("nombre", "Raúl"), ("edad", 33)]
#   resultado = dict(pares)
# Imprimí el resultado y su type()
print(f"Ejercicio 5  {'=' * 50}")
print("dict(pares) →", dict(pares))
print("type(dict(pares)) →", type(dict(pares))) # dict


# Ejercicio 6: Valores falsy
# ¿Cuáles de estos dan False al convertir con bool()?
# Probá: 0, "", [], {}, None, 0.0, (), set()
print(f"Ejercicio 6  {'=' * 50}")
print("bool(0) →", bool(0))
print("bool('') →", bool(''))
print("bool([]) →", bool([]))
print("bool({}) →", bool({}))
print("bool(None) →", bool(None))
print("bool(0.0) →", bool(0.0))
print("bool(()) →", bool(()))
print("bool(set()) →", bool(set())) # False
print("True si el valor es True, False si el valor es False")

# Ejercicio 7: Casting inválido
# ¿Qué pasa si hacés int("hola")?
# Probalo y después pensá cómo lo resolverías (lo vas a ver en try/except más adelante)
print(f"Ejercicio 7  {'=' * 50}")
print("int('hola') →", int('hola'))
print("Error: 'hola' no es un número válido")
print("Se puede resolver con try/except para manejar el error")

