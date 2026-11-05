# Práctica extra — variables

Una variable es un nombre pegado a un valor. Reasignar crea otro valor si es un número. La comisión de un cajero puede ser un nombre en mayúsculas para recordar que no se cambia.

## Documentación

- [naming](https://peps.python.org/pep-0008/#naming-conventions)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 04 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. aplicar

Sumá delta al saldo y devolvé el saldo nuevo. No uses una variable global.

Ejemplo: `aplicar(1000, -200) → 800`

Función a completar en `practica_extra.py`: `aplicar`.

### 2. intercambiar

Devolvé la tupla (b, a).

Ejemplo: `intercambiar(1, 2) → (2, 1)`

Función a completar en `practica_extra.py`: `intercambiar`.

### 3. con_comision

Restá el 1% entero del monto (división entera) y devolvé lo que queda. 1000 → 990.

Ejemplo: `con_comision(1000) → 990`

Función a completar en `practica_extra.py`: `con_comision`.
