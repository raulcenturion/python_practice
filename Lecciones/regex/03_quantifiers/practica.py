# ============================
# 📝 Ejercicios: Cuantificadores
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import re

# 🔸 Ejemplo:
print(re.findall(r"a+", "dddd aaa ccc a bb aa casa"))

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_estrella_vs_mas() -> None:
    # ENUNCIADO:
    # Sobre el texto "aaaba", imprimí re.findall de a* y de a+.
    # Observá la diferencia (vacíos vs no).
    #
    # Guía:
    # print(re.findall(r"a*", texto))
    # print(re.findall(r"a+", texto))
    #
    # TIP / EJEMPLO:
    # * = 0 o más → puede devolver ''
    # + = 1 o más → solo rachas de 'a'

    texto = "aaaba"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1 (* vs +)")


def ejercicio_2_opcional() -> None:
    # ENUNCIADO:
    # Matcheá "color" y "colour" (la 'u' es opcional).
    # Texto: "color colour colorado"
    # Esperado típico: color y colour (no "colorado" entero si usás \b).
    #
    # Guía:
    # r"\bcolou?r\b"
    #
    # TIP / EJEMPLO:
    # re.findall(r"colou?r", "color colour")  # ['color', 'colour']

    texto = "color colour colorado"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2 (?)")


def ejercicio_3_llaves() -> None:
    # ENUNCIADO:
    # En "tengo 7, 42, 100 y 9999 manzanas":
    # 1) números de exactamente 3 dígitos
    # 2) números de 2 a 4 dígitos
    #
    # Guía:
    # r"\b\d{3}\b" y r"\b\d{2,4}\b"
    #
    # TIP / EJEMPLO:
    # re.findall(r"\d{2}", "1 12 123")  # ['12', '12']  (ojo con solapes/cortes)

    texto = "tengo 7, 42, 100 y 9999 manzanas"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3 ({n} / {n,m})")


def ejercicio_4_ab() -> None:
    # ENUNCIADO:
    # Sobre "aaaba ab aab b", listá matches de una o más "a" seguidas de "b".
    #
    # Guía:
    # r"a+b"
    #
    # TIP / EJEMPLO:
    # re.findall(r"a+b", "aaaba ab aab b")  # ['aaab', 'ab', 'aab']

    texto = "aaaba ab aab b"
    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4 (a+b)")


def ejercicio_5_palabras() -> None:
    # ENUNCIADO:
    # A) Palabras de 4 a 6 letras en:
    #    "ala casa árbol león cinco murcielago"
    # B) Palabras de 6 o más letras en:
    #    "ala fantastico casa árbol león cinco murcielago"
    #
    # Guía:
    # r"\b\w{4,6}\b" y r"\b\w{6,}\b"
    # Nota: "árbol" puede no matchear igual según \w y acentos (OK para esta práctica).
    #
    # TIP / EJEMPLO:
    # re.findall(r"\b\w{3}\b", "un sol dos")

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 5 (longitud de palabras)")


if __name__ == "__main__":
    for fn in (
        ejercicio_1_estrella_vs_mas,
        ejercicio_2_opcional,
        ejercicio_3_llaves,
        ejercicio_4_ab,
        ejercicio_5_palabras,
    ):
        print(f"\n=== {fn.__name__} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
