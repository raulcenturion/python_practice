# Práctica extra — condiciones

if elige un camino. El orden importa: una tarjeta bloqueada no se evalúa como activa. and, or y not combinan condiciones.

## Documentación

- [if](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 06 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. estado_tarjeta

Si bloqueada, 'bloqueada'. Si no, si vencida, 'vencida'. Si no, si activa, 'activa'. Si no, 'inactiva'.

Ejemplo: `estado_tarjeta(True, True, True) → 'bloqueada'`

Función a completar en `practica_extra.py`: `estado_tarjeta`.

### 2. puede_comprar

True si la tarjeta está activa, el monto es positivo y saldo+límite cubre el monto. El límite es el descubierto permitido, en centavos.

Ejemplo: `puede_comprar(100, 150, 100, True) es True`

Función a completar en `practica_extra.py`: `puede_comprar`.

### 3. categoria

Menos de 1 año: 'nuevo'. De 1 a 4: 'estandar'. 5 o más: 'premium'. Si mora es True, siempre 'en_mora'.

Ejemplo: `categoria(6, True) → 'en_mora'`

Función a completar en `practica_extra.py`: `categoria`.
