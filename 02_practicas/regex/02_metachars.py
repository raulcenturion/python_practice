# ============================
# 📝 Ejercicios: Metacaracteres
# 📘 Teoría: Clases_teoria/regex/02_metachars.py
# ============================

import re

# 🔸 Ejemplo:
text = "Hola mundo, H0la de nuevo, H$la otra vez"
print(re.findall(r"H.la", text))

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: El punto (.)
# Encontrá todas las variantes H.la en:
# "Hola H0la H$la Holaa"


# Ejercicio 2: Inicio y fin (^ $)
# Validá si un string empieza con "Error" y si otro termina con ".py".


# Ejercicio 3: Alternancia (|)
# Buscá "gato" o "perro" en "tengo un gato y un pez".


# Ejercicio 4: Escapar caracteres
# Encontrá el literal "precio$" en "el precio$ es 10" (escapá el $).
