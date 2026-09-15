# ============================
# 🧪 Integrador de repaso — Mini presupuesto CLI
# 📘 Enunciado: enunciado.md (checklist completo por lección)
# Temas: lecciones 01→10 + 13 — todo interactivo por terminal
# ============================
#
# Cómo correr UNA sola función (como el previo):
#   ./r integradores/00 presupuesto --list
#   ./r integradores/00 presupuesto 01
#   ./r integradores/00_repaso_presupuesto 04
#   ./r integradores/00 presupuesto app      ← app completa (menú while)
#
# Cómo correr todos los stubs:
#   ./r integradores/00 presupuesto --all

from __future__ import annotations

import argparse
from collections.abc import Callable

# --- Lección 02 (tipos) + 07 (listas) ---
# lista de tuplas: (nombre: str, monto: float)
gastos: list[tuple[str, float]] = []

# --- Lección 02 (bool) + 06 (condicionales) ---
modo_ahorro: bool = False

# ---------------------------------------------------------------------------
# Helpers de menú (mismo sistema que 00_previo_repaso_fundamentos)
# ---------------------------------------------------------------------------

EJERCICIOS: dict[str, Callable[[], None]] = {}


def ejercicio(eid: str, titulo: str):
    """Decorador: registra una función como ejercicio ejecutable por ID."""

    def deco(fn):
        fn._eid = eid
        fn._titulo = titulo
        EJERCICIOS[eid] = fn
        return fn

    return deco


def _header(eid: str, titulo: str) -> None:
    print(f"\n=== [{eid}] {titulo} ===")


def _demo_lista() -> list[tuple[str, float]]:
    """Datos de prueba para probar listar/stats/buscar/eliminar sin cargar la app."""
    return [("Cafe", 1500.0), ("Bondi", 800.0), ("Almuerzo", 4500.0)]


# ============================
# Funciones del proyecto (completalas vos)
# ============================

# --- Lección 01 (print: sep/end/f-string) + 10 (def, default, docstring) ---
def mostrar_menu(titulo: str = "Mini presupuesto") -> None:
    """
    Imprimí el menú (opciones 1-7).
    Practica: print con varios args, sep=..., end=..., f-strings, comentarios.
    """
    # titulo (default) se usa en el encabezado — parámetro con valor por defecto (L10)
    print(f"=== {titulo} ===")
    print(
        "1. Agregar gasto",
        "2. Listar gastos",
        "3. Ver estadísticas",
        "4. Buscar gastos",
        "5. Eliminar gasto",
        "6. Modo ahorro",
        "7. Salir",
        sep="\n",
        end="\n\n",  # end= deja una línea extra antes del input del menú
    )


# --- Lección 05 (input/strings) + 03 (casting) + 13 (try/except/else/finally) ---
def pedir_monto() -> float | None:
    """
    Pedí un monto con input().strip(), convertí con float().
    Si falla o es <= 0 → avisá y devolvé None.
    Ideal: try / except ValueError / else / finally (aunque finally solo imprima un tip).
    """
    # 1) Leer texto y limpiar espacios
    texto = input("Ingrese el monto: ").strip()
    try:
        # 2) Casting str → float (puede fallar si no es número)
        monto = float(texto)
    except ValueError:
        print("Ingrese un monto válido")
        return None
    # 3) Validar que sea positivo
    if monto <= 0:
        print("El monto debe ser mayor a 0")
        return None
    # 4) Éxito: HAY QUE devolver el float (si no, Python devuelve None)
    return monto

# --- Lección 05 + 06 (and/or/not) + 07 (append) + 10 ---
def agregar_gasto(lista: list[tuple[str, float]]) -> None:
    """
    Pedí nombre (.strip().title()) y monto (pedir_monto).
    Validá con and/or/not (ej. nombre no vacío y monto válido).
    Si OK → lista.append((nombre, monto)) y confirmá con print/f-string.
    """
    nombre = input("Ingrese el nombre del gasto: ").strip().title()
    monto = pedir_monto()
    if nombre and monto:
        lista.append((nombre, monto))
        print(f"Gasto agregado: {nombre} - {monto}")
    else:
        print("Ingrese un nombre y un monto válido")
    
# --- Ejercicio: Registro de gastos ---
#
# nombre = input(...).strip().title()
# - Pide nombre del gasto al usuario.
# - strip() → elimina espacios extra.
# - title() → formatea con mayúscula inicial en cada palabra.
#
# monto = pedir_monto()
# - Llama a función auxiliar que valida y devuelve el monto.
#
# if nombre and monto:
# - Valida que nombre no esté vacío y monto sea válido.
# - Si OK:
#   lista.append((nombre, monto)) → guarda gasto en lista como tupla.
#   print(...) → confirma registro al usuario.
# else:
# - Si falla, muestra mensaje de error.
#
# Buenas prácticas:
# - Usar strip() y title() para limpiar y formatear entradas.
# - Validar con and/or/not para asegurar datos correctos.
# - Guardar datos en lista de tuplas para fácil manejo posterior.


