# Práctica extra — while

while repite mientras una condición siga siendo cierta. Sirve cuando no sabés cuántas vueltas van a hacer falta: los dígitos de un monto, el resto de Euclides, o ir restando billetes.

## Documentación

- [while](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 08 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. cantidad_digitos

Cuántos dígitos tiene un entero positivo.

Ejemplo: `cantidad_digitos(1500) → 4`

Función a completar en `practica_extra.py`: `cantidad_digitos`.

### 2. mcd

Máximo común divisor con el algoritmo de Euclides.

Ejemplo: `mcd(12, 8) → 4`

Función a completar en `practica_extra.py`: `mcd`.

### 3. billetes

Devolvé cuántos billetes de 1000, 500 y 100 se necesitan, en ese orden, como tupla. El monto es múltiplo de 100.

Ejemplo: `billetes(1600) → (1, 1, 1)`

Función a completar en `practica_extra.py`: `billetes`.
