# Práctica extra — contar encabezados
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r scraping/04 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert contar_h1('<h1>a</h1><h1>b</h1>') == 2


from bs4 import BeautifulSoup


def contar_h1(html):
    raise NotImplementedError


PRUEBAS = [
    ("contar_h1", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
