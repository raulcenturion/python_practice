# 05 — Comisión en el medio de las capas

Una transferencia de este ejercicio cobra 1% entero, con un mínimo de 1 centavo si el monto es positivo. `1000` paga `10`. `50` paga `1`, porque `50 // 100` es `0` y el mínimo sube a 1. `0` paga `0`.

Esa cuenta es la función que falta. El resto del archivo ya está armado como en Devinote:

| Pieza | Dónde | Por qué |
|---|---|---|
| `Transferencia` | modelo Pydantic, sin tabla | valida el JSON |
| `comision_centavos` | servicio | la regla |
| `POST /transferencias` | router | orquesta y no calcula el porcentaje |
| `TestClient` | la prueba | no hace falta uvicorn |

Documentación: [Body](https://fastapi.tiangolo.com/tutorial/body/), [response model](https://fastapi.tiangolo.com/tutorial/response-model/).

La respuesta es `{"centavos": ..., "comision": ..., "total": ...}`. `total` es monto más comisión.

```bash
.venv/bin/python fastApi/practicas/05_comision/practica.py
```
