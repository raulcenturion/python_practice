# Práctica extra — armar una URL de búsqueda

Playwright abre un navegador. Esta práctica no lo abre: arma la URL que el script le pediría. Los espacios del término van como %20. La lección 05 sigue siendo el lugar para correr el navegador.

## Documentación

- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html)
- [Playwright Python](https://playwright.dev/python/docs/intro)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r scraping/05 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. url_busqueda

Devolvé https://ejemplo.test/buscar?q= con el término citado.

Ejemplo: `un espacio queda como %20`

Función a completar en `practica_extra.py`: `from urllib.parse import quote


url_busqueda`.
