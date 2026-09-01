# Repaso práctico — Fundamentos (01–20)

Archivo para practicar **sin IA**: leé el enunciado, mirá el tip/ejemplo de patrón, y resolvé en un block de notas o archivo vacío.

**Cómo usarlo**
1. Elegí un módulo (o hacé 3–4 por sesión).
2. Leé: **Qué practicar** → **Enunciado** → **Guía** → **Tip**.
3. Escribí vos la solución (no mires `practica.py` hasta terminar).
4. Después compará con la práctica de esa carpeta o corré `./r NN`.

**Leyenda**
- **Qué practicar** = para qué sirve este ejercicio.
- **Guía** = qué implementar y en qué orden.
- **Tip / ejemplo de patrón** = idea o fragmento parecido (no es la solución completa).

---

## 01 — Print y comentarios

### Qué practicar
Mostrar texto en consola con control de separador y formato.

### Ejercicio A — Presentación
Creá variables `nombre`, `edad`, `pais`. Imprimilas en **una sola línea** con `sep=" | "`.  
Resultado esperado (ejemplo): `Raúl | 33 | Argentina`

**Guía**
1. Asigná las 3 variables.
2. Un solo `print` con los 3 valores.
3. Pasá `sep=" | "`.

**Tip / patrón**
```python
print("a", "b", "c", sep=" - ")  # a - b - c
```

### Ejercicio B — Recuadro
Imprimí un marco así:

```text
********************
*   Hola, Raúl!   *
********************
```

**Guía:** tres `print` (línea superior, centro, inferior). Podés armar el centro con f-string.

---

## 02 — Tipos de datos

### Qué practicar
Reconocer tipos y usar `type()`.

### Ejercicio A — Todos los tipos
Creá una variable de cada tipo: `str`, `int`, `float`, `bool`, `list`, `tuple`, `dict`, `set`.  
Imprimí el valor y su `type()`.

**Guía:** una variable por tipo → `print(variable, type(variable))`.

**Tip:** `set` usa `{}` con valores (sin pares clave:valor). Diccionario sí usa `clave: valor`.

### Ejercicio B — Dict personal
Creá un dict con `nombre`, `edad` y `hobbies` (lista).  
Imprimí `type` del dict y de cada valor.

**Cuándo:** cuando necesitás saber qué tipo tenés antes de operar (casting, métodos, etc.).

---

## 03 — Casting

### Qué practicar
Convertir tipos a propósito y entender side-effects (truncado, falsy, duplicados).

### Ejercicio A — Tupla → lista y set
Partí de `datos = (1, 2, 3, 3)`. Convertí a lista y a set.  
¿Qué diferencia ves?

**Guía:** `list(datos)` y `set(datos)`. Imprimí ambos.

**Tip:** el set **elimina duplicados** y no garantiza orden.

### Ejercicio B — Valores falsy
Probá `bool()` con: `0`, `""`, `[]`, `{}`, `None`, `0.0`, `()`, `set()`.  
Anotá cuáles dan `False`.

**Cuándo:** en `if` esas cosas se comportan como “vacío/falso”.

---

## 04 — Variables y operaciones

### Qué practicar
Reasignación, tipado fuerte y aritmética con `//` y `%`.

### Ejercicio A — Intercambio
`a = 5`, `b = 10`. Intercambialas **sin** tercera variable.

**Tip / patrón**
```python
a, b = b, a
```

### Ejercicio B — Descomponer segundos
Dado `3661` segundos, descomponé en horas, minutos y segundos con `//` y `%`.  
Esperado: `1h 1m 1s`.

**Guía**
1. Horas = total // 3600.
2. Resto = total % 3600.
3. Minutos = resto // 60.
4. Segundos = resto % 60.

**Cuándo:** cualquier “partir un número en unidades” (tiempo, cambio de moneda, etc.).

---

## 05 — Input y strings

### Qué practicar
Entrada de usuario + slicing. En notepad podés simular con variables fijas.

