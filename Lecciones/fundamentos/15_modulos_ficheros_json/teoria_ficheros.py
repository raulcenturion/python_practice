# Ficheros en Python
# Los ficheros son una forma de almacenar datos de manera persistente en el sistema de archivos.
# Python proporciona varias funciones integradas para trabajar con ficheros, como abrir, leer, escribir y cerrar ficheros.
# Abrir un fichero
# La función open() se utiliza para abrir un fichero. Toma dos argumentos: el nombre del fichero y el modo de apertura.
# Modos comunes:
# 'r' - lectura (por defecto)
# 'w' - escritura (crea un nuevo fichero o sobrescribe uno existente)
# 'a' - añadir (escribe al final del fichero)
# 'b' - modo binario (se puede combinar con otros modos, por ejemplo, 'rb' o 'wb')
# 'x' - creación exclusiva (falla si el fichero ya existe)
# Ejemplo de abrir un fichero para lectura
try:
    fichero = open("ejemplo.txt", "r")
    contenido = fichero.read()  # Leer todo el contenido del fichero
    print(contenido)
except FileNotFoundError:
    print("Error: El fichero no existe.")
finally:
    if 'fichero' in locals():
        fichero.close()  # Cerrar el fichero
# Ejemplo de abrir un fichero para escritura
with open("ejemplo_escritura.txt", "w") as fichero:
    fichero.write("Hola, este es un ejemplo de escritura en un fichero.\n")
    fichero.write("Segunda línea del fichero.\n")
# El uso de 'with' asegura que el fichero se cierre automáticamente al salir del bloque.
# Leer un fichero línea por línea
with open("ejemplo.txt", "r") as fichero:
    for linea in fichero:
        print(linea.strip())  # strip() elimina espacios en blanco y saltos de línea
# Leer un fichero en modo binario
with open("imagen.png", "rb") as fichero:
    datos = fichero.read()
    print(f"Leídos {len(datos)} bytes.")
# Añadir contenido a un fichero existente
with open("ejemplo_escritura.txt", "a") as fichero:
    fichero.write("Añadiendo una nueva línea al final del fichero.\n")
# Eliminar un fichero
import os
if os.path.exists("ejemplo_escritura.txt"):
    os.remove("ejemplo_escritura.txt")
    print("Fichero eliminado.")
else:
    print("El fichero no existe.")
# Resumen:
# - Utiliza open() para abrir ficheros en diferentes modos.
# - Usa read(), readline() o readlines() para leer contenido.
# - Usa write() o writelines() para escribir contenido.
# ===============================
# 🔹 Apertura y Cierre de Ficheros
# ===============================
# - Siempre cierra los ficheros con close() o usa 'with' para manejo automático.
# - Usa 'encoding="utf-8"' al abrir ficheros de texto para asegurar compatibilidad con caracteres especiales.
# - El modo 'b' es esencial para trabajar con ficheros binarios como imágenes o archivos comprimidos.
# - El modo 'a' permite agregar contenido sin sobrescribir el archivo existente.

# ===============================
# 🔹 Lectura y Escritura
# ===============================
# - readline() y readlines() permiten leer líneas individuales o todas las líneas de un fichero.
# - seek() y tell() permiten mover el puntero del fichero y saber en qué posición se encuentra.

# ===============================
# 🔹 Manejo de Errores y Seguridad
# ===============================
# - Maneja excepciones como FileNotFoundError para evitar errores al abrir ficheros.
# - Siempre valida y sanitiza las entradas relacionadas con ficheros para prevenir vulnerabilidades como inyección de rutas.
# - Considera la seguridad al manejar datos sensibles o confidenciales.

# ===============================
# 🔹 Herramientas y Utilidades
# ===============================
# - Usa el módulo os para operaciones de sistema de archivos como eliminar ficheros.
# - La función os.path.exists() es útil para verificar la existencia de un fichero antes de operar.
# - pathlib ofrece una forma moderna y orientada a objetos para trabajar con rutas y ficheros.
# - tempfile permite trabajar con ficheros temporales que no deban persistir.

# ===============================
# 🔹 Buenas Prácticas y Recomendaciones
# ===============================
# 🔹 Ejemplo práctico completo
# ===============================

import os

# ===============================
# 📌 Definimos el nombre del archivo
# ===============================
file_name = "ejemplo.txt"

# ===============================
# ✍️ 1. Escribir en un archivo (modo "w")
# ===============================
# - "w" crea el archivo si no existe o lo sobrescribe si ya existe
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Hola, este es un ejemplo de fichero.\n")
    file.write("Estamos practicando Python.\n")
    file.write("Línea final.\n")

print("Archivo creado y escrito ✅")

# ===============================
# 📖 2. Leer el archivo completo (modo "r")
# ===============================
with open(file_name, "r", encoding="utf-8") as file:
    contenido = file.read()   # Lee todo el archivo como un solo string
    print("\n--- Contenido completo ---")
    print(contenido)

# ===============================
# 📖 3. Leer línea por línea
# ===============================
with open(file_name, "r", encoding="utf-8") as file:
    print("--- Lectura línea por línea ---")
    for linea in file:
        print(linea.strip())  # strip() elimina saltos de línea al imprimir

# ===============================
# ➕ 4. Agregar contenido al archivo (modo "a")
# ===============================
with open(file_name, "a", encoding="utf-8") as file:
    file.write("\nNueva línea agregada al final del archivo.")

print("\nSe agregó una nueva línea al archivo ✅")

# ===============================
# 📖 5. Volver a leer para verificar cambios
# ===============================
with open(file_name, "r", encoding="utf-8") as file:
    print("\n--- Contenido actualizado ---")
    print(file.read())

# ===============================
# ❌ 6. Eliminar archivo (opcional)
# ===============================
if os.path.exists(file_name):
    os.remove(file_name)
    print("\nArchivo eliminado ✅")
else:
    print("\nEl archivo no existe ❌")

