# Práctica extra — enmascarar

\d es un dígito. A veces no hace falta una expresión: los últimos 4 caracteres alcanzan. El ejercicio pide dejar solo esos y reemplazar el resto por asteriscos, de un texto que ya son solo dígitos.

## Documentación

- [re](https://docs.python.org/3/library/re.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r regex/02 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. enmascarar

Si el texto tiene 4 dígitos o menos, devolvelo igual. Si tiene más, asteriscos y los últimos 4.

Ejemplo: `enmascarar('4242424242424242') termina en 4242`

Función a completar en `practica_extra.py`: `enmascarar`.

### 2. solo_digitos

True si el texto completo son dígitos y no está vacío.

Ejemplo: `solo_digitos('123') es True`

Función a completar en `practica_extra.py`: `import re


solo_digitos`.
