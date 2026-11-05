# Prácticas de FastAPI — un banco chico

Estas prácticas usan el mismo recorrido que Devinote, con un dominio de banco: cuentas, tarjetas y movimientos. El mapa de capas está en [`ESTRUCTURA.md`](../../ESTRUCTURA.md), sección **Devinote: capas para el próximo desarrollo**.

La plata va en **centavos enteros**. `1500` es $15,00. Un `float` arrastra error (`0.1 + 0.2`). Cuando haga falta un decimal de verdad, es [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html).

El número de tarjeta, en estas prácticas, se guarda enmascarado (últimos 4). El CVV no se guarda.

## Frameworks

| Pieza | Rol en el banco | Documentación |
|---|---|---|
| [FastAPI](https://fastapi.tiangolo.com/tutorial/) | La app HTTP, las rutas y `Depends` | [aplicaciones más grandes](https://fastapi.tiangolo.com/tutorial/bigger-applications/), [dependencias](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| [Pydantic](https://docs.pydantic.dev/latest/concepts/models/) | El JSON que entra y sale. Si no cumple, la API responde 422 | [Field](https://docs.pydantic.dev/latest/concepts/fields/) |
| [SQLModel](https://sqlmodel.tiangolo.com/tutorial/fastapi/) | La tabla y, sin `table=True`, el mismo estilo de modelo | [select](https://sqlmodel.tiangolo.com/tutorial/select/), [sesión](https://sqlmodel.tiangolo.com/tutorial/where/) |
| SQLAlchemy | El motor que SQLModel usa por debajo | [engine](https://docs.sqlalchemy.org/en/20/core/engines.html) |

## Cómo se reparte

| Capa | En estas prácticas | Qué no hace |
|---|---|---|
| `api` | Recibe el POST, valida el body, llama al servicio | No decide si hay saldo |
| `services` | Autoriza, calcula la comisión, arma el rechazo | No escribe SQL |
| `repositories` | `select`, `add`, `commit` | No conoce el HTTP |
| `models` | `Cuenta` con `table=True`. `Transferencia` sin tabla, solo JSON | No abre el socket |
| `core` | La URL de la base y la sesión | No tiene reglas de negocio |
| `main.py` | Crea la app y monta el router | No transfiere plata |

Flujo de una transferencia:

1. El router recibe el JSON. Pydantic ya lo convirtió en un modelo.
2. Llama al servicio.
3. El servicio pide la cuenta al repositorio y aplica la regla.
4. El repositorio lee la fila `Cuenta`.
5. La respuesta vuelve al router. FastAPI la serializa.

## Las cinco prácticas

Cada carpeta tiene `enunciado.md` y `practica.py`. El archivo corre el ejemplo y marca la función que falta.

```bash
.venv/bin/python fastApi/practicas/01_modelos/practica.py
.venv/bin/python fastApi/practicas/02_cuentas/practica.py
.venv/bin/python fastApi/practicas/03_autorizar/practica.py
.venv/bin/python fastApi/practicas/04_transferencias/practica.py
.venv/bin/python fastApi/practicas/05_comision/practica.py
```

| # | Carpeta | Capa que se practica |
|---|---|---|
| 01 | `01_modelos` | Pydantic. Una tarjeta y un movimiento |
| 02 | `02_cuentas` | SQLModel. Alta y débito en sqlite en memoria |
| 03 | `03_autorizar` | Servicio. Reglas de una compra, sin HTTP |
| 04 | `04_transferencias` | FastAPI. `POST` con `TestClient`, sin levantar uvicorn |
| 05 | `05_comision` | Las capas juntas. La comisión es la función a completar |

## Enunciados para seguir

Misma forma: una función pura, con un ejemplo, y después enchufarla a un servicio. No hace falta red.

1. **Idempotencia.** `ya_procesada(claves, clave) -> bool`. Si la clave ya está en la lista, la transferencia no se vuelve a aplicar. Ejemplo: `ya_procesada(["abc"], "abc")` es `True`.
2. **Extracto.** `del_mes(movimientos, anio, mes)` deja los dicts cuya clave `fecha` empieza con `AAAA-MM`.
3. **Límite diario.** `dentro_del_limite(gastado_hoy, monto, limite)` es `True` solo si `gastado_hoy + monto` no pasa el límite. Todos son centavos.
4. **Contracargo.** `contracargo(saldo, monto)` suma el monto de nuevo. No puede dejar el saldo negativo: el monto del contracargo ya había salido.
5. **Conciliación.** `diferencia(extracto_banco, extracto_propio)` devuelve los ids que están en uno y no en el otro. Los dos argumentos son listas de strings.
6. **Enmascarar.** `enmascarar(numero)` deja los últimos 4 y el resto en `*`. El PAN completo no se imprime en un log.

Cuando una de estas pase a una ruta, el body es un modelo Pydantic, la regla queda en el servicio y la fila en SQLModel. Es el mismo corte que `NoteService` en `devinotes/app/services/note_service.py`.
