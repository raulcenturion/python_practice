# Práctica extra — BeautifulSoup sobre un string
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r scraping/02 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert textos_li('<ul><li> pan </li><li>leche</li></ul>') == ['pan', 'leche']


from bs4 import BeautifulSoup


def textos_li(html):
    raise NotImplementedError


PRUEBAS = [
    ("textos_li", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
