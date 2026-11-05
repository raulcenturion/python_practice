# Práctica extra — invertir un dict

Si cada valor aparece una sola vez, se puede dar vuelta: la clave pasa a ser el valor. Sirve para pasar de 'código → nombre' a 'nombre → código'.

## Documentación

- [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r logica/04 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. invertir

Devolvé un dict nuevo con claves y valores cambiados. Los valores son únicos.

Ejemplo: `invertir({'a': 1}) → {1: 'a'}`

Función a completar en `practica_extra.py`: `invertir`.

### 2. faltantes

Claves de pedido que no están en stock.

Ejemplo: `faltantes({'pan': 1}, {'pan': 2, 'leche': 1}) → ['leche']`

Función a completar en `practica_extra.py`: `faltantes`.
