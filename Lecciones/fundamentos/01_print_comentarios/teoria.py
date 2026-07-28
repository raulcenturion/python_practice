# ============================
# 📘 00 - Print, Comentarios y primeros pasos
# ============================
# Este archivo cubre lo básico: comentarios, print() y sus opciones.

# 🔹 Comentarios en Python
# Este es un comentario de una sola línea

# Hablemos del print
# El print es una función que nos permite mostrar información en la consola


# Arrancamos el programa
"""
Comentario de varias líneas
"""
'''
Este es otro comentario de varias líneas
'''
print("Print")
print("validando",  " concatenación" , "en print", "y Python")
# 👉 print() puede recibir múltiples argumentos separados por coma
# 👉 sep="" cambia el separador entre argumentos (por defecto es un espacio)
# 👉 end="" cambia lo que se imprime al final (por defecto es \n = salto de línea)
print("Validando", "Python", sep="-") # Cambiando el separador
print("Esto se imprime", end="\n") # Cambiando el final de línea
print("en la misma línea")
print("Ahora si, esto se imprime", end=" ") # Cambiando el final de línea
print("en la misma línea")