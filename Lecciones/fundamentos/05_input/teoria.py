# Entrada de datos
# La función input() permite al usuario ingresar datos por consola
# El valor ingresado siempre es de tipo string
nombre = input("Ingrese su nombre: ")  # Solicita al usuario ingresar su nombre
edad = input("Ingrese su edad: ")      # Solicita al usuario ingresar su edad   
altura = input("Ingrese su altura en metros (ejemplo 1.75): ")  # Solicita al usuario ingresar su altura
# Mostrar los datos ingresados y sus tipos
print("Nombre:", nombre, type(nombre))  # Muestra el nombre y su tipo (debe ser str)
print("Edad:", edad, type(edad))        # Muestra la edad y su tipo (debe ser str)
print("Altura:", altura, type(altura))  # Muestra la altura y su tipo (debe ser str)

print("Hola, como te llamas?")
nombre = input()  # Lee el nombre ingresado por el usuario
print("Hola " + nombre + ", es un gusto conocerte!")
print(f"Hola {nombre}, es un gusto conocerte! -> f-string")  # Usando f-string para formateo