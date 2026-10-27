# python -m app, parado en devinotes/.
# Sección 16: init_db() hacía create_all y el print decía
# "Tablas de Devinote creadas".
# Sección 18: init_db queda en pass. Las tablas las arma Alembic.
# Los comandos están en app/core/db.py.

from app.core.db import init_db


def main() -> None:
    init_db()
    print("init_db ya no crea tablas. Desde devinotes/: alembic upgrade head")


if __name__ == "__main__":
    main()
