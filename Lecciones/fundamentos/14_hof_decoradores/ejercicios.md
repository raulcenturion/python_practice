# Práctica extra — funciones de orden superior

Una función puede recibir otra. filter se queda con los que cumplen. Un decorador envuelve una función y le agrega un comportamiento, que es la idea de las rutas de FastAPI.

## Documentación

- [funciones](https://docs.python.org/3/glossary.html#term-decorator)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 14 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. mayores

Devolvé los montos estrictamente mayores que el piso, en el mismo orden.

Ejemplo: `mayores([100, 500, 200], 150) → [500, 200]`

Función a completar en `practica_extra.py`: `mayores`.

### 2. ordenar_por_monto

Lista de dicts ordenada por la clave 'monto', de menor a mayor. No modifiques la lista original: devolvé otra.

Ejemplo: `el de monto 10 queda primero`

Función a completar en `practica_extra.py`: `ordenar_por_monto`.

### 3. en_mayuscula

Devolvé cada texto en mayúscula, en el mismo orden.

Ejemplo: `en_mayuscula(['ana']) → ['ANA']`

Función a completar en `practica_extra.py`: `en_mayuscula`.
