# Práctica extra — HTTP sin red
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r fechas/02 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert es_exito(201) and not es_exito(404)


def prueba_1():
    assert leer_saldo({'status': 200, 'body': {'saldo': 10}}) == 10 and leer_saldo({'status': 503, 'body': {}}) is None


def es_exito(status):
    """True si el status está entre 200 y 299. Ejemplo: es_exito(201) es True"""
    raise NotImplementedError


def leer_saldo(respuesta):
    """respuesta es {'status': int, 'body': {'saldo': int}}. Si el status no es éxito, devolvé None. Si lo es, el saldo. Ejemplo: status 200 y saldo 10 → 10"""
    raise NotImplementedError


PRUEBAS = [
    ("es_exito", prueba_0),
    ("leer_saldo", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
