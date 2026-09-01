# Guía rápida — Fundamentos (módulos 01–20)

Ayuda memoria para repasar en minutos. Por cada unidad: **qué es**, **ideas clave** y **un ejemplo mínimo**.

**Mapa mental:** sintaxis (01–05) → control de flujo (06–09) → abstracción (10–14) → I/O y proyecto (15–18) → async + modelos (19–20).

---

## 01 — Print y comentarios

**Qué es:** mostrar texto en consola y documentar el código.

**Recordá:** `#` comentario de línea · `"""..."""` varias líneas · `print(..., sep=..., end=...)`.

```python
print("Hola", "Python", sep="-")  # Hola-Python
print("misma", end=" ")
print("línea")                    # misma línea
```

---

## 02 — Tipos de datos

**Qué es:** cada valor tiene un tipo (`type()` lo revela).

**Recordá:** `int` `float` `str` `bool` `None` · colecciones `list` `tuple` `dict` `set` · f-strings · `/` `//` `%`.

```python
nombre = "Raúl"
print(f"{nombre}: {type(nombre)}")
print(17 // 5, 17 % 5)  # 3  2
```

---

## 03 — Casting

**Qué es:** convertir de un tipo a otro a propósito.

**Recordá:** `int()` `float()` `str()` `bool()` · `int(3.9)` trunca (queda `3`) · `""` `0` `None` → `False`.

```python
edad = int("25")
print(int(3.9), bool(""), set([1, 2, 2]))  # 3, False, {1, 2}
```

---

## 04 — Variables

**Qué es:** nombre que apunta a un valor (tipado dinámico).

**Recordá:** se puede reasignar · tipado fuerte (no mezclar sin cast) · `snake_case` · `MAYUSCULAS` = “constante” por convención.

```python
nombre = "Juan"
edad = 30
nombre = "María"
print(f"{nombre} tiene {edad}")
```

---

## 05 — Input

**Qué es:** leer datos del usuario por teclado.

**Recordá:** `input()` **siempre** devuelve `str` → castear si necesitás número.

```python
nombre = input("Nombre: ")
edad = int(input("Edad: "))
print(f"Hola {nombre}, {edad} años")
```

---

## 06 — Condicionales y booleanos

**Qué es:** decidir qué camino ejecutar según una condición.

**Recordá:** `True`/`False` · `and` `or` `not` · `if`/`elif`/`else` · falsy: `0` `""` `[]` `{}` `None`.

```python
edad = 20
if edad < 18:
    print("menor")
elif edad == 18:
    print("justo 18")
else:
    print("mayor")
```

---

## 07 — Listas

**Qué es:** colección **ordenada** y **mutable**.

**Recordá:** índices `0` / `-1` · `append` `insert` `remove` · `sort` vs `sorted` · slicing `[inicio:fin:paso]`.

```python
nums = [3, 1, 2]
nums.append(4)
print(nums[0], nums[-1], nums[::-1])
print(sorted(nums))  # no modifica nums
```

---

## 08 — While

**Qué es:** repetir **mientras** la condición sea `True`.

**Recordá:** `break` sale · `continue` salta esa vuelta · `else` del while solo si terminó **sin** `break`.

```python
n = 1
while n <= 5:
    if n == 3:
        n += 1
        continue
    print(n)
    n += 1
```

---

## 09 — For y rangos

**Qué es:** recorrer un iterable una vez por elemento.

**Recordá:** `for x in iterable` · `range(inicio, fin, paso)` (fin exclusivo) · `enumerate` · `break`/`continue`.

```python
for i in range(1, 6, 2):
    print(i)  # 1, 3, 5
for fruta in ["manzana", "pera"]:
    print(fruta)
```

---

## 10 — Funciones

**Qué es:** empaquetar lógica reutilizable.

**Recordá:** `def` + `return` · parámetros por defecto · `*args` / `**kwargs` · `lambda` · docstring.

```python
def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"

def suma(*args):
    return sum(args)

print(saludar("Ana"), suma(1, 2, 3))
```

---

## 11 — Diccionarios, tuplas y sets

