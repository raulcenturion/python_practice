# ============================
# 📝 Ejercicios: Metacaracteres
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import re

# 🔸 Ejemplo:
text = "Hola mundo, H0la de nuevo, H$la otra vez"
print(re.findall(r"H.la", text))

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_punto() -> None:
    # ENUNCIADO:
    # Encontrá todas las variantes H.la en:
    # "Hola H0la H$la Holaa"
    # (Holaa NO debería entrar: hay una 'a' de más).
    #
    # Guía:
    # re.findall(r"H.la", texto)
    #
    # TIP / EJEMPLO:
    # re.findall(r"c.sa", "casa cosa cisa")  # ['casa', 'cosa', 'cisa']

    texto = "Hola H0la H$la Holaa"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1 (punto .)")


def ejercicio_2_anclas() -> None:
    # ENUNCIADO:
    # 1) Validá si "Error: falló el login" EMPIEZA con "Error" (^).
    # 2) Validá si "script.py" TERMINA con ".py" (escapá el punto: r"\.py$").
    # Imprimí True/False en cada caso.
    #
    # Guía:
    # bool(re.search(r"^Error", s1))
    # bool(re.search(r"\.py$", s2))
    #
    # TIP / EJEMPLO:
    # re.search(r"^Hola", "Hola mundo")  # Match
    # re.search(r"mundo$", "Hola mundo")  # Match

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2 (^ y $)")


def ejercicio_3_alternancia() -> None:
    # ENUNCIADO:
    # Buscá "gato" o "perro" en "tengo un gato y un pez".
    # Imprimí la lista de coincidencias.
    #
    # Guía:
    # re.findall(r"gato|perro", texto)
    #
    # TIP / EJEMPLO:
    # re.findall(r"rojo|azul", "auto azul y rojo")  # ['azul', 'rojo']

    texto = "tengo un gato y un pez"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3 (|)")


def ejercicio_4_escapar() -> None:
    # ENUNCIADO:
    # Encontrá el literal "precio$" en "el precio$ es 10".
    # Recordá escapar el $: r"precio\$"
    #
    # Guía:
    # re.search(r"precio\$", texto) → .group()
    #
    # TIP / EJEMPLO:
    # re.findall(r"\.", "a.b.c")  # ['.', '.']

    texto = "el precio$ es 10"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4 (escapar $)")


def ejercicio_5_gmail_y_txt() -> None:
    # ENUNCIADO:
    # A) Validá si el email termina en @gmail.com (escapá el punto del .com).
    #    Probá: "miduga@hotmail.com" y "hola@gmail.com"
    # B) De "file1.txt file2.pdf secret.txt" listá solo los nombres *.txt
    #
    # Guía:
    # A) r"@gmail\.com$"
    # B) r"\b\w+\.txt\b"  (o similar)
    #
    # TIP / EJEMPLO:
    # re.search(r"@gmail\.com$", "x@gmail.com")
    # re.findall(r"\w+\.pdf", "a.pdf b.txt")

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 5 (gmail + txt)")


if __name__ == "__main__":
    for fn in (
        ejercicio_1_punto,
        ejercicio_2_anclas,
        ejercicio_3_alternancia,
        ejercicio_4_escapar,
        ejercicio_5_gmail_y_txt,
    ):
        print(f"\n=== {fn.__name__} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
