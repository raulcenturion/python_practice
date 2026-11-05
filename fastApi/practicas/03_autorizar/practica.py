# Regla de autorización. El enunciado está en enunciado.md.
# Correr: .venv/bin/python fastApi/practicas/03_autorizar/practica.py
#
# El servicio decide. No abre la base y no conoce el status HTTP.
# Cuando esto viva en una ruta, el 402 o el 200 los pone el router
# según el texto que devuelva esta función.

def autorizar(tarjeta: dict, centavos: int) -> str:
    """'autorizada' o 'rechazada'.

    Ejemplo: saldo 100, límite 50, compra 120 y activa → autorizada.
    """
    raise NotImplementedError


def _correr():
    tarjeta = {"activa": True, "saldo_centavos": 100, "limite_centavos": 50}
    ok = autorizar(tarjeta, 120) == "autorizada"
    ok = ok and autorizar({**tarjeta, "activa": False}, 120) == "rechazada"
    ok = ok and autorizar(tarjeta, 200) == "rechazada"
    ok = ok and autorizar(tarjeta, True) == "rechazada"
    if not ok:
        raise AssertionError("autorizar no cumple los ejemplos")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Lecciones"))
    from menu_extra import abrir

    abrir([("autorizar", _correr)], globals())