# --- Lección 01 + 06 + 07 (len) + 09 (for, enumerate) ---
def listar_gastos(lista: list[tuple[str, float]]) -> None:
    """
    Si len(lista) == 0 → mensaje y return.
    Si no → for i, (nombre, monto) in enumerate(lista, start=1): ...
    """
    # ("Completá listar_gastos — Lección 01 + 07 + 09")
    if len(lista) == 0:
        print("No hay gastos")
        return
    for i, (nombre, monto) in enumerate(lista, start=1):
        print(f"{i}. {nombre} - {monto}")


# --- Lección 02 (type) + 04 (ops) + 06 + 09 ---
def mostrar_total_y_estadisticas(lista: list[tuple[str, float]]) -> None:
    """
    Calculá:
      - total (suma con for o sum)
      - cantidad = len(lista)
      - promedio = total / cantidad  (solo si cantidad > 0)
      - alguna de: total // 2, cantidad % 3, o 2 ** 3 como demo de **
    Mostrá también type(total) o type(cantidad) (lección 02).
    Si modo_ahorro es True, agregá un tip extra (lección 06 + bool).
    """
    total = sum(monto for _, monto in lista)
    cantidad = len(lista)
    promedio = total / cantidad if cantidad > 0 else 0
    print(f"Total: {total}")
    print(f"Cantidad: {cantidad}")
    print(f"Promedio: {promedio}")
    print(f"Tipo de total: {type(total)}")
    print(f"Tipo de cantidad: {type(cantidad)}")
    # Demo ops (L04): //  %  **
    print(f"Mitad entera del total: {total // 2}")
    print(f"Cantidad % 3: {cantidad % 3}")
    print(f"2 ** 3: {2 ** 3}")
    # El bloque del if DEBE ir indentado; el else al mismo nivel que el if
    if modo_ahorro:
        print("Modo ahorro: ON — tip: revisá gastos chicos del día")
    else:
        print("Modo ahorro: OFF")


# --- Lección 05 (lower) + 06 + 09 ---
def buscar_gastos(lista: list[tuple[str, float]]) -> None:
    """
    Pedí palabra, filtrá con .lower() en el nombre.
    Recorré con for; si no hay coincidencias, avisá.
    """
    #("Completá buscar_gastos — Lección 05 + 06 + 09")
    palabra = input("Ingrese la palabra a buscar: ").strip().lower()
    if not palabra:
        print("Ingrese una palabra válida")
        return
    encontrados = [nombre for nombre, _ in lista if palabra in nombre.lower()]
    if not encontrados:
        print("No se encontraron gastos")
        return
    print("Gastos encontrados:")
    for nombre in encontrados:
        print(f"- {nombre}")


# --- Lección 03 (int) + 07 (pop/del) + 09 + 13 (IndexError / ValueError) ---
def eliminar_gasto(lista: list[tuple[str, float]]) -> None:
    """
    Listá gastos, pedí el número (1..n), convertí con int().
    Eliminá con pop(indice) o del lista[indice] (acordate: enumerate usa 1..n).
    Capturá ValueError e IndexError (o validá el rango antes).
    """
    #("Completá eliminar_gasto — Lección 03 + 07 + 09 + 13")
    print("Gastos:")
    for i, (nombre, monto) in enumerate(lista, start=1):
        print(f"{i}. {nombre} - {monto}")
    indice = int(input("Ingrese el número del gasto a eliminar: ")) - 1
    if 0 <= indice < len(lista):
        del lista[indice]
        print("Gasto eliminado")
    else:
        print("Ingrese un número de gasto válido")


# --- Lección 02 (bool) + 06 (not) + 01 ---
def toggle_modo_ahorro() -> None:
    """
    Invertí modo_ahorro con not (global o devolvé el nuevo valor y asigná en main).
    Informá el estado actual con print.
    """
    #("Completá toggle_modo_ahorro — Lección 02 + 06")
    global modo_ahorro
    modo_ahorro = not modo_ahorro
    print("Modo ahorro: ON" if modo_ahorro else "Modo ahorro: OFF")


