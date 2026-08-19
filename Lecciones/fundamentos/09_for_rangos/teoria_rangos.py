# ============================
# 📘 range() — secuencias de números
# ============================
# Idea clave: range NO es una lista; es una secuencia "perezosa" de enteros.
# Para VERLA completa en consola usamos list(range(...)).
#
# Formas más usadas:
#   range(fin)              → 0, 1, 2, ..., fin-1
#   range(inicio, fin)      → inicio, ..., fin-1
#   range(inicio, fin, paso)→ salta de 'paso' en 'paso'
#
# Ojo: el 'fin' NUNCA se incluye (es exclusivo).

# ---------------------------
# range(fin) → desde 0
# ---------------------------
# Meta: números del 0 al 9 (10 números en total).
print("--- range(10) → 0..9 ---")
print("Idea: un solo argumento = desde 0 hasta fin-1")
print("list(range(10)):", list(range(10)))

# ---------------------------
# range(inicio, fin)
# ---------------------------
# Meta: empezar en 5 y llegar hasta 9 (el 10 no entra).
print("\n--- range(5, 10) → inicio, fin ---")
print("Idea: dos argumentos = desde inicio (incluido) hasta fin (excluido)")
print("list(range(5, 10)):", list(range(5, 10)))

# ---------------------------
# range(inicio, fin, paso)
# ---------------------------
# Meta: de 0 a 19 de 5 en 5 → 0, 5, 10, 15
# La misma idea escala a range(0, 1000, 5); acá usamos un rango chico.
print("\n--- range(0, 20, 5) → inicio, fin, paso ---")
print("Idea: el tercer argumento es el salto")
print("list(range(0, 20, 5)):", list(range(0, 20, 5)))

# ---------------------------
# Números negativos
# ---------------------------
# Meta: de -5 a -1 (el 0 no entra).
print("\n--- range(-5, 0) ---")
print("Idea: también funciona con negativos")
print("list(range(-5, 0)):", list(range(-5, 0)))

# ---------------------------
# Countdown (paso negativo)
# ---------------------------
# Meta: contar hacia atrás: 10, 9, ..., 1 (el 0 no entra).
# Si el paso es negativo, inicio debe ser MAYOR que fin.
print("\n--- range(10, 0, -1) → countdown ---")
print("Idea: paso -1 = ir hacia atrás")
print("list(range(10, 0, -1)):", list(range(10, 0, -1)))

# ---------------------------
# for + range (el uso más común)
# ---------------------------
# Meta: repetir un bloque imprimiendo n = 0, 1, 2, 3, 4.
print("\n--- Iterar con for + range(5) ---")
print("Idea: for n in range(...): usa cada número del rango")
for n in range(5):
    print("n:", n)

# ---------------------------
# Repetir N veces (sin usar el número)
# ---------------------------
# Meta: hacer algo 5 veces. El _ significa "no me importa el valor".
print("\n--- Repetir algo 5 veces ---")
print("Idea: for _ in range(5): solo importa CUÁNTAS vueltas")
for _ in range(5):
    print("hacer cinco veces algo")

# ---------------------------
# Mini mapa mental
# ---------------------------
# range(10)        → 0..9
# range(5, 10)     → 5..9
# range(0, 20, 5)  → 0, 5, 10, 15
# range(10, 0, -1) → 10..1
# for x in range(...):  → recorrer esos números
# for _ in range(n):    → repetir n veces
