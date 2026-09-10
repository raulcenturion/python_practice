# ============================
# 📝 Ejercicios: Regex básico (módulo re)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import re

# 🔸 Ejemplo:
text = "Hola mundo"
result = re.search(r"Hola", text)
print(result.group() if result else "No encontrado")

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_search() -> None:
    # ENUNCIADO:
    # Buscá la primera ocurrencia de "IA" en el texto de abajo.
    # Si existe, imprimí start() y end().
    #
    # Guía:
    # 1) re.search(r"IA", texto)
    # 2) if match: print(match.start(), match.end())
    #
    # TIP / EJEMPLO:
    # m = re.search(r"py", "me gusta python")
    # print(m.group(), m.start(), m.end())  # py 9 11

    texto = (
        "Todo el mundo dice que la IA nos va a quitar el trabajo. "
        "Pero solo hace falta ver cómo la puede cagar con las Regex."
    )
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1 (search IA)")


def ejercicio_2_finditer() -> None:
    # ENUNCIADO:
    # Encontrá todas las ocurrencias de "midu" (como subcadena) en el texto.
    # Para cada una imprimí group(), start() y end().
    # Al final imprimí cuántas veces se encontró.
    #
    # Guía:
    # Usá re.finditer (necesitás posiciones). Contá con un contador o len(list(...)).
    #
    # TIP / EJEMPLO:
    # for m in re.finditer(r"Python", "Python y más Python"):
    #     print(m.group(), m.start(), m.end())

    texto = (
        "Este es el curso de Python de midudev. "
        "¡Suscríbete a midudev si te gusta este contenido! midu"
    )
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2 (finditer midu)")


def ejercicio_3_ignorecase() -> None:
    # ENUNCIADO:
    # Encontrá todas las ocurrencias de "python" sin distinguir mayúsculas.
    # Imprimí la lista (findall + IGNORECASE).
    #
    # Guía:
    # re.findall(r"python", texto, flags=re.IGNORECASE)
    #
    # TIP / EJEMPLO:
    # re.findall(r"ia", "IA ia Ia", flags=re.I)

    texto = (
        "Este es el curso de Python de midudev. "
        "¡Suscríbete a python si te gusta este contenido! PYTHON"
    )
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3 (IGNORECASE)")


def ejercicio_4_sub() -> None:
    # ENUNCIADO:
    # Reemplazá todas las vocales de "Hola Mundo" por "*" con re.sub.
    # Patrón de vocales (simple): r"[aeiouAEIOU]"
    #
    # Guía:
    # print(re.sub(patron, "*", "Hola Mundo"))
    #
    # TIP / EJEMPLO:
    # re.sub(r"\d", "#", "a1b2")  # a#b#

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4 (sub vocales)")


if __name__ == "__main__":
    for fn in (
        ejercicio_1_search,
        ejercicio_2_finditer,
        ejercicio_3_ignorecase,
        ejercicio_4_sub,
    ):
        print(f"\n=== {fn.__name__} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
