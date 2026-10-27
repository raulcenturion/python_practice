# Mini chat por WebSocket. Sección 21, proyecto aparte.
# Repo: ricardocuellar/Devtalles-Fastapi-Websocket, archivo main.py.
# El front (HTML, CSS y JS) sale de este gist y vive en client/:
# https://gist.github.com/ricardocuellar/5e98670310b4095670e12fe3c83bd2d6
#
# Desde esta carpeta (websocket/):
#   ../.venv/bin/python -m uvicorn main:app --host 127.0.0.1 --port 8002
# Página: http://127.0.0.1:8002/
# Este comando, el eco, el blog y Devinote están juntos en el README
# de la raíz, sección "Cómo levantar".
# El blog está en el 8000 y Devinote en el 8001. La clase apunta el JS a
# ws://localhost:8000. Acá el JS usa el mismo host que sirvió la página.
#
# Un solo proceso de uvicorn. ConnectionManager es un dict en memoria.
# Si se levanta con varios workers de gunicorn, cada worker tiene el suyo
# y un usuario no ve los mensajes del otro. Por eso esta clase va con uvicorn.
#
# fastapi.FastAPI / WebSocket / WebSocketDisconnect → igual que en echo.py.
# FileResponse → starlette, reexportado por FastAPI. Devuelve un archivo.

from pathlib import Path

from fastapi.responses import FileResponse

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# client/ está al lado de este archivo, no depende de la carpeta desde donde se corre.
CLIENT = Path(__file__).resolve().parent / "client"

app = FastAPI(title="MiniChat WebSocket")


class ConnectionManager:
    # Guarda cada socket abierto y el nombre que mandó en el query param.
    # La clase anota Dict[WebSocket, str], de typing.
    # dict[WebSocket, str] es el mismo tipo.
    def __init__(self) -> None:
        self.active_connections: dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket, username: str) -> None:
        # accept() abre el socket. Después se anota y se avisa a todos,
        # incluido el que acaba de entrar.
        await websocket.accept()
        self.active_connections[websocket] = username
        await self.broadcast(f"🔵 {username} se ha conectado")

    async def disconnect(self, websocket: WebSocket) -> None:
        # pop saca la clave y no falla si ya no está.
        # get da "Usuario" si el socket no llegó a anotarse.
        username = self.active_connections.get(websocket, "Usuario")
        self.active_connections.pop(websocket, None)
        await self.broadcast(f"🔴 {username} se ha desconectado")

    async def broadcast(self, message: str) -> None:
        # list() copia las claves. Si durante el envío alguien se desconecta
        # y se modifica el dict, recorrerlo directo revienta.
        for connection in list(self.active_connections.keys()):
            await connection.send_text(message)


# Una sola instancia para toda la app. Todos los /ws/chat comparten este dict.
manager = ConnectionManager()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket, username: str) -> None:
    # username no va en el path. FastAPI lo lee del query:
    #   ws://127.0.0.1:8002/ws/chat?username=Ana
    # Si no viene, la conexión se rechaza.
    await manager.connect(websocket, username)

    try:
        while True:
            data = await websocket.receive_text()
            # El nombre sale del query, no del texto. El cliente no puede
            # cambiar de identidad escribiendo otro nombre en el mensaje.
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


# La clase no sirve el HTML: el gist se abre como archivo suelto.
# El HTML de ese gist apunta a styles.css y no incluye el script.
# Acá la misma app entrega los tres archivos, con los nombres del gist,
# para que la página y el socket salgan del mismo puerto.
@app.get("/")
def chat_page() -> FileResponse:
    return FileResponse(CLIENT / "indexClient.html")


@app.get("/cssClient.css")
def chat_css() -> FileResponse:
    return FileResponse(CLIENT / "cssClient.css", media_type="text/css")


@app.get("/scriptClient.js")
def chat_js() -> FileResponse:
    return FileResponse(CLIENT / "scriptClient.js", media_type="text/javascript")
