# ============================
# 📝 Ejercicios: Fechas y horas
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

from datetime import datetime, timedelta, timezone

UTC = timezone.utc

# 🔸 Ejemplo:
now = datetime.now(UTC)
print(f"Ahora (UTC): {now}")
print(now.strftime("%d/%m/%Y %H:%M"))
# timedelta suma/resta tiempo (útil para el ejercicio 4):
print("Mañana:", now + timedelta(days=1))
print("+1 hora:", now + timedelta(hours=1))

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_ahora() -> None:
    # ENUNCIADO:
    # Imprimí la fecha y hora actual con datetime.now(timezone.utc).
    #
    # Guía:
    # 1) from datetime import datetime, timezone
    # 2) ahora = datetime.now(timezone.utc)
    # 3) print(ahora)
    #
    # TIP / EJEMPLO:
    # print(datetime.now(timezone.utc))

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_especifica() -> None:
    # ENUNCIADO:
    # Creá un datetime para el 12/02/2025 a las 15:30:00 (UTC) e imprimilo.
    #
    # Guía:
    # datetime(2025, 2, 12, 15, 30, 0, tzinfo=timezone.utc)
    #
    # TIP:
    # El orden es: año, mes, día, hora, minuto, segundo

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_formato() -> None:
    # ENUNCIADO:
    # Formateá la fecha actual como "día/mes/año hora:minuto" con strftime.
    #
    # TIP / EJEMPLO:
    # datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M")

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


def ejercicio_4_timedelta() -> None:
    # ENUNCIADO:
    # Calculá e imprimí: ayer, mañana y una hora después de ahora.
    #
    # Guía:
    # ahora = datetime.now(timezone.utc)
    # ayer = ahora - timedelta(days=1)
    # manana = ahora + timedelta(days=1)
    # mas_hora = ahora + timedelta(hours=1)
    #
    # TIP:
    # timedelta(days=…, hours=…, minutes=…, seconds=…)

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4")


def ejercicio_5_componentes() -> None:
    # ENUNCIADO:
    # Extraé year, month, day, hour y minute de datetime.now(UTC) e imprimilos.
    #
    # TIP:
    # n = datetime.now(timezone.utc)
    # print(n.year, n.month, n.day, n.hour, n.minute)

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 5")


if __name__ == "__main__":
    print("--- Práctica 01 dates ---")
    for fn in (
        ejercicio_1_ahora,
        ejercicio_2_especifica,
        ejercicio_3_formato,
        ejercicio_4_timedelta,
        ejercicio_5_componentes,
    ):
        try:
            fn()
            print(f"✅ {fn.__name__}")
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
