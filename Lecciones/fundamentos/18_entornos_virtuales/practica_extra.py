# Práctica extra — entornos virtuales
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 18 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert parece_venv('/repo/.venv/bin/python') and not parece_venv('/repo/venv_backup/python')


def prueba_1():
    assert usando_el_del_repo() is True


def parece_venv(ruta):
    """True si la ruta contiene '.venv' como una parte, no como un pedazo de otra palabra. Ejemplo: parece_venv('/repo/.venv/bin/python') es True"""
    raise NotImplementedError


import sys


def usando_el_del_repo():
    raise NotImplementedError


PRUEBAS = [
    ("parece_venv", prueba_0),
    ("usando_el_del_repo", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
