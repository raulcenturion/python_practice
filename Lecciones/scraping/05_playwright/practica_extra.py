# Práctica extra — armar una URL de búsqueda
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r scraping/05 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert url_busqueda('tarjeta oro') == 'https://ejemplo.test/buscar?q=tarjeta%20oro'


from urllib.parse import quote


def url_busqueda(termino):
    raise NotImplementedError


PRUEBAS = [
    ("url_busqueda", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
