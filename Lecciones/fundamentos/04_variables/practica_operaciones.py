# ============================
# 📝 Ejercicios: Operaciones Aritméticas
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import math

# 🔸 Ejemplo:
a = 15
b = 4
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo (resto):", a % b)
print("Potencia:", a ** b)

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Los 7 operadores
# Pedí dos números al usuario y mostrá: +, -, *, /, //, %, **
#Acá la idea todavía no es usar input, sino que usar variables ya definidas.
print("Ejercicio 1:" )
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo (resto):", a % b)
print("Potencia:", a ** b)



# Ejercicio 2: Diferencia / vs //
# Probá 7/2 y 7//2. ¿Y con negativos? -7//2. Imprimí los resultados.
print("Ejercicio 2:")
print("7/2:", 7/2)
print("7//2:", 7//2)
print("-7//2:", -7//2)




# Ejercicio 3: Área del círculo
# Calculá el área de un círculo con radio = 5 (area = pi * radio ** 2)
# Usá pi = 3.14159
print("Ejercicio 3:")
pi = 3.14159
radio = 5
area = pi * radio ** 2
print("El área del círculo es:", area)



# Ejercicio 4: Descomponer segundos
# Dado 3661 segundos, descomponelo en horas, minutos y segundos con // y %.
# Resultado esperado: 1h 1m 1s
print("Ejercicio 4:")
segundos = 3661
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = segundos % 60
print("1h 1m 1s")
print("1h", minutos, "m", segundos, "s")


# Ejercicio 5: Precisión de floats
# ¿Cuánto da 0.1 + 0.2? ¿Es exactamente 0.3? Imprimilo y descubrí por qué.
# Nota: no uses == con floats (Sonar lo marca). Mejor mirar la diferencia o math.isclose.
print("Ejercicio 5:")
suma = 0.1 + 0.2
print("0.1 + 0.2:", suma)                         # 0.30000000000000004
print("diferencia con 0.3:", abs(suma - 0.3))     # no es 0 → no es exacto
print("¿casi iguales?:", math.isclose(suma, 0.3)) # True (comparación segura)


# Ejercicio 6: Conversión de temperatura
# Pedí la temperatura en Celsius y convertila a Fahrenheit: F = C * 9/5 + 32
#
# Nota: acá usamos input() para interactuar con el usuario.
# - input("mensaje") muestra el mensaje y espera que escribas algo + Enter
# - Siempre devuelve un str → por eso hacemos float(...) para poder calcular
# Lo vas a ver con más detalle en la lección 05 (input / strings).
print("Ejercicio 6:")
celsius = float(input("Ingrese la temperatura en Celsius: "))  # input → usuario
fahrenheit = celsius * 9 / 5 + 32
print("La temperatura en Fahrenheit es:", fahrenheit)
