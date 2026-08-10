# ============================
# 📝 Ejercicios: Variables
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
# Las variables son contenedores. Python es de tipado dinámico (el tipo se detecta solo).
nombre = "Raúl"      # str
edad = 33             # int
nombre = 100          # ahora es int (se puede reasignar con otro tipo)
print(nombre, type(nombre))

# ============================
# Ejercicio 1: Reasignación
# Creá una variable x = 10. Imprimí su tipo.
# Reasignala a x = "diez". Imprimí su tipo de nuevo.
# ¿Cambió el tipo? ¿Python te dejó hacerlo?
print("Ejercicio 1:")
x = 10
print(x, type(x))
x = "diez"
print(x, type(x))


# Ejercicio 2: Intercambio de variables
# Dadas a = 5 y b = 10, intercambialas SIN usar una tercera variable.
# Pista: Python permite a, b = b, a
print("Ejercicio 2:")
a = 5
b = 10
print('a, b:', a, b)
a, b = b, a
print('a, b:', a, b)

# Ejercicio 4: Constantes
# Creá "constantes" PI = 3.14159 y GRAVEDAD = 9.81
# Imprimilas. ¿Python impide que las modifiques?
print("Ejercicio 4:")
PI = 3.14159
GRAVEDAD = 9.81
print('PI:', PI)
print('GRAVEDAD:', GRAVEDAD)
PI = 3.14
GRAVEDAD = 9.8
print('PI:', PI)
print('GRAVEDAD:', GRAVEDAD)


# Ejercicio 5: Tipado fuerte
# ¿Qué pasa si intentás hacer "edad: " + 25? (sin convertir)
# Probalo y después arreglalo con str() o f-string.
#
# Ojo: edad = 25 es el NÚMERO.
#      etiqueta = "edad: " es el TEXTO del mensaje (eso es lo que Sonar pedía no repetir).
print("Ejercicio 5:")
edad = 25
etiqueta = "edad: "

# Ejemplo que da error de tipo (descomentá para verlo):
# print(etiqueta + edad)  # TypeError: can only concatenate str (not "int") to str

print(etiqueta + str(edad))   # ok: convertís el número a texto
print(f"{etiqueta}{edad}")    # ok: f-string (más cómodo)
