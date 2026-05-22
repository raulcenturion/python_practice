#Casting de tipos de datos
#Convertir un tipo de dato en otro
#int() float() str() bool()
#Ejemplos
print(int(3.5)) #Convierte float a int (trunca el decimal)
print(float(3)) #Convierte int a float
print(str(3.5)) #Convierte float a str
print(bool(1)) #Convierte int a bool (0 es False, cualquier otro valor es True)
print(bool(0)) #Convierte int a bool (0 es False, cualquier otro valor es True)
print(bool("")) #Convierte str a bool (str vacio es False, cualquier otro str es True)
print(bool("Hola")) #Convierte str a bool (str vacio es False, cualquier otro str es True)
print(bool([])) #Convierte lista a bool (lista vacia es False, cualquier otra lista es True)
print(bool([1, 2, 3])) #Convierte lista a bool (lista vacia es False, cualquier otra lista es True)
print(bool(None)) #Convierte None a bool (None es False)
print(int("123")) #Convierte str a int (str debe ser un numero valido)
print(float("123.45")) #Convierte str a float (str debe ser un numero valido)
#Nota: Convertir str a int o float puede generar un error si el str no  es un numero valido
#Ejemplo de error
# print(int("Hola")) #Genera ValueError
# print(float("Hola")) #Genera ValueError
#Para evitar errores, se puede usar try-except
try:
    print(int("Hola"))
except ValueError:
    print("Error: No se puede convertir 'Hola' a int")  
try:
    print(float("Hola"))
except ValueError:
    print("Error: No se puede convertir 'Hola' a float")
#Convertir listas y tuplas a otros tipos
print(list((1, 2, 3))) #Convierte tupla a lista
print(tuple([1, 2, 3])) #Convierte lista a tupla
print(set([1, 2, 2, 3])) #Convierte lista a set (elimina duplicados)
print(dict([("a", 1), ("b", 2)])) #Convierte lista de tuplas a diccionario
#Nota: Convertir a dict requiere una lista de tuplas con dos elementos cada una
#Ejemplo de error
# print(dict([("a", 1), ("b", 2, 3)]) #Genera ValueError
#Para evitar errores, se puede usar try-except
try:
    print(dict([("a", 1), ("b", 2, 3)]))
except ValueError:
    print("Error: No se puede convertir a dict, cada tupla debe tener dos elementos")

print(type(int("100"))) #Muestra el tipo de dato (debe ser int)
print(type(float("100.5"))) #Muestra el tipo de dato (debe ser float)
print(type(str(100))) #Muestra el tipo de dato (debe ser str)
print(type(bool(1))) #Muestra el tipo de dato (debe ser bool)
print(type(list((1, 2, 3)))) #Muestra el tipo de dato (debe ser list)
print(type(tuple([1, 2, 3]))) #Muestra el tipo de dato (debe ser tuple)
print(type(set([1, 2, 2, 3]))) #Muestra el tipo de dato (debe ser set)
print(type(dict([("a", 1), ("b", 2)]))) #Muestra el tipo de dato (debe ser dict) 

# 🧠 PYTHON TYPE CASTING - Guía rápida
# ===================================

# 🔹 Conversión implícita (automática)
x = 5      # int
y = 2.5    # float
z = x + y  # Python convierte int → float automáticamente
print(z, type(z))  # 7.5 <class 'float'>

# 🔹 Conversión explícita (manual)
# --------------------------------
# 👉 Se usa cuando necesitamos cambiar el tipo de dato nosotros mismos

# 🧱 Básicos
int("10")        # str → int → 10
float("3.14")    # str → float → 3.14
str(100)         # int → str → "100"
bool("")         # str vacío → False
bool("hola")     # str no vacío → True

# 🧺 Colecciones
list((1, 2, 3))            # tuple → list → [1, 2, 3]
tuple([1, 2, 3])           # list → tuple → (1, 2, 3)
set([1, 2, 2, 3])          # list → set → {1, 2, 3}
dict([("a", 1), ("b", 2)]) # lista de tuplas → dict → {'a': 1, 'b': 2}

# 🧩 Ejemplos útiles
edad = "25"
edad_num = int(edad) + 5   # Convierte a número antes de sumar
print(edad_num)  # 30

precio = 100
mensaje = "El precio es: " + str(precio)
print(mensaje)  # "El precio es: 100"

numeros = [1, 2, 2, 3]
unicos = set(numeros)
print(unicos)   # {1, 2, 3}

# ⚠️ Errores comunes
# int("hola")  → ValueError ❌ (no se puede convertir texto no numérico)
# float("abc") → ValueError ❌

# ✅ Tip: Usá type() para chequear antes de convertir
valor = "50"
if isinstance(valor, str):
    valor = int(valor)
print(valor, type(valor))
