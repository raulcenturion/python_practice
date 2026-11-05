# Práctica extra — dict, tupla y set

Un dict busca por clave en un paso. Una tupla no se modifica: sirve para una coordenada o un par (índice, índice). Un set guarda únicos y pierde el orden.

## Documentación

- [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [set](https://docs.python.org/3/tutorial/datastructures.html#sets)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 11 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. frecuencia

Dict con cuántas veces aparece cada valor.

Ejemplo: `frecuencia(['a', 'b', 'a']) → {'a': 2, 'b': 1}`

Función a completar en `practica_extra.py`: `frecuencia`.

### 2. primer_par

Índices i < j del primer par que suma meta, recorriendo desde la izquierda. Si no hay, None. Un dict recuerda el índice de cada número ya visto.

Ejemplo: `primer_par([2, 7, 11, 15], 9) → (0, 1)`

Función a completar en `practica_extra.py`: `primer_par`.

### 3. comunes

Lista ordenada de los números que están en las dos listas.

Ejemplo: `comunes([1, 2, 2], [2, 3]) → [2]`

Función a completar en `practica_extra.py`: `comunes`.
