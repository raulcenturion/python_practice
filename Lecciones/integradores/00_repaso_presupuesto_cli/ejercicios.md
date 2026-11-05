# Práctica extra — presupuesto

El CLI completo está en practica.py. Acá el cálculo, separado del input, para poder probarlo con una lista.

## Documentación

- [funciones](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r Lecciones/integradores/00_repaso_presupuesto_cli/practica_extra.py`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. balance

Ingresos menos egresos. Cada fila es ('ingreso', monto) o ('egreso', monto).

Ejemplo: `balance([('ingreso', 100), ('egreso', 40)]) → 60`

Función a completar en `practica_extra.py`: `balance`.
