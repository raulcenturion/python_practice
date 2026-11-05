# Práctica extra — racha de gastos

Dada una lista de montos, la racha es la suma seguida más alta. Un número negativo corta la racha anterior si conviene más empezar de nuevo. Es el mismo recorrido lineal que sumar pares, con una decisión en cada paso.

## Documentación

- [for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r logica/02 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. racha

La suma consecutiva más alta. La lista tiene al menos un número.

Ejemplo: `racha([1, -2, 3, 4]) → 7`

Función a completar en `practica_extra.py`: `racha`.
