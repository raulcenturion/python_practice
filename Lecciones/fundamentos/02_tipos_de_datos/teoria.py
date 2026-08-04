# ============================
# 📘 Tipos de datos en Python
# ============================
# En Python cada valor tiene un tipo. type() te dice cuál es en runtime.
# Nota: guardamos valores en variables y después usamos type(variable).
#
# ---------------------------
# CONCEPTOS QUE VAS A VER MUCHO
# ---------------------------
# 1) \  → barra invertida = “el próximo carácter es especial” (escape)
#    Idea clave: la \ NO se imprime. Solo cambia el significado de lo que sigue.
#
#    Misma letra, distinto significado:
#      "n"   → se imprime la letra n
#      "\n"  → NO imprime n: ejecuta un salto de línea
#      "t"   → se imprime la letra t
#      "\t"  → NO imprime t: inserta una tabulación
#      "\\"  → la segunda \ queda “especial”: se imprime una sola \
#      "\""  → la " queda especial: comilla dentro del string
#
#    Regla mental:  \ + carácter  =  instrucción   (no texto normal)
#
# 2) / vs //  → dos divisiones distintas
#    /  → división “normal” (siempre da float):  17 / 5  → 3.4
#    // → división entera (quita el decimal):     17 // 5 → 3
#    %  → resto (módulo):                         17 % 5  → 2
#
# 3) f"..."  → f-string (formatted string)
#    La f delante del string permite meter variables entre { }.
#    Es más claro que concatenar con +.
#      nombre = "Raúl"
#      print(f"Hola {nombre}")   → Hola Raúl
#
# 4) ¿Por qué a veces ves [str] “fantasma” al lado de una lista?
#    Eso NO está en el archivo .py ni lo imprime Python.
#    Es una pista del editor (Cursor/Pylance): “inlay hint” de tipos.
#    Te dice: hobbies parece list[str] (lista de strings).
#    Podés ocultarlo en settings si molesta; no afecta la ejecución.

print("=" * 50)
print("ESCAPES CON \\ (barra invertida)")
print("=" * 50)
# La \ avisa: “lo que viene NO es texto normal, es una instrucción”.

# --- Ejemplo A: letra n vs \n ---
print("--- A) carácter 'n' ---")
print("solo n :", "A" + "n" + "B")     # AnB  → n se imprime
print("con \\n:", "A" + "\n" + "B")    # A
#                                      # B    → n ya no se imprime; baja de línea

# --- Ejemplo B: letra t vs \t ---
print("--- B) carácter 't' ---")
print("solo t :", "A" + "t" + "B")     # AtB  → t se imprime
print("con \\t:", "A" + "\t" + "B")    # A       B  → t no se imprime; pone un tab

# --- Ejemplo C: comilla " vs \" ---
print("--- C) carácter comilla ---")
# Sin escape, la " cerraría el string a mitad de camino.
# Con \", esa comilla pasa a ser “especial”: forma parte del texto.
print("con \\\":", "dijo: \"hola\"")   # dijo: "hola"

# --- Ejemplo D: la propia barra \ ---
print("--- D) carácter barra ---")
print("con \\\\:", "C:\\Users\\Raul")  # C:\Users\Raul
# Cada \\ significa: “imprimí UNA barra”. Por eso van de a pares.

print("resumen: la \\ no se ve; transforma la letra de al lado en instrucción")

print("\n" + "=" * 50)
print("TIPOS BÁSICOS (los vas a usar todo el tiempo)")
print("=" * 50)

