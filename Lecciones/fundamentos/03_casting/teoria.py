# ============================
# 📘 Casting (conversión de tipos)
# ============================
# Casting = cambiar un valor de un tipo a otro.
# Funciones principales: int()  float()  str()  bool()
# También: list()  tuple()  set()  dict()
#
# ¿Para qué sirve?
# - input() siempre devuelve str → a veces necesitás un número
# - sumar texto + número falla → hay que convertir
# - limpiar duplicados → list a set
# - armar un dict desde pares (clave, valor)

print("=" * 50)
print("1) CASTING BÁSICO")
print("=" * 50)

# --- int() ---
# Pasa a entero. Si viene de float, TRUNCA (no redondea): corta los decimales.
decimal = 3.9
print("float original:", decimal)
print("int(3.9) →", int(decimal))          # 3  (no es 4)
print("int(9.99) →", int(9.99))            # 9

# --- float() ---
# Pasa a número con decimal.
entero = 3
print("\nfloat(3) →", float(entero))       # 3.0

# --- str() ---
# Pasa a texto. Muy útil para concatenar con otros strings.
precio = 100
print("\nstr(100) →", str(precio), type(str(precio)))
print("mensaje:", "El precio es: " + str(precio))

# --- De texto a número ---
# Ojo: el texto tiene que “parecer” un número válido.
texto_entero = "123"
texto_decimal = "123.45"
print("\nint('123') →", int(texto_entero), type(int(texto_entero)))
print("float('123.45') →", float(texto_decimal), type(float(texto_decimal)))

# Caso real: edad viene como texto (como si viniera de input)
edad_texto = "25"
edad_numero = int(edad_texto)
print("edad + 5 →", edad_numero + 5)       # 30


print("\n" + "=" * 50)
print("2) bool() — ¿qué es True y qué es False?")
print("=" * 50)
# Regla simple:
# - “vacío” / cero / None → False
# - “con algo” → True

print("bool(1) →", bool(1))                # True
print("bool(0) →", bool(0))                # False  (cero)
print("bool(0.0) →", bool(0.0))            # False
print("bool('') →", bool(""))              # False  (string vacío)
print("bool('Hola') →", bool("Hola"))      # True
print("bool([]) →", bool([]))              # False  (lista vacía)
print("bool([1, 2]) →", bool([1, 2]))      # True
print("bool({}) →", bool({}))              # False  (dict vacío)
print("bool(()) →", bool(()))              # False  (tupla vacía)
print("bool(set()) →", bool(set()))        # False  (set vacío)
print("bool(None) →", bool(None))          # False

# bool también convierte True/False a números si lo necesitás:
verdadero = True
print("\nint(True) →", int(verdadero))     # 1
print("str(True) →", str(verdadero))       # "True"


print("\n" + "=" * 50)
print("3) CASTING ENTRE COLECCIONES")
print("=" * 50)

# Guardamos en variables (así el casting se ve claro y el linter no se queja)
tupla_nums = (1, 2, 3)
lista_nums = [1, 2, 3]
lista_con_duplicados = [1, 2, 2, 3]
pares = [("a", 1), ("b", 2)]

print("tuple → list:", list(tupla_nums))                 # [1, 2, 3]
print("list → tuple:", tuple(lista_nums))                # (1, 2, 3)
print("list → set :", set(lista_con_duplicados))         # {1, 2, 3} (sin duplicados)
print("pares → dict:", dict(pares))                      # {'a': 1, 'b': 2}

# dict necesita pares (clave, valor). Si una tupla tiene 3 elementos, falla.
pares_malos = [("a", 1), ("b", 2, 3)]
try:
    print(dict(pares_malos))
except ValueError:
    print("Error: cada tupla del dict debe tener exactamente 2 elementos")


print("\n" + "=" * 50)
print("4) bin() / oct() / hex() — otras formas de ver un número")
print("=" * 50)
# No cambian el valor del número: cambian cómo se muestra (como texto).
numero = 255
print("decimal:", numero)
print("binario (bin):", bin(numero))       # 0b11111111
print("octal (oct)  :", oct(numero))       # 0o377
print("hex (hex)    :", hex(numero))       # 0xff
print("type de bin():", type(bin(numero))) # str


print("\n" + "=" * 50)
print("5) CUANDO EL CASTING FALLA")
print("=" * 50)
# int("Hola") o float("abc") lanzan ValueError.
# Para no romper el programa, usamos try/except (lo vas a practicar más adelante).

texto_invalido = "Hola"
try:
    print(int(texto_invalido))
except ValueError:
    print("No se puede hacer int('Hola') → ValueError")

try:
    print(float(texto_invalido))
except ValueError:
    print("No se puede hacer float('Hola') → ValueError")


print("\n" + "=" * 50)
print("6) IMPLÍCITO vs EXPLÍCITO")
print("=" * 50)
# Implícito: Python convierte solo (ej. int + float → float)
x = 5
y = 2.5
z = x + y
print("5 + 2.5 →", z, type(z))             # 7.5 <class 'float'>

# Explícito: lo convertís vos con int(), str(), etc.
valor = "50"
if isinstance(valor, str):
    valor = int(valor)
print("después del casting:", valor, type(valor))


print("\n" + "=" * 50)
print("MINI RESUMEN")
print("=" * 50)
print("""
int(x)    → entero (float: trunca, no redondea)
float(x)  → decimal
str(x)    → texto
bool(x)   → False si está vacío/cero/None; si no, True
list/tuple/set/dict → cambian la colección
bin/oct/hex → muestran el número en otra base (devuelven str)

Para la práctica de esta lección:
1) int(9.99) → ¿trunca o redondea?
2) tuple → list y set
3) bin/oct/hex de 255
4) True → int y str
5) lista de tuplas → dict
6) valores falsy con bool()
7) int("hola") y cómo manejar el error
""")
# Comparativa de conversiones en Python
# (la tabla va dentro de un string; si la dejás suelta, Python la interpreta como código)
print("\n" + "=" * 50)
print("TABLA COMPARATIVA")
print("=" * 50)
print("""
| Operación         | Ejemplo          | Resultado | Nota                              |
|-------------------|------------------|-----------|-----------------------------------|
| int(3.9)          | int(3.9)         | 3         | Trunca, NO redondea               |
| int(-3.9)         | int(-3.9)        | -3        | Trunca hacia cero                 |
| float(3)          | float(3)         | 3.0       | Convierte entero a decimal        |
| float("3.14")     | float("3.14")    | 3.14      | String numérico → float           |
| round(3.9)        | round(3.9)       | 4         | Redondea al entero más cercano    |
| round(3.14159, 2) | round(3.14159,2) | 3.14      | Redondea a 2 decimales            |
| int(True)         | int(True)        | 1         | Booleano → entero                 |
| int(False)        | int(False)       | 0         | Booleano → entero                 |
""")

# Verificación en vivo (mismo contenido de la tabla)
print("Verificación:")
print("  int(3.9) →", int(3.9))
print("  int(-3.9) →", int(-3.9))
print("  float(3) →", float(3))
print('  float("3.14") →', float("3.14"))
print("  round(3.9) →", round(3.9))
print("  round(3.14159, 2) →", round(3.14159, 2))
print("  int(True) →", int(True))
print("  int(False) →", int(False))
