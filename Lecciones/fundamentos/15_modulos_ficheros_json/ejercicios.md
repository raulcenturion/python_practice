# Práctica extra — archivos y JSON

json guarda una estructura. Un extracto es una lista de dicts. El archivo se abre, se usa y se cierra. pathlib arma la ruta sin pegar strings a mano.

## Documentación

- [json](https://docs.python.org/3/library/json.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 15 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. guardar_y_leer

Escribí la lista de movimientos como JSON en ruta y devolvé lo que leés de nuevo.

Ejemplo: `un movimiento de 100 vuelve igual`

Función a completar en `practica_extra.py`: `import json
from pathlib import Path


guardar_y_leer`.

### 2. total_json

Sumá la clave monto de cada dict.

Ejemplo: `total_json([{'monto': 10}, {'monto': 5}]) → 15`

Función a completar en `practica_extra.py`: `total_json`.
