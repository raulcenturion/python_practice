# ============================
# 📝 Challenge: Battle
# 📘 Teoría: Clases_teoria/logica/05_challenge_battle.py
# ============================

# ============================
# ENUNCIADO
# ============================
# lista_a y lista_b tienen la misma longitud.
# Cada índice se enfrenta:
# - si a > b, el valor de a se suma al siguiente de lista_a
# - si b > a, el valor de b se suma al siguiente de lista_b
# - si empatan, ambos se eliminan (no afectan al siguiente)
#
# Resultado final:
# - queda valor en a -> "Xa"
# - queda valor en b -> "Xb"
# - empate -> "x"
#
# Ejemplo:
# lista_a = [2, 4, 2]
# lista_b = [3, 3, 4]
# battle(lista_a, lista_b)  # "2b"


def battle(lista_a: list[int], lista_b: list[int]) -> str:
    # Tu solución acá
    pass


if __name__ == "__main__":
    print(battle([2, 4, 2], [3, 3, 4]))  # 2b
