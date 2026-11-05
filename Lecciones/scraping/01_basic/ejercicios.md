# Práctica extra — texto de un HTML mínimo

Antes de una librería, un HTML corto se puede leer como texto. Esta función busca el primer título entre <h1> y </h1>. No abre la red.

## Documentación

- [str.find](https://docs.python.org/3/library/stdtypes.html#str.find)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r scraping/01 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. primer_h1

Devolvé el texto del primer h1, sin los tags. Si no hay, None.

Ejemplo: `primer_h1('<h1>Hola</h1>') → 'Hola'`

Función a completar en `practica_extra.py`: `primer_h1`.
