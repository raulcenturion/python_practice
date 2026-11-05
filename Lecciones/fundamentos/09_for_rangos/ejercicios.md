# Práctica extra — for y range

for recorre algo que ya tiene tamaño. range(inicio, fin, paso) no incluye el fin. enumerate da el índice. zip junta dos listas del mismo largo.

## Documentación

- [for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 09 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. indices_pares

Devolvé los elementos que están en índice par: 0, 2, 4...

Ejemplo: `indices_pares(['a', 'b', 'c', 'd']) → ['a', 'c']`

Función a completar en `practica_extra.py`: `indices_pares`.

### 2. tabla

Devolvé las 10 filas 'n x i = r' para i de 1 a 10.

Ejemplo: `tabla(2)[0] → '2 x 1 = 2'`

Función a completar en `practica_extra.py`: `tabla`.

### 3. sumar_pares

Sumá elemento a elemento dos listas del mismo largo.

Ejemplo: `sumar_pares([1, 2], [10, 20]) → [11, 22]`

Función a completar en `practica_extra.py`: `sumar_pares`.
