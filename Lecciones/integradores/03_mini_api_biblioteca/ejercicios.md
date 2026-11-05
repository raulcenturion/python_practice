# Práctica extra — normalizar una ruta

El integrador 03 imita rutas de FastAPI. Una ruta de este ejercicio empieza con /, no termina con / salvo que sea la raíz, y no trae espacios.

## Documentación

- [FastAPI path](https://fastapi.tiangolo.com/tutorial/path-params/)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r Lecciones/integradores/03_mini_api_biblioteca/practica_extra.py`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. normalizar_ruta

Poné una barra al principio si falta. Sacá la barra final si hay más path. No cambies '/'.

Ejemplo: `normalizar_ruta('libros/') → '/libros'`

Función a completar en `practica_extra.py`: `normalizar_ruta`.
