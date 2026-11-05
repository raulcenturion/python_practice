# Cuenta en SQLModel. El enunciado está en enunciado.md.
# Correr: .venv/bin/python fastApi/practicas/02_cuentas/practica.py
#
# SQLModel junta la tabla de SQLAlchemy y la validación de Pydantic.
# sqlite:// es una base en memoria: se borra al cerrar el proceso.
# https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/

from sqlmodel import Field, Session, SQLModel, create_engine


class Cuenta(SQLModel, table=True):
    __tablename__ = "cuenta_practica_banco"
    id: int | None = Field(default=None, primary_key=True)
    titular: str
    saldo_centavos: int = 0


engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)


def debitar(session: Session, cuenta_id: int, centavos: int) -> int:
    """Resta centavos si hay saldo. Si no se puede, devuelve -1.

    Ejemplo: saldo 1000 y débito 400 → 600.
    """
    raise NotImplementedError


def _ejemplo():
    with Session(engine) as session:
        cuenta = Cuenta(titular="Ana", saldo_centavos=1000)
        session.add(cuenta)
        session.commit()
        session.refresh(cuenta)
        print("ejemplo", cuenta.id, cuenta.titular, cuenta.saldo_centavos)
        return cuenta.id


def _correr():
    cuenta_id = _ejemplo()
    with Session(engine) as session:
        saldo = debitar(session, cuenta_id, 400)
        segundo = debitar(session, cuenta_id, 700)
    if saldo != 600 or segundo != -1:
        raise AssertionError(f"debitar devolvió {saldo} y {segundo}")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Lecciones"))
    from menu_extra import abrir

    abrir([("debitar", _correr)], globals())
