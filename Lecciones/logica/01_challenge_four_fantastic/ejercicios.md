# Práctica extra — paréntesis

Un texto de grupos está balanceado si cada cierre corresponde al último que se abrió. Se resuelve con una pila: una lista donde append abre y pop cierra.

## Documentación

- [listas como pila](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r logica/01 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. balanceado

Solo paréntesis redondos. True si cierra todo y no sobra ninguno.

Ejemplo: `balanceado('(())') es True; balanceado('())') es False`

Función a completar en `practica_extra.py`: `balanceado`.
