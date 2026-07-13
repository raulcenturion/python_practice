# ============================
# 01D - Strings, concatenación y f-strings
# ============================

nombre = input("¿Cómo te llamás? ")
ciudad = input("¿De qué ciudad sos? ")

print("Hola " + nombre + ", sos de " + ciudad + ".")  # concatenación
print(f"Hola {nombre}, sos de {ciudad}.")             # f-string

# ============================
# 📝 EJERCICIOS PARA PRACTICAR:
# ============================

# 1. Pedí nombre y edad, e imprimí con f-string: "Me llamo X y tengo Y años"

# 2. Dado un texto = "  Hola Mundo  ", aplicá:
#    .upper(), .lower(), .strip(), .replace("Mundo", "Python"), .split()
#    Imprimí cada resultado.

# 3. Dado texto = "Python es genial", imprimí:
#    - Los primeros 6 caracteres (slicing)
#    - Los últimos 6 caracteres
#    - El texto al revés ([::-1])
#    - La longitud con len()

# 4. Creá una variable precio = 49.99 e imprimí con f-string formateado:
#    f"El precio es: ${precio:.2f}"

# 5. Dado nombre = "raúl", imprimí el nombre con la primera letra en mayúscula
#    usando .capitalize() y .title()