### Ejercicio A — Datos personales
Pedí (o simulá) nombre y edad. Imprimí: `Me llamo X y tengo Y años`.

**Guía:** `input` → edad con `int(...)` → f-string.

**Tip:** `input()` siempre es `str`. Si sumás edades sin cast → error o concatenación rara.

### Ejercicio B — Slicing
`texto = "Python es genial"`. Imprimí:
- primeros 6 caracteres
- últimos 6
- al revés
- `len(texto)`

**Patrón**
```python
s[:6]      # inicio
s[-6:]     # final
s[::-1]    # reverso
```

---

## 06 — Condicionales y booleanos

### Qué practicar
Decisiones con `if/elif/else` y operadores lógicos.

### Ejercicio A — Año bisiesto
Dado un año, decí si es bisiesto.  
Regla: divisible por 4, **no** por 100, **salvo** que sea divisible por 400.

**Guía:** armá la condición con `%` + `and`/`or`. Probá con 2000, 1900, 2024.

**Tip / patrón**
```python
if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    ...
```

### Ejercicio B — Mini calculadora
Dos números + operación `+ - * /`. Si dividen por 0, mensaje de error (sin romper).

**Cuándo:** validar casos especiales **antes** de operar.

---

## 07 — Listas

### Qué practicar
Slicing avanzado y mutabilidad (copia vs alias).

### Ejercicio A — Reversa parcial
`[1, 2, 3, 4, 5, 6]` → invertí **solo la primera mitad** → `[3, 2, 1, 4, 5, 6]`.

**Guía**
1. Mitad = `len(lista) // 2`.
2. Primera mitad invertida + segunda mitad intacta.
3. Concatená.

**Patrón**
```python
mitad = len(nums) // 2
nueva = nums[:mitad][::-1] + nums[mitad:]
```

### Ejercicio B — Copia vs referencia
`original = [1, 2, 3]`.  
Creá: `copia_1 = original[:]`, `copia_2 = original.copy()`, `referencia = original`.  
Cambiá `referencia[0] = 10`. Imprimí las 4. ¿Qué cambió?

**Cuándo:** siempre que pases listas a funciones o “copies” sin querer compartir el mismo objeto.

---

## 08 — While

### Qué practicar
Repetir **mientras** una condición sea verdadera.

### Ejercicio A — Validar contraseña
Pedí una contraseña. Seguí pidiendo hasta que tenga **≥ 8** caracteres.  
Cuando sea válida: `"Contraseña válida"`.

**Guía**
1. Pedí la primera vez.
2. `while len(clave) < 8:` pedí de nuevo.
3. Fuera del while, mensaje OK.

**Tip:** el contador/condición **debe cambiar** dentro del loop (si no → infinito).

### Ejercicio B — Factorial
Con `while`, calculá `n!` (ej. `5! = 120`).

**Guía:** acumulador `resultado = 1`; mientras `n > 1` multiplicá y restá 1.  
Cuidado: guardá el `n` original si lo necesitás imprimir después.

---

## 09 — For y rangos

### Qué practicar
Recorrer con `for` y algoritmos simples (sin helpers mágicos).

### Ejercicio A — Máximo sin `max()`
`numeros = [15, 5, 25, 10, 20]`. Encontrá el máximo con `for`.

**Guía**
1. Arrancá asumiendo que el primero es el máximo.
2. Compará el resto uno por uno.
3. Si hay uno mayor, actualizá.

**Patrón**
```python
mayor = numeros[0]
for n in numeros[1:]:
    if n > mayor:
        mayor = n
```

### Ejercicio B — Filtrar con comprehension
`palabras = ["casa", "arbol", "sol", "elefante", "luna"]`  
Nueva lista solo con palabras de **más de 4** letras.

**Tip:** `[p for p in palabras if len(p) > 4]`

---

## 10 — Funciones

### Qué practicar
Encapsular lógica, retornos múltiples y `*args`.

### Ejercicio A — `estadisticas(lista)`
Función que reciba una lista de números y retorne una **tupla** `(minimo, maximo, promedio)`.

