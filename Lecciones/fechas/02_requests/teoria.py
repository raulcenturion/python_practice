# ============================
# 📘 HTTP / APIs con Python
# ============================
# Dos caminos:
#   1) urllib (stdlib) → sin instalar nada
#   2) requests (pip)  → API más cómoda (recomendado)
#
# Usamos jsonplaceholder.typicode.com (API de prueba pública, sin API key).
# Tip: NUNCA subas claves reales al repo. Usá variables de entorno.

import json
import urllib.error
import urllib.request

# ============================
# 🔹 GET sin dependencias (urllib)
# ============================
print("--- GET con urllib (stdlib) ---")

url = "https://jsonplaceholder.typicode.com/posts/1"
# urlopen abre la URL; read() trae bytes; decode → str; loads → dict
try:
    with urllib.request.urlopen(url, timeout=10) as response:
        raw = response.read().decode("utf-8")
        data = json.loads(raw)
        print("status implícito OK")
        print("title:", data["title"])
except urllib.error.URLError as e:
    # Tip: en algunos macOS, urllib falla por certificados SSL.
    # Si ves CERTIFICATE_VERIFY_FAILED, usá requests (más abajo) o instalá certs.
    print("Error de red/URL:", e)

# TIP / patrón:
# with urllib.request.urlopen(url, timeout=10) as r:
#     data = json.loads(r.read().decode("utf-8"))

# ============================
# 🔹 GET con requests
# ============================
print("\n--- GET con requests ---")

try:
    import requests
except ImportError:
    requests = None
    print("aviso: pip install requests")

if requests is not None:
    # .get → Response; .status_code; .json() parsea el body
    r = requests.get(url, timeout=10)
    print("status_code:", r.status_code)
    print("title:", r.json()["title"])

    # ============================
    # 🔹 POST (crear recurso de prueba)
    # ============================
    print("\n--- POST con requests ---")
    # json=... manda el body como JSON y pone Content-Type automáticamente
    try:
        r = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json={"title": "foo", "body": "bar", "userId": 1},
            timeout=10,
        )
        print("POST status:", r.status_code)  # suele ser 201
        print("respuesta id:", r.json().get("id"))
    except requests.exceptions.RequestException as e:
        print("Error POST:", e)

    # ============================
    # 🔹 PUT (actualizar)
    # ============================
    print("\n--- PUT con requests ---")
    try:
        r = requests.put(
            "https://jsonplaceholder.typicode.com/posts/1",
            json={"title": "foo", "body": "bar", "userId": 1},
            timeout=10,
        )
        print("PUT status:", r.status_code)
    except requests.exceptions.RequestException as e:
        print("Error PUT:", e)

# ============================
# 🔹 APIs con API key (solo patrón, NO llamar con claves falsas)
# ============================
print("\n--- Patrón para APIs con Bearer token (comentado) ---")
# Tip: guardá la key en una variable de entorno, no en el código.
#
# import os
# import requests
#
# def call_chat_api(api_key: str, prompt: str) -> dict:
#     url = "https://api.openai.com/v1/chat/completions"  # ejemplo
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}",
#     }
#     payload = {
#         "model": "gpt-4o-mini",
#         "messages": [{"role": "user", "content": prompt}],
#     }
#     r = requests.post(url, headers=headers, json=payload, timeout=30)
#     r.raise_for_status()
#     return r.json()
#
# key = os.environ.get("OPENAI_API_KEY")
# if key:
#     print(call_chat_api(key, "Hola"))

print("Usá jsonplaceholder para practicar. APIs de pago → solo con env vars.")

# ============================
# 🔹 Resumen
# ============================
# - urllib: stdlib, más verboso
# - requests.get/post/put + .json() + timeout
# - try/except RequestException o URLError
# - Nunca hardcodear API keys en el código
