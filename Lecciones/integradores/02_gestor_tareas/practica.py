# ============================
# 🧪 Integrador 02 — Gestor de tareas (MEDIO)
# 📘 Enunciado: enunciado.md (misma carpeta)
# ============================
# Creá models.py y storage.py en esta misma carpeta.
# Importá desde ahí: GestorTareas, TareaInvalidaError, cargar_tareas, guardar_tareas.

from __future__ import annotations


def mostrar_menu() -> None:
    print(
        """
=== Gestor de tareas ===
1) Crear tarea
2) Listar todas
3) Listar pendientes
4) Marcar como hecha
5) Eliminar
6) Resumen
7) Salir
"""
    )


def main() -> None:
    # 1) from models import GestorTareas, TareaInvalidaError
    # 2) from storage import cargar_tareas, guardar_tareas
    # 3) gestor = GestorTareas(cargar_tareas())
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        if opcion == "7":
            print("Chau!")
            break
        # Implementá 1-6. Al mutar: guardar_tareas(gestor.to_list())
        # Capturá TareaInvalidaError y mostrá el mensaje.
        print(
            "Todavía no implementado. "
            "Leé enunciado.md y creá models.py / storage.py."
        )


if __name__ == "__main__":
    main()
