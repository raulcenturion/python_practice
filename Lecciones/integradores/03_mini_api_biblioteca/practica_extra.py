# Práctica extra — normalizar una ruta
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r Lecciones/integradores/03_mini_api_biblioteca/practica_extra.py

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert normalizar_ruta('libros/') == '/libros' and normalizar_ruta('/') == '/'


def normalizar_ruta(ruta):
    """Poné una barra al principio si falta. Sacá la barra final si hay más path. No cambies '/'. Ejemplo: normalizar_ruta('libros/') → '/libros'"""
    raise NotImplementedError


PRUEBAS = [
    ("normalizar_ruta", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
