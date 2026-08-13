# Integrador de repaso — Mini presupuesto CLI

Repaso **intermedio** de fundamentos (lecciones **01 → 10** + **13**).  
Es **aparte** de los integradores 01/02/03 (agenda, tareas, mini API).

## Objetivo

Una app de **terminal** para anotar gastos del día.  
El usuario interactúa con `input()`; vos aplicás **todo lo visto** en esas lecciones.

## Cómo correrlo

```bash
./r integradores/00
# o
python Lecciones/integradores/00_repaso_presupuesto_cli/practica.py
```

## Menú (todo por terminal)

1. Agregar gasto  
2. Listar gastos  
3. Total, promedio y estadísticas  
4. Buscar gastos por palabra  
5. Eliminar gasto por número de lista  
6. Activar / desactivar “modo ahorro” (flag bool)  
7. Salir  

---

## Checklist por lección (tiene que aparecer en tu código)

### 01 — print / comentarios
- [ ] Comentarios `#` explicando partes
- [ ] `print` con **varios argumentos**
- [ ] Al menos un `print(..., sep="...")`
- [ ] Al menos un `print(..., end="...")`
- [ ] Mensajes con **f-strings**

### 02 — tipos de datos
- [ ] Usás `str` (nombre), `float` (monto), `bool` (modo ahorro), `list` (gastos)
- [ ] Mostrás el tipo de algo con `type(...)` (ej. en el resumen)

### 03 — casting
- [ ] `float(...)` para montos
- [ ] `int(...)` para opción de menú e índice a eliminar
- [ ] `str(...)` si necesitás mostrar un número como texto

### 04 — variables y operaciones
- [ ] Variables claras: `total`, `promedio`, `cantidad`, etc.
- [ ] Operaciones: `+` (suma), `/` (promedio)
- [ ] Al menos una de: `//`, `%` o `**` (ej. “mitad del total” con `/2` o `total // 2`, o “resto de dividir cantidad en grupos de 3” con `%`)

### 05 — input / strings
- [ ] `input()` en menú, nombre, monto, búsqueda, índice
- [ ] `.strip()` al leer
- [ ] `.title()` o `.capitalize()` en el nombre del gasto
- [ ] `.lower()` para buscar sin importar mayúsculas

### 06 — condicionales / booleanos
- [ ] `if` / `elif` / `else` en el menú
- [ ] Comparaciones (`==`, `>`, `<=`, etc.)
- [ ] Al menos un `and` / `or` / `not` (ej. validar monto > 0 **y** nombre no vacío)
- [ ] Uso de un `bool` (`modo_ahorro`) para cambiar un mensaje o regla

### 07 — listas
- [ ] Lista de gastos (`append` al agregar)
- [ ] `len(lista)`
- [ ] Acceso por índice
- [ ] `pop` o `del` al eliminar

### 08 — while
- [ ] `while True` para el menú
- [ ] `break` al salir
- [ ] `continue` si la opción es inválida (vuelve al menú sin hacer nada más)

### 09 — for / range
- [ ] `for` para recorrer gastos
- [ ] `enumerate(...)` al listar (numeración 1, 2, 3…)
- [ ] Al menos un `range(...)` (ej. imprimir una línea separadora, o recorrer índices)

### 10 — funciones
- [ ] Varias funciones con `def`
- [ ] Parámetros y `return` donde corresponda
- [ ] Al menos **un parámetro con valor por defecto** (ej. `mostrar_menu(titulo="Menú")`)
- [ ] Docstrings cortos en las funciones

### 13 — excepciones
- [ ] `try` / `except ValueError` al convertir monto u opción
- [ ] `try` / `except IndexError` (o validación + mensaje) al eliminar
- [ ] Ideal: `else` y/o `finally` en **una** lectura (ej. pedir monto)

---

## Reglas del dominio

- Cada gasto: `nombre` (str) + `monto` (float **> 0**).  
- Guardá en una **lista** de tuplas `(nombre, monto)` o listas `[nombre, monto]`.  
- Monto inválido o ≤ 0 → mensaje claro, **sin romper** el programa.  
- Sin gastos → listar / total / buscar / eliminar avisan con mensaje amable.  
- `modo_ahorro` (bool): si está activo, en el resumen mostrás un tip extra (ej. “intentá gastar menos de la mitad del total”).

## Criterios de aceptación

- [ ] Todo el flujo es por terminal (`input` / `print`)
- [ ] El menú se repite hasta Salir
- [ ] Se pueden agregar, listar, buscar y eliminar gastos
- [ ] Total / promedio / alguna estadística con operaciones de la lección 04
- [ ] Inputs inválidos no tiran el programa
- [ ] El checklist de **cada lección** queda cubierto en `practica.py`

## Dónde trabajar

Completá `practica.py` en esta misma carpeta.  
Cada función tiene comentarios `# --- Lección XX ---` con lo que debe practicar.
