# Práctica extra — texto de un HTML mínimo
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r scraping/01 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert primer_h1('<h1>Hola</h1>') == 'Hola' and primer_h1('<p>x</p>') is None


def primer_h1(html):
    """Devolvé el texto del primer h1, sin los tags. Si no hay, None. Ejemplo: primer_h1('<h1>Hola</h1>') → 'Hola'"""
    raise NotImplementedError


PRUEBAS = [
    ("primer_h1", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
