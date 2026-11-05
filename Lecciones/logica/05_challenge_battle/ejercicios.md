# Práctica extra — mejor de tres

Cada ronda suma puntos. Gana quien llegue a 2. Si se acaban las rondas empatados, es empate. No es el duelo con carry de la práctica principal: acá cada ronda es un punto cerrado.

## Documentación

- [comparar](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r logica/05 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. mejor_de

rondas es una lista de 'a' o 'b'. Devolvé 'a', 'b' o 'empate'. Gana el primero que llega a ganar. Si no, el que tenga más. Si igualan, empate.

Ejemplo: `mejor_de(['a', 'a', 'b']) → 'a'`

Función a completar en `practica_extra.py`: `mejor_de`.
