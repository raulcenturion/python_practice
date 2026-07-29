# ============================
# 📝 Ejercicios: Print y Comentarios
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
SEPARADOR = "***************************"
# 🔸 Ejemplo:
# print() puede recibir varios argumentos y personalizar separador y final
print("Hola", "Mundo", sep=" - ", end="!\n")  # Hola - Mundo!

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Presentación personal
# Creá variables con tu nombre, edad y país.
# Imprimilas en una sola línea usando sep=" | "
# Resultado esperado: Raúl | 33 | Argentina
print("Ejercicio 1:")
nombre = "Raúl"
edad = 33
pais = "Argentina"
print(nombre, edad, pais, sep=" | ")

# Ejercicio 2: Misma línea
# Usá 3 prints que queden todos en la MISMA línea (usá end="")
# Resultado esperado: Python es genial
print("Ejercicio 2:")
print("Python", "es", "genial", sep=" ")
print("Python", "es", "genial", sep=" ", end="!\n")


# Ejercicio 3: Recuadro
# Imprimí un recuadro con tu nombre:
# ********************
# *   Hola, Raúl!   *
# ********************
print("Ejercicio 3:")
print(SEPARADOR)
print("*  Hola, Raúl!     *")
print(SEPARADOR)

# Ejercicio 4: Tabla con tabs
# Imprimí una tabla con 3 columnas usando \t:
# Nombre    Edad    País
# Raúl      33      Argentina
print("Ejercicio 4:")
print("Nombre\tEdad\tPaís")
print(nombre, edad, pais, sep="\t")

# Ejercicio 5: String multilínea
# Imprimí un texto de 3 líneas usando triple comillas (""")
print("Ejercicio 5:")
print("""
Este es un string
multilínea que se
imprime en varias
líneas.
""")

# ============================
# SOLUCIONES (práctica previa)
# ============================
print("SOLUCIONES: B")
print("Información personal:")
nombre = "Raúl"
edad = 35
pais = "Argentina"
profesion = "QA engineer"
idioma = "Español"
sexo = "Masculino"
altura = 1.80
empleado = True
relacion_dependecia = True


print("Nombre:", nombre)
print("Edad:", edad)
print("País:", pais)
print(SEPARADOR)

print("1. sep") 
print(profesion, idioma, sexo, sep=" | ")
print(SEPARADOR)

print("2. end")# 2. end
print("Altura:", altura, end=" | ")
print("Empleado:", empleado, end=" | ")
print("Relación de dependencia:", relacion_dependecia)
print(SEPARADOR)

# Notas de sep / end
print("3. Notas de sep / end")
print("A", "B", sep="-")
print('Imprime con el separador que le indique, puede ser sep=" |",')
print("Es un print normal, con salto de línea al final", end="\n")
print("No baja, no deja nada, el próximo print queda pegadito", end=" ")
print("en la misma línea---")

print("4. Recuadro")
print("********************")
print("*  Hola, Raúl!     *")
print("********************")

print("5. Tabla con \t")
print("Nombre\tEdad\tPaís")
print(nombre, edad, pais, sep="\t")

print("6. Multilínea")
print("""
Este es un string
multilínea que se
imprime en varias
líneas.
""")
