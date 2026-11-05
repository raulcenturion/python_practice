# Práctica extra — tipos

Cada valor tiene un tipo. bool es un entero por dentro, así que un monto no puede aceptar True. type() muestra la clase. En plata se usa int (centavos) o Decimal, no un float suelto.

## Documentación

- [tipos](https://docs.python.org/3/library/stdtypes.html)
- [Decimal](https://docs.python.org/3/library/decimal.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 02 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. clasificar

Devolvé 'entero', 'decimal', 'texto', 'logico' o 'vacio' según el tipo. None es vacio. bool es logico, aunque herede de int.

Ejemplo: `clasificar(True) → 'logico'`

Función a completar en `practica_extra.py`: `clasificar`.

### 2. es_monto

True solo si es int y no es bool. Un float no cuenta: la plata de estos ejercicios va en centavos enteros.

Ejemplo: `es_monto(1500) es True; es_monto(True) es False`

Función a completar en `practica_extra.py`: `es_monto`.

### 3. contar_tipos

Devolvé un dict con la cantidad de cada clasificar() de la lista.

Ejemplo: `contar_tipos([1, True, 'a'])`

Función a completar en `practica_extra.py`: `contar_tipos`.
