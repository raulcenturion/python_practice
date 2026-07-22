# ============================
# 📝 Ejercicios: Input y Strings
# 📘 Teoría: Clases_teoria/fundamentos/05_input.py
# ============================

# 🔸 Ejemplo:
# input() siempre devuelve un string; hay que hacer casting si querés un número.
# Simulamos datos para que el archivo corra sin pedir input.
nombre = "Raúl"
ciudad = "Asunción"
precio = 49.99

print("Hola " + nombre + ", sos de " + ciudad + ".")  # concatenación
print(f"Hola {nombre}, sos de {ciudad}.")             # f-string
print(f"Hola {nombre}, el precio es: ${precio:.2f}")

# Ejemplo de casting con input (descomentá para probar):
# edad = input("Ingresá tu edad: ")
# edad = int(edad)
# print("Tu edad dentro de 5 años será:", edad + 5)

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Datos personales
# Pedí nombre y edad al usuario. Imprimí con f-string:
# "Me llamo X y tengo Y años"


# Ejercicio 2: Métodos de strings
# Dado texto = "  Hola Mundo  ", aplicá y mostrá el resultado de:
# .upper(), .lower(), .strip(), .replace("Mundo", "Python"), .split()


# Ejercicio 3: Slicing
# Dado texto = "Python es genial", imprimí:
# - Los primeros 6 caracteres
# - Los últimos 6 caracteres
# - El texto al revés ([::-1])
# - La longitud con len()


# Ejercicio 4: F-string con formato
# Creá precio = 49.99 e imprimí con f-string formateado:
# f"El precio es: ${precio:.2f}"


# Ejercicio 5: Capitalize y title
# Dado nombre = "raúl centurión", imprimí usando .capitalize() y .title()


# Ejercicio 6: Suma de dos números
# Pedí dos números al usuario y mostrá la suma, resta, multiplicación y división.
# Recordá que input() devuelve string: usá int() o float()


# Ejercicio 7: Decimal como string
# Pedí un número decimal como string y convertilo a float. Mostrá el resultado.
