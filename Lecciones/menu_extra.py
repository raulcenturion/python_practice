# Menú de las prácticas extra.
# Cada practica_extra.py llama a abrir() con su lista de pruebas.
# Con un número en la terminal corre solo ese ejercicio:
#   ./r 07 practica_extra 2
# Sin número, input() pide cuál.

import ast
import inspect
import re
from datetime import date


def abrir(pruebas, entorno):
    """Muestra los ejercicios y corre el que se elige."""
    import sys

    if len(sys.argv) > 1:
        _elegir(pruebas, entorno, sys.argv[1], preguntar=True)
        return

    while True:
        print()
        for indice, (nombre, _prueba) in enumerate(pruebas, start=1):
            print(f"{indice}. {nombre}")
        print("0. salir")
        try:
            eleccion = input("Ejercicio: ").strip()
        except EOFError:
            print()
            return
        if eleccion in {"0", "q", "salir"}:
            print("Listo.")
            return
        _elegir(pruebas, entorno, eleccion, preguntar=True)


def _elegir(pruebas, entorno, eleccion, preguntar):
    if eleccion == "todos":
        for nombre, prueba in pruebas:
            _ejemplo(nombre, prueba, entorno)
        return
    if not eleccion.isdigit():
        print("Ese número no está en la lista.")
        return
    numero = int(eleccion)
    if numero < 1 or numero > len(pruebas):
        print("Ese número no está en la lista.")
        return
    nombre, prueba = pruebas[numero - 1]
    _ejemplo(nombre, prueba, entorno)
    if preguntar:
        _propio(nombre, entorno)


def _ejemplo(nombre, prueba, entorno):
    print()
    print(f"--- {nombre} ---")
    fn = entorno.get(nombre)
    doc = inspect.getdoc(fn) if fn is not None else None
    if doc:
        print(doc)
    try:
        prueba()
    except NotImplementedError:
        print("Pendiente: completá la función en este archivo.")
        return
    except AssertionError as exc:
        detalle = str(exc).strip() or "el ejemplo no dio el resultado esperado"
        print(f"Revisar: {detalle}")
        return
    print("Ejemplo: ok")


def _propio(nombre, entorno):
    fn = entorno.get(nombre)
    if fn is None or not _se_puede_probar(fn):
        return
    try:
        texto = input("¿Probar con tus datos? (s/n): ").strip().lower()
    except EOFError:
        print()
        return
    if texto not in {"s", "si"}:
        return
    params = _parametros(fn)
    args = []
    for param in params:
        crudo = input(f"  {param.name}: ")
        args.append(_interpretar(crudo))
    try:
        resultado = fn(*args)
    except NotImplementedError:
        print("Pendiente: completá la función en este archivo.")
        return
    except (TypeError, ValueError) as exc:
        print(f"No se pudo usar esos datos: {exc}")
        return
    if inspect.isclass(fn):
        volcar = getattr(resultado, "model_dump", None)
        print(volcar() if volcar else vars(resultado))
        return
    print("Resultado:", resultado)


def _se_puede_probar(fn):
    params = _parametros(fn)
    return not any(param.name in {"session", "fn"} for param in params)


def _parametros(fn):
    objetivo = fn.__init__ if inspect.isclass(fn) else fn
    params = list(inspect.signature(objetivo).parameters.values())
    if inspect.isclass(fn):
        params = params[1:]
    return params


def _interpretar(texto):
    limpio = texto.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", limpio):
        return date.fromisoformat(limpio)
    try:
        return ast.literal_eval(limpio)
    except (ValueError, SyntaxError):
        return limpio
