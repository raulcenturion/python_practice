# Práctica extra — clases

Una clase junta datos y operaciones. Cuenta es el objeto: el saldo vive adentro y depositar cambia ese objeto. El que llama no toca el número suelto.

## Documentación

- [clases](https://docs.python.org/3/tutorial/classes.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 12 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. Cuenta

titular y saldo. depositar suma. extraer resta si hay saldo y devuelve True. Si no alcanza, no cambia el saldo y devuelve False.

Ejemplo: `Cuenta('Ana', 100).depositar(50) deja saldo 150`

Función a completar en `practica_extra.py`: `Cuenta:
    __init__`.
