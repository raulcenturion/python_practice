# Práctica extra — encontrar montos

re.findall devuelve todas las coincidencias. Un monto de este ejercicio es dígitos, un punto y dos dígitos.

## Documentación

- [re](https://docs.python.org/3/library/re.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r regex/01 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. montos

Lista de los textos que parecen un monto, en orden.

Ejemplo: `montos('pagué 10.50 y 2.00') → ['10.50', '2.00']`

Función a completar en `practica_extra.py`: `import re


montos`.
