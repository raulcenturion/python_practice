# Práctica extra — una tarjeta con vencimiento

La clase junta el número enmascarado y la fecha de vencimiento. Quien la usa pregunta esta_vigente(hoy) y no calcula el mes por su cuenta.

## Documentación

- [clases](https://docs.python.org/3/tutorial/classes.html)
- [date](https://docs.python.org/3/library/datetime.html#date-objects)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r fechas/03 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. Tarjeta

Guardá ultimos4, mes y anio. esta_vigente(hoy) usa la misma regla que vigente de la lección de dates.

Ejemplo: `una tarjeta 2030-12 está vigente en 2026`

Función a completar en `practica_extra.py`: `Tarjeta:
    __init__`.
