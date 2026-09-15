# ============================
# 🧪 Integrador previo — Repaso guiado (fundamentos 01–20)
# 📘 Enunciado: enunciado.md (misma carpeta)
# 🔜 Siguiente: 00_repaso_presupuesto_cli
# ============================
#
# Cómo correr UN solo ejercicio:
#   ./r integradores/00 01a
#   ./r integradores/00 14b
#   .venv/bin/python Lecciones/integradores/00_previo_repaso_fundamentos/practica.py --list
#   .venv/bin/python .../practica.py 20c
#
# Cómo correr todos:
#   ./r integradores/00 --all

from __future__ import annotations

import argparse
import asyncio  # — disponible para ejercicios 19*
import json
import sys  #  — disponible para ejercicio 18a
import time  # — disponible para ejercicios 19*
from collections.abc import Callable
from pathlib import Path

DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Helpers de menú
# ---------------------------------------------------------------------------

EJERCICIOS: dict[str, Callable[[], None]] = {}


def ejercicio(eid: str, titulo: str):
    """Decorador: registra una función como ejercicio ejecutable."""

    def deco(fn):
        fn._eid = eid
        fn._titulo = titulo
        EJERCICIOS[eid] = fn
        return fn

    return deco


def _header(eid: str, titulo: str) -> None:
    print(f"\n=== [{eid}] {titulo} ===")
# --- Sistema de registro de ejercicios ---
#
# EJERCICIOS: dict[str, Callable[[], None]]
#   Diccionario global que guarda funciones registradas como ejercicios.
#   Clave: string (ej. "ej1"), Valor: función ejecutable.
#
# def ejercicio(eid: str, titulo: str):
#   Decorador que registra una función como ejercicio.
#   - Crea deco(fn) → recibe la función.
#   - fn._eid / fn._titulo → agrega metadatos a la función.
#   - EJERCICIOS[eid] = fn → guarda la función en el diccionario.
#   - return fn → devuelve la función original.
#   → Se usa como @ejercicio("id", "titulo").
#
# def _header(eid: str, titulo: str):
#   Imprime un encabezado con el ID y título del ejercicio.
#
# --- Buenas prácticas ---
# - Usar decoradores para registrar funciones automáticamente.
# - Guardar funciones en un diccionario permite ejecutarlas dinámicamente.
# - Agregar metadatos (eid, titulo) facilita identificación y documentación.
# - Separar lógica de registro (decorador) de lógica de presentación (_header).



# ============================
# 01 — Print
# ============================
@ejercicio("01a", "Print con sep")
def ej_01a() -> None:
    _header("01a", "Print con sep")
    # ENUNCIADO:
    # Variables nombre, edad, pais → un solo print con sep=" | "
    # Esperado (ej.): Raúl | 33 | Argentina
    #
    # GUÍA:
    # 1) Asigná las 3 variables.
    # 2) print(v1, v2, v3, sep=" | ")
    #
    # TIP / EJEMPLO (patrón):
    # print("a", "b", "c", sep=" - ")  # → a - b - c
    # El sep reemplaza el espacio por defecto entre argumentos.

    # --- TU SOLUCIÓN ---
    # raise NotImplementedError("Completá 01a")
    nombre = "Juan"
    edad = 25
    pais = "Argentina"
    print(nombre, edad, pais, sep=" | ")

# --- raise NotImplementedError ---
#
# raise NotImplementedError("Completá 01a")
# - Lanza una excepción en tiempo de ejecución.
# - NotImplementedError → indica que la función/bloque aún no está implementado.
# - El mensaje "Completá 01a" se muestra en el error.
#
# Uso típico:
# - Marcador de lugar en ejercicios o proyectos.
# - Obligar a implementar métodos en clases abstractas.
# - Recordatorio de que falta completar lógica.
#
# Ejemplo:
# def pendiente():
#     raise NotImplementedError("Falta implementar")
#
# pendiente() → detiene el programa con NotImplementedError.
# --- NotImplementedError ---
#
# raise NotImplementedError("Completá 01a")
# - Lanza una excepción y detiene el programa.
# - Se usa como marcador de lugar para indicar que falta implementar lógica.
# - Mientras esté presente, la ejecución se corta con error.
#
# Buenas prácticas:
# - Usarlo solo como placeholder durante el desarrollo.
# - Al completar la función, eliminar o comentar la línea.
# - En clases abstractas, se usa para obligar a implementar métodos en subclases.
#
# Ejemplo:
# def pendiente():
#     raise NotImplementedError("Falta implementar")
#
# pendiente() → detiene el programa con NotImplementedError.


