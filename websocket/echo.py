# Eco de WebSocket. Sección 21, proyecto aparte del blog y de Devinote.
# Repo de la clase: ricardocuellar/Devtalles-Fastapi-Websocket, archivo echo.py.
# Un solo cliente manda texto y el servidor lo devuelve con el prefijo "Echo: ".
# No guarda nada y no se lo reenvía a nadie más. Sirve para probar el cable.
#
# Desde esta carpeta (websocket/):
#   ../.venv/bin/python -m uvicorn echo:app --host 127.0.0.1 --port 8003
# El comando también está en el README de la raíz, sección "Cómo levantar".
# Probar con un cliente:
#   websocat ws://127.0.0.1:8003/ws/echo
# El chat de la clase es main.py, en el puerto 8002. Este archivo no lo usa.
#
# fastapi.FastAPI    → la app. El mismo paquete del blog.
# fastapi.WebSocket  → la conexión que queda abierta. No es un request de una vez.
# WebSocketDisconnect → el cliente cerró. Starlette lo tira desde receive_text.

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="WebSocket echo")


@app.websocket("/ws/echo")
async def websocket_echo(websocket: WebSocket):
    # async porque accept, receive_text y send_text esperan al cliente.
    # Sin await, la función seguiría de largo y no habría mensaje.
    # accept() es el saludo: hasta acá el navegador está en "connecting".
    await websocket.accept()

    try:
        while True:
            # receive_text se queda esperando el próximo texto.
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        # La clase no tiene este except. El while True no termina solo:
        # cuando el cliente cierra, receive_text lanza y sin atraparlo
        # el proceso imprime el error. El eco no tiene a quién avisarle.
        return
