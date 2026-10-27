// Cliente del chat. Gist de la sección 21, archivo scriptClient.js.
// Corre en el navegador. No es Python.
//
// WebSocket es del navegador. Abre una conexión que queda viva:
// el servidor puede mandar texto sin que el cliente lo pida.
// HTTP normal es al revés: el cliente pide, el servidor responde, se cierra.

const messagesDiv = document.getElementById("messages");
const input = document.getElementById("msgInput");
const button = document.getElementById("sendBtn");
const usernameLabel = document.getElementById("usernameLabel");

// La clase solo usa prompt(). Si la página se abre con ?username=Ana,
// se usa ese nombre y no aparece el cuadro. Sirve para dos pestañas distintas.
const params = new URLSearchParams(window.location.search);
let username = params.get("username") || prompt("Escribe tu nombre de usuario:");
if (!username || !username.trim()) {
  const randomId = Math.floor(Math.random() * 9999)
    .toString()
    .padStart(4, "0");
  username = `Invitado-${randomId}`;
}
username = username.trim();
usernameLabel.textContent = username;

// La clase fija ws://localhost:8000. En este repo el 8000 es el blog.
// location.host es el host y el puerto que sirvieron esta página (8002).
const wsUrl =
  `${location.protocol === "https:" ? "wss:" : "ws:"}//${location.host}` +
  `/ws/chat?username=${encodeURIComponent(username)}`;
const ws = new WebSocket(wsUrl);

// onopen: el servidor ya hizo accept().
ws.onopen = () => {
  addSystemMessage("✅ Conectado al servidor");
};

// onmessage: llegó un texto. El servidor manda tres formas:
//   "🔵 Ana se ha conectado" / "🔴 Ana se ha desconectado"  → sistema
//   "Ana: hola"                                              → burbuja
ws.onmessage = (event) => {
  const text = event.data;
  // split en el primer ":". El resto se vuelve a unir por si el mensaje
  // también tenía dos puntos. "Ana: hola: mundo" sigue siendo de Ana.
  const [msgUser, ...rest] = text.split(":");

  if (text.startsWith("🔵") || text.startsWith("🔴")) {
    addSystemMessage(text);
  } else if (rest.length > 0) {
    const isSelf = msgUser.trim() === username;
    addChatMessage(text, isSelf);
  } else {
    addChatMessage(text, false);
  }
};

// onclose: el socket se cortó. El servidor, en ese caso, avisa a los demás.
ws.onclose = () => {
  addSystemMessage("🔴 Desconectado del servidor");
};

button.onclick = sendMessage;

input.addEventListener("keyup", (e) => {
  if (e.key === "Enter") {
    sendMessage();
  }
});

function sendMessage() {
  const text = input.value.trim();
  // No se manda vacío. El servidor igual reenviaría lo que reciba.
  if (!text || ws.readyState !== WebSocket.OPEN) return;
  ws.send(text);
  input.value = "";
}

function addChatMessage(text, isSelf) {
  const div = document.createElement("div");
  // msg-self a la derecha, msg-other a la izquierda. Las clases están en el CSS.
  div.classList.add("msg", isSelf ? "msg-self" : "msg-other");
  div.textContent = text;
  messagesDiv.appendChild(div);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function addSystemMessage(text) {
  const div = document.createElement("div");
  div.classList.add("msg", "msg-system");
  div.textContent = text;
  messagesDiv.appendChild(div);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