# --- Lección 03 (int) + 08 (while/break/continue) + 06 + 09 (range) + 10 ---
def app() -> None:
    """
    App completa (menú interactivo).

    while True:
      mostrar_menu()
      leer opción con input().strip() → int (try/except)
      if 1: agregar ...
      elif 2: listar ...
      elif 3: estadisticas ...
      elif 4: buscar ...
      elif 5: eliminar ...
      elif 6: toggle ...
      elif 7: break
      else: continue   # opción inválida → vuelve al menú

    Extra lección 09: antes del menú, usá range() para imprimir una línea
    decorativa (ej. print("-" * n) o un for _ in range(3): ...).
    """
    #"Completá app — Lección 03 + 06 + 08 + 09 + 10 + 13")
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción: ").strip()
        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            listar_gastos(gastos)
        elif opcion == "3":
            mostrar_total_y_estadisticas(gastos)

        elif opcion == "4":
            buscar_gastos(gastos)
        elif opcion == "5":
            eliminar_gasto(gastos)
        elif opcion == "6":
            toggle_modo_ahorro()
        elif opcion == "7":
            break
        else:
            print("Ingrese una opción válida")
    for _ in range(3):
        print("-" * 30)
    print("Gracias por usar el mini presupuesto")

# Alias: el enunciado habla de main(); el CLI usa "app" / "09"
main = app


# ============================
# Ejercicios ejecutables (un ID = una función)
# ============================


@ejercicio("01", "mostrar_menu")
def ej_01() -> None:
    _header("01", "mostrar_menu")
    mostrar_menu()
    mostrar_menu("Demo título custom")


@ejercicio("02", "pedir_monto")
def ej_02() -> None:
    _header("02", "pedir_monto")
    print("Resultado:", pedir_monto())


@ejercicio("03", "agregar_gasto")
def ej_03() -> None:
    _header("03", "agregar_gasto")
    # Usa la lista global para que puedas listar después con 04
    agregar_gasto(gastos)
    print("Lista ahora:", gastos)


@ejercicio("04", "listar_gastos")
def ej_04() -> None:
    _header("04", "listar_gastos")
    lista = gastos if gastos else _demo_lista()
    print("(usando lista global si tiene datos; si no, demo)")
    listar_gastos(lista)


@ejercicio("05", "mostrar_total_y_estadisticas")
def ej_05() -> None:
    _header("05", "mostrar_total_y_estadisticas")
    lista = gastos if gastos else _demo_lista()
    mostrar_total_y_estadisticas(lista)


@ejercicio("06", "buscar_gastos")
def ej_06() -> None:
    _header("06", "buscar_gastos")
    lista = gastos if gastos else _demo_lista()
    buscar_gastos(lista)


@ejercicio("07", "eliminar_gasto")
def ej_07() -> None:
    _header("07", "eliminar_gasto")
    # Copia local para no romper demos si fallás el índice
    lista = list(gastos) if gastos else _demo_lista()
    print("Antes:", lista)
    eliminar_gasto(lista)
    print("Después:", lista)


@ejercicio("08", "toggle_modo_ahorro")
def ej_08() -> None:
    _header("08", "toggle_modo_ahorro")
    print("Antes:", modo_ahorro)
    toggle_modo_ahorro()
    print("Después (global):", modo_ahorro)


@ejercicio("09", "app completa (menú while)")
def ej_09() -> None:
    _header("09", "app completa")
    print("===", "Mini presupuesto", "===", sep=" ")
    print("Repaso lecciones 01-10 + 13. Enunciado: enunciado.md", end="\n\n")
    app()


@ejercicio("app", "app completa (alias de 09)")
def ej_app() -> None:
    ej_09()


# ============================
# CLI — elegir un ejercicio
# ============================
def listar() -> None:
    print("Ejercicios disponibles (presupuesto CLI):\n")
    for eid in sorted(EJERCICIOS, key=lambda x: (len(x), x)):
        fn = EJERCICIOS[eid]
        print(f"  {eid:4}  {fn._titulo}")
    print("\nEjemplo:  ./r integradores/00 presupuesto 01")
    print("          ./r integradores/00_repaso_presupuesto 04")
    print("          ./r integradores/00 presupuesto app")


def _correr_todos() -> int:
    errores: list[str] = []
    # No correr "app" en --all (es interactivo y duplica 09)
    ids = [e for e in EJERCICIOS if e != "app"]
    for eid in sorted(ids, key=lambda x: (len(x), x)):
        try:
            EJERCICIOS[eid]()
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
        print("Completá la función correspondiente arriba y volvé a correr este ID.")
        return 2
    return 0


def cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Mini presupuesto — corré UNA función por vez, o la app completa."
    )
    parser.add_argument(
        "ejercicio",
        nargs="?",
        help="ID (01..09 o app). Usá --list para ver todos.",
    )
    parser.add_argument("--list", "-l", action="store_true", help="Listar ejercicios")
    parser.add_argument("--all", action="store_true", help="Correr todos (stubs pueden fallar)")
    args = parser.parse_args(argv)

    if args.ejercicio is None and not args.all and not args.list:
        listar()
        print("\nPasá un ID para correr solo esa función (ej. 01 o app).")
        return 0

    if args.list or args.ejercicio in ("list", "--list"):
        listar()
        return 0

    if args.all:
        return _correr_todos()

    return _correr_uno(args.ejercicio)


if __name__ == "__main__":
    raise SystemExit(cli())
