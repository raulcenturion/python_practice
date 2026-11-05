# Práctica extra — listas

Una lista guarda un orden. El último lugar es -1. Estas tres salen del mismo estilo que los catálogos de algoritmos, con datos de movimientos bancarios: rotar un extracto, la ventana de gastos más alta y quitar duplicados sin perder el orden.

## Documentación

- [listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 07 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. rotar

Devolvé una lista nueva con los últimos k elementos al frente. No modifiques la original.

Ejemplo: `rotar([1, 2, 3, 4], 1) → [4, 1, 2, 3]`

Función a completar en `practica_extra.py`: `rotar`.

### 2. ventana_maxima

La suma más alta de k elementos seguidos. k cabe en la lista.

Ejemplo: `ventana_maxima([1, 3, 2, 5], 2) → 7`

Función a completar en `practica_extra.py`: `ventana_maxima`.

### 3. unicos

Devolvé los valores una sola vez, en el orden de la primera aparición.

Ejemplo: `unicos([2, 1, 2, 3, 1]) → [2, 1, 3]`

Función a completar en `practica_extra.py`: `unicos`.