# ============================
# 02 — Tipos
# ============================
@ejercicio("02a", "Tipos con type()")
def ej_02a() -> None:
    _header("02a", "Tipos con type()")
    # ENUNCIADO:
    # Creá una variable de cada tipo: str, int, float, bool, list, tuple, dict, set.
    # Imprimí valor y type().
    #
    # GUÍA:
    # texto = "hola" ; print(texto, type(texto))
    # set → {1, 2}  |  dict → {"k": "v"}
    #
    # TIP:
    # type(x) no convierte; solo INFORMÁ el tipo en runtime.

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 02a")
    print("Ejercicio 2")
    texto = 'Cadena de texto'
    numero = 20
    decimal = 3.14
    activo = True
    lista = [1,2,3,4]
    tupla = (1,2,3,4)
    diccionario = {"nombre": "Raul", "Edad": 30}
    conjunto = {1,2,3,4}
    print(texto, type(texto))
    print(numero, type(numero))
    print(decimal, type(decimal))
    print(activo, type(activo))
    print(lista, type(lista))
    print(tupla, type(tupla))
    print(diccionario, type(diccionario))
    print(conjunto, type(conjunto))
    
    


# ============================
# 03 — Casting
# ============================
@ejercicio("03a", "Tupla → list y set")
def ej_03a() -> None:
    _header("03a", "Tupla → list y set")
    # ENUNCIADO:
    # datos = (1, 2, 3, 3) → convertí a list y a set. ¿Qué cambia?
    #
    # GUÍA:
    # list(datos)  # conserva orden y duplicados
    # set(datos)   # saca duplicados (sin orden garantizado)
    #
    # TIP:
    # print(list(datos), set(datos))

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 03a")
    datos = (1,2,3,3)
    print(list(datos),set(datos))


# ============================
# 04 — Operaciones
# ============================
@ejercicio("04a", "Descomponer segundos")
def ej_04a() -> None:
    _header("04a", "Descomponer segundos")
    # ENUNCIADO:
    # 3661 segundos → "1h 1m 1s" usando // y %
    #
    # GUÍA:
    # horas = total // 3600
    # resto = total % 3600
    # minutos = resto // 60
    # segundos = resto % 60
    #
    # TIP:
    # // = división entera; % = resto. Se usan juntos para "partir" unidades.

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 04a")
    total = 3661
    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(f"{horas}h {minutos}m {segundos}s")


# ============================
# 05 — Strings / slicing
# ============================
@ejercicio("05a", "Slicing de strings")
def ej_05a() -> None:
    _header("05a", "Slicing de strings")
    # ENUNCIADO:
    # texto = "Python es genial"
    # Imprimí: primeros 6, últimos 6, al revés, len(texto)
    #
    # GUÍA / TIP:
    # s[:6]     → desde el inicio hasta índice 6 (sin incluir 6)
    # s[-6:]    → últimos 6
    # s[::-1]   → reverso
    # len(s)    → cantidad de caracteres

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 05a")
    texto = "Python es genial"
    print(texto[:6])
    print(texto[-6:])
    print(texto[::-1])
    print(len(texto))
    cadena = "Cadena de caracteres"
    print(cadena[:5])
    print(cadena[-5:])
    print(cadena[::-1])
    print(len(cadena))


