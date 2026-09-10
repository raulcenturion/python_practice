# ============================
# 📘 Challenge: Battle — duelo con carry entre rondas
# ============================
# Historia / reglas:
#   Tenés lista_a y lista_b (misma longitud). En cada índice i se enfrentan.
#
#   - Si a[i] > b[i]: gana A. El SUPERÁVIT (a - b) se SUMA al siguiente de A.
#   - Si b[i] > a[i]: gana B. El SUPERÁVIT (b - a) se SUMA al siguiente de B.
#   - Si empatan: nadie aporta al siguiente.
#
# Resultado final (después de la última ronda):
#   - Quedó superávit de A → "Xa"  (ej. "3a")
#   - Quedó superávit de B → "Xb"
#   - Empate total → "x"
#
# Importante:
#   NO alcanza con sum(lista_a) - sum(lista_b) como "atajo mental" pedagógico.
#   Aunque a veces el número final coincida, acá practicamos la SIMULACIÓN
#   ronda a ronda con carry. Eso es lo que pedís en el challenge.

# ============================
# 🔹 Trazas del enunciado
# ============================
print("--- Ejemplo 1 (traza) ---")
print("A = [2, 4, 2]")
print("B = [3, 3, 4]")
print("  Ronda 0: 2 vs 3 → gana B por 1 → carry +1 a B[1]")
print("  Ronda 1: 4 vs (3+1)=4 → empate → sin carry")
print("  Ronda 2: 2 vs 4 → gana B por 2 (última ronda)")
print("  Resultado: '2b'")

print("\n--- Ejemplo 2 (traza) ---")
print("A = [4, 4, 4]")
print("B = [2, 8, 2]")
print("  Ronda 0: 4 vs 2 → gana A por 2 → carry +2 a A[1]")
print("  Ronda 1: (4+2)=6 vs 8 → gana B por 2 → carry +2 a B[2]")
print("  Ronda 2: 4 vs (2+2)=4 → empate")
print("  Resultado: 'x'")


# ============================
# 🔹 Solución con carry
# ============================
print("\n--- Solución simulando rondas ---")


def battle(lista_a: list[int], lista_b: list[int]) -> str:
    """Simula el duelo con carry del superávit entre rondas."""
    # Trabajamos sobre copias para no mutar las listas originales.
    a = lista_a.copy()
    b = lista_b.copy()
    n = len(a)

    for i in range(n):
        va, vb = a[i], b[i]
        print(f"  Ronda {i}: {va} vs {vb}", end="")

        if va > vb:
            surplus = va - vb
            if i + 1 < n:
                a[i + 1] += surplus
                print(f" → gana A (+{surplus}) → A[{i + 1}] ahora {a[i + 1]}")
            else:
                print(f" → gana A (+{surplus}) [última] → '{surplus}a'")
                return f"{surplus}a"
        elif vb > va:
            surplus = vb - va
            if i + 1 < n:
                b[i + 1] += surplus
                print(f" → gana B (+{surplus}) → B[{i + 1}] ahora {b[i + 1]}")
            else:
                print(f" → gana B (+{surplus}) [última] → '{surplus}b'")
                return f"{surplus}b"
        else:
            print(" → empate (sin carry)")

    print("  Fin de rondas sin superávit final → 'x'")
    return "x"


# Tip — anti-patrón (NO uses esto como solución "real"):
#   # return f"{sum(a)-sum(b)}a" if sum(a) > sum(b) else ...
#   # No enseña el carry ni deja claras las rondas intermedias.


# ============================
# 🔹 Demos
# ============================
print("\n--- Demo 1 ---")
r1 = battle([2, 4, 2], [3, 3, 4])
print(f"battle([2, 4, 2], [3, 3, 4]) → {r1}")  # 2b

print("\n--- Demo 2 ---")
r2 = battle([4, 4, 4], [2, 8, 2])
print(f"battle([4, 4, 4], [2, 8, 2]) → {r2}")  # x

print("\n--- Demo 3 ---")
r3 = battle([5, 1], [1, 1])
print(f"battle([5, 1], [1, 1]) → {r3}")
# Ronda 0: 5 vs 1 → +4 a A[1] → A=[5, 5]
# Ronda 1: 5 vs 1 → +4 última → "4a"


# ============================
# 🔹 Resumen
# ============================
# - Enfrentá índice a índice.
# - Carry = diferencia (superávit del ganador), no el valor completo.
# - Si gana en ronda intermedia → sumá el surplus al siguiente de esa lista.
# - Si gana en la última → devolvé "Xa" o "Xb".
# - Si todo empata al final → "x".
# - Copiá las listas (.copy()) si no querés mutar las originales.
