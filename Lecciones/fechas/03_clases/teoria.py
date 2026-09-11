# ============================
# 📘 Clases + cliente HTTP (repaso POO)
# ============================
# Idea: una clase agrupa datos + comportamiento.
# Acá repasamos POO y armamos un cliente simple para una API pública
# (jsonplaceholder), sin claves secretas.

import requests

# ============================
# 🔹 Clase básica (atributos + métodos)
# ============================
print("--- Clase Coche ---")


class Coche:
    # Atributo de CLASE: compartido por todas las instancias
    tipo = "vehículo de cuatro ruedas"
    ruedas = 4

    def __init__(self, marca: str, modelo: str, color: str):
        # Atributos de INSTANCIA: propios de cada objeto
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self) -> str:
        # Método de instancia: usa self para leer datos del objeto
        return f"El coche {self.marca} {self.modelo} arrancó!"


mi_coche = Coche("Toyota", "Corolla", "rojo")
otro = Coche("Ford", "Fiesta", "azul")
print(mi_coche.arrancar())
print(otro.arrancar())
print("tipo (clase):", Coche.tipo, "| ruedas:", mi_coche.ruedas)

# TIP:
# class Nombre:
#     def __init__(self, ...):
#         self.x = ...
#     def metodo(self):
#         return self.x

# ============================
# 🔹 Cliente HTTP encapsulado
# ============================
print("\n--- Clase JsonPlaceholderClient ---")


class JsonPlaceholderClient:
    """Cliente mínimo: guarda la base URL y ofrece get_post(id)."""

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        # Guardamos config en la instancia (no hardcodeamos en cada método)
        self.base_url = base_url.rstrip("/")

    def get_post(self, post_id: int) -> dict | None:
        # Armamos la URL y pedimos el recurso
        url = f"{self.base_url}/posts/{post_id}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # error HTTP → excepción
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None

    def list_titles(self, limit: int = 3) -> list[str]:
        url = f"{self.base_url}/posts"
        try:
            posts = requests.get(url, timeout=10).json()
            return [p["title"] for p in posts[:limit]]
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return []


client = JsonPlaceholderClient()
post = client.get_post(1)
if post:
    print("Post 1 title:", post["title"])
print("Primeros títulos:", client.list_titles(3))

# TIP — APIs con Bearer (solo patrón, no ejecutar con keys vacías):
# class ChatClient:
#     def __init__(self, api_key: str, url: str, model: str):
#         self.api_key = api_key
#         self.url = url
#         self.model = model
#     def call(self, prompt: str) -> str | None:
#         headers = {"Authorization": f"Bearer {self.api_key}"}
#         ...

# ============================
# 🔹 Resumen
# ============================
# - class + __init__ + self
# - atributo de clase vs de instancia
# - encapsular requests dentro de métodos de una clase
# - raise_for_status() + try/except RequestException
