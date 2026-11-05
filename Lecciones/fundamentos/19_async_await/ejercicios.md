# Práctica extra — async y await

async def define una corrutina. No corre hasta que alguien la espera. await cede el control mientras esa espera dura. asyncio.gather lanza varias y espera a todas. En FastAPI, await aparece cuando hay una espera real: otra API, un archivo, un socket.

## Documentación

- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [FastAPI async](https://fastapi.tiangolo.com/async/)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 19 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. sumar_esperas

dos_veces espera y devuelve n * 2. sumar_esperas lanza dos_veces(a) y dos_veces(b) juntas y devuelve la suma de los dos resultados.

Ejemplo: `asyncio.run(sumar_esperas(2, 3)) → 10`

Función a completar en `practica_extra.py`: `import asyncio


async dos_veces`.
