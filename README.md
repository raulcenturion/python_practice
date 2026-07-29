# welcomePy

Repo de estudio de Python: cada lección junta **teoría + práctica** (checklist hacia FastAPI).

## Cómo estudiar

Abrí una carpeta de lección (ej. `Lecciones/fundamentos/01_print_comentarios/`):

1. Leé `teoria.py` (o `teoria_*.py` si hay más de una)
2. Resolvé `practica.py` en la misma carpeta
3. Pasá a la lección siguiente (`02_...`, `03_...`)

## Estructura

```text
Lecciones/
  fundamentos/     → base Python (orden 01 → 20)
  fechas/
  logica/
  regex/
  scraping/
  integradores/    → 3 proyectos de cierre (fácil → difícil)
```

Cada lección:

```text
01_print_comentarios/
  teoria.py
  practica.py
```

Si el tema necesita más de un archivo de teoría:

```text
07_listas/
  teoria_listas.py
  teoria_metodos.py
  practica.py
```

## Fundamentos (checklist)

| # | Lección | Contenido |
|---|---------|-----------|
| 01 | `print_comentarios` | print, comentarios |
| 02 | `tipos_de_datos` | str, int, float, bool, … |
| 03 | `casting` | conversiones |
| 04 | `variables` | variables + `practica_operaciones.py` |
| 05 | `input` | input y strings |
| 06 | `condicionales_booleanos` | if/else, bool |
| 07 | `listas` | listas y métodos |
| 08 | `while` | while |
| 09 | `for_rangos` | for y range |
| 10 | `funciones` | def, params, return |
| 11 | `diccionarios_tuplas_sets` | dict, tuple, set |
| 12 | `clases_poo` | clases y herencia |
| 13 | `excepciones` | try/except/finally |
| 14 | `hof_decoradores` | HOF y `@` (estilo FastAPI) |
| 15 | `modulos_ficheros_json` | módulos, archivos, JSON |
| 16 | `valor_referencia` | teoría |
| 17 | `librerias` | pip / paquetes (teoría) |
| 18 | `entornos_virtuales` | venv + requirements |
| 19 | `async_await` | async / await |
| 20 | `modelos_datos_pydantic` | dataclasses → Pydantic |

## Checklist pre-FastAPI

| Tema | Lección |
|------|---------|
| Variables y tipos | 01–05 |
| Listas / dict / tuplas / sets | 07, 11 |
| if / for / while | 06, 08, 09 |
| Funciones y módulos | 10, 15 |
| Errores | 13 |
| POO | 12 |
| Archivos y JSON | 15 |
| venv + pip | 18 (+ 17) |
| Decoradores | 14 |
| async / await | 19 |
| Pydantic | 20 |

## Integradores (cierre antes de FastAPI)

Cuando termines fundamentos (y idealmente fechas/regex si te interesan), cerrá con:

| # | Proyecto | Nivel | Qué integra |
|---|----------|-------|-------------|
| 01 | `integradores/01_agenda_contactos` | Fácil | menú, dict/list, JSON, funciones, try/except |
| 02 | `integradores/02_gestor_tareas` | Medio | POO, módulos, excepción propia, decorador |
| 03 | `integradores/03_mini_api_biblioteca` | Difícil | rutas con `@`, Pydantic, async (+ `tips.md`) |

Detalle en `Lecciones/integradores/README.md`.