**Qué es:** tres colecciones con reglas distintas.

| Tipo | Idea | Mutable |
|------|------|---------|
| `dict` | clave → valor | sí |
| `tuple` | secuencia fija | no |
| `set` | valores únicos | sí |

```python
user = {"name": "Raúl", "age": 33}
punto = (10, 20)
tags = {"py", "py", "api"}  # {'py', 'api'}
print(user.get("email", "n/a"), punto, tags)
```

---

## 12 — Clases y POO

**Qué es:** modelar cosas del mundo real con plantillas (clases) e instancias.

**Recordá:** `__init__` + `self` · herencia + `super()` · `@classmethod` / `@staticmethod` · encapsulamiento.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, {self.nombre}"

print(Persona("Ana").saludar())
```

---

## 13 — Excepciones

**Qué es:** manejar errores sin que el programa se caiga a ciegas.

**Recordá:** `try`/`except`/`else`/`finally` · `raise` · `except (A, B)` · excepciones propias · `assert`.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("división por cero")
finally:
    print("siempre corre")
```

---

## 14 — HOF y decoradores

**Qué es:** funciones que reciben/devuelven funciones; decoradores las envuelven.

**Recordá:** `map` `filter` `sorted(key=…)` · closures · `@decorador` encima de `def`.

```python
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

def log(f):
    def wrap(*a):
        print("llamada")
        return f(*a)
    return wrap

@log
def sumar(a, b):
    return a + b
```

---

## 15 — Módulos, ficheros y JSON

**Qué es:** organizar código, leer/escribir archivos y serializar datos.

**Recordá:** `import` / `from` / `as` · `with open(...)` · `json.dumps`/`loads` (str) · `dump`/`load` (archivo).

```python
import json

data = {"nombre": "Raúl", "edad": 35}
texto = json.dumps(data, indent=2)
print(json.loads(texto)["nombre"])
```

---

## 16 — Valor vs referencia

**Qué es:** entender qué se copia y qué se comparte al asignar.

**Recordá:** inmutables (`int` `str` `tuple`) → nueva referencia · mutables (`list` `dict` `set`) → alias · `copy` vs `deepcopy`.

```python
a = [1, 2]
b = a          # misma lista
a.append(3)    # b también cambia
c = a.copy()   # copia superficial (lista plana)
```

---

## 17 — Librerías

**Qué es:** usar código de terceros (y de la stdlib).

**Recordá:** `pip install` · `requirements.txt` · módulo ≠ paquete ≠ librería.

```python
# Terminal: pip install requests
import requests

r = requests.get("https://httpbin.org/get")
print(r.status_code)
```

---

## 18 — Entornos virtuales

**Qué es:** aislar las dependencias de cada proyecto.

**Recordá:** `python3 -m venv .venv` · `source .venv/bin/activate` · versionar `requirements.txt`, **no** `.venv/`.

```python
import sys

en_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
print("¿venv?", en_venv, sys.executable)
```

---

## 19 — Async / await

**Qué es:** concurrencia para I/O sin bloquear (red, disco, DB).

**Recordá:** `async def` · `await` · `asyncio.run()` · `asyncio.gather()` · no es magia para CPU pesada.

```python
import asyncio

async def tarea(n):
    await asyncio.sleep(0.1)
    return n

async def main():
    print(await asyncio.gather(tarea(1), tarea(2)))

asyncio.run(main())
```

---

## 20 — Modelos de datos (Pydantic)

**Qué es:** validar y tipar datos en runtime (puente a FastAPI).

**Recordá:** `BaseModel` · `Field` · coerción · `ValidationError` · `model_dump` / `model_validate`.

```python
from pydantic import BaseModel, Field

class Usuario(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(ge=0)

u = Usuario(nombre="Raúl", edad="35")  # "35" → int
print(u.model_dump())
```

---

## Cómo usarla

1. Leé solo el título + “Recordá” de cada módulo (barrido de 5–10 min).
2. Si no te suena, mirá el ejemplo y después abrí `teoria.py` / `practica.py` de esa carpeta.
3. Corré la práctica con `./r NN` (ej. `./r 13`).
