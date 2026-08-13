# ============================
# 🧪 Integrador de repaso — Mini presupuesto CLI
# 📘 Enunciado: enunciado.md (checklist completo por lección)
# Temas: lecciones 01→10 + 13 — todo interactivo por terminal
# ============================

from __future__ import annotations

# --- Lección 02 (tipos) + 07 (listas) ---
# lista de tuplas: (nombre: str, monto: float)
gastos: list[tuple[str, float]] = []

# --- Lección 02 (bool) + 06 (condicionales) ---
modo_ahorro: bool = False


# --- Lección 01 (print: sep/end/f-string) + 10 (def, default, docstring) ---
def mostrar_menu(titulo: str = "Mini presupuesto") -> None:
    """
    Imprimí el menú (opciones 1-7).
    Practica: print con varios args, sep=..., end=..., f-strings, comentarios.
    """
    raise NotImplementedError("Completá mostrar_menu — Lección 01 + 10")


# --- Lección 05 (input/strings) + 03 (casting) + 13 (try/except/else/finally) ---
def pedir_monto() -> float | None:
    """
    Pedí un monto con input().strip(), convertí con float().
    Si falla o es <= 0 → avisá y devolvé None.
    Ideal: try / except ValueError / else / finally (aunque finally solo imprima un tip).
    """
    raise NotImplementedError("Completá pedir_monto — Lección 05 + 03 + 13")


# --- Lección 05 + 06 (and/or/not) + 07 (append) + 10 ---
def agregar_gasto(lista: list[tuple[str, float]]) -> None:
    """
    Pedí nombre (.strip().title()) y monto (pedir_monto).
    Validá con and/or/not (ej. nombre no vacío y monto válido).
    Si OK → lista.append((nombre, monto)) y confirmá con print/f-string.
    """
    raise NotImplementedError("Completá agregar_gasto — Lección 05 + 06 + 07 + 10")


# --- Lección 01 + 06 + 07 (len) + 09 (for, enumerate) ---
def listar_gastos(lista: list[tuple[str, float]]) -> None:
    """
    Si len(lista) == 0 → mensaje y return.
    Si no → for i, (nombre, monto) in enumerate(lista, start=1): ...
    """
    raise NotImplementedError("Completá listar_gastos — Lección 01 + 07 + 09")


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
    raise NotImplementedError(
        "Completá mostrar_total_y_estadisticas — Lección 02 + 04 + 06 + 09"
    )


# --- Lección 05 (lower) + 06 + 09 ---
def buscar_gastos(lista: list[tuple[str, float]]) -> None:
    """
    Pedí palabra, filtrá con .lower() en el nombre.
    Recorré con for; si no hay coincidencias, avisá.
    """
    raise NotImplementedError("Completá buscar_gastos — Lección 05 + 06 + 09")


# --- Lección 03 (int) + 07 (pop/del) + 09 + 13 (IndexError / ValueError) ---
def eliminar_gasto(lista: list[tuple[str, float]]) -> None:
    """
    Listá gastos, pedí el número (1..n), convertí con int().
    Eliminá con pop(indice) o del lista[indice] (acordate: enumerate usa 1..n).
    Capturá ValueError e IndexError (o validá el rango antes).
    """
    raise NotImplementedError("Completá eliminar_gasto — Lección 03 + 07 + 09 + 13")


# --- Lección 02 (bool) + 06 (not) + 01 ---
def toggle_modo_ahorro() -> None:
    """
    Invertí modo_ahorro con not (global o devolvé el nuevo valor y asigná en main).
    Informá el estado actual con print.
    """
    raise NotImplementedError("Completá toggle_modo_ahorro — Lección 02 + 06")


# --- Lección 03 (int) + 08 (while/break/continue) + 06 + 09 (range) + 10 ---
def main() -> None:
    """
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
    raise NotImplementedError("Completá main — Lección 03 + 06 + 08 + 09 + 10 + 13")


if __name__ == "__main__":
    # --- Lección 01: bienvenida (sep / end de ejemplo) ---
    print("===", "Mini presupuesto", "===", sep=" ")
    print("Repaso lecciones 01-10 + 13. Enunciado: enunciado.md", end="\n\n")
    main()
