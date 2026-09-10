# ============================
# 📝 Ejercicios: Diccionarios (lógica)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo:
persona = {
    "nombre": "Raúl",
    "edad": 35,
    "socials": {"twitter": "@raul", "github": "raul"},
}
print("Ejemplo acceso:", persona["nombre"], "|", persona["socials"]["github"])

# ============================
# ENUNCIADOS
# ============================

# ----------------------------
# Ejercicio 1: Acceso anidado
# ----------------------------
# Creá un dict con nombre, edad y socials (twitter/instagram).
# Imprimí el twitter.
#
# Guía:
# 1) Armá el dict con "socials" como dict interno
# 2) print(dict["socials"]["twitter"])
#
# TIP / EJEMPLO (comentado):
#   data = {"nombre": "Ana", "edad": 20, "socials": {"twitter": "@ana", "instagram": "@ana"}}
#   print(data["socials"]["twitter"])


def ejercicio_1_acceso_anidado() -> None:
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


# ----------------------------
# Ejercicio 2: Agregar y actualizar
# ----------------------------
# Partí de un dict persona. Agregá "pais". Actualizá "edad". Imprimí el dict.
#
# Guía:
# 1) persona["pais"] = "Argentina"
# 2) persona["edad"] = 36
# 3) print(persona)
#
# TIP / EJEMPLO (comentado):
#   persona = {"nombre": "Raúl", "edad": 35}
#   persona["pais"] = "Argentina"
#   persona["edad"] = 36


def ejercicio_2_agregar_actualizar() -> dict:
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


# ----------------------------
# Ejercicio 3: Recorrido con items
# ----------------------------
# Recorré el dict con .items() e imprimí "clave -> valor".
#
# Guía:
# 1) for clave, valor in persona.items():
# 2)     print(f"{clave} -> {valor}")
#
# TIP / EJEMPLO (comentado):
#   for k, v in {"a": 1, "b": 2}.items():
#       print(f"{k} -> {v}")


def ejercicio_3_recorrido(persona: dict) -> None:
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


if __name__ == "__main__":
    print("\n--- Ejercicio 1 ---")
    try:
        ejercicio_1_acceso_anidado()
    except NotImplementedError:
        print("Pendiente")

    print("\n--- Ejercicio 2 ---")
    try:
        print(ejercicio_2_agregar_actualizar())
    except NotImplementedError:
        print("Pendiente")

    print("\n--- Ejercicio 3 ---")
    try:
        ejercicio_3_recorrido({"nombre": "Raúl", "pais": "Argentina"})
    except NotImplementedError:
        print("Pendiente")
