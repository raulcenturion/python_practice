# Práctica extra — el primer párrafo

La lección de Wikipedia baja una página. Este ejercicio hace la parte que se puede probar sin red: dado un HTML, el texto del primer <p>.

## Documentación

- [find](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r scraping/03 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. primer_parrafo

Texto del primer p, con strip. None si no hay.

Ejemplo: `primer_parrafo('<p> Hola </p>') → 'Hola'`

Función a completar en `practica_extra.py`: `from bs4 import BeautifulSoup


primer_parrafo`.
