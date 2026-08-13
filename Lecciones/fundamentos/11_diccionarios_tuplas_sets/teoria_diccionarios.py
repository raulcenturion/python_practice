# ============================
# 📘 Diccionarios en Python
# ============================
# Un diccionario es una colección de pares clave-valor.
# Se definen con llaves {} y permiten acceso rápido por clave.
# Son mutables (se pueden modificar) y no permiten claves duplicadas.

# 🔹 Crear un diccionario
print("--- Crear un diccionario ---")
user = {
    "name": "Raúl",
    "age": 33,
    "email": "raul@email.com",
    "active": True,
}
print("user:", user)
print("type(user):", type(user))  # <class 'dict'>

# 🔹 Acceder a valores
print("\n--- Acceder a valores ---")
print('user["name"]:', user["name"])       # Acceso directo (lanza error si no existe la clave)
print('user.get("email"):', user.get("email"))  # Acceso seguro (devuelve None si no existe)
print('user.get("phone", "No tiene"):', user.get("phone", "No tiene"))  # Valor por defecto si no existe

# 🔹 Modificar y agregar
print("\n--- Modificar y agregar ---")
user["name"] = "Raúl C."      # Modificar valor existente
user["country"] = "Argentina"  # Agregar nueva clave
print("user (modificado):", user)

# 🔹 Eliminar elementos
print("\n--- Eliminar elementos ---")
del user["active"]            # Elimina la clave "active"
email = user.pop("email")    # Elimina y devuelve el valor
print("Email eliminado:", email)
print("user (sin active/email):", user)

# 🔹 Métodos principales
print("\n--- Métodos principales ---")
print("user.keys():", user.keys())    # Todas las claves → dict_keys(['name', 'age', 'country'])
print("user.values():", user.values())  # Todos los valores → dict_values(['Raúl C.', 33, 'Argentina'])
print("user.items():", user.items())   # Pares clave-valor → dict_items([('name', 'Raúl C.'), ...])

# 🔹 Recorrer un diccionario
print("\n--- Recorriendo con items() ---")
for clave, valor in user.items():
    print(f"{clave}: {valor}")

print("\n--- Solo claves ---")
for clave in user:
    print(clave)

print("\n--- Solo valores ---")
for valor in user.values():
    print(valor)

# 🔹 Verificar si una clave existe
print("\n--- Verificar si una clave existe ---")
print('"name" in user:', "name" in user)   # True
print('"phone" in user:', "phone" in user)  # False

# 🔹 Diccionarios anidados
print("\n--- Diccionarios anidados ---")
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "dev1": {"nombre": "Ana", "rol": "Backend"},
        "dev2": {"nombre": "Luis", "rol": "Frontend"},
    }
}
print('empresa["empleados"]["dev1"]["nombre"]:', empresa["empleados"]["dev1"]["nombre"])  # Ana

# 🔹 Crear diccionario desde lista de tuplas
print("\n--- dict() desde lista de tuplas ---")
pares = [("a", 1), ("b", 2), ("c", 3)]
mi_dict = dict(pares)
print("mi_dict:", mi_dict)  # {'a': 1, 'b': 2, 'c': 3}

# 🔹 Diccionarios por comprensión (dict comprehension)
print("\n--- Dict comprehension ---")
cuadrados = {x: x**2 for x in range(1, 6)}
print("cuadrados:", cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 🔹 Merge de diccionarios (Python 3.9+)
print("\n--- Merge de diccionarios (|) ---")
defaults = {"theme": "dark", "lang": "es"}
custom = {"lang": "en", "font": 14}
config = defaults | custom  # custom sobreescribe las claves duplicadas
print("config:", config)  # {'theme': 'dark', 'lang': 'en', 'font': 14}

# 🔹 Métodos útiles adicionales
print("\n--- update / copy / clear ---")
otro = {"x": 1, "y": 2}
otro.update({"y": 99, "z": 3})  # Actualiza/agrega múltiples claves
print("otro (tras update):", otro)  # {'x': 1, 'y': 99, 'z': 3}

copia = otro.copy()  # Copia superficial
otro.clear()         # Vacía el diccionario
print("copia:", copia, "| original (clear):", otro)

# 🔹 Claves válidas: cualquier tipo inmutable (str, int, float, tuple)
print("\n--- Claves inmutables (tuple, int) ---")
raro = {
    (19.12, -98.32): "Coordenadas de Cancún",
    42: "La respuesta",
}
print("raro[(19.12, -98.32)]:", raro[(19.12, -98.32)])
