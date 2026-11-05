# Práctica extra — biblioteca estándar

Una librería es código ya escrito. La estándar viene con Python: decimal, pathlib, statistics. Un paquete de pip se instala en el venv y se anota en requirements.txt. Para plata, Decimal no arrastra el error de 0.1 + 0.2.

## Documentación

- [decimal](https://docs.python.org/3/library/decimal.html)
- [pip](https://docs.python.org/3/installing/index.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 17 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. sumar_plata

Sumá textos decimales con Decimal y devolvé el resultado como texto, sin pasar por float.

Ejemplo: `sumar_plata(['0.10', '0.20']) → '0.30'`

Función a completar en `practica_extra.py`: `from decimal import Decimal


sumar_plata`.

### 2. sufijo

Devolvé el sufijo del nombre de archivo, incluyendo el punto.

Ejemplo: `sufijo('extracto.csv') → '.csv'`

Función a completar en `practica_extra.py`: `from pathlib import Path


sufijo`.
