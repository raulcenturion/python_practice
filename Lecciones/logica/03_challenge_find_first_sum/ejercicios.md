# Práctica extra — los dos más cercanos

Ya existe el primer par que suma un objetivo. Este pide otra cosa: de una lista de montos, los dos que más se acercan a una meta sin pasarse. Si ninguno entra, None.

## Documentación

- [orden](https://docs.python.org/3/howto/sorting.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r logica/03 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. mejor_par

Devolvé (a, b) con a <= b, a + b <= meta, y esa suma la más alta posible. None si no hay par.

Ejemplo: `mejor_par([3, 8, 5, 1], 10) → (1, 8) no, 5+3=8 y 1+8=9, gana (1, 8)`

Función a completar en `practica_extra.py`: `mejor_par`.