**Guía**
1. `def estadisticas(lista):`
2. Calculá los 3 valores.
3. `return minimo, maximo, promedio`
4. Probá: `print(estadisticas([10, 20, 30]))`

**Cuándo:** cuando una función debe devolver **varios** resultados juntos.

### Ejercicio B — `sumar_todos(*args)`
Sume todos los argumentos: `sumar_todos(1, 2, 3, 4) → 10`.

**Tip:** `*args` llega como tupla. Podés usar `sum(args)`.

---

## 11 — Diccionarios, tuplas y sets

### Qué practicar
CRUD de dict y operaciones de conjuntos.

### Ejercicio A — CRUD dict
Creá dict con `nombre`, `edad`, `email`.  
Agregá `pais`. Modificá `edad`. Eliminá `email` con `pop()`. Imprimí.

**Guía**
- Crear: `d = {...}`
- Agregar/modificar: `d["clave"] = valor`
- Borrar: `d.pop("email")`

### Ejercicio B — Sets
`a = {1, 2, 3, 4}`, `b = {3, 4, 5, 6}`  
Imprimí: unión `|`, intersección `&`, diferencia `-`.

**Cuándo:** unir/cruzar colecciones de IDs, tags, etc. sin duplicados.

---

## 12 — Clases y POO

### Qué practicar
Modelar con clases, instancias y herencia.

### Ejercicio A — Clase `Persona`
Atributos `nombre`, `edad`. Método `presentarse()` → `"Soy X, tengo Y años"`.  
Creá 2 instancias y probá.

**Guía**
1. `class Persona:`
2. `__init__(self, nombre, edad)` guarda en `self.`
3. Método usa `self.nombre` / `self.edad`.
4. Instanciá: `p = Persona("Ana", 20)` → `p.presentarse()`

### Ejercicio B — Herencia
`Vehiculo(marca, modelo)`.  
`Auto` hereda y agrega `puertas`. Creá un `Auto` y mostrá todos los atributos.

**Tip / patrón**
```python
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
```

---

## 13 — Excepciones

### Qué practicar
Capturar errores esperados y lanzar los propios.

### Ejercicio A — Conversión segura
Pedí un número. Si el usuario pone texto, capturá `ValueError` y mostrá `"Ingresá un número válido"`.

**Guía**
```python
try:
    n = int(...)
except ValueError:
    print("...")
```

**Cuándo:** cuando el cast puede fallar (input, archivos, APIs).

### Ejercicio B — Excepción personalizada
Creá `class EdadInvalidaError(Exception): ...`  
`validar_edad(edad)` lanza esa excepción si `edad < 0`. Probá con try/except.

**Tip:** las excepciones propias **heredan** de `Exception`.

---

## 14 — HOF y decoradores

### Qué practicar
Transformar colecciones y envolver funciones.

### Ejercicio A — `filter`
Lista 1..20. Quedate solo con divisibles por 3. Convertí a `list`.

**Patrón**
```python
list(filter(lambda x: x % 3 == 0, range(1, 21)))
```

### Ejercicio B — Decorador `@log`
Decorador que imprima el nombre de la función **antes** de ejecutarla.  
Aplicalo a `saludar(nombre)`.

**Guía**
1. `def log(func):`
2. Dentro, `def wrapper(*args, **kwargs):` → print → `return func(...)`
3. `return wrapper`
4. `@log` arriba de `saludar`

**Cuándo:** logging, auth, timing — sin tocar el cuerpo de la función original.

---

## 15 — Módulos, ficheros y JSON

### Qué practicar
Persistir datos (archivo + JSON).

### Ejercicio A — Escribir y leer
Escribí 3 líneas en `notas.txt` (modo `"w"`). Después leélas e imprimí cada una.

**Guía:** preferí `with open(...) as f:`. Primero escribir, después abrir en `"r"`.

### Ejercicio B — Dict → JSON
Dict con tus datos → `json.dumps(...)` (ver string) y `json.dump(...)` a `perfil.json`.

