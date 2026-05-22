# ============================
# 01A - Print y sus opciones
# ============================

# Información personal en consola
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

# ============================
# 📝 EJERCICIOS PARA PRACTICAR:
# ============================
print("Nombre:", nombre)
print("Edad:", edad)
print("País:", pais)
print("***************************")
# 1. Imprimí tu nombre, edad y ciudad en una sola línea usando sep=" | "
print(profesion, idioma, sexo, sep=" | ")
print("***************************")
# 2. Imprimí 3 prints seguidos que queden en la MISMA línea (usá end="")
print("Altura:", altura, end=" | ")
print("Empleado:", empleado, end=" | ")
print("Relación de dependencia:", relacion_dependecia)
print("***************************")
# Opciones del print
# Nota: sep="-" no tiene efecto si solo pasás UN argumento al print.
# Para verlo en acción necesitás varios argumentos: print("A", "B", sep="-") → A-B
print("A", "B", sep="-")
print("Imprime con el separador que le indique, puede ser sep=\" |\",", sep="-")
print("Es un print normal, con salto de línea al final", end="\n")
print("No baja, no deja nada, el próximo print queda pegadito", end=" ")
print("en la misma línea---")
# 3. Imprimí un "recuadro" usando print:
#    Resultado esperado:
#    ********************
#    *  Hola, Raúl!    *
#    ********************
print("********************")
print("*  Hola, Raúl!     *")
print("********************")

# 4. Usá \t para imprimir una "tabla" con 3 columnas:
#    Nombre    Edad    País
# ✅ Bien resuelto. \t genera tabulaciones. Se ven como espacios en la terminal
#    pero son "tabs". Si las columnas se desalinean con textos largos, es normal.
print("Nombre\tEdad\tPaís")
print(nombre, edad, pais, sep="\t")

# 5. Imprimí un string multilínea con """ (triple comillas)
print("""
Este es un string
multilínea que se
imprime en varias
líneas.
""")
