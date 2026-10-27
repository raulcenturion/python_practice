# Cómo Alembic ve los modelos y a qué base se conecta. Sección 18.
#
# logging.config.fileConfig → biblioteca estándar. Activa el log del alembic.ini.
# sqlalchemy.create_engine  → abre la base. El mismo que usa la app.
# sqlalchemy.pool.NullPool  → sin pool: Alembic abre, migra y cierra.
# alembic.context            → paquete alembic. La migración en curso.
# sqlmodel.SQLModel          → metadata con todas las tablas. Autogenerate
#   compara esto contra la base.
# settings                   → DATABASE_URL de app/core/config.py.
# app.models                 → importar los modelos llena SQLModel.metadata.
#
# La clase importa engine_from_config y no lo usa: la URL no sale del ini.
# También hace load_dotenv() y os.getenv("DATABASE_URL"). Si esa variable
# no está, getenv devuelve None y create_engine revienta.
# settings ya lee el .env y, si no hay variable, usa sqlite:///./devinotes.db.
# Sección 19: la clase reescribe postgres:// a postgresql+psycopg:// acá
# y otra vez en core/db.py. La reescritura está en normalize_database_url.
#
# Hay que correr los comandos desde devinotes/. Desde la raíz del repo,
# `app` es el paquete del blog.

from logging.config import fileConfig

import app.models  # noqa: F401
from alembic import context
from app.core.config import settings
from app.core.db import normalize_database_url
from sqlalchemy import create_engine, pool
from sqlmodel import SQLModel

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# La clase asigna target_metadata = SQLModel.metadata después de importar
# cada modelo a mano (User, Note, Label, NoteLabelLink, NoteShare, LabelShare).
# import app.models hace lo mismo: models/__init__.py los importa a todos.
target_metadata = SQLModel.metadata

database_url = normalize_database_url(settings.DATABASE_URL)


def run_migrations_offline() -> None:
    # offline: no abre la base. Imprime el SQL (`alembic upgrade head --sql`).
    # compare_type y compare_server_default hacen que autogenerate mire
    # el tipo de la columna y el default de la base, no solo tablas nuevas.
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # online: abre la base y aplica upgrade() o downgrade().
    # La clase pasa future=True. En SQLAlchemy 2 el engine ya es el nuevo.
    # Este proyecto usa SQLAlchemy 2.1, y ese argumento no hace falta.
    connectable = create_engine(database_url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
