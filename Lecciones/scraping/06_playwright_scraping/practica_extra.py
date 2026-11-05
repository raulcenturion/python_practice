# Práctica extra — limpiar un precio leído
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r scraping/06 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert pesos('$ 1.234') == 1234


def pesos(texto):
    """Uní los dígitos del texto y devolvé el int. '$ 1.234' → 1234. Ejemplo: pesos('$ 1.234') → 1234"""
    raise NotImplementedError


PRUEBAS = [
    ("pesos", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
