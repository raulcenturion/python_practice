# Práctica extra — clases
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 12 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    c = Cuenta('Ana', 100)
    c.depositar(50)
    assert c.saldo == 150 and c.extraer(200) is False and c.saldo == 150 and c.extraer(20) is True


class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def extraer(self, monto):
        raise NotImplementedError


PRUEBAS = [
    ("Cuenta", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
