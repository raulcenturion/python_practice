# La fila que se guarda cuando GitHub avisa que se abrió un issue.
# SQLModel junta el modelo de Pydantic y la tabla de SQLAlchemy.

from datetime import datetime

from sqlmodel import Field, SQLModel


class Issue(SQLModel, table=True):
    """Un issue de GitHub guardado en sqlite."""

    # table=True crea la tabla "issue". Sin eso, SQLModel solo valida JSON.
    # id lo asigna sqlite. int | None es el optional de Python 3.10+.
    # La clase vieja escribe Optional[int], de typing.
    id: int | None = Field(default=None, primary_key=True)
    # La clase anota github_issue_id: int, sin unique.
    # GitHub reenvía el mismo evento si tarda la respuesta.
    # Sin unique, cada reenvío inserta otra fila igual.
    github_issue_id: int = Field(unique=True)
    title: str
    url: str
    state: str
    # datetime es de la stdlib. GitHub manda la fecha en texto;
    # github_webhook.py la convierte antes de armar este objeto.
    created_at: datetime
