# Práctica extra — Pydantic

Un modelo declara la forma del dato y la valida al construirlo. Si el monto no es int, o no es positivo, Pydantic tira ValidationError y el endpoint de FastAPI responde 422 sin llegar a la base. Es el mismo papel que UserCreate en Devinote.

## Documentación

- [modelos](https://docs.pydantic.dev/latest/concepts/models/)
- [Field](https://docs.pydantic.dev/latest/concepts/fields/)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 20 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. Movimiento

Modelo con concepto: str y monto_centavos: int mayor que 0. como_dict devuelve concepto y monto_centavos.

Ejemplo: `Movimiento(concepto='pan', monto_centavos=100)`

Función a completar en `practica_extra.py`: `from pydantic import BaseModel, Field


Movimiento`.
