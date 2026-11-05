# Práctica extra — paréntesis
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r logica/01 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert balanceado('(())') and not balanceado('())')


def balanceado(texto):
    """Solo paréntesis redondos. True si cierra todo y no sobra ninguno. Ejemplo: balanceado('(())') es True; balanceado('())') es False"""
    raise NotImplementedError


PRUEBAS = [
    ("balanceado", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
