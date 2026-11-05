# Modelos de tarjeta. El enunciado está en enunciado.md.
# Correr: .venv/bin/python fastApi/practicas/01_modelos/practica.py
#
# pydantic.BaseModel valida al construir. Field(min_length=4, max_length=4)
# limita ultimos4. Documentación:
# https://docs.pydantic.dev/latest/concepts/models/

from pydantic import BaseModel, Field


class TarjetaVista(BaseModel):
    # Lo que se puede mostrar. No es el PAN ni el CVV.
    ultimos4: str = Field(min_length=4, max_length=4)
    activa: bool


def movimiento_valido(concepto, centavos) -> bool:
    """True si hay un concepto y el monto es un int positivo.

    Ejemplo: movimiento_valido("pan", 100) es True.
    """
    raise NotImplementedError


def _correr():
    vista = TarjetaVista(ultimos4="4242", activa=True)
    print("ejemplo", vista.model_dump())
    ok = movimiento_valido("pan", 100) is True
    ok = ok and movimiento_valido("  ", 100) is False
    ok = ok and movimiento_valido("pan", 0) is False
    ok = ok and movimiento_valido("pan", True) is False
    if not ok:
        raise AssertionError("movimiento_valido no cumple los ejemplos")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Lecciones"))
    from menu_extra import abrir

    abrir([("movimiento_valido", _correr)], globals())