**Tip**
```python
import json
with open("perfil.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

**Cuándo:** guardar configs, perfiles, respuestas de API.

---

## 16 — Valor vs referencia *(sin practica.py oficial)*

### Qué practicar
Entender alias vs copia (complementa el ej. de listas).

### Ejercicio A — Mutables
```python
a = [1, 2]
b = a
a.append(3)
```
¿Qué imprime `b`? ¿Por qué?

### Ejercicio B — Copia superficial
Usá `.copy()` (o `[:]`). Modificá la copia. ¿La original cambia?

**Guía:** imprimí también `id(a)` e `id(b)` para ver si es el mismo objeto.

**Tip:** para listas de listas anidadas hace falta `copy.deepcopy`.

---

## 17 — Librerías *(sin practica.py oficial)*

### Qué practicar
Instalar y fijar dependencias (mental + terminal).

### Ejercicio A — Checklist pip
Anotá (y si podés, ejecutá) el orden:
1. `pip install requests`
2. `pip list`
3. `pip freeze > requirements.txt`

### Ejercicio B — Import defensivo
Escribí un snippet que intente `import requests` y, si falta, imprima `"Instalá requests"`.

**Patrón**
```python
try:
    import requests
except ImportError:
    print("Instalá requests")
```

---

## 18 — Entornos virtuales

### Qué practicar
Aislar dependencias + detectar venv desde código.

### Ejercicio A — Comandos (checklist)
Anotá el flujo: crear `.venv` → activar → `pip install` → `pip freeze > requirements.txt`.

### Ejercicio B — `corriendo_en_venv()`
Función que retorne `True` si el script corre dentro de un venv.  
Imprimí también `sys.executable`.

**Guía / tip**
```python
import sys
return sys.prefix != getattr(sys, "base_prefix", sys.prefix)
```

**Cuándo:** scripts de setup, checks de entorno, docs del proyecto.

---

## 19 — Async / await

### Qué practicar
Corutinas y concurrencia I/O.

### Ejercicio A — Primera corutina
`async def ping()`: espera `0.2s` con `asyncio.sleep` y retorna `"pong"`.  
Ejecutá con `asyncio.run(ping())`.

**Guía:** `async def` → `await` adentro → `asyncio.run(...)` afuera.

### Ejercicio B — Secuencial vs `gather`
`trabajo(nombre, segundos)` duerme y retorna el nombre.  
Compará 2 awaits seguidos vs `asyncio.gather(...)`. Medí con `time.perf_counter()`.

**Cuándo:** varias llamadas de red/DB que pueden ir en paralelo.

**Tip:** `gather` debería ser ~más rápido que lo secuencial si ambas esperas son I/O.

---

## 20 — Pydantic

### Qué practicar
Modelar y validar datos (estilo API).

### Ejercicio A — `BaseModel`
`class Libro(BaseModel)` con `titulo: str`, `anio: int`, `leido: bool = False`.  
Creá instancia y mostrá `model_dump()`.

### Ejercicio B — Desde dict (body)
```python
payload = {"titulo": "Dune", "anio": "1965", "leido": False}
```
Usá `Libro.model_validate(payload)` e imprimí el modelo.  
Observá la coerción `"1965"` → `int`.

**Guía**
1. Definir el modelo.
2. Validar el payload.
3. Si falla, capturar `ValidationError` (opcional pero útil).

**Cuándo:** entrada de usuario/API antes de tocar la lógica de negocio.

---

## Rutina sugerida (1 semana)

| Día | Módulos | Foco |
|-----|---------|------|
| 1 | 01–05 | Bases + casting + input |
| 2 | 06–09 | Control de flujo |
| 3 | 10–12 | Funciones + colecciones + clases |
| 4 | 13–15 | Errores + HOF + archivos/JSON |
| 5 | 16–20 | Referencias + entorno + async + Pydantic |

Si un ejercicio te traba más de 15–20 min: mirá solo el **Tip** otra vez; si sigue, abrí `teoria.py` de esa carpeta; recién al final mirá `practica.py`.
