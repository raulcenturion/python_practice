# Integrador 03 — Mini API de biblioteca (difícil, pre-FastAPI)

Este es el cierre fuerte: simulás el **estilo FastAPI** sin instalar FastAPI todavía.

## Objetivo

Una “API” en memoria para una biblioteca: rutas con decoradores, modelos Pydantic, handlers `async` y un pequeño cliente de prueba.

## Temas que integra

- Decoradores estilo `@app.get` / `@app.post` (lección 14)
- Pydantic / validación (lección 20)
- `async` / `await` + `asyncio.gather` (lección 19)
- Clases, dicts, listas, excepciones
- Tipado básico y separación de responsabilidades
- (Opcional) regex para validar ISBN simple

## Qué tenés que construir

### 1) Modelos (`models.py`)

- `LibroCreate`: `titulo` (str min 1), `autor` (str), `anio` (int 0–2100), `isbn` (str)
- `Libro` (respuesta): todo lo anterior + `id: int`
- `ErrorResponse`: `detail: str`

### 2) Mini framework (`app.py`)

Clase `MiniAPI` (como en la teoría de decoradores):

- `get(path)` / `post(path)` / `delete(path)` registran handlers
- `async def handle(method, path, **kwargs)` ejecuta el handler
- Si no hay ruta → `{"detail": "Not Found"}` (status mental 404)

### 3) “Base de datos” en memoria

`dict[int, Libro]` + contador de ids.

### 4) Rutas (handlers async)

| Método | Ruta | Comportamiento |
|--------|------|----------------|
| `POST` | `/libros` | Body: `LibroCreate` → crea y retorna `Libro` |
| `GET` | `/libros` | Lista todos |
| `GET` | `/libros/{libro_id}` | Uno por id o error |
| `DELETE` | `/libros/{libro_id}` | Borra o error |
| `GET` | `/stats` | `{"total": N, "autores_unicos": M}` |

Simulá I/O con `await asyncio.sleep(0.05)` dentro de cada handler (como si fuera DB).

### 5) Cliente de prueba (`practica.py`)

`async def demo()` que:

1. Cree 2–3 libros (uno inválido a propósito y capture `ValidationError`)
2. Liste libros
3. Consulte uno por id
4. Pida stats
5. Borre uno
6. Use `asyncio.gather` para crear 2 libros “en paralelo”

## Criterios de aceptación

- [ ] Hay `app.py`, `models.py` y `practica.py`
- [ ] Rutas registradas con decoradores
- [ ] Handlers son `async def`
- [ ] Pydantic valida entradas (año negativo / título vacío fallan)
- [ ] `demo()` corre con `asyncio.run(demo())` sin romper por errores controlados
- [ ] Stats calculados correctamente

## Cómo entregar

```bash
python practica.py
```

## Ayuda

Si te trabás, abrí `tips.md` **de a un tip**. No leas todos de una.
