# ============================
# 📝 Challenge: Four Fantastic
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# ============================
# ENUNCIADO
# ============================
# Reed Richards = R, Johnny Storm = J.
# Creá check_is_balanced(text) que:
# - cuente R y J (mayúsculas/minúsculas igual)
# - retorne True si hay la misma cantidad (incluye 0 = 0)
# - retorne False si no

# Casos de prueba esperados:
# check_is_balanced("RRRRJJJjjjrrr")  -> True
# check_is_balanced("RRRJ")           -> False
# check_is_balanced("")               -> True
# check_is_balanced("abc")            -> True


def check_is_balanced(text: str) -> bool:
    # Tu solución acá
    pass


if __name__ == "__main__":
    print(check_is_balanced("RRRRJJJjjjrrr"))
    print(check_is_balanced("RRRJ"))
    print(check_is_balanced(""))
