# Regex — expresiones regulares en Python

Cuatro lecciones cortas. En cada carpeta:

| Archivo | Rol |
|---------|-----|
| `teoria.py` | Demos ejecutables + tips |
| `practica.py` | Ejercicios con stubs (`NotImplementedError`) |

## Orden

| # | Carpeta | Tema |
|---|---------|------|
| 01 | `01_re/` | `re.search`, `findall`, `finditer`, `IGNORECASE`, `sub`, Match |
| 02 | `02_metachars/` | `.`, escapes, `\d` `\w` `\s`, `^` `$`, `\b`, `\|` |
| 03 | `03_quantifiers/` | `*` `+` `?` `{n}` `{n,m}` `{n,}` |
| 04 | `04_sets/` | `[ ]`, rangos, `[^ ]`, demos username/email |

## Cómo correr

Desde la **raíz del repo** (`welcomePy/`), con el venv del proyecto si existe:

```bash
# Teoría (deben terminar con exit 0)
.venv/bin/python Lecciones/regex/01_re/teoria.py
.venv/bin/python Lecciones/regex/02_metachars/teoria.py
.venv/bin/python Lecciones/regex/03_quantifiers/teoria.py
.venv/bin/python Lecciones/regex/04_sets/teoria.py

# Práctica (stubs → mensaje "Pendiente" hasta que completes)
.venv/bin/python Lecciones/regex/01_re/practica.py
.venv/bin/python Lecciones/regex/02_metachars/practica.py
.venv/bin/python Lecciones/regex/03_quantifiers/practica.py
.venv/bin/python Lecciones/regex/04_sets/practica.py
```

Si no tenés `.venv`, usá `python3` en lugar de `.venv/bin/python`.

Atajo del repo (si estás en la carpeta de la lección):

```bash
./r teoria
./r practica
```

O desde la raíz, pasando la ruta al archivo:

```bash
./r Lecciones/regex/01_re/teoria.py
```

## Consejo

Usá siempre **raw strings** en patrones: `r"\d+"`, `r"\."`, `r"\bpalabra\b"`.
