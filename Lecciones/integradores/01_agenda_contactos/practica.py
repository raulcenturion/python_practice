# ============================
# 🧪 Integrador 01 — Agenda de contactos (FÁCIL)
# 📘 Enunciado: enunciado.md (misma carpeta)
# ============================

from __future__ import annotations

from pathlib import Path

ARCHIVO = Path(__file__).with_name("contactos.json")

_MSG = "Completá esta función. Guía: enunciado.md"


def cargar_contactos() -> list[dict]:
    """Cargá contactos desde ARCHIVO. Si no existe, devolvés []."""
    raise NotImplementedError(_MSG)


def guardar_contactos(contactos: list[dict]) -> None:
    """Guardá la lista en ARCHIVO con indent=2 y ensure_ascii=False."""
    raise NotImplementedError(_MSG)


def agregar_contacto(contactos: list[dict]) -> None:
    """Pedí datos por input, validá edad, agregá a la lista y guardá."""
    raise NotImplementedError(_MSG)


def listar_contactos(contactos: list[dict]) -> None:
    """Imprimí todos los contactos. Si está vacía, avisá."""
    raise NotImplementedError(_MSG)


def buscar_contacto(contactos: list[dict]) -> None:
    """Pedí un nombre y mostrá coincidencias (case-insensitive)."""
    raise NotImplementedError(_MSG)


def eliminar_contacto(contactos: list[dict]) -> None:
    """Pedí un nombre, eliminá el primero que coincida y guardá."""
    raise NotImplementedError(_MSG)


def mostrar_menu() -> None:
    print(
        """
=== Agenda de contactos ===
1) Agregar
2) Listar
3) Buscar
4) Eliminar
5) Salir
"""
    )


def main() -> None:
    """Menú CLI. Cuando tengas cargar_contactos, usala en lugar de []."""
    contactos: list[dict] = []

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            listar_contactos(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("Chau!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
