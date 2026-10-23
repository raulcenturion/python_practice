# python -m app, parado en devinotes/. Crea las tablas y termina.
# La clase de esta sección no trae este archivo: el árbol de GitHub
# llega hasta core, models y repositories. Sirve para comprobar que
# el metadata de SQLModel tiene las tablas y que create_all corre.

from app.core.db import init_db


def main() -> None:
    init_db()
    print("Tablas de Devinote creadas")


if __name__ == "__main__":
    main()
