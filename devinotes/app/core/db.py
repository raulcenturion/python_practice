# Motor y sesión de Devinote. Sección 16.
#
# typing.Iterator     → biblioteca estándar. get_session es un generador:
#                       yield entrega la sesión y el with la cierra.
# sqlmodel.SQLModel   → paquete sqlmodel. La clase madre de las tablas.
#                       metadata junta todas las que heredan de SQLModel.
# sqlmodel.Session    → la charla con la base. Es la Session de SQLAlchemy,
#                       con exec() en vez de execute() para las consultas del ORM.
# sqlmodel.create_engine
#                     → el mismo create_engine de SQLAlchemy. Abre la base
#                       a partir de la URL (sqlite, postgres, ...).

from collections.abc import Iterator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

# echo=False no imprime el SQL. La clase lo deja así.
# check_same_thread=False solo en SQLite: FastAPI puede usar la conexión
# en otro hilo, y SQLite por defecto lo prohíbe. En otra base el dict queda vacío.
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
)


def init_db() -> None:
    # La clase llama create_all sin importar los modelos. Si nadie importó
    # user.py, note.py, label.py y share.py, metadata está vacío y no crea nada.
    # import app.models registra las tablas en SQLModel.metadata.
    import app.models  # noqa: F401

    # dev: en un proyecto real las tablas las arma una migración, no esto.
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    # with cierra la sesión al salir, también si la ruta falla.
    # api/deps.py hace yield from get_session() para que el with dure el request.
    # exec() de esta Session ya devuelve ScalarResult: no se le encadena .scalars().
    with Session(engine) as session:
        yield session
