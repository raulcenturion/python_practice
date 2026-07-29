# Integrador 02 — Gestor de tareas (medio)

Subís un nivel: **POO**, excepciones propias, decorador y módulos.

## Objetivo

Un gestor de tareas por consola con estados, prioridades y persistencia JSON. El código debe estar **separado en módulos**.

## Temas que integra

- Clases, atributos, métodos
- Herencia o al menos composición clara
- Excepciones personalizadas
- Decoradores (logging simple)
- Funciones + módulos (varios `.py`)
- JSON / archivos
- Listas, dicts, `for`/`while`, condicionales

## Estructura pedida

```text
02_gestor_tareas/
  enunciado.md
  practica.py          → menú / punto de entrada
  models.py            → clases Tarea, GestorTareas
  storage.py           → cargar / guardar JSON
  (opcional) utils.py  → helpers
```

Creá `models.py` y `storage.py` vos. `practica.py` ya importa desde ahí.

## Modelo de datos

Cada tarea:

| Campo | Tipo | Notas |
|-------|------|--------|
| `id` | int | autoincremental |
| `titulo` | str | obligatorio, no vacío |
| `prioridad` | str | `"baja"` \| `"media"` \| `"alta"` |
| `hecha` | bool | default `False` |
| `creada_en` | str | ISO date (`YYYY-MM-DD`) |

## Requisitos funcionales

Menú:

1. Crear tarea  
2. Listar todas  
3. Listar solo pendientes  
4. Marcar como hecha (por id)  
5. Eliminar (por id)  
6. Resumen (cuántas hechas / pendientes / por prioridad)  
7. Salir  

Reglas:

- Título vacío → `TareaInvalidaError` (excepción propia)
- Prioridad inválida → misma excepción o una específica
- Id inexistente al marcar/borrar → mensaje claro (no traceback crudo)
- Decorá al menos `crear_tarea` o `guardar` con un `@log_accion` que imprima qué se ejecutó

## Criterios de aceptación

- [ ] Hay al menos `models.py` + `storage.py` + `practica.py`
- [ ] Existe una clase `GestorTareas` que concentra la lógica
- [ ] Persistencia en `tareas.json`
- [ ] Excepción personalizada usada de verdad
- [ ] Un decorador propio en uso
- [ ] El resumen imprime totales útiles

## Cómo entregar

```bash
python practica.py
```

## Tip general

Primero hacé que `Tarea` + `GestorTareas` anden en memoria. La persistencia JSON la enganchás después.

## Ayuda rápida (esqueleto)

Podés basarte en esto al crear `models.py` y `storage.py` (no copies ciego: completá los `...`).

**models.py**

```python
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import date

class TareaInvalidaError(Exception):
    pass

def log_accion(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@dataclass
class Tarea:
    id: int
    titulo: str
    prioridad: str
    hecha: bool = False
    creada_en: str = ""

class GestorTareas:
    PRIORIDADES = {"baja", "media", "alta"}

    def __init__(self, tareas: list[dict] | None = None):
        ...

    @log_accion
    def crear(self, titulo: str, prioridad: str) -> Tarea:
        ...

    def to_list(self) -> list[dict]:
        ...
```

**storage.py**

```python
from __future__ import annotations
import json
from pathlib import Path

ARCHIVO = Path(__file__).with_name("tareas.json")

def cargar_tareas() -> list[dict]:
    ...

def guardar_tareas(tareas: list[dict]) -> None:
    ...
```
