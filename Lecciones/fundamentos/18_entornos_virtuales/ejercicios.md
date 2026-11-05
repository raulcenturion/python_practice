# Práctica extra — entornos virtuales

El venv de este repo es la carpeta .venv de la raíz. Ahí viven FastAPI, SQLModel y el resto. El Python del sistema no los tiene. teoria.py de esta carpeta explica venv, Pipenv, Poetry y uv. Este proyecto se queda en .venv y requirements.txt.

## Documentación

- [venv](https://docs.python.org/3/library/venv.html)

Los enunciados de esta carpeta son propios. Para seguir con más problemas del mismo tipo, estos catálogos publican los suyos (no están copiados acá):

- [LeetCode Explore](https://leetcode.com/explore/)
- [Coding Challenges](https://coding-challenges.dev/problems)

## Cómo practicar

1. Leé este archivo.
2. Completá las funciones en `practica_extra.py` (hoy lanzan `NotImplementedError`).
3. Corré `./r 18 practica_extra`.
Sin número, `input()` muestra el menú y elegís el ejercicio. Con un número al final corre solo ese, por ejemplo `./r 07 practica_extra 2` (en otras áreas, `./r logica/01 practica_extra 1`). Imprime el enunciado y dice si el ejemplo quedó ok, pendiente o hay que revisarlo. Después pregunta si querés probar con tus propios datos.

## Ejercicios

### 1. parece_venv

True si la ruta contiene '.venv' como una parte, no como un pedazo de otra palabra.

Ejemplo: `parece_venv('/repo/.venv/bin/python') es True`

Función a completar en `practica_extra.py`: `parece_venv`.

### 2. usando_el_del_repo

True si sys.prefix apunta a un entorno cuyo nombre de carpeta es .venv.

Ejemplo: `con ./r 18 practica_extra tiene que dar True`

Función a completar en `practica_extra.py`: `import sys


usando_el_del_repo`.
