# Práctica extra — condiciones
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 06 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert estado_tarjeta(True, True, True) == 'bloqueada' and estado_tarjeta(True, False, False) == 'activa'


def prueba_1():
    assert puede_comprar(100, 150, 100, True) and not puede_comprar(100, 150, 100, False)


def prueba_2():
    assert categoria(6, True) == 'en_mora' and categoria(0, False) == 'nuevo' and categoria(5, False) == 'premium'


def estado_tarjeta(activa, vencida, bloqueada):
    """Si bloqueada, 'bloqueada'. Si no, si vencida, 'vencida'. Si no, si activa, 'activa'. Si no, 'inactiva'. Ejemplo: estado_tarjeta(True, True, True) → 'bloqueada'"""
    raise NotImplementedError


def puede_comprar(saldo, monto, limite, activa):
    """True si la tarjeta está activa, el monto es positivo y saldo+límite cubre el monto. El límite es el descubierto permitido, en centavos. Ejemplo: puede_comprar(100, 150, 100, True) es True"""
    raise NotImplementedError


def categoria(anios, mora):
    """Menos de 1 año: 'nuevo'. De 1 a 4: 'estandar'. 5 o más: 'premium'. Si mora es True, siempre 'en_mora'. Ejemplo: categoria(6, True) → 'en_mora'"""
    raise NotImplementedError


PRUEBAS = [
    ("estado_tarjeta", prueba_0),
    ("puede_comprar", prueba_1),
    ("categoria", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
