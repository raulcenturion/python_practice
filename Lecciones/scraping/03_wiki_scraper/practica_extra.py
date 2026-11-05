# Práctica extra — el primer párrafo
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r scraping/03 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert primer_parrafo('<p> Hola </p>') == 'Hola'


from bs4 import BeautifulSoup


def primer_parrafo(html):
    raise NotImplementedError


PRUEBAS = [
    ("primer_parrafo", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
