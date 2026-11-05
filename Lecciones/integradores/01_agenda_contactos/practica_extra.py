# Práctica extra — buscar en la agenda
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r Lecciones/integradores/01_agenda_contactos/practica_extra.py

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert por_prefijo(['Ana', 'andro', 'Bea'], 'an') == ['Ana', 'andro']


def por_prefijo(nombres, prefijo):
    """Lista de nombres que empiezan con prefijo, en el orden original. Ejemplo: por_prefijo(['Ana', 'andro'], 'an') → ['Ana', 'andro']"""
    raise NotImplementedError


PRUEBAS = [
    ("por_prefijo", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