# ============================
# 06 — Condicionales
# ============================
@ejercicio("06a", "Año bisiesto")
def ej_06a() -> None:
    _header("06a", "Año bisiesto")
    # ENUNCIADO:
    # Dado un año (variable fija OK), decí si es bisiesto.
    # Regla: %400==0  OR  (%4==0 AND %100!=0)
    # Probá mentalmente: 2000 sí, 1900 no, 2024 sí.
    #
    # TIP:
    # if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    #     print("bisiesto")
    # else:
    #     print("no bisiesto")

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 06a")
    anio = int(input("Ingrese un año:"))
    if (anio % 400 ==0) or (anio % 4 == 0 and anio % 100 !=0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")


# ============================
# 07 — Listas
# ============================
@ejercicio("07a", "Copia vs referencia")
def ej_07a() -> None:
    _header("07a", "Copia vs referencia")
    # ENUNCIADO:
    # original = [1, 2, 3]
    # copia_1 = original[:] ; copia_2 = original.copy() ; ref = original
    # ref[0] = 10 → imprimí las 4. ¿Cuáles cambiaron?
    #
    # GUÍA:
    # ref es ALIAS (mismo objeto). Las copias son independientes (lista plana).
    #
    # TIP:
    # print(id(original), id(ref), id(copia_1))  # mismos ids → mismo objeto

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 07a")
    original = [1,2,3]
    copia_1 = original[:]
    copia_2 = original.copy()
    ref = original
    ref[0] = 10
    print(original, copia_1, copia_2, ref)
# --- Copia vs Referencia en listas ---
#
# original = [1,2,3] → lista base.
#
# copia_1 = original[:] → copia superficial con slicing.
# copia_2 = original.copy() → copia superficial con método copy().
#   Ambas son independientes: cambios en original no las afectan.
#
# ref = original → NO crea copia, solo otro nombre para el mismo objeto.
# ref[0] = 10 → modifica también original porque apuntan al mismo objeto.
#
# Resultado:
# original   → [10, 2, 3] (cambió)
# copia_1    → [1, 2, 3]  (independiente)
# copia_2    → [1, 2, 3]  (independiente)
# ref        → [10, 2, 3] (igual que original)
#
# Buenas prácticas:
# - Usar [:] o .copy() para copias superficiales.
# - Usar copy.deepcopy() para listas anidadas.
# - Recordar que asignar ref = original no copia, solo referencia.


# ============================
# 08 — While
# ============================
@ejercicio("08a", "Validar contraseña (simulado)")
def ej_08a() -> None:
    _header("08a", "Validar contraseña (simulado)")
    # ENUNCIADO:
    # Simulá intentos = ["123", "abcdef", "clave1234"]
    # Recorré con while hasta encontrar una clave con len >= 8.
    # Imprimí "Contraseña válida" y la clave.
    #
    # GUÍA:
    # i = 0
    # while i < len(intentos) and len(intentos[i]) < 8:
    #     i += 1
    # (o un while True + break)
    #
    # TIP: la condición/índice DEBE avanzar o hay loop infinito.

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 08a")

    # Ejemplo 1: lista fija (simulada)
    print("--- Ejemplo 1: lista simulada ---")
    intentos = ["123", "abcdef", "clave1234"]
    i = 0
    while i < len(intentos) and len(intentos[i]) < 8:
        i += 1
    if i < len(intentos):
        print("Contraseña válida", intentos[i])
    else:
        print("No se encontró una contraseña válida")

    # Ejemplo 2: pedir intentos al usuario
    print("\n--- Ejemplo 2: input del usuario ---")
    intentos = [
        input("Ingresá intento 1: "),
        input("Ingresá intento 2: "),
        input("Ingresá intento 3: "),
    ]
    i = 0
    while i < len(intentos) and len(intentos[i]) < 8:
        i += 1
    if i < len(intentos):
        print("Contraseña válida", intentos[i])
    else:
        print("No se encontró una contraseña válida")

    # --- Notas ---
    # while i < len(intentos) and len(intentos[i]) < 8:
    #   recorre mientras la clave sea corta; i debe avanzar.
    # if i < len(intentos): encontró una válida; else: ninguna.


# ============================
# 09 — For
# ============================
@ejercicio("09a", "Máximo sin max()")
def ej_09a() -> None:
    _header("09a", "Máximo sin max()")
    # ENUNCIADO:
    # numeros = [15, 5, 25, 10, 20] → máximo con for (sin max()).
    #
    # TIP:
    # mayor = numeros[0]
    # for n in numeros[1:]:
    #     if n > mayor:
    #         mayor = n
    # print(mayor)

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 09a")
    numeros = [15, 5, 25, 10, 20]
    mayor = numeros[0]
    for n in numeros[1:]:
        if n > mayor:
            mayor = n
    print(mayor)


# ============================
# 10 — Funciones
# ============================
@ejercicio("10a", "sumar_todos(*args)")
def ej_10a() -> None:
    _header("10a", "sumar_todos(*args)")
    # ENUNCIADO:
    # def sumar_todos(*args) → suma todos. Ej: sumar_todos(1,2,3,4) → 10
    #
    # GUÍA:
    # *args llega como tupla. return sum(args)
    #
    # TIP:
    # def sumar_todos(*args):
    #     return sum(args)
    # print(sumar_todos(1, 2, 3, 4))

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 10a")
    def sumar_todos(*args):
        return sum(args)

    print(sumar_todos(1, 2, 3, 4))


# ============================
# 11 — Dict / set
# ============================
@ejercicio("11a", "CRUD dict + sets")
def ej_11a() -> None:
    _header("11a", "CRUD dict + sets")
    # ENUNCIADO:
    # 1) dict con nombre, edad, email → agregá pais, cambiá edad, pop email.
    # 2) a={1,2,3,4} b={3,4,5,6} → unión |, intersección &, diferencia -
    #
    # TIP:
    # d["pais"] = "AR"
    # d.pop("email")
    # print(a | b, a & b, a - b)

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 11a")
    print("Dict - User")
    user = {
        "nombre": "Raúl",
        "edad": 39,
        "email": "raul@tengo.com"
    }
    print(user)
    user["pais"] = "AR"
    user["edad"] = 33
    user.pop("email")
    print(user)
    print("Sets - a y b")
    a = {1,2,3,4}
    b = {3,4,5,6}
    print(a | b, a & b, a - b)


# ============================
# 12 — POO
# ============================
@ejercicio("12a", "Clase Persona")
def ej_12a() -> None:
    _header("12a", "Clase Persona")
    # ENUNCIADO:
    # class Persona(nombre, edad) + presentarse() → "Soy X, tengo Y años"
    # Creá 2 instancias y probá.
    #
    # TIP:
    # class Persona:
    #     def __init__(self, nombre, edad):
    #         self.nombre = nombre
    #         self.edad = edad
    #     def presentarse(self):
    #         return f"Soy {self.nombre}, tengo {self.edad} años"

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 12a")
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def presentarse(self):
            return f"Soy {self.nombre}, tengo {self.edad} años"

    persona1 = Persona("Juan", 30)
    persona2 = Persona("Maria", 25)
    persona3 = Persona("Julian", 38)
    print(persona1.presentarse())
    print(persona2.presentarse())
    print(persona3.presentarse())


# ============================
# 13 — Excepciones
# ============================
@ejercicio("13a", "ValueError + excepción propia")
def ej_13a() -> None:
    _header("13a", "ValueError + excepción propia")
    # ENUNCIADO:
    # 1) int("hola") dentro de try/except ValueError → mensaje amigable.
    # 2) class EdadInvalidaError(Exception) + validar_edad(edad) con raise si < 0.
    #
    # TIP:
    # try:
    #     int("hola")
    # except ValueError:
    #     print("Ingresá un número válido")
    #
    # class EdadInvalidaError(Exception):
    #     pass
    # def validar_edad(edad):
    #     if edad < 0:
    #         raise EdadInvalidaError("edad negativa")

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 13a")
    print("Validar numero")
    try:
        numero = int(input("Ingrese un numero: "))
        print("Número ingresado:", numero)
    except ValueError:
        print("Ingresa un número válido")
    
    class EdadInvalidaError(Exception):
        pass
    print("Validar edad")
    def validar_edad(edad):
        if edad < 0:
            raise EdadInvalidaError("edad negativa")

    try:
        edad = int(input("Ingrese su edad: "))
        validar_edad(edad)
        print("Edad ingresada:", edad)
    except EdadInvalidaError as e:
        print(e)
    except ValueError:
        print("Ingresa un número válido")


# ============================
# 14 — HOF / Decoradores  (+ extras)
# ============================
@ejercicio("14a", "filter / comprehension")
def ej_14a() -> None:
    _header("14a", "filter / comprehension")
    # ENUNCIADO:
    # Del 1 al 20, quedate solo con divisibles por 3.
    #
    # TIP (dos formas):
    # list(filter(lambda x: x % 3 == 0, range(1, 21)))
    # [x for x in range(1, 21) if x % 3 == 0]

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 14a")
    print("Divisibles por 3")
    numeros = list(filter(lambda x: x % 3 == 0, range(1, 21)))
    print(numeros)
    numeros = [x for x in range(1, 21) if x % 3 == 0]
    print(numeros)


@ejercicio("14b", "Decorador @log")
def ej_14b() -> None:
    _header("14b", "Decorador @log")
    # ENUNCIADO:
    # @log imprime el nombre de la función ANTES de ejecutarla.
    # Aplicarlo a saludar(nombre).
    #
    # GUÍA paso a paso:
    # 1) def log(func):
    # 2)     def wrapper(*args, **kwargs):
    # 3)         print(f"llamando {func.__name__}")
    # 4)         return func(*args, **kwargs)
    # 5)     return wrapper
    # 6) @log
    #    def saludar(nombre): ...
    #
    # TIP (esqueleto comentado):
    # def log(func):
    #     def wrapper(*args, **kwargs):
    #         print("Ejecutando", func.__name__)
    #         return func(*args, **kwargs)
    #     return wrapper

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 14b")
    def log(func):
        def wrapper(*args, **kwargs):
            print(f"llamando {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    @log
    def saludar(nombre):
        print(f"Hola, {nombre}")

    saludar("Juan")
    saludar("Maria")
    saludar("Pedro")
    saludar("Ana")
    saludar("Luis")
    saludar("Carlos")


@ejercicio("14c", "Decorador @requiere_admin")
def ej_14c() -> None:
    _header("14c", "Decorador @requiere_admin")
    # ENUNCIADO:
    # Solo ejecuta la función si usuario == "admin"; si no, "Acceso denegado".
    # Probá panel("admin") y panel("invitado").
    #
    # GUÍA:
    # 1) wrapper recibe *args/**kwargs
    # 2) usuario = kwargs.get("usuario") or (args[0] si hay args)
    # 3) if usuario != "admin": print(...); return
    # 4) return func(*args, **kwargs)
    #
    # TIP:
    # def requiere_admin(func):
    #     def wrapper(*args, **kwargs):
    #         usuario = kwargs.get("usuario", args[0] if args else None)
    #         if usuario != "admin":
    #             print("Acceso denegado")
    #             return
    #         return func(*args, **kwargs)
    #     return wrapper

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 14c")
    def requiere_admin(func):
        def wrapper(*args, **kwargs):
            usuario = kwargs.get("usuario", args[0] if args else None)
            if usuario != "admin":
                print("Acceso denegado")
                return
            return func(*args, **kwargs)
        return wrapper

    @requiere_admin
    def panel(usuario):
        print(f"Bienvenido al panel, {usuario}")

    panel("admin")
    panel("invitado")
    usuario = input("Ingrese usuario: ")
    panel(usuario)
    # --- Decoradores y wrapper ---
#
# ¿Qué es wrapper?
# - Función interna que "envuelve" a la original.
# - Recibe los mismos argumentos (*args, **kwargs).
# - Permite ejecutar lógica antes o después de la función original.
#
# ¿Por qué se usa?
# - Para agregar validaciones, logs, permisos, etc. sin modificar la función.
# - Separa responsabilidades: la función hace su tarea, el decorador controla acceso.
# - Es la forma práctica y común de implementar decoradores en Python.
#
# Alternativa:
# - Podrías poner la validación dentro de la función, pero eso mezcla lógica de negocio con control.
# - Con wrapper, el código queda más limpio y reutilizable.
#
# Ejemplo:
# @requiere_admin
# def panel(usuario):
#     print("Bienvenido al panel")
#
# panel("admin") → pasa validación.
# panel("invitado") → bloqueado por wrapper.



# --- Decorador requiere_admin ---
#
# def requiere_admin(func): → define un decorador que recibe una función.
# def wrapper(*args, **kwargs): → función interna que controla acceso.
#   usuario = kwargs.get("usuario", args[0] if args else None)
#     - Busca argumento 'usuario' en kwargs.
#     - Si no existe, toma el primer argumento posicional.
#     - Si no hay argumentos, asigna None.
#   if usuario != "admin": → si no es admin, imprime "Acceso denegado" y termina.
#   return func(*args, **kwargs) → si es admin, ejecuta la función original.
# return wrapper → devuelve la función interna como reemplazo.
#
# @requiere_admin → aplica el decorador a la función panel.
# def panel(usuario): → imprime bienvenida si pasa la validación.
#
# Ejemplo:
# panel("admin") → Bienvenido al panel, admin
# panel("invitado") → Acceso denegado
#
# Interactivo:
# usuario = input("Ingrese usuario: ")
# panel(usuario)
#
# --- Conceptos ---
# - Decorador: modifica el comportamiento de una función.
# - wrapper: función interna que decide si ejecutar o no la original.
# - None: valor por defecto si no se pasa ningún usuario.
# - Validación: solo usuario == "admin" puede entrar.

@ejercicio("14d", "Decorador @repetir(n)")
def ej_14d() -> None:
    _header("14d", "Decorador con parámetros @repetir(n)")
    # ENUNCIADO:
    # @repetir(3) hace que la función se ejecute 3 veces.
    # Aplicarlo a decir_hola() que imprime "hola".
    #
    # GUÍA (3 capas):
    # repetir(veces) → decorator(func) → wrapper(*args)
    # @repetir(3) primero llama repetir(3) y obtiene el decorador real.
    #
    # TIP:
    # def repetir(veces):
    #     def decorator(func):
    #         def wrapper(*args, **kwargs):
    #             for _ in range(veces):
    #                 result = func(*args, **kwargs)
    #             return result
    #         return wrapper
    #     return decorator

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 14d")
    def repetir(veces):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(veces):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    @repetir(3)
    def decir_hola():
        print("hola")

    decir_hola()

# ============================
# 15 — Ficheros / JSON  (+ extra)
# ============================
@ejercicio("15a", "Escribir y leer archivo")
def ej_15a() -> None:
    _header("15a", "Escribir y leer archivo")
    # ENUNCIADO:
    # Escribí 3 líneas en DIR/"notas_repaso.txt" (modo "w").
    # Después leélas e imprimí cada una.
    #
    # GUÍA:
    # ruta = DIR / "notas_repaso.txt"
    # with open(ruta, "w", encoding="utf-8") as f:
    #     f.write("linea1\n")
    # with open(ruta, "r", encoding="utf-8") as f:
    #     for linea in f:
    #         print(linea.strip())
    #
    # TIP: preferí Path(__file__).parent (DIR) para no depender del cwd.

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 15a")
    ruta = Path(__file__).parent / "notas_repaso.txt"
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("linea1\n")
        f.write("linea2\n")
        f.write("linea3\n")
        for i in range(3):
            texto = input(f"Ingresá línea {i+1}: ")
            f.write(texto + "\n")
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            print(linea)


@ejercicio("15b", "Dict ↔ JSON")
def ej_15b() -> None:
    _header("15b", "Dict ↔ JSON")
    # ENUNCIADO:
    # Dict personal → json.dumps (mostrar string) y json.dump a DIR/"perfil_repaso.json"
    # Luego json.load y print del dict.
    #
    # TIP:
    # with open(ruta, "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=2, ensure_ascii=False)
    # with open(ruta, "r", encoding="utf-8") as f:
    #     print(json.load(f))

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 15b")
    # Flujo siempre: dict → (string/archivo) → dict.
    # Nunca uses una variable antes de asignarla (ej. dump(data) sin crear data).
    # Tip: Cmd+S para que el otro editor vea lo mismo que Cursor.

    ruta = DIR / "perfil_repaso.json"  # archivo junto a este .py (no depende del cwd)
    data = {  # 1) PRIMERO el dict en memoria (Python)
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Buenos Aires",
    }
    # 2) dumps = dict → str JSON (útil para imprimir / enviar por red)
    # indent=2 → legible; ensure_ascii=False → conserva tildes (ej. "Buenos Aires")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    # 3) dump = dict → archivo .json (persiste en disco)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    # 4) load = archivo → dict (volvés a objetos Python)
    with open(ruta, "r", encoding="utf-8") as f:
        print(json.load(f))

    # --- Notas rápidas ---
    # dumps / dump  → serializar (Python → JSON)
    # loads / load  → deserializar (JSON → Python)
    # "s" al final  → trabaja con string; sin "s" → trabaja con archivo
    # open(..., "w") crea/pisa; open(..., "r") solo lee


@ejercicio("15c", "Append a archivo")
def ej_15c() -> None:
    _header("15c", "Append a archivo")
    # ENUNCIADO:
    # Si no existe, creá DIR/"bitacora.txt" con una línea (modo "w").
    # Después agregá OTRA línea con modo "a".
    # Leé todo y mostralo.
    #
    # GUÍA:
    # "w" pisa el archivo; "a" agrega al final sin borrar lo anterior.
    #
    # TIP:
    # with open(ruta, "a", encoding="utf-8") as f:
    #     f.write("segunda linea\n")

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 15c")
    ruta = Path(__file__).parent / "bitacora.txt"
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("primera linea\n")
    with open(ruta, "a", encoding="utf-8") as f:
        f.write("segunda linea\n")
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            print(linea)


# ============================
# 16 — Valor / referencia
# ============================
@ejercicio("16a", "Alias vs copy")
def ej_16a() -> None:
    _header("16a", "Alias vs copy")
    # ENUNCIADO:
    # a = [1, 2]; b = a; a.append(3) → ¿qué es b?
    # c = a.copy(); c.append(99) → ¿cambia a?
    # Imprimí también id(a), id(b), id(c).
    #
    # TIP:
    # b es alias (mismo id). copy() crea otro objeto (id distinto).

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 16a")
    a = [1, 2]
    b = a
    a.append(3)
    print(b)
    print(id(a), id(b))
    c = a.copy()
    c.append(99)
    print(a)
    print(id(a), id(b), id(c))

    # --- Notas rápidas ---
    # - alias: b = a → mismo id.
    # - copy: c = a.copy() → id distinto.
    # - append: a.append(3) → cambia a y b.
    # - id: función para obtener el identificador de un objeto.


# ============================
# 17 — Librerías
# ============================
@ejercicio("17a", "Import defensivo")
def ej_17a() -> None:
    _header("17a", "Import defensivo")
    # ENUNCIADO:
    # Intentá import requests; si falta, print("Instalá requests").
    # Si está, print("requests OK", requests.__name__)
    #
    # TIP:
    # try:
    #     import requests
    # except ImportError:
    #     print("Instalá requests")

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 17a")
    try:
        import requests
    except ImportError:
        print("Instalá requests")
    else:
        print("requests OK", requests.__name__)


# ============================
# 18 — Venv
# ============================
@ejercicio("18a", "Detectar venv")
def ej_18a() -> None:
    _header("18a", "Detectar venv")
    # ENUNCIADO:
    # Función corriendo_en_venv() -> bool
    # Imprimí el bool y sys.executable
    #
    # TIP:
    # return sys.prefix != getattr(sys, "base_prefix", sys.prefix)

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 18a")
    def corriendo_en_venv():
        return sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    print(corriendo_en_venv())
    print(sys.executable)


# ============================
# 19 — Async  (+ extras)
# ============================
@ejercicio("19a", "async ping → pong")
def ej_19a() -> None:
    _header("19a", "async ping → pong")
    # ENUNCIADO:
    # async def ping(): await asyncio.sleep(0.2); return "pong"
    # Ejecutar con asyncio.run(ping()) e imprimir.
    #
    # GUÍA:
    # 1) Definí la corutina (async def)
    # 2) await adentro
    # 3) asyncio.run(...) afuera (una sola vez por proceso de event loop)
    #
    # TIP:
    # async def ping():
    #     await asyncio.sleep(0.2)
    #     return "pong"
    # print(asyncio.run(ping()))

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 19a")
    async def ping():
        await asyncio.sleep(0.2)
        return "pong"

    input("Presioná Enter para hacer ping: ")  # solo pausa; no hace falta guardar el valor
    print(asyncio.run(ping()))



@ejercicio("19b", "Secuencial vs gather")
def ej_19b() -> None:
    _header("19b", "Secuencial vs gather")
    # ENUNCIADO:
    # trabajo(nombre, segundos) duerme y retorna nombre.
    # Compará:
    #   a) await A; await B
    #   b) await asyncio.gather(A, B)
    # Medí con time.perf_counter(). Concurrente ~ mitad del secuencial.
    #
    # IMPORTANTE:
    # gather se await DENTRO de una async def; NO hagas asyncio.run(gather(...))
    #
    # TIP:
    # async def demo():
    #     t0 = time.perf_counter()
    #     await trabajo("A", 0.3)
    #     await trabajo("B", 0.3)
    #     print("sec", time.perf_counter() - t0)
    #     t0 = time.perf_counter()
    #     print(await asyncio.gather(trabajo("A", 0.3), trabajo("B", 0.3)))
    #     print("par", time.perf_counter() - t0)
    # asyncio.run(demo())

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 19b")
    async def trabajo(nombre, segundos):
        await asyncio.sleep(segundos)
        return nombre
    async def demo():
        t0 = time.perf_counter()
        await trabajo("A", 0.3)
        await trabajo("B", 0.3)
        print("sec", time.perf_counter() - t0)
        t0 = time.perf_counter()
        print(await asyncio.gather(trabajo("A", 0.3), trabajo("B", 0.3)))
        print("par", time.perf_counter() - t0)
    asyncio.run(demo())
# --- Ejercicio 19b: Concurrencia con asyncio ---
#
# async def trabajo(nombre, segundos):
#   - Corutina que espera 'segundos' y devuelve 'nombre'.
#
# demo():
#   - Mide tiempo secuencial:
#       await trabajo("A", 0.3)
#       await trabajo("B", 0.3)
#       → total ≈ 0.6 seg
#   - Mide tiempo concurrente:
#       await asyncio.gather(trabajo("A", 0.3), trabajo("B", 0.3))
#       → total ≈ 0.3 seg
#       → gather ejecuta ambas tareas en paralelo dentro del event loop.
#
# asyncio.run(demo()) → arranca el event loop y corre la corutina principal.
#
# Resultado:
# - Secuencial: suma de tiempos.
# - Concurrente: máximo de tiempos (más eficiente).
#
# Conceptos clave:
# - async def → define corutina.
# - await → espera resultado.
# - asyncio.gather → corre varias corutinas en paralelo.
# - time.perf_counter() → mide tiempo con precisión.


@ejercicio("19c", "5 tareas concurrentes")
def ej_19c() -> None:
    _header("19c", "5 tareas concurrentes")
    # ENUNCIADO:
    # 5 corutinas (delay 0.2s) con gather. Tiempo total ~0.2s (no ~1.0s).
    # Cada una debe RETORNAR un valor (si usás solo sleep → lista de None).
    #
    # TIP:
    # async def tarea(i):
    #     await asyncio.sleep(0.2)
    #     return f"T{i}"
    # async def demo():
    #     t0 = time.perf_counter()
    #     res = await asyncio.gather(*[tarea(i) for i in range(1, 6)])
    #     print(res, round(time.perf_counter() - t0, 3))
    # asyncio.run(demo())

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 19c")
    async def tarea(i):
        await asyncio.sleep(0.2)
        return f"T{i}"
    async def demo():
        t0 = time.perf_counter()
        res = await asyncio.gather(*[tarea(i) for i in range(1, 6)])
        print(res, round(time.perf_counter() - t0, 3))
    asyncio.run(demo())


# ============================
# 20 — Pydantic  (+ extra)
# ============================
@ejercicio("20a", "BaseModel + model_dump")
def ej_20a() -> None:
    _header("20a", "BaseModel + model_dump")
    # ENUNCIADO:
    # class Libro(BaseModel): titulo: str; anio: int; leido: bool = False
    # Instanciá y mostrá model_dump().
    #
    # TIP:
    # from pydantic import BaseModel
    # class Libro(BaseModel):
    #     titulo: str
    #     anio: int
    #     leido: bool = False
    # print(Libro(titulo="Dune", anio=1965).model_dump())

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 20a")

    from pydantic import BaseModel
    class Libro(BaseModel):
        titulo: str
        anio: int
        leido: bool = False
    print(Libro(titulo="Dune", anio=1965).model_dump())


@ejercicio("20b", "model_validate (coerción)")
def ej_20b() -> None:
    _header("20b", "model_validate (coerción)")
    # ENUNCIADO:
    # payload = {"titulo": "Dune", "anio": "1965", "leido": False}
    # Libro.model_validate(payload) → "1965" debe pasar a int.
    #
    # TIP:
    # print(Libro.model_validate(payload))
    # print(type(Libro.model_validate(payload).anio))  # int

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 20b")
    from pydantic import BaseModel
    class Libro(BaseModel):
        titulo: str
        anio: int
        leido: bool = False
    payload = {"titulo": "Dune", "anio": "1965", "leido": False}
    print(Libro.model_validate(payload))
    print(type(Libro.model_validate(payload).anio))


@ejercicio("20c", "Field + ValidationError")
def ej_20c() -> None:
    _header("20c", "Field + ValidationError")
    # ENUNCIADO:
    # anio: int = Field(ge=0)
    # Intentá Libro(titulo="X", anio=-1) y capturá ValidationError.
    #
    # GUÍA:
    # 1) from pydantic import BaseModel, Field, ValidationError
    # 2) Field(ge=0) = greater or equal 0
    # 3) try/except ValidationError
    #
    # TIP:
    # try:
    #     Libro(titulo="X", anio=-1)
    # except ValidationError as e:
    #     print(e)

    # --- TU SOLUCIÓN ---
    #raise NotImplementedError("Completá 20c")
    from pydantic import BaseModel, Field, ValidationError
    class Libro(BaseModel):
        titulo: str
        anio: int = Field(ge=0)
    try:
        Libro(titulo="X", anio=-1)
    except ValidationError as e:
        print(e)

#==========================
# ============================
# CLI — elegir un ejercicio
# ============================
def listar() -> None:
    print("Ejercicios disponibles:\n")
    for eid in sorted(EJERCICIOS, key=lambda x: (len(x), x)):
        fn = EJERCICIOS[eid]
        print(f"  {eid:4}  {fn._titulo}")
    print("\nEjemplo:  python practica.py 14b")
    print("          ./r integradores/00 14b")


def _correr_todos() -> int:
    errores: list[str] = []
    ordenados = sorted(EJERCICIOS.items(), key=lambda kv: (len(kv[0]), kv[0]))
    for eid, fn in ordenados:
        try:
            fn()
        except NotImplementedError as e:
            errores.append(f"{eid}: {e}")
        except Exception as e:  # noqa: BLE001 — feedback de aprendizaje
            errores.append(f"{eid}: {type(e).__name__}: {e}")
    if errores:
        print("\n--- Pendientes / errores ---")
        for msg in errores:
            print("·", msg)
    return 0


def _correr_uno(eid: str) -> int:
    eid = eid.lower()
    if eid not in EJERCICIOS:
        print(f"No existe el ejercicio '{eid}'. Usá --list.\n")
        listar()
        return 1
    try:
        EJERCICIOS[eid]()
    except NotImplementedError as e:
        print(f"\n⏳ Pendiente: {e}")
        print(
            "Leé la GUÍA / TIP comentados arriba en la función "
            "y completá '# --- TU SOLUCIÓN ---'."
        )
        return 2
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Repaso guiado fundamentos — corré UN ejercicio por vez."
    )
    parser.add_argument(
        "ejercicio",
        nargs="?",
        help="ID del ejercicio (ej. 01a, 14b, 20c). Usá --list para ver todos.",
    )
    parser.add_argument("--list", "-l", action="store_true", help="Listar ejercicios")
    parser.add_argument("--all", action="store_true", help="Correr todos (puede fallar en stubs)")
    args = parser.parse_args(argv)

    # Sin args → mostrar menú (no confundir con --all)
    if args.ejercicio is None and not args.all and not args.list:
        listar()
        print("\nPasá un ID para correr solo ese ejercicio.")
        return 0

    if args.list or args.ejercicio in ("list", "--list"):
        listar()
        return 0

    if args.all:
        return _correr_todos()

    return _correr_uno(args.ejercicio)


if __name__ == "__main__":
    raise SystemExit(main())