# ---------------------------
# int — números enteros
# ---------------------------
edad = 35
cantidad = 10
print("int:", edad, type(edad))
print("  suma:", edad + 5)
print("  potencia:", 2 ** 10)          # 1024  (2 elevado a 10)
print("  división normal / :", 17 / 5) # 3.4   (float)
print("  división entera // :", 17 // 5)  # 3  (se queda con la parte entera)
print("  resto (módulo) % :", 17 % 5)     # 2  (lo que sobra al dividir)
# Uso típico: contadores, ids, edades, cantidades.

# ---------------------------
# float — números con decimal
# ---------------------------
precio = 19.99
altura = 1.80
# \n al inicio → deja una línea en blanco antes de este print
print("\nfloat:", precio, type(precio))
print("  precio con IVA 21%:", round(precio * 1.21, 2))
print("  int + float →", type(10 + 3.14))  # float (se “promueve”)
# Uso típico: dinero*, medidas, promedios.
# *En sistemas reales el dinero a veces se maneja con Decimal; float alcanza para practicar.

# ---------------------------
# str — texto
# ---------------------------
nombre = "Raúl"
saludo = "Hola"
print("\nstr:", nombre, type(nombre))  # \n = salto de línea antes del texto
print("  concatenar:", saludo + ", " + nombre)
print("  repetir:", "ja" * 3)              # jajaja
# f-string: la f permite incrustar variables con {nombre} y {edad}
print("  f-string:", f"Me llamo {nombre} y tengo {edad} años")
print("  sin f (más engorroso):", "Me llamo " + nombre + " y tengo " + str(edad) + " años")
print("  mayúsculas:", nombre.upper())
print("  largo:", len(nombre))
# Uso típico: mensajes, nombres, rutas, JSON como texto.

# ---------------------------
# bool — True / False
# ---------------------------
activo = True
mayor_de_edad = edad >= 18
print("\nbool:", activo, type(activo))
print("  comparación:", mayor_de_edad, type(mayor_de_edad))
print("  True + True =", True + True)      # 2 (bool es subclase de int)
print("  True + False =", True + False)    # 1
if mayor_de_edad:
    print("  → puede registrarse (ejemplo de if)")
# Uso típico: flags, condiciones, resultados de comparaciones.

# ---------------------------
# None — “no hay valor”
# ---------------------------
resultado = None
print("\nNoneType:", resultado, type(resultado))


def buscar_usuario(user_id: int):
    """Simula una búsqueda: id 0 → no existe."""
    if user_id == 0:
        return None
    return "Raúl"


for uid in (0, 1):
    encontrado = buscar_usuario(uid)
    if encontrado is None:
        print(f"  id={uid} → no se encontró el usuario")
    else:
        print(f"  id={uid} → usuario: {encontrado}")
# Uso típico: valor por defecto, “aún no calculé nada”, respuesta vacía.


print("\n" + "=" * 50)
print("COLECCIONES (agrupan varios valores)")
print("=" * 50)

# ---------------------------
# list — lista (ordenada, mutable)
# ---------------------------
hobbies = ["leer", "programar", "correr"]
# Si el editor muestra algo como [str] cerca de hobbies, es solo una pista visual
# de tipos (inlay hint). No forma parte del código.
print("\nlist:", hobbies, type(hobbies))
print("  primer elemento:", hobbies[0])
print("  último:", hobbies[-1])
hobbies.append("cocinar")                  # agrega al final
print("  después de append:", hobbies)
print("  slicing [0:2]:", hobbies[0:2])    # ['leer', 'programar']
# Uso típico: listas de ítems, resultados, colas simples.
# Mutable → podés cambiarla después de crearla.

# ---------------------------
# tuple — tupla (ordenada, inmutable)
# ---------------------------
# Parecida a una list, pero NO se puede modificar después de creada.
# Se escribe con paréntesis ( ) — o a veces solo comas.
punto = (10, 20)
rgb = (255, 128, 0)
print("\ntuple:", punto, type(punto))

# 1) Acceso por índice (igual que una lista)
print("  rgb[0] =", rgb[0])               # 255
print("  rgb[-1] =", rgb[-1])             # 0 (último)

# 2) Desempaquetado: repartir la tupla en variables
x, y = punto
print("  desempaquetado → x =", x, "| y =", y)

# 3) Función que retorna VARIOS valores → en realidad retorna una tupla
def min_y_max(numeros):
    return min(numeros), max(numeros)     # equivalente a return (min(...), max(...))


menor, mayor = min_y_max([4, 9, 1, 7])
print("  retorno múltiple → menor =", menor, "| mayor =", mayor)
print("  type del return:", type(min_y_max([1, 2])))  # <class 'tuple'>

# 4) Tupla de un solo elemento: hace falta la coma
uno = (42,)
print("  tupla de un elemento:", uno, type(uno))
no_es_tupla = (42)
print("  sin coma NO es tupla:", no_es_tupla, type(no_es_tupla))  # int

# 5) Inmutabilidad: esto rompería si lo descomentás
# punto[0] = 99  → TypeError

# 6) Caso de uso: clave compuesta / dato fijo
# Ideal cuando el valor “es un paquete” que no debería mutar
fecha = (2026, 7, 31)                     # año, mes, día
print("  fecha fija:", fecha)
# Uso típico: coordenadas, RGB, retornos múltiples, configs que no cambian.

# ---------------------------
# dict — diccionario (clave → valor)
# ---------------------------
persona = {
    "nombre": "Raúl",
    "edad": 35,
    "hobbies": ["leer", "programar"],
    "activo": True,
}
print("\ndict:", persona, type(persona))
print("  nombre:", persona["nombre"])
print("  type de hobbies:", type(persona["hobbies"]))
persona["pais"] = "Argentina"              # agregar clave
persona["edad"] = 36                       # actualizar
print("  después de cambios:", persona)
print("  claves:", list(persona.keys()))
print("  .get seguro:", persona.get("email", "sin email"))
# Uso típico: objetos/JSON, configs, respuestas de APIs (muy importante para FastAPI).

# ---------------------------
# set — conjunto (sin duplicados, no ordenado)
# ---------------------------
con_duplicados = ["python", "api", "python", "qa"]
tags = set(con_duplicados)
print("\nset:", tags, type(tags))          # {'python', 'api', 'qa'}
print("  lista original:", con_duplicados)
print("  sin duplicados:", tags)
a = {1, 2, 3}
b = {3, 4, 5}
print("  unión:", a | b)                   # {1, 2, 3, 4, 5}
print("  intersección:", a & b)            # {3}
print("  diferencia:", a - b)              # {1, 2}
# Uso típico: eliminar duplicados, pertenencia rápida (x in set).


print("\n" + "=" * 50)
print("OTROS TIPOS (útiles de conocer; se ven menos al inicio)")
print("=" * 50)

# ---------------------------
# complex — poco usado fuera de ciencia/matemática
# ---------------------------
z = 3 + 4j
print("\ncomplex:", z, type(z))
print("  real:", z.real, "| imag:", z.imag)

# ---------------------------
# bytes / bytearray — datos binarios
# ---------------------------
# Una str es texto (caracteres). bytes es una secuencia de números 0–255
# (datos “crudos”), típico de archivos, red o encodings.

# b"hola" → literal de bytes. La b delante indica: esto NO es str, es bytes.
raw = b"hola"
print("\nbytes:", raw, type(raw))
# Cada posición es un número (código del carácter en Latin-1/ASCII básico):
print("  raw[0] =", raw[0])               # 104 → código de 'h'
print("  list(raw) =", list(raw))         # [104, 111, 108, 97]
# Decodificar bytes → str (hay que saber el encoding):
print("  decode utf-8:", raw.decode("utf-8"))  # "hola"
# Encode: str → bytes. El encoding cambia los bytes resultantes:
ene = "ñ"
print("  'ñ' en utf-8 :", ene.encode("utf-8"))     # b'\xc3\xb1' (2 bytes)
print("  'ñ' en latin-1:", ene.encode("latin-1"))  # b'\xf1'     (1 byte)
# bytes es INMUTABLE: no podés hacer raw[0] = 72

# bytearray: igual que bytes, pero MUTABLE (sí se puede cambiar)
mutable = bytearray(b"hola")
print("bytearray:", mutable, type(mutable))
print("  antes:", mutable)
mutable[0] = 72                            # 72 es el código ASCII de 'H'
print("  después de mutable[0]=72:", mutable)  # bytearray(b'Hola')
# ¿Cuándo usar cada uno?
# - bytes: leer un archivo/binario y no lo vas a editar
# - bytearray: necesitás modificar el buffer (protocolos, parsers, etc.)

# ---------------------------
# frozenset — set inmutable (puede ser clave de dict)
# ---------------------------
permisos = frozenset(["leer", "escribir"])
print("\nfrozenset:", permisos, type(permisos))

# ---------------------------
# range — secuencia perezosa (ideal para for)
# ---------------------------
# “Perezosa” = no crea todos los números en memoria de golpe.
# Solo guarda inicio/fin/paso y genera valores cuando los pedís.
# Casos de uso: bucles for, generar índices, repetir N veces.

rango = range(1, 6)                        # 1, 2, 3, 4, 5 (el 6 no entra)
print("\nrange:", rango, type(rango))
print("  como lista:", list(rango))        # materializa todos los valores

# range(stop) → 0 .. stop-1
print("  range(3) →", list(range(3)))      # [0, 1, 2]

# range(start, stop, step) → con salto
print("  range(0, 10, 2) →", list(range(0, 10, 2)))  # pares: 0,2,4,6,8
print("  range(5, 0, -1) →", list(range(5, 0, -1)))  # cuenta regresiva

print("  for sobre range(3):", end=" ")
for i in range(3):
    print(i, end=" ")
print()

# Ejemplo práctico: repetir una acción N veces (no te importa el valor de i)
print("  repetir 3 veces:")
for _ in range(3):
    print("    hola")

# ¿Por qué no usar siempre list(range(1_000_000))?
# Porque list ocupa mucha memoria. range(1_000_000) casi no ocupa:
print("  len(range(1_000_000)) =", len(range(1_000_000)))

# ---------------------------
# memoryview — vista sobre bytes sin copiar
# ---------------------------
# Pensalo así: bytes es el “archivo en memoria”.
# memoryview es una “ventana” para mirar/cortar esa memoria SIN copiarla.
# Útil con datos grandes (imágenes, audio, paquetes de red) para no
# duplicar RAM al hacer slices.

datos = b"ABCDEF"
vista = memoryview(datos)
print("\nmemoryview:", vista, type(vista))
print("  primer byte:", vista[0])          # 65 → 'A' en ASCII
print("  como bytes otra vez:", vista.tobytes())

# Slice sin copiar el buffer original (sigue siendo una vista)
parte = vista[1:4]                         # bytes de 'B', 'C', 'D'
print("  slice vista[1:4]:", parte.tobytes())  # b'BCD'
print("  list(parte):", list(parte))       # [66, 67, 68]

# Caso de uso mental:
# - Recibís un paquete grande en bytes
# - Querés procesar de a “chunks” (pedazos)
# - Con memoryview evitás crear mil copias intermedias
chunk_size = 2
print("  chunks de 2 bytes:")
for i in range(0, len(vista), chunk_size):
    chunk = vista[i : i + chunk_size]
    print("   ", chunk.tobytes())


print("\n" + "=" * 50)
print("MINI RESUMEN PRACTICO")
print("=" * 50)
print("""
int / float / str / bool  → datos simples
list                      → colección que cambia
tuple                     → colección fija
dict                      → datos con nombre (JSON/API)
set                       → únicos / sin duplicados
None                      → ausencia de valor
type(x)                   → ¿qué tipo es x?

Recordatorios rápidos:
\\n     → salto de línea dentro de un string
/      → división con decimal
//     → división entera
f"..." → meter variables dentro del texto con {variable}
[str]  → pista del EDITOR, no del código

Para la práctica de esta lección enfocáte en:
str, int, float, bool, list, tuple, dict, set
y en probar type() + alguna operación (suma mixta, "ja"*3, True+True).
""")
