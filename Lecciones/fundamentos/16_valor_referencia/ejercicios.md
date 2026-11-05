# Práctica extra — valor y referencia

Un int se reasigna y el nombre viejo sigue igual. Una lista es un objeto: dos nombres pueden apuntar al mismo. Si una función hace append sobre la lista que le pasaron, el que llamó ve el cambio. Para no tocarla, se copia.

## Documentación

- [objetos](https://docs.python.org/3/library/copy.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 16 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. duplicar

Devolvé una lista nueva con los elementos repetidos dos veces. La original queda igual.

Ejemplo: `duplicar([1, 2]) → [1, 2, 1, 2]`

Función a completar en `practica_extra.py`: `duplicar`.

### 2. anotar_copia

Devolvé una lista nueva con el texto agregado al final. No uses append sobre la lista recibida.

Ejemplo: `anotar_copia(['a'], 'b') → ['a', 'b']`

Función a completar en `practica_extra.py`: `anotar_copia`.
