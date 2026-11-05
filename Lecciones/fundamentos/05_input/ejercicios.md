# Práctica extra — input

input() frena el programa hasta que alguien escribe. Estas funciones reciben el texto ya leído, para poder probarlas sin el teclado. Es el mismo trabajo: cortar la línea y validar.

## Documentación

- [input](https://docs.python.org/3/library/functions.html#input)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 05 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. parsear_alta

La línea es 'nombre,centavos'. Devolvé un dict con esas claves. El monto es int.

Ejemplo: `parsear_alta('Ana,1500')`

Función a completar en `practica_extra.py`: `parsear_alta`.

### 2. opcion_menu

1 es consultar, 2 es extraer, 3 es salir. Otro texto devuelve 'invalida'.

Ejemplo: `opcion_menu('2') → 'extraer'`

Función a completar en `practica_extra.py`: `opcion_menu`.

### 3. confirmar

True si el texto, sin espacios y en minúscula, es 's' o 'si'.

Ejemplo: `confirmar(' S ') es True`

Función a completar en `practica_extra.py`: `confirmar`.
