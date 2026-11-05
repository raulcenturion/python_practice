# Práctica extra — tareas de un día

Una tarea es un dict con titulo y vence ('AAAA-MM-DD'). Esta función deja las que vencen en esa fecha o antes y todavía no están hechas.

## Documentación

- [listas](https://docs.python.org/3/tutorial/datastructures.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r Lecciones/integradores/02_gestor_tareas/practica_extra.py`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. pendientes_hasta

Las no hechas con vence <= dia. Hecha es la clave hecha, un bool.

Ejemplo: `una hecha no entra`

Función a completar en `practica_extra.py`: `pendientes_hasta`.
