# Práctica extra — una tarjeta con vencimiento
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r fechas/03 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    from datetime import date
    t = Tarjeta('4242', 12, 2030)
    assert t.esta_vigente(date(2026, 5, 1)) and t.ultimos4 == '4242'


class Tarjeta:
    def __init__(self, ultimos4, mes, anio):
        self.ultimos4 = ultimos4
        self.mes = mes
        self.anio = anio

    def esta_vigente(self, hoy):
        raise NotImplementedError


PRUEBAS = [
    ("Tarjeta", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
