# Práctica extra — contar encabezados

Un control de SEO mínimo cuenta cuántos h1 hay. Más de uno suele ser una página mal armada. Contá sobre el HTML recibido, sin abrir un archivo.

## Documentación

- [find_all](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r scraping/04 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. contar_h1

Cuántos h1 hay.

Ejemplo: `contar_h1('<h1>a</h1><h1>b</h1>') → 2`

Función a completar en `practica_extra.py`: `from bs4 import BeautifulSoup


contar_h1`.
