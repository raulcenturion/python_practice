# Tips — Integrador 03 (leé de a uno)

## Tip 1 — Orden de ataque

1. `models.py` (Pydantic)  
2. `MiniAPI` en `app.py` (solo registro + handle)  
3. Una sola ruta `GET /libros` que devuelva `[]`  
4. Recién ahí POST y el resto  

Si intentás todo junto, se mezcla.

## Tip 2 — MiniAPI (esqueleto mental)

```python
class MiniAPI:
    def __init__(self):
        self.routes = {}  # (METHOD, path) -> coroutine function

    def get(self, path: str):
        def decorator(func):
            self.routes[("GET", path)] = func
            return func
        return decorator

    # igual para post/delete

    async def handle(self, method: str, path: str, **kwargs):
        handler = self.routes.get((method, path))
        if not handler:
            return {"detail": "Not Found"}
        return await handler(**kwargs)
```

Los paths con `{libro_id}` podés tratarlos como string literal `"/libros/{libro_id}"` y pasar `libro_id=...` en `handle`.

## Tip 3 — Pydantic rápido

```python
from pydantic import BaseModel, Field, ValidationError

class LibroCreate(BaseModel):
    titulo: str = Field(min_length=1)
    autor: str
    anio: int = Field(ge=0, le=2100)
    isbn: str
```

Crear: `LibroCreate(titulo="...", ...)`  
Desde dict: `LibroCreate.model_validate({...})`  
Salida: `libro.model_dump()`

## Tip 4 — DB en memoria

```python
db: dict[int, Libro] = {}
next_id = 1

async def crear(data: LibroCreate) -> Libro:
    global next_id
    await asyncio.sleep(0.05)
    libro = Libro(id=next_id, **data.model_dump())
    db[next_id] = libro
    next_id += 1
    return libro
```

## Tip 5 — Validación vs 404

- Datos mal formados → `ValidationError` (lo capturás en `demo`)
- Id que no existe → retorná `ErrorResponse(detail="Libro no encontrado").model_dump()`

No hace falta HTTP real; solo el shape del JSON.

## Tip 6 — gather

```python
r1, r2 = await asyncio.gather(
    app.handle("POST", "/libros", data=LibroCreate(...)),
    app.handle("POST", "/libros", data=LibroCreate(...)),
)
```

## Tip 7 — Si `await handler` falla

¿Tu handler es `async def`?  
¿Llamás `return await handler(**kwargs)` y no `return handler(**kwargs)`?

## Tip 8 — Autores únicos

```python
autores = {libro.autor for libro in db.values()}
len(autores)
```

## Tip 9 — Checklist final

- [ ] `asyncio.run(demo())` imprime algo coherente  
- [ ] Un create inválido no tumba el programa  
- [ ] Después de delete, ese id ya no aparece en el listado  
- [ ] Stats cambia al crear/borrar  

## Tip 10 — Puente a FastAPI

Lo que hiciste acá mapea casi 1:1:

| Acá | FastAPI |
|-----|---------|
| `@app.get("/libros")` | igual |
| `LibroCreate` Pydantic | body / response model |
| `async def` + `await` | endpoints async |
| `db` dict | después será SQLAlchemy / DB real |

Cuando pases a FastAPI, reutilizás modelos y la idea de rutas; el framework te regala el servidor HTTP.
