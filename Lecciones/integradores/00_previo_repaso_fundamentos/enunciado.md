# Integrador previo — Repaso guiado de fundamentos (01–20)

**Paso anterior a** `00_repaso_presupuesto_cli`.  
Acá asentás conceptos sueltos (1–2 por tema) **antes** del mini presupuesto CLI.

## Cómo trabajar

1. Abrí `practica.py`.
2. Elegí un ejercicio (ej. `01a`, `14b`, `20c`).
3. Leé el enunciado + la **guía** + el **tip comentado**.
4. Escribí tu solución debajo de `# --- TU SOLUCIÓN ---`.
5. Corré **solo ese** ejercicio (ver abajo).

## Cómo correr un solo ejercicio

Desde la raíz del repo:

```bash
# Listar todos los IDs disponibles
./r integradores/00 --list

# Correr solo uno (ejemplos)
./r integradores/00 01a
./r integradores/00 14b
./r integradores/00 15c
./r integradores/00 19b
./r integradores/00 20c
```

Equivalente directo:

```bash
.venv/bin/python Lecciones/integradores/00_previo_repaso_fundamentos/practica.py --list
.venv/bin/python Lecciones/integradores/00_previo_repaso_fundamentos/practica.py 14b
```

Para correr **todos** (solo si querés un barrido completo):

```bash
./r integradores/00 --all
```

> Tip: el presupuesto CLI sigue siendo `00_repaso_presupuesto_cli`.  
> Si `./r integradores/00` no alcanza, usá:
> `./r integradores/00_previo` o `./r integradores/00_repaso_presupuesto`.

## Mapa de ejercicios

| ID | Tema | Qué practicar |
|----|------|----------------|
| `01a` | Print | `sep` |
| `02a` | Tipos | `type()` |
| `03a` | Casting | `list` / `set` |
| `04a` | Ops | `//` y `%` (segundos) |
| `05a` | Strings | slicing |
| `06a` | If | año bisiesto |
| `07a` | Listas | copia vs referencia |
| `08a` | While | validar contraseña (simulado) |
| `09a` | For | máximo sin `max()` |
| `10a` | Funciones | `*args` |
| `11a` | Dict/set | CRUD + conjuntos |
| `12a` | POO | clase + método |
| `13a` | Excepciones | `ValueError` + propia |
| `14a` | HOF | `filter` / comprehension |
| `14b` | Decorador | `@log` |
| `14c` | Decorador | `@requiere_admin` |
| `14d` | Decorador | `@repetir(n)` |
| `15a` | Ficheros | escribir/leer |
| `15b` | JSON | `dump` / `load` |
| `15c` | Ficheros | append `"a"` |
| `16a` | Referencias | alias vs copy |
| `17a` | Librerías | `ImportError` defensivo |
| `18a` | Venv | detectar venv |
| `19a` | Async | `ping` → `"pong"` |
| `19b` | Async | secuencial vs `gather` |
| `19c` | Async | 5 tareas + tiempo |
| `20a` | Pydantic | `BaseModel` + `model_dump` |
| `20b` | Pydantic | `model_validate` (coerción) |
| `20c` | Pydantic | `Field` + `ValidationError` |

## Orden sugerido

1. Barrido rápido `01a`→`13a` (bases).  
2. Bloque puente FastAPI: `14*` → `15*` → `19*` → `20*`.  
3. Recién después: `./r integradores/00` del **presupuesto CLI** (`00_repaso_presupuesto_cli`).
