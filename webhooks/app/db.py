# SQLite de los issues que avisa GitHub.
# La clase titula este archivo "Fastapi library". Los imports son de SQLModel.

from collections.abc import Iterator

from sqlmodel import Session, SQLModel, create_engine

# La clase fija esta URL y no lee DATABASE_URL del entorno.
# Se deja así. El blog y Devinote ya usan esa variable: si esta app la
# leyera, un shell con el .env del blog escribiría los issues en blog.db.
# El archivo queda en la carpeta desde donde se corre el comando.
# Hay que correr desde webhooks/. *.db está en el .gitignore de la raíz.
DATABASE_URL = "sqlite:///./issues.db"

# La clase: engine = create_engine(DATABASE_URL, echo=True)
# echo=True imprime cada SQL en la terminal. Sirve para ver el INSERT.
# check_same_thread=False no está en la clase. El POST es async y la
# sesión la abre una dependencia sync, en otro hilo. Sin esto, SQLite
# rechaza usar la conexión en el hilo del request.
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
)


def init_db() -> None:
    """Crea las tablas que todavía no existen."""
    # SQLModel.metadata viene de SQLAlchemy. create_all no altera una tabla
    # que ya está. Si cambia el modelo, hay que borrar issues.db.
    # Devinote dejó esto y pasó a Alembic. Esta clase no tiene migraciones.
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    """Abre una sesión y la cierra al terminar el request."""
    # La clase no anota el retorno. Iterator, de collections.abc, dice que
    # esto es un generador. La forma vieja es typing.Iterator.
    # FastAPI entra, recibe la sesión y, al salir del request, sigue después
    # del yield: el with cierra la sesión.
    # next(get_session()) la cerraría antes de terminar el request.
    with Session(engine) as session:
        yield session
