###
# range() — secuencia de números (muy usada con for)
###

print("--- range(10) → 0..9 ---")
print("list(range(10)):", list(range(10)))

print("\n--- range(5, 10) → inicio, fin ---")
print("list(range(5, 10)):", list(range(5, 10)))

# Misma idea escala a range(0, 1000, 5); acá usamos un rango chico para la consola
print("\n--- range(0, 20, 5) → inicio, fin, paso ---")
print("list(range(0, 20, 5)):", list(range(0, 20, 5)))

print("\n--- range(-5, 0) ---")
print("list(range(-5, 0)):", list(range(-5, 0)))

print("\n--- range(10, 0, -1) → countdown ---")
print("list(range(10, 0, -1)):", list(range(10, 0, -1)))

print("\n--- Iterar con for + range(5) ---")
for n in range(5):
    print("n:", n)

print("\n--- Repetir algo 5 veces ---")
for _ in range(5):
    print("hacer cinco veces algo")
