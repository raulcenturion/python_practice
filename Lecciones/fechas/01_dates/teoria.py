# ============================
# 📘 Fechas y horas (datetime)
# ============================
# Módulo stdlib: datetime
# - datetime → fecha + hora
# - timedelta → sumar/restar tiempo
# - timezone → fechas "con zona" (evita ambigüedad)
#
# Tip: datetime.now() sin tz es "ingenuo" (naive). Preferí timezone.utc
# en código nuevo (también silencia el warning del linter).

import locale
from datetime import datetime, timedelta, timezone

UTC = timezone.utc

# ============================
# 🔹 Ahora
# ============================
print("--- Fecha y hora actual ---")
# datetime.now(UTC) → momento actual en UTC
now = datetime.now(UTC)
print(f"Ahora (UTC): {now}")

# ============================
# 🔹 Fecha específica
# ============================
print("\n--- Fecha específica ---")
# Año, mes, día, hora, minuto, segundo + tzinfo
specific = datetime(2025, 2, 12, 15, 30, 0, tzinfo=UTC)
print(f"Específica: {specific}")

# ============================
# 🔹 Formatear (strftime)
# ============================
print("\n--- Formato strftime ---")
# strftime convierte datetime → str con un patrón
# %d día  %m mes  %Y año  %H hora  %M minuto  %S segundo
print("Formato corto:", now.strftime("%d/%m/%Y %H:%M"))

# Locale en español (si el SO lo tiene instalado)
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    print("Formato largo:", now.strftime("%A %d de %B de %Y"))
except locale.Error:
    # Tip: en macOS a veces es "es_ES" o no está el locale.
    print("aviso: locale es_ES no disponible; usá formato numérico")

# ============================
# 🔹 timedelta (sumar / restar)
# ============================
print("\n--- timedelta ---")
# timedelta(days=1, hours=2, minutes=30, ...)
ayer = now - timedelta(days=1)
manana = now + timedelta(days=1)
mas_una_hora = now + timedelta(hours=1)
print("Ayer:", ayer)
print("Mañana:", manana)
print("+1 hora:", mas_una_hora)

# TIP / patrón:
# ahora + timedelta(days=7)   → dentro de una semana
# ahora - timedelta(minutes=30)

# ============================
# 🔹 Componentes
# ============================
print("\n--- Componentes ---")
# Acceso directo a partes del datetime
print("year:", now.year, "month:", now.month, "day:", now.day)
print("hour:", now.hour, "minute:", now.minute, "second:", now.second)

# ============================
# 🔹 Diferencia entre fechas
# ============================
print("\n--- Diferencia entre 2 fechas ---")
# Restar dos datetime → timedelta
inicio = datetime(2026, 1, 1, tzinfo=UTC)
fin = datetime(2026, 9, 11, tzinfo=UTC)
delta = fin - inicio
print("Días entre 1/1/2026 y 11/9/2026:", delta.days)

# ============================
# 🔹 Resumen
# ============================
# - datetime.now(timezone.utc) → ahora con zona
# - datetime(y, m, d, ..., tzinfo=UTC) → fecha concreta
# - strftime("%d/%m/%Y") → texto legible
# - timedelta → sumar/restar
# - fecha_a - fecha_b → timedelta (días, segundos…)
