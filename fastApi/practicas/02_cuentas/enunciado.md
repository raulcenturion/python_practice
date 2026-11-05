# 02 — Cuenta con SQLModel

`table=True` crea la tabla. Sin eso, la clase solo valida JSON. La sesión se abre, se usa y se cierra. El ejemplo inserta una cuenta en una base en memoria. No queda un archivo `.db`.

Documentación: [SQLModel y FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/), [crear la tabla](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/), [consultar](https://sqlmodel.tiangolo.com/tutorial/select/).

## Para completar

`debitar(session, cuenta_id, centavos) -> int`

- Buscá la cuenta con `session.get(Cuenta, cuenta_id)`.
- Si no está, o `centavos` no es positivo, o el saldo no alcanza, devolvé `-1` y no cambies la fila.
- Si alcanza, restá y hacé `commit`. Devolvé el saldo nuevo.

Ejemplo: una cuenta con 1000, `debitar(..., 400)` devuelve `600`. Un segundo débito de `700` devuelve `-1` y el saldo sigue en `600`.

```bash
.venv/bin/python fastApi/practicas/02_cuentas/practica.py
```
