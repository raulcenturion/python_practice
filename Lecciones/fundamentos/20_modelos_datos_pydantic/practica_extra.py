# Práctica extra — Pydantic
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 20 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    m = Movimiento(concepto='pan', monto_centavos=100)
    assert m.como_dict() == {'concepto': 'pan', 'monto_centavos': 100}
    try:
        Movimiento(concepto='pan', monto_centavos=0)
        raise AssertionError('tenía que fallar')
    except Exception as exc:
        if type(exc).__name__ != 'ValidationError':
            raise


from pydantic import BaseModel, Field


class Movimiento(BaseModel):
    concepto: str
    monto_centavos: int = Field(gt=0)

    def como_dict(self):
        raise NotImplementedError


PRUEBAS = [
    ("Movimiento", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
