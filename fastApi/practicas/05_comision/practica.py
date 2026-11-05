# Comisión de una transferencia. El enunciado está en enunciado.md.
# Correr: .venv/bin/python fastApi/practicas/05_comision/practica.py
#
# El router llama al servicio. La regla del 1% vive en comision_centavos.
# https://fastapi.tiangolo.com/tutorial/body/

from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

# from fastapi queda después de pydantic: la carpeta fastapi/ del repo
# hace que ruff lo cuente como paquete local.
from fastapi import FastAPI

app = FastAPI(title="Práctica comisión")

# La misma ruta en el decorador y en cada TestClient. Un nombre solo:
# si mañana cambia el path, se toca esta línea.
RUTA = "/transferencias"


class Transferencia(BaseModel):
    centavos: int = Field(ge=0)


def comision_centavos(centavos: int) -> int:
    """1% entero, mínimo 1 si el monto es positivo. 0 si el monto es 0.

    Ejemplo: comision_centavos(1000) → 10. comision_centavos(50) → 1.
    """
    raise NotImplementedError


@app.post(RUTA)
def transferir(payload: Transferencia):
    extra = comision_centavos(payload.centavos)
    return {
        "centavos": payload.centavos,
        "comision": extra,
        "total": payload.centavos + extra,
    }


def _correr():
    client = TestClient(app)
    mil = client.post(RUTA, json={"centavos": 1000})
    chica = client.post(RUTA, json={"centavos": 50})
    cero = client.post(RUTA, json={"centavos": 0})
    ok = mil.json() == {"centavos": 1000, "comision": 10, "total": 1010}
    ok = ok and chica.json() == {"centavos": 50, "comision": 1, "total": 51}
    ok = ok and cero.json() == {"centavos": 0, "comision": 0, "total": 0}
    if not ok:
        raise AssertionError("comision_centavos no cumple los ejemplos")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Lecciones"))
    from menu_extra import abrir

    abrir([("comision_centavos", _correr)], globals())
