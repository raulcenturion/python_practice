# Integradores — cierre del repo (antes de FastAPI)

## Orden recomendado

1. **Previo:** repaso guiado por ejercicio (`00_previo_repaso_fundamentos`)
2. **Repaso CLI:** mini presupuesto (`00_repaso_presupuesto_cli`)
3. Integradores 01 → 03

---

## 00 — Previo: repaso guiado de fundamentos

| Carpeta | Qué es |
|---------|--------|
| `00_previo_repaso_fundamentos/` | 1–2 ejercicios por tema (01–20) con guía + tip comentado |

Corré **un ejercicio por vez** (no tira todos juntos):

```bash
./r integradores/00 --list
./r integradores/00 01a
./r integradores/00 14b
./r integradores/00 20c
```

Si hay dos carpetas `00_*`, `./r integradores/00` apunta al **previo**.  
Para el presupuesto CLI:

```bash
./r integradores/00 presupuesto
# o
./r integradores/00_repaso_presupuesto
```

---

## Repaso intermedio (presupuesto CLI)

| # | Proyecto | Nivel | Carpeta |
|---|----------|-------|---------|
| 00 | Mini presupuesto CLI | Repaso 01→10 + 13 | `00_repaso_presupuesto_cli/` |

Hacelo **después** del previo si querés asentar la base en un proyecto chico.
El `enunciado.md` trae un **checklist por lección**. Todo el flujo es por terminal.

```bash
./r integradores/00 presupuesto
```

## Integradores de cierre

Hacé estos **en orden**. Cada uno suma temas; el último simula el estilo FastAPI.

| # | Proyecto | Nivel | Carpeta |
|---|----------|-------|---------|
| 01 | Agenda de contactos | Fácil | `01_agenda_contactos/` |
| 02 | Gestor de tareas | Medio | `02_gestor_tareas/` |
| 03 | Mini API biblioteca | Difícil (+ tips) | `03_mini_api_biblioteca/` |

## Cómo trabajar cada uno

1. Leé `enunciado.md`
2. Completá `practica.py` (y los módulos que pida el enunciado)
3. En el 03, usá `tips.md` solo si hace falta (de a un tip)

## Mapa rápido de temas

- **00 previo** → ejercicios sueltos 01–20 (incluye decoradores, ficheros/JSON, async, Pydantic)  
- **00 presupuesto** → print, tipos, casting, variables, input, if, listas, while, for, funciones, try/except  
- **01** → funciones, menú, dict/list, JSON, excepciones básicas  
- **02** → POO, módulos, excepción propia, decorador, JSON  
- **03** → decoradores tipo ruta, Pydantic, async/await (puente a FastAPI)
