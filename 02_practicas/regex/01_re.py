# ============================
# 📝 Ejercicios: Regex básico
# 📘 Teoría: Clases_teoria/regex/01_re.py
# ============================

import re

# 🔸 Ejemplo:
text = "Hola mundo"
result = re.search("Hola", text)
print(result.group() if result else "No encontrado")

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: search
# Buscá la palabra "Python" en "Me gusta Python y Java".
# Si existe, imprimí el match.


# Ejercicio 2: findall
# Encontrá todas las apariciones de "la" en:
# "la casa, la mesa, el patio, la silla"


# Ejercicio 3: sub
# Reemplazá todas las vocales de "Hola Mundo" por "*" usando re.sub.


# Ejercicio 4: Validar email simple
# Escribí un patrón que valide emails del estilo usuario@dominio.com
# Probá con: "raul@mail.com", "malo@", "ok@ok.py"
