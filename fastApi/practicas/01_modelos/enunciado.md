# 01 — Modelos de una tarjeta

Pydantic arma el objeto y rechaza lo que no cumple. En una API, ese rechazo lo convierte FastAPI en 422. Acá todavía no hay ruta: se prueba el modelo directo.

Documentación: [Models](https://docs.pydantic.dev/latest/concepts/models/), [Fields](https://docs.pydantic.dev/latest/concepts/fields/).

## Ejemplo que ya corre

`TarjetaVista` tiene `ultimos4` de largo 4 y `activa`. `practica.py` construye una y la imprime.

## Para completar

`movimiento_valido(concepto, centavos) -> bool`

- `concepto` no puede ser vacío ni solo espacios.
- `centavos` tiene que ser un `int` y no un `bool`, y mayor que 0.

Ejemplos:

- `movimiento_valido("pan", 100)` → `True`
- `movimiento_valido("  ", 100)` → `False`
- `movimiento_valido("pan", 0)` → `False`
- `movimiento_valido("pan", True)` → `False`

```bash
.venv/bin/python fastApi/practicas/01_modelos/practica.py
```
