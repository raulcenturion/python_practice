# ============================
# 📘 Modelos de datos → camino a Pydantic / FastAPI
# ============================
# En FastAPI, los "modelos" validan y documentan el shape de request/response.
# Acá vemos la evolución: dict → dataclass → Pydantic BaseModel.

from dataclasses import dataclass, asdict
from typing import Optional

# ============================
# 🔹 1) Dict: flexible, pero sin validación
# ============================
usuario_dict = {"nombre": "Raúl", "edad": 35, "activo": True}
print("dict:", usuario_dict)
# Problema: nadie te impide usuario_dict["edad"] = "treinta"

# ============================
# 🔹 2) dataclass: estructura clara (stdlib)
# ============================


@dataclass
class UsuarioDC:
    nombre: str
    edad: int
    activo: bool = True
    email: Optional[str] = None


u1 = UsuarioDC(nombre="Raúl", edad=35, email="raul@mail.com")
print("dataclass:", u1)
print("como dict:", asdict(u1))
# Sigue sin validar tipos en runtime: UsuarioDC(nombre="Raúl", edad="35") "pasa"

# ============================
# 🔹 3) Pydantic: validación en runtime (como en FastAPI)
# ============================
try:
    from pydantic import BaseModel, EmailStr, Field, ValidationError
except ImportError:
    print(
        "\n⚠️ pydantic no está instalado.\n"
        "   Activá el venv e instalá: pip install 'pydantic[email]'\n"
        "   Luego: pip freeze > requirements.txt"
    )
    raise SystemExit(0)


class Usuario(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(ge=0, le=120)
    activo: bool = True
    email: EmailStr


# Creación válida
usuario = Usuario(nombre="Raúl", edad=35, email="raul@mail.com")
print("\npydantic model:", usuario)
print("model_dump():", usuario.model_dump())          # → dict (JSON-serializable)
print("model_dump_json():", usuario.model_dump_json())  # → string JSON

# Coerción / validación
# edad llega como string desde un JSON de API → Pydantic la convierte a int
desde_api = Usuario.model_validate(
    {"nombre": "Ana", "edad": "28", "email": "ana@mail.com"}
)
print("desde JSON-like:", desde_api)

# Error de validación
try:
    Usuario(nombre="", edad=-1, email="no-es-email")
except ValidationError as e:
    print("\nValidationError (esperado):")
    print(e.errors()[0]["type"], "→", e.errors()[0]["loc"])

# ============================
# 🔹 Analogía FastAPI
# ============================
# @app.post("/users")
# async def create_user(user: Usuario):  # FastAPI usa el modelo para validar el body
#     return user
#
# El request JSON se transforma automáticamente en Usuario.
# Si falla la validación → HTTP 422.

# ============================
# 🔹 Resumen
# ============================
# - dict: rápido, sin garantías
# - dataclass: tipado estructural (desarrollo), poca validación runtime
# - Pydantic BaseModel: validación + serialización → base de FastAPI
# - model_dump / model_validate: puente dict ↔ modelo
