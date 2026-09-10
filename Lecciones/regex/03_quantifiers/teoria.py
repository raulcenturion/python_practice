# ============================
# 📘 Regex 03 — Cuantificadores
# ============================
# Un cuantificador dice CUÁNTAS veces repetir lo que está inmediatamente antes.
#
#   *     → 0 o más
#   +     → 1 o más
#   ?     → 0 o 1 (opcional)
#   {n}   → exactamente n
#   {n,m} → entre n y m (inclusive)
#   {n,}  → n o más
#
# Contraste clave: * puede matchear vacío; + exige al menos uno.

import re

# ============================
# 🔹 * — cero o más
# ============================
# "a*" matchea "", "a", "aa", "aaa", …
# Cuidado: findall con * a menudo incluye strings vacíos entre caracteres.
print("--- * (cero o más) ---")

texto = "aaaba"
print("a* sobre 'aaaba':", re.findall(r"a*", texto))
# Tip: ves varios '' porque entre letras que no son 'a' también "matchea" 0 veces.


# ============================
# 🔹 + — una o más
# ============================
# "a+" exige al menos una 'a'. No genera vacíos como *.
print("\n--- + (una o más) ---")

texto = "dddd aaa ccc a bb aa casa"
print("a+:", re.findall(r"a+", texto))

# Contraste * vs + (mismo texto)
print("* vs + sobre 'aaaba':")
print("  a* →", re.findall(r"a*", "aaaba"))
print("  a+ →", re.findall(r"a+", "aaaba"))


# ============================
# 🔹 ? — cero o una (opcional)
# ============================
# Hace opcional el elemento anterior.
print("\n--- ? (opcional) ---")

texto = "aaabacb"
print("a?b:", re.findall(r"a?b", texto))
# Interpreta: 'b' sola o 'ab' (la 'a' es opcional justo antes de b).

# SOLVED mini-demo: +34 opcional delante del número
phones = ["+34 688999999", "688999999", "34 688999999"]
patron_tel = r"(?:\+34 )?\d{9}"
for p in phones:
    m = re.search(patron_tel, p)
    print(f"  {p!r} →", m.group() if m else None)
# Tip: (?:...) es grupo no-capturante (agrupa sin crear group extra).


# ============================
# 🔹 {n} — exactamente n veces
# ============================
print("\n--- {n} ---")

texto = "aaaaaa         aa   aaaa"
print("a{3}:", re.findall(r"a{3}", texto))
# Tip: en "aaaaaa" findall no solapa: toma 'aaa' + 'aaa'.


# ============================
# 🔹 {n,m} y {n,} — rangos
# ============================
print("\n--- {n,m} y {n,} ---")

texto = "u uu uuu u"
print(r"\w{2,3}:", re.findall(r"\w{2,3}", texto))

# SOLVED mini-demo: palabras de 4 a 6 letras
words = "ala casa árbol león cinco murcielago"
print(r"\b\w{4,6}\b:", re.findall(r"\b\w{4,6}\b", words))

# SOLVED mini-demo: 6 o más letras
words2 = "ala fantastico casa árbol león cinco murcielago"
print(r"\b\w{6,}\b:", re.findall(r"\b\w{6,}\b", words2))

# Tip: \b evita cortar "murcielago" a pedazos de 4–6 si usás solo \w{4,6}.

# ============================
# 🔹 Resumen
# ============================
# - *  → 0+ (puede ser vacío)
# - +  → 1+ (nunca vacío)
# - ?  → 0 o 1
# - {n} {n,m} {n,} → conteos exactos / rangos / mínimo
# - Combiná con \b / grupos cuando midas "palabras"
#
# Práctica: practica.py (misma carpeta)
