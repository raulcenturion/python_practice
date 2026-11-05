# 04 — POST de una transferencia

FastAPI valida el body con el modelo `Transferencia` antes de entrar a la función. [TestClient](https://fastapi.tiangolo.com/tutorial/testing/) llama a la app sin levantar uvicorn.

El ejemplo `GET /salud` ya responde 200. Los saldos de práctica están fijos en el router: Ana tiene 10000 centavos, Luis tiene 500. No hay base en esta carpeta.

Documentación: [cuerpo de la petición](https://fastapi.tiangolo.com/tutorial/body/), [testing](https://fastapi.tiangolo.com/tutorial/testing/).

## Para completar

`decidir(saldo_origen, destino, centavos) -> dict`

- Si `destino` está vacío, o el saldo no alcanza, devolvé `{"ok": False}`.
- Si alcanza, devolvé `{"ok": True, "resta": saldo_origen - centavos}`.

El `POST /transferencias` ya llama a `decidir`. Un body inválido (centavos 0) lo rechaza Pydantic con 422 sin llegar a tu función.

Ejemplo: origen Ana, destino Luis, 100 centavos → `ok` true y `resta` 9900.

```bash
.venv/bin/python fastApi/practicas/04_transferencias/practica.py
```
