# ============================
# 📘 Ficheros en Python
# ============================
# Un fichero (archivo) guarda datos en disco. En Python se abre con open()
# o con pathlib.Path, se lee/escribe, y se cierra.
#
# Modos frecuentes de open():
#   "r"  → lectura (el archivo debe existir)
#   "w"  → escritura (crea o SOBRESCRIBE)
#   "a"  → append (añade al final)
#   "rb" / "wb" → binario (bytes, no texto)
#
# with open(...) as f:  → cierra el archivo automáticamente al salir del bloque
# (aunque haya error). Es la forma recomendada.
#
# Path(__file__).parent → carpeta de ESTA lección, no el cwd de la terminal.
# Así el script funciona aunque lo ejecutes desde otra ruta.

from pathlib import Path

ENCODING = "utf-8"  # UTF-8 soporta tildes, ñ, etc.
LABEL_CONTENIDO = "contenido:"

# __file__ = ruta de este .py; resolve() absolutiza; parent = carpeta de la lección.
DIR = Path(__file__).resolve().parent
ARCHIVO_DEMO = DIR / "ejemplo_escritura.txt"   # Path / str → une rutas
ARCHIVO_PRACTICO = DIR / "ejemplo.txt"

# ============================
# 🔹 Escribir (modo "w")
# ============================
print("--- Abrir fichero para escritura (with) ---")

# "w" crea el archivo si no existe; si existe, borra el contenido previo.
# encoding=ENCODING asegura que el texto se guarde como UTF-8.
with open(ARCHIVO_DEMO, "w", encoding=ENCODING) as fichero:
    # write() escribe un string; \n = salto de línea.
    fichero.write("Hola, este es un ejemplo de escritura en un fichero.\n")
    fichero.write("Segunda línea del fichero.\n")
# Al salir del with, el archivo ya está cerrado.
print("Escritura OK:", ARCHIVO_DEMO.name)

# ============================
# 🔹 Leer todo de una vez (read)
# ============================
print("\n--- Leer todo el contenido ---")

# "r" = solo lectura. read() devuelve TODO el texto como un solo str.
with open(ARCHIVO_DEMO, "r", encoding=ENCODING) as fichero:
    contenido = fichero.read()
    print(LABEL_CONTENIDO, contenido)

# ============================
# 🔹 Leer línea por línea
# ============================
print("\n--- Leer línea por línea ---")

# Iterar el fichero recorre línea a línea (eficiente con archivos grandes).
# strip() quita el \n final para que print no deje líneas en blanco de más.
with open(ARCHIVO_DEMO, "r", encoding=ENCODING) as fichero:
    for linea in fichero:
        print("línea:", linea.strip())

# ============================
# 🔹 Añadir al final (modo "a")
# ============================
print("\n--- Añadir contenido (modo a) ---")

# "a" (append) NO borra lo anterior: escribe al final.
with open(ARCHIVO_DEMO, "a", encoding=ENCODING) as fichero:
    fichero.write("Añadiendo una nueva línea al final del fichero.\n")
print("Append OK")

# ============================
# 🔹 Lectura binaria (bytes)
# ============================
print("\n--- Leer en modo binario (los mismos bytes del texto) ---")

# "rb" = read binary: devuelve bytes, no str. Útil para imágenes, PDF, etc.
# Acá leemos el mismo .txt para ver cuántos bytes ocupan esos caracteres.
with open(ARCHIVO_DEMO, "rb") as fichero:
    datos = fichero.read()
    print("bytes leídos:", len(datos))

# ============================
# 🔹 Eliminar un fichero
# ============================
print("\n--- Eliminar un fichero ---")

# exists() evita error si el archivo ya no está; unlink() lo borra del disco.
if ARCHIVO_DEMO.exists():
    ARCHIVO_DEMO.unlink()
    print("Fichero eliminado:", ARCHIVO_DEMO.name)
else:
    print("El fichero no existe.")

# ============================
# 🔹 Ejemplo práctico completo (crear → leer → append → borrar)
# ============================
print("\n--- Ejemplo práctico completo ---")

# 1) Crear / sobrescribir ejemplo.txt con tres líneas.
with open(ARCHIVO_PRACTICO, "w", encoding=ENCODING) as file:
    file.write("Hola, este es un ejemplo de fichero.\n")
    file.write("Estamos practicando Python.\n")
    file.write("Línea final.\n")
print("Archivo creado:", ARCHIVO_PRACTICO.name)

print("\n--- Contenido completo ---")
# 2) Leer todo de una vez.
with open(ARCHIVO_PRACTICO, "r", encoding=ENCODING) as file:
    print(LABEL_CONTENIDO, file.read())

print("\n--- Línea por línea ---")
# 3) Recorrer línea a línea.
with open(ARCHIVO_PRACTICO, "r", encoding=ENCODING) as file:
    for linea in file:
        print("línea:", linea.strip())

print("\n--- Agregar (modo a) ---")
# 4) Append: agregamos una línea más al final.
with open(ARCHIVO_PRACTICO, "a", encoding=ENCODING) as file:
    file.write("\nNueva línea agregada al final del archivo.")

print("\n--- Contenido actualizado ---")
# 5) Volvemos a leer para ver el resultado del append.
with open(ARCHIVO_PRACTICO, "r", encoding=ENCODING) as file:
    print(LABEL_CONTENIDO, file.read())

print("\n--- Eliminar archivo práctico ---")
# 6) Limpieza: borramos el archivo de demo para no dejar basura en la lección.
if ARCHIVO_PRACTICO.exists():
    ARCHIVO_PRACTICO.unlink()
    print("Archivo eliminado ✅")
else:
    print("El archivo no existe ❌")

# Tip: pathlib (Path) es la forma moderna de trabajar rutas; os.path también sirve.

# ============================
# 🔹 Resumen
# ============================
# - open(ruta, modo, encoding=...) abre el archivo; preferí with para cerrarlo solo
# - "r" leer, "w" escribir (sobrescribe), "a" append, "rb"/"wb" binario
# - read() → todo el texto; for linea in f → línea a línea
# - Path(__file__).parent ancla rutas a la carpeta de la lección
# - Path.exists() / Path.unlink() comprueban y borran archivos
# 💡 Siempre usá encoding="utf-8" al trabajar con texto
