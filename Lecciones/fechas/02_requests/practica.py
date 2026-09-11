# ============================
# 📝 Ejercicios: Requests / APIs
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

# 🔸 Ejemplo (urllib + JSON):
import json
import urllib.error
import urllib.request

url_ejemplo = "https://jsonplaceholder.typicode.com/posts/1"
try:
    with urllib.request.urlopen(url_ejemplo, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
        print("Ejemplo title:", data["title"])
except urllib.error.URLError as e:
    # Tip: si es SSL en macOS, el ejercicio 2 (requests) suele funcionar igual.
    print("Ejemplo falló (red/SSL?):", e)

# ============================
# ENUNCIADOS
# ============================


def ejercicio_1_urllib() -> None:
    # ENUNCIADO:
    # Usá urllib.request para obtener
    # https://jsonplaceholder.typicode.com/posts/1
    # Parseá el JSON e imprimí el title.
    #
    # Guía:
    # 1) urllib.request.urlopen(url)
    # 2) read().decode("utf-8")
    # 3) json.loads(...)
    # 4) print(data["title"])
    #
    # TIP: mirá el ejemplo de arriba.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1 (urllib)")


def ejercicio_2_requests() -> None:
    # ENUNCIADO:
    # Con requests, pedí la misma URL e imprimí status_code y el body (json).
    #
    # Guía:
    # import requests
    # r = requests.get(url, timeout=10)
    # print(r.status_code, r.json())
    #
    # TIP: si falta → pip install requests

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2 (requests)")


def ejercicio_3_lista() -> None:
    # ENUNCIADO:
    # Pedí https://jsonplaceholder.typicode.com/posts
    # Mostrá los títulos de los 3 primeros.
    #
    # TIP:
    # posts = requests.get(url).json()  # lista de dicts
    # for p in posts[:3]:
    #     print(p["title"])

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3 (lista)")


def ejercicio_4_errores() -> None:
    # ENUNCIADO:
    # Intentá una URL inválida y capturá el error
    # (URLError o requests.exceptions.RequestException).
    # Imprimí un mensaje claro.
    #
    # TIP:
    # try:
    #     requests.get("http://no-existe-xyz.invalid", timeout=5)
    # except requests.exceptions.RequestException as e:
    #     print("Falló:", e)

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4 (errores)")


if __name__ == "__main__":
    print("--- Práctica 02 requests ---")
    for fn in (
        ejercicio_1_urllib,
        ejercicio_2_requests,
        ejercicio_3_lista,
        ejercicio_4_errores,
    ):
        try:
            fn()
            print(f"✅ {fn.__name__}")
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
