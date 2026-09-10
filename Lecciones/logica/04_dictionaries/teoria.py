# ============================
# 📘 Diccionarios — CRUD, anidados y métodos
# ============================
# Qué es un dict:
#   Colección de pares clave → valor. Acceso rápido por clave.
#   Mutable (se puede cambiar). Las claves deben ser hashables (str, int, tuple...).
#
# Por qué importa en lógica:
#   Contadores, lookups O(1), datos anidados (JSON-like), mapas índice↔valor.

# ============================
# 🔹 Crear (Create)
# ============================
print("--- Crear ---")
persona = {
    "nombre": "Raúl",
    "edad": 35,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@raul",
        "instagram": "@raul",
        "github": "raul",
    },
}
print("persona:", persona)


# ============================
# 🔹 Leer (Read)
# ============================
print("\n--- Leer ---")
# Acceso directo: falla con KeyError si la clave no existe.
print('persona["nombre"]:', persona["nombre"])
# Acceso anidado:
print('persona["calificaciones"][2]:', persona["calificaciones"][2])
print('persona["socials"]["twitter"]:', persona["socials"]["twitter"])
# Acceso seguro:
print('persona.get("telefono", "N/A"):', persona.get("telefono", "N/A"))


# ============================
# 🔹 Actualizar / Agregar (Update)
# ============================
print("\n--- Actualizar / Agregar ---")
persona["nombre"] = "Raúl C."       # modificar existente
persona["pais"] = "Argentina"       # agregar nueva clave
persona["calificaciones"][2] = 10   # mutar lista anidada
print("persona (tras update):", persona)


# ============================
# 🔹 Eliminar (Delete) — del / pop
# ============================
print("\n--- Eliminar ---")
del persona["edad"]  # borra la clave (no devuelve el valor)
es_estudiante = persona.pop("es_estudiante")  # borra Y devuelve el valor
print("pop es_estudiante →", es_estudiante)
print("persona (sin edad / es_estudiante):", persona)

# Tip:
#   persona.pop("clave_inexistente", None)  # no lanza error; default None


# ============================
# 🔹 update() — fusionar dicts
# ============================
print("\n--- update() ---")
a = {"name": "midudev", "age": 25}
b = {"name": "madeval", "es_estudiante": True}
# b sobrescribe claves en común y agrega las nuevas.
a.update(b)
print("a tras update(b):", a)  # name=madeval, age=25, es_estudiante=True


# ============================
# 🔹 keys / values / items
# ============================
print("\n--- keys / values / items ---")
print("keys:", persona.keys())
print("values:", persona.values())
print("items:", persona.items())

print("\n--- Recorrer con items() ---")
for clave, valor in persona.items():
    print(f"  {clave} → {valor}")


# ============================
# 🔹 ¿Existe la clave?
# ============================
print("\n--- in ---")
print('"nombre" in persona:', "nombre" in persona)  # True
print('"edad" in persona:', "edad" in persona)      # False (la borramos)


# ============================
# 🔹 Mini demo lógica: contador con dict
# ============================
print("\n--- Contador con dict ---")
texto = "banana"
contador = {}
for ch in texto:
    contador[ch] = contador.get(ch, 0) + 1
print("contador 'banana':", contador)  # {'b': 1, 'a': 3, 'n': 2}


# ============================
# 🔹 Resumen
# ============================
# - Crear: { "k": v }
# - Leer: d["k"] o d.get("k", default)
# - Agregar/modificar: d["k"] = v
# - Borrar: del d["k"] | d.pop("k")
# - Fusionar: d.update(otro)
# - Recorrer: for k, v in d.items()
# - Anidados: d["socials"]["twitter"]
# - Tip: dict = lookup O(1) → base de muchos algoritmos (ver challenge 03)
