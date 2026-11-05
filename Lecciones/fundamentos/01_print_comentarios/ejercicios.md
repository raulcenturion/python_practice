# Práctica extra — print y comentarios

print muestra texto. Un comentario con # no se ejecuta: le explica a la persona que lee el archivo qué representa ese número o esa línea. En un ticket de banco el texto que ve el cliente se arma con datos, no se escribe fijo.

## Documentación

- [print](https://docs.python.org/3/library/functions.html#print)
- [f-strings](https://docs.python.org/3/tutorial/input.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 01 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. linea_ticket

Devolvé `concepto` y el monto separados por dos puntos y un espacio.

Ejemplo: `linea_ticket('Cafe', 800) → 'Cafe: 800'`

Función a completar en `practica_extra.py`: `linea_ticket`.

### 2. banner

Devolvé el título centrado con guiones a cada lado, ancho total 12. Si el título es más corto, rellená con `-`.

Ejemplo: `banner('OK') empieza y termina con `-``

Función a completar en `practica_extra.py`: `banner`.

### 3. resumen

Devolvé tres líneas unidas con salto de línea: comercio, cantidad de ítems y total.

Ejemplo: `resumen('Kiosco', 2, 1500)`

Función a completar en `practica_extra.py`: `resumen`.
