# Práctica extra — fechas

date no tiene hora. El vencimiento de una tarjeta es un mes y un año: sigue vigente durante todo ese mes. Un día hábil, en este ejercicio, es lunes a viernes.

## Documentación

- [datetime](https://docs.python.org/3/library/datetime.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r fechas/01 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. vigente

True si (anio, mes) es posterior a hoy, o es el mismo mes.

Ejemplo: `vigente(2030, 1, date(2026, 5, 1)) es True`

Función a completar en `practica_extra.py`: `from datetime import date


vigente`.

### 2. es_habil

True de lunes a viernes.

Ejemplo: `un sábado es False`

Función a completar en `practica_extra.py`: `es_habil`.
