# ============================
# 📝 Ejercicios: Sets / clases de caracteres
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import re

# 🔸 Ejemplo:
print(re.findall(r"[aeiou]", "Hola mundo"))

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_vocales() -> None:
    # ENUNCIADO:
    # Extraé todas las vocales de "Programación en Python".
    # Incluí mayúsculas si querés: r"[aeiouAEIOUáéíóúÁÉÍÓÚ]"
    # (o empezá simple con [aeiouAEIOU]).
    #
    # Guía:
    # re.findall(r"[aeiouAEIOU]", texto)
    #
    # TIP / EJEMPLO:
    # re.findall(r"[aeiou]", "Hola")  # ['o', 'a']

    texto = "Programación en Python"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1 (vocales)")


def ejercicio_2_username() -> None:
    # ENUNCIADO:
    # Validá usernames que solo tengan letras, números y ._ % + -
    # Patrón sugerido: r"^[\w._%+-]+$"
    # Probá: "raul_69", "rub.$ius+", "invalido!"
    # Imprimí válido/inválido para cada uno.
    #
    # Guía:
    # for u in (...):
    #     print(u, bool(re.search(patron, u)))
    #
    # TIP / EJEMPLO:
    # re.search(r"^[\w.-]+$", "a_b.c")  # Match
    # re.search(r"^[\w.-]+$", "a!")     # None

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2 (username)")


def ejercicio_3_negacion() -> None:
    # ENUNCIADO:
    # Encontrá todos los caracteres que NO sean dígitos en "abc123xyz".
    #
    # Guía:
    # re.findall(r"[^0-9]", texto)  # o r"\D"
    #
    # TIP / EJEMPLO:
    # re.findall(r"[^aeiou]", "hola")  # consonantes + resto

    texto = "abc123xyz"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3 ([^])")


def ejercicio_4_rangos() -> None:
    # ENUNCIADO:
    # Extraé todas las letras mayúsculas de "RaUl CeNtUrIoN 2026".
    #
    # Guía:
    # re.findall(r"[A-Z]", texto)
    #
    # TIP / EJEMPLO:
    # re.findall(r"[a-z]", "AbC")  # ['b']

    texto = "RaUl CeNtUrIoN 2026"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4 (rangos)")


def ejercicio_5_man_fan_ban() -> None:
    # ENUNCIADO:
    # En "omniman fanatico man bandana fan ban"
    # encontrá solo las palabras exactas man, fan y ban (no subcadenas).
    #
    # Guía:
    # r"\b[mfb]an\b"
    #
    # TIP / EJEMPLO:
    # re.findall(r"\b[mfb]an\b", "man bandana fan")  # ['man', 'fan']

    texto = "omniman fanatico man bandana fan ban"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 5 (man|fan|ban)")


def ejercicio_6_email() -> None:
    # ENUNCIADO:
    # Escribí un patrón simple de email y probalo con:
    #   "raul@mail.com", "malo@", "ok@ok.py",
    #   "lo.que+sea@shopping.online", "michael@gov.co.uk"
    # Imprimí OK/NO para cada uno.
    #
    # Guía (punto de partida):
    # r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    # Ajustá si algún caso corner no pasa como esperás.
    #
    # TIP / EJEMPLO:
    # bool(re.search(r"^[\w.-]+@[\w.-]+\.\w+$", "a@b.co"))

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 6 (email)")


if __name__ == "__main__":
    for fn in (
        ejercicio_1_vocales,
        ejercicio_2_username,
        ejercicio_3_negacion,
        ejercicio_4_rangos,
        ejercicio_5_man_fan_ban,
        ejercicio_6_email,
    ):
        print(f"\n=== {fn.__name__} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
