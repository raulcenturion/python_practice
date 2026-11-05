# 03 — Autorizar una compra

Esta es la capa de servicio. No hay HTTP ni base: entra un dict y sale una decisión. En Devinote, `NoteService` hace este papel con las notas.

La compra se autoriza solo si pasan todas:

- `activa` es `True`
- `centavos` es un `int` mayor que 0 y no es `bool`
- `centavos` no supera `saldo_centavos + limite_centavos`

## Para completar

`autorizar(tarjeta, centavos) -> str`

Devolvé `"autorizada"` o `"rechazada"`.

`tarjeta` es un dict con `activa`, `saldo_centavos` y `limite_centavos`.

Ejemplos:

- saldo 100, límite 50, compra 120, activa → `"autorizada"`
- la misma compra con `activa` en `False` → `"rechazada"`
- compra 200 → `"rechazada"`

```bash
.venv/bin/python fastApi/practicas/03_autorizar/practica.py
```
