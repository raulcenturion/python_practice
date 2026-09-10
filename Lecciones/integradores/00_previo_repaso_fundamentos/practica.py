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
import asyncio  # noqa: F401 — disponible para ejercicios 19*
import json  # noqa: F401 — disponible para ejercicios 15*
import sys  # noqa: F401 — disponible para ejercicio 18a
import time  # noqa: F401 — disponible para ejercicios 19*
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
    raise NotImplementedError("Completá 01a")


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
    raise NotImplementedError("Completá 02a")


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
    raise NotImplementedError("Completá 03a")


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
    raise NotImplementedError("Completá 04a")


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
    raise NotImplementedError("Completá 05a")


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
    raise NotImplementedError("Completá 06a")


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
    raise NotImplementedError("Completá 07a")


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
    raise NotImplementedError("Completá 08a")


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
    raise NotImplementedError("Completá 09a")


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
    raise NotImplementedError("Completá 10a")


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
    raise NotImplementedError("Completá 11a")


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
    raise NotImplementedError("Completá 12a")


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
    raise NotImplementedError("Completá 13a")


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
    raise NotImplementedError("Completá 14a")


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
    raise NotImplementedError("Completá 14b")


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
    raise NotImplementedError("Completá 14c")


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
    raise NotImplementedError("Completá 14d")


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
    raise NotImplementedError("Completá 15a")


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
    raise NotImplementedError("Completá 15b")


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
    raise NotImplementedError("Completá 15c")


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
    raise NotImplementedError("Completá 16a")


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
    raise NotImplementedError("Completá 17a")


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
    raise NotImplementedError("Completá 18a")


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
    raise NotImplementedError("Completá 19a")


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
    raise NotImplementedError("Completá 19b")


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
    raise NotImplementedError("Completá 19c")


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
    raise NotImplementedError("Completá 20a")


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
    raise NotImplementedError("Completá 20b")


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
    raise NotImplementedError("Completá 20c")


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

    if args.list or args.ejercicio in (None, "list", "--list"):
        if args.ejercicio is None and not args.all and not args.list:
            listar()
            print("\nPasá un ID para correr solo ese ejercicio.")
            return 0
        if args.list or args.ejercicio in ("list", "--list"):
            listar()
            return 0

    if args.all:
        errores = []
        for eid, fn in sorted(EJERCICIOS.items(), key=lambda kv: (len(kv[0]), kv[0])):
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

    eid = args.ejercicio.lower()
    if eid not in EJERCICIOS:
        print(f"No existe el ejercicio '{eid}'. Usá --list.\n")
        listar()
        return 1

    try:
        EJERCICIOS[eid]()
    except NotImplementedError as e:
        print(f"\n⏳ Pendiente: {e}")
        print("Leé la GUÍA / TIP comentados arriba en la función y completá '# --- TU SOLUCIÓN ---'.")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
