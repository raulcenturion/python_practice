# Aviso opcional a Discord. Si no hay URL, el issue igual se guarda.
# httpx es el cliente HTTP. El import es httpx, el paquete también.

import os

import httpx

from .models import Issue


def discord_webhook_url() -> str:
    # La clase lee esto al importar el módulo:
    #   DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
    # main.py cargaba el .env después de ese import, así que la URL
    # quedaba vacía aunque el archivo existiera.
    # os.getenv es de la stdlib. Se lee en cada aviso, ya con el .env cargado.
    # Vacío significa "no hay canal": no es un error.
    return os.getenv("DISCORD_WEBHOOK_URL", "")


async def send_discord_notification(issue: Issue) -> None:
    # La clase escribe "notificacio2n" en el docstring.
    """Envía una notificación a un canal de Discord."""
    url = discord_webhook_url()
    if not url:
        print("Discord webhook no configurado. Saltando notificación.")
        return

    # El texto que ve el canal. Discord interpreta **como negrita**.
    content = (
        f"NUEVO issue creado en Github:\n"
        f"**{issue.title}**\n"
        f"📎 {issue.url}\n"
        f"📁 Estado: {issue.state}"
    )

    # AsyncClient es la versión async de httpx. El async with cierra el cliente
    # al salir, también si el POST falla. La clase abre uno por cada issue.
    async with httpx.AsyncClient() as client:
        try:
            # POST a la URL del canal. timeout=10 corta si Discord no responde.
            # json= arma el body y el header Content-Type.
            response = await client.post(
                url,
                json={"content": content},
                timeout=10,
            )
            # 4xx y 5xx pasan a ser una excepción. Sin esto, un 404 parecería enviado.
            response.raise_for_status()
            print("Notificación enviada a Discord")
        # La clase captura Exception. Eso también esconde un error nuestro
        # al armar el texto. httpx.HTTPError es la familia de esta librería:
        # no hay red, el host no responde, o Discord contesta 4xx/5xx.
        except httpx.HTTPError as error:
            print(f"Error al enviar notificación a Discord: {error}")
