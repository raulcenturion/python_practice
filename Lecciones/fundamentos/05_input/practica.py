# ============================
# 📝 Ejercicios: Input y Strings
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
# input() siempre devuelve un string; hay que hacer casting si querés un número.
# Simulamos datos para que el archivo corra sin pedir input.
nombre = "Raúl"
ciudad = "Asunción"
precio = 49.99

print("Hola " + nombre + ", sos de " + ciudad + ".")  # concatenación
print(f"Hola {nombre}, sos de {ciudad}. -> f-string")             # f-string
print(f"Hola {nombre}, el precio es: ${precio:.2f} -> f-string")

# Ejemplo de casting con input (descomentá para probar):
edad = input("Ingresá tu edad: ")
edad = int(edad)
print("Tu edad dentro de 5 años será: -> casting", edad + 5)

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Datos personales
# Pedí nombre y edad al usuario. Imprimí con f-string:
# "Me llamo X y tengo Y años"
print("Ejercicio 1:")
nombre = input("Ingresá tu nombre: ")
edad = input("Ingresá tu edad: ")
edad = int(edad) # casting
print(f"Me llamo {nombre} y tengo {edad} años -> f-string")


# Ejercicio 2: Métodos de strings
# Dado texto = "  Hola Mundo  ", aplicá y mostrá el resultado de:
# .upper(), .lower(), .strip(), .replace("Mundo", "Python"), .split()
print("Ejercicio 2:")
texto = input("Ingresá un texto: ")
print(texto.upper())
print(texto.lower())
print(texto.strip())
print(texto.replace("Mundo", "Python"))
print(texto.split())


# Ejercicio 3: Slicing
# Dado texto = "Python es genial", imprimí:
# - Los primeros 6 caracteres
# - Los últimos 6 caracteres
# - El texto al revés ([::-1])
# - La longitud con len()
print("Ejercicio 3:")
texto = input("Ingresá un texto: ")
print(texto[:6])
print(texto[-6:])
print(texto[::-1])
print(len(texto))


# Ejercicio 4: F-string con formato
# Creá precio = 49.99 e imprimí con f-string formateado:
# f"El precio es: ${precio:.2f}"
print("Ejercicio 4:")
precio = input("Ingresá un precio: ")
precio = float(precio)
print(f"El precio es: ${precio:.2f} -> f-string")


# Ejercicio 5: Capitalize y title
# Dado nombre = "raúl centurión", imprimí usando .capitalize() y .title()
print("Ejercicio 5:")
nombre = input("Ingresá un nombre: ")
print(nombre.capitalize())
print(nombre.title())

# Ejercicio 6: Suma de dos números
# Pedí dos números al usuario y mostrá la suma, resta, multiplicación y división.
# Recordá que input() devuelve string: usá int() o float()
print("Ejercicio 6:")
numero1 = input("Ingresá un número: ")
numero1 = int(numero1)
numero2 = input("Ingresá otro número: ")
numero2 = int(numero2)
print(f"La suma de {numero1} y {numero2} es: {numero1 + numero2} -> f-string")
print(f"La resta de {numero1} y {numero2} es: {numero1 - numero2} -> f-string")
print(f"La multiplicación de {numero1} y {numero2} es: {numero1 * numero2} -> f-string")
print(f"La división de {numero1} y {numero2} es: {numero1 / numero2} -> f-string")

# Ejercicio 7: Decimal como string
# Pedí un número decimal como string y convertilo a float. Mostrá el resultado.
print("Ejercicio 7:")
numero = input("Ingresá un número decimal: ")
numero = float(numero)
print(f"El número es: {numero} -> f-string")