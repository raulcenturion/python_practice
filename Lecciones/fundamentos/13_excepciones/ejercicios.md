# Práctica extra — excepciones

Una excepción corta el flujo cuando seguir sería un dato mentiroso. SaldoInsuficiente es una excepción propia: el que llama la distingue de un ValueError de un monto negativo.

## Documentación

- [errores](https://docs.python.org/3/tutorial/errors.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 13 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. extraer_o_fallar

Si monto <= 0, ValueError. Si monto > saldo, SaldoInsuficiente. Si no, devolvé el saldo nuevo.

Ejemplo: `extraer_o_fallar(100, 40) → 60`

Función a completar en `practica_extra.py`: `SaldoInsuficiente`.

### 2. mensaje_de

Si fn() termina bien, devolvé 'ok'. Si lanza SaldoInsuficiente, 'sin_saldo'. Si lanza ValueError, 'monto_invalido'.

Ejemplo: `mensaje_de(lambda: extraer_o_fallar(10, 40)) → 'sin_saldo'`

Función a completar en `practica_extra.py`: `mensaje_de`.
