# Ruta de transferencia. El enunciado está en enunciado.md.
# Correr: .venv/bin/python fastApi/practicas/04_transferencias/practica.py
#
# FastAPI es el framework HTTP. Pydantic valida el body.
# TestClient ejecuta la app en el mismo proceso.
# https://fastapi.tiangolo.com/tutorial/testing/

from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

# from fastapi queda después de pydantic: la carpeta fastapi/ del repo
# hace que ruff lo cuente como paquete local.
from fastapi import FastAPI

app = FastAPI(title="Práctica transferencias")

# Un solo nombre para el path: el decorador y los tres POST de prueba.
RUTA = "/transferencias"
SALDOS = {"ana": 10_000, "luis": 500}


class Transferencia(BaseModel):
    origen: str
    destino: str
    centavos: int = Field(gt=0)


def decidir(saldo_origen: int, destino: str, centavos: int) -> dict:
    """ok y, si alcanza, la resta del origen.

    Ejemplo: decidir(10000, "luis", 100) → {"ok": True, "resta": 9900}
    """
    raise NotImplementedError


@app.get("/salud")
def salud():
    return {"status": "ok"}


@app.post(RUTA)
def transferir(payload: Transferencia):
    # El router no resta a mano: le pasa los datos al servicio.
    return decidir(SALDOS.get(payload.origen, 0), payload.destino, payload.centavos)


def _correr():
    client = TestClient(app)
    salud_resp = client.get("/salud")
    print("ejemplo", salud_resp.status_code, salud_resp.json())
    invalido = client.post(
        RUTA,
        json={"origen": "ana", "destino": "luis", "centavos": 0},
    )
    print("ejemplo 422", invalido.status_code)
    resp = client.post(
        RUTA,
        json={"origen": "ana", "destino": "luis", "centavos": 100},
    )
    sin_saldo = client.post(
        RUTA,
        json={"origen": "luis", "destino": "ana", "centavos": 501},
    )
    ok = resp.status_code == 200 and resp.json() == {"ok": True, "resta": 9900}
    ok = ok and sin_saldo.json() == {"ok": False}
    if not ok:
        raise AssertionError("decidir no cumple los ejemplos")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Lecciones"))
    from menu_extra import abrir

    abrir([("decidir", _correr)], globals())
