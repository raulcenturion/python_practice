# Práctica extra — HTTP sin red

Una llamada HTTP de verdad depende de otro servidor. Acá el ejercicio es leer el resultado: un dict con status y un cuerpo. 2xx es éxito. Así se prueba un cliente sin abrir la red. La lección de requests, cuando pega a una URL, hace este mismo análisis sobre la respuesta.

## Documentación

- [HTTP status](https://developer.mozilla.org/es/docs/Web/HTTP/Status)
- [requests](https://requests.readthedocs.io/en/latest/api/#requests.Response)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r fechas/02 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. es_exito

True si el status está entre 200 y 299.

Ejemplo: `es_exito(201) es True`

Función a completar en `practica_extra.py`: `es_exito`.

### 2. leer_saldo

respuesta es {'status': int, 'body': {'saldo': int}}. Si el status no es éxito, devolvé None. Si lo es, el saldo.

Ejemplo: `status 200 y saldo 10 → 10`

Función a completar en `practica_extra.py`: `leer_saldo`.
