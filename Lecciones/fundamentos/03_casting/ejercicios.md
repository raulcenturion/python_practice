# Práctica extra — casting

Convertir de texto a número es explícito. int('42') funciona. int('42.0') no. Un monto con punto se parte en pesos y centavos para no usar float.

## Documentación

- [int](https://docs.python.org/3/library/functions.html#int)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 03 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. a_centavos

El texto es pesos con punto y dos decimales. Devolvé el entero en centavos.

Ejemplo: `a_centavos('12.50') → 1250`

Función a completar en `practica_extra.py`: `a_centavos`.

### 2. a_entero_seguro

Devolvé el int, o None si el texto no es un entero.

Ejemplo: `a_entero_seguro('42') → 42; a_entero_seguro('x') → None`

Función a completar en `practica_extra.py`: `a_entero_seguro`.

### 3. si_no

Aceptá 'si' o 'no' en cualquier mayúscula. Otro texto devuelve None.

Ejemplo: `si_no('SI') → True`

Función a completar en `practica_extra.py`: `si_no`.
