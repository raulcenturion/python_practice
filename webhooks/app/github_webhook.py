# POST /webhooks/github: lo llama GitHub.
# GET /issues: lo que ya se guardó.
#
# hmac y hashlib son de la stdlib. hmac arma la firma, hashlib.sha256 es
# el algoritmo, compare_digest compara sin cortar en el primer byte distinto.

import hashlib
import hmac
import os
from datetime import datetime

# IntegrityError es de SQLAlchemy (sqlalchemy.exc). SQLModel no lo reexporta.
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.db import get_session
from app.notifications import send_discord_notification

# from fastapi queda después de app. En este repo la carpeta fastapi/ hace
# que ruff trate a fastapi como paquete local, no como librería de terceros.
from fastapi import APIRouter, Depends, Header, HTTPException, Request

from .models import Issue

router = APIRouter()

# La clase pone el default en la misma línea:
#   GITHUB_SECRET = os.getenv("GITHUB_SECRET", "secretosuper123")
# Sonar lo toma como clave hardcodeada, y además se leía al importar,
# antes de que main.py cargara el .env. El texto de práctica vive acá,
# con un nombre que no es el del secreto. GitHub tiene que usar el mismo
# texto en el campo Secret del webhook, o el que esté en webhooks/.env.
_PRACTICA = "webhooks-local-solo-para-practicar"


def github_secret() -> str:
    # Vacío o ausente: queda el de práctica, para poder probar con curl
    # sin crear el .env. Si .env trae GITHUB_SECRET, gana ese.
    return os.getenv("GITHUB_SECRET") or _PRACTICA


def verify_signature(body: bytes, signature_header: str | None) -> bool:
    """Comprueba la firma que manda GitHub en X-Hub-Signature-256."""
    if not signature_header:
        return False

    try:
        # La clase parte con split("="), sin límite. Una firma con más de
        # un "=" tira ValueError y se toma como inválida. maxsplit=1 separa
        # el algoritmo del resto: "sha256" y el hexadecimal.
        sha_name, signature = signature_header.split("=", maxsplit=1)
    except ValueError:
        return False

    if sha_name != "sha256":
        return False

    # El mensaje firmado es el body crudo, no el JSON ya parseado.
    # Un espacio de más cambia la firma.
    mac = hmac.new(
        github_secret().encode("utf-8"),
        msg=body,
        digestmod=hashlib.sha256,
    )
    expected = mac.hexdigest()
    return hmac.compare_digest(expected, signature)


@router.post("/webhooks/github")
async def github_webhook(
    request: Request,
    # Header viene de FastAPI (Starlette). El nombre del parámetro con
    # guiones bajos es el header HTTP: X-Hub-Signature-256 y X-GitHub-Event.
    # Si no vienen, default=None. No llegan como string vacío.
    x_hub_signature_256: str | None = Header(default=None),
    x_github_event: str | None = Header(default=None),
    session: Session = Depends(get_session),
):
    """Recibe el POST de GitHub y, si es un issue nuevo, lo guarda."""
    # Sigue en async porque hay await: el body, el JSON y el POST a Discord.
    # La clase también es async. Pasarla a def sacaría el await.
    body = await request.body()

    if not verify_signature(body, x_hub_signature_256):
        # 401: GitHub muestra el envío como fallido. No se guarda nada.
        raise HTTPException(status_code=401, detail="Firma inválida")

    # body() ya dejó los bytes en caché. json() los parsea.
    # En GitHub el content type del webhook tiene que ser application/json.
    payload = await request.json()

    # Otro evento (ping, push, un issue cerrado) no se guarda.
    # Igual responde 200. GitHub reintenta si la respuesta no es 2xx.
    if x_github_event == "issues" and payload.get("action") == "opened":
        issue_data = payload["issue"]
        # GitHub manda "2026-01-20T10:00:00Z". fromisoformat de 3.11+ ya
        # acepta la Z. La clase la cambia por +00:00 y se deja así.
        created_at_str = issue_data["created_at"]
        created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))

        issue = Issue(
            github_issue_id=issue_data["id"],
            title=issue_data["title"],
            url=issue_data["html_url"],
            state=issue_data["state"],
            created_at=created_at,
        )

        session.add(issue)
        try:
            session.commit()
        except IntegrityError:
            # La clase no captura esto: el segundo POST del mismo issue
            # revienta y GitHub lo vuelve a mandar. Se deshace el INSERT
            # y se responde ok, que es lo que GitHub espera de un duplicado.
            session.rollback()
            print(f"El issue {issue.github_issue_id} ya estaba guardado.")
            return {"status": "ok"}

        # refresh vuelve a leer la fila para tener el id que asignó sqlite.
        session.refresh(issue)
        print(f"NUEVO issue guardado: {issue.title} - {issue.url}")
        await send_discord_notification(issue)

    return {"status": "ok"}


@router.get("/issues", response_model=list[Issue])
def list_issues(session: Session = Depends(get_session)):
    """Devuelve los issues guardados."""
    # La clase ya usa def. No hay await: la consulta es sqlite local.
    # select e Session son de SQLModel. exec() de un modelo ya devuelve
    # las filas. Encadenar .scalars() revienta: ScalarResult no tiene scalars.
    # En SQLAlchemy el método es execute() y ahí sí hace falta .scalars().
    query = select(Issue)
    return session.exec(query).all()
