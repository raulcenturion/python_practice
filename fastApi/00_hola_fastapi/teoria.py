# ============================
# 📘 FastAPI — Hola mundo
# ============================
# FastAPI = framework web para APIs en Python.
# Se apoya en:
#   - type hints → valida datos (Pydantic)
#   - async/await → I/O concurrente
#   - decoradores @app.get / @app.post → rutas (como en lección 14)
#
# Cómo correr este archivo (desde la raíz del repo):
#   .venv/bin/uvicorn fastApi.00_hola_fastapi.main:app --reload
# o:
#   ./r fastapi/00 teoria   # solo imprime tips; el server es con uvicorn
#
# Docs interactivas (con el server arriba):
#   http://127.0.0.1:8000/docs

print("--- Ideas clave FastAPI ---")
print("1) app = FastAPI() crea la aplicación")
print("2) @app.get('/') registra un endpoint GET")
print("3) return dict → FastAPI lo convierte a JSON")
print("4) /docs → Swagger UI automático")
print("5) uvicorn ... --reload → server de desarrollo")

print("\n--- Cómo probar sin levantar el server ---")
print("Usá TestClient (httpx) en practica.py / tests.")
print("Ejemplo mental:")
print("  from fastapi.testclient import TestClient")
print("  client = TestClient(app)")
print("  r = client.get('/')")
print("  assert r.status_code == 200")

# ============================
# 🔹 Resumen
# ============================
# - FastAPI + Uvicorn = app + servidor ASGI
# - Pydantic ya lo usaste en lección 20 (modelos / validación)
# - python-multipart → forms y uploads (más adelante)
# - httpx → cliente HTTP (tests y llamadas a otras APIs)
