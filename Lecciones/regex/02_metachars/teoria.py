# ============================
# 📘 Regex 02 — Metacaracteres
# ============================
# Los metacaracteres son símbolos con significado especial en regex.
# Ejemplos: . ^ $ \ | ( ) [ ] { } * + ?
#
# Para buscar el símbolo LITERAL, hay que escaparlo: \. \$ \|
# Siempre preferí raw strings: r"\d", r"\.", r"\b"

import re

# ============================
# 🔹 El punto (.) — cualquier carácter (salvo salto de línea)
# ============================
# "." matchea UN carácter cualquiera (no \n por defecto).
print("--- El punto (.) ---")

texto = "Hola mundo, H0la de nuevo, H$la otra vez"
patron = r"H.la"  # H + cualquier char + la
print("findall H.la:", re.findall(patron, texto))

texto2 = "casa caasa cosa cisa cesa causa"
print("findall c.sa:", re.findall(r"c.sa", texto2))
# Tip: "caasa" NO matchea c.sa (hay dos 'a' entre c y s).


# ============================
# 🔹 Escapar metacaracteres
# ============================
# Si querés el punto literal ".", usá r"\."
print("\n--- Escapes (\\.) ---")

texto = "Mi casa es blanca. Y el coche es negro."
print("puntos literales:", re.findall(r"\.", texto))

# Tip: r"\$" busca el signo pesos; r"\|" busca la barra vertical.


# ============================
# 🔹 \d \w \s — clases abreviadas
# ============================
# \d → dígito [0-9]
# \w → "word char": letra, dígito o _  (aprox. [a-zA-Z0-9_])
# \s → espacio en blanco (espacio, tab, \n, …)
# Mayúscula invierte: \D no-dígito, \W no-word, \S no-espacio
print("\n--- \\d \\w \\s ---")

texto = "El número de teléfono es 123456789"
print(r"\d{9}:", re.findall(r"\d{9}", texto))

# SOLVED mini-demo: teléfono con prefijo +34
texto_tel = "Mi número de teléfono es +34 688999999 apúntalo vale?"
m = re.search(r"\+34 \d{9}", texto_tel)
if m:
    print("teléfono:", m.group())

usuario = "el_rubius_69"
print(r"\w chars:", re.findall(r"\w", usuario))

texto_ws = "Hola mundo\n¿Cómo estás?\t"
print(r"\s count:", len(re.findall(r"\s", texto_ws)))


# ============================
# 🔹 ^ y $ — inicio y fin de cadena
# ============================
# ^ → ancla al INICIO del string
# $ → ancla al FINAL del string
# Tip: sin ^/$ el patrón puede matchear en cualquier parte.
print("\n--- ^ y $ ---")

username = "423_name%22"
if re.search(r"^\w", username):
    print("empieza con word-char")

phone = "+34 688999999"
if re.search(r"^\+\d{1,3} ", phone):
    print("prefijo internacional OK")

# "mundo$" falla si hay un punto después
print("mundo$ en 'Hola mundo.':", bool(re.search(r"mundo$", "Hola mundo.")))
print("mundo\\.$ en 'Hola mundo.':", bool(re.search(r"mundo\.$", "Hola mundo.")))

# SOLVED mini-demo: ¿termina en @gmail.com?
email = "miduga@hotmail.com"
print("es gmail?:", bool(re.search(r"@gmail\.com$", email)))


# ============================
# 🔹 \b — límite de palabra
# ============================
# \b es el "borde" entre un \w y un no-\w (o inicio/fin).
# Sirve para no matchear "casa" dentro de "casada".
print("\n--- \\b (word boundary) ---")

texto = "casa casada cosa cosas casado casa"
print(r"\bc.sa\b:", re.findall(r"\bc.sa\b", texto))

# SOLVED mini-demo: archivos .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
print("archivos .txt:", re.findall(r"\b\w+\.txt\b", files))


# ============================
# 🔹 | — alternancia (OR)
# ============================
# A|B matchea A o B. La izquierda se prueba primero.
print("\n--- | (alternancia) ---")

fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate"
patron = r"palta|aguacate|pera"
print("frutas:", re.findall(patron, fruits))

# Tip: agrupá con ( ) si combinás | con más patrón: r"(gato|perro)s"

# ============================
# 🔹 Resumen
# ============================
# - . → un carácter cualquiera (no \n)
# - \. \$ \| → literales escapados
# - \d dígito | \w word | \s whitespace (+ mayúsculas = inverso)
# - ^ inicio | $ fin
# - \b borde de palabra
# - | alternativa
# - Usá r"..." siempre que haya barras
#
# Práctica: practica.py (misma carpeta)
