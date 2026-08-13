# Ficheros en Python
# open(), read/write, with, pathlib

from pathlib import Path

ENCODING = "utf-8"
LABEL_CONTENIDO = "contenido:"
DIR = Path(__file__).resolve().parent
ARCHIVO_DEMO = DIR / "ejemplo_escritura.txt"
ARCHIVO_PRACTICO = DIR / "ejemplo.txt"

print("--- Abrir fichero para escritura (with) ---")
with open(ARCHIVO_DEMO, "w", encoding=ENCODING) as fichero:
    fichero.write("Hola, este es un ejemplo de escritura en un fichero.\n")
    fichero.write("Segunda línea del fichero.\n")
print("Escritura OK:", ARCHIVO_DEMO.name)

print("\n--- Leer todo el contenido ---")
with open(ARCHIVO_DEMO, "r", encoding=ENCODING) as fichero:
    contenido = fichero.read()
    print(LABEL_CONTENIDO, contenido)

print("\n--- Leer línea por línea ---")
with open(ARCHIVO_DEMO, "r", encoding=ENCODING) as fichero:
    for linea in fichero:
        print("línea:", linea.strip())

print("\n--- Añadir contenido (modo a) ---")
with open(ARCHIVO_DEMO, "a", encoding=ENCODING) as fichero:
    fichero.write("Añadiendo una nueva línea al final del fichero.\n")
print("Append OK")

print("\n--- Leer en modo binario (los mismos bytes del texto) ---")
with open(ARCHIVO_DEMO, "rb") as fichero:
    datos = fichero.read()
    print("bytes leídos:", len(datos))

print("\n--- Eliminar un fichero ---")
if ARCHIVO_DEMO.exists():
    ARCHIVO_DEMO.unlink()
    print("Fichero eliminado:", ARCHIVO_DEMO.name)
else:
    print("El fichero no existe.")

print("\n--- Ejemplo práctico completo ---")
with open(ARCHIVO_PRACTICO, "w", encoding=ENCODING) as file:
    file.write("Hola, este es un ejemplo de fichero.\n")
    file.write("Estamos practicando Python.\n")
    file.write("Línea final.\n")
print("Archivo creado:", ARCHIVO_PRACTICO.name)

print("\n--- Contenido completo ---")
with open(ARCHIVO_PRACTICO, "r", encoding=ENCODING) as file:
    print(LABEL_CONTENIDO, file.read())

print("\n--- Línea por línea ---")
with open(ARCHIVO_PRACTICO, "r", encoding=ENCODING) as file:
    for linea in file:
        print("línea:", linea.strip())

print("\n--- Agregar (modo a) ---")
with open(ARCHIVO_PRACTICO, "a", encoding=ENCODING) as file:
    file.write("\nNueva línea agregada al final del archivo.")

print("\n--- Contenido actualizado ---")
with open(ARCHIVO_PRACTICO, "r", encoding=ENCODING) as file:
    print(LABEL_CONTENIDO, file.read())

print("\n--- Eliminar archivo práctico ---")
if ARCHIVO_PRACTICO.exists():
    ARCHIVO_PRACTICO.unlink()
    print("Archivo eliminado ✅")
else:
    print("El archivo no existe ❌")

# Tip: pathlib (Path) es la forma moderna de trabajar rutas; os.path también sirve.
