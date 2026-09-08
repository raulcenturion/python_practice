# ============================
# 📘 Modelos de datos → camino a Pydantic / FastAPI
# ============================
# En FastAPI, los "modelos" validan y documentan el shape de request/response.
# Acá vemos la evolución: dict → dataclass → Pydantic BaseModel.
#
# Idea mental:
#   dict        → flexible, cero garantías
#   dataclass   → estructura clara en código, poca validación en runtime
#   Pydantic    → valida tipos/reglas al crear el objeto (como FastAPI)

from dataclasses import asdict, dataclass

print("--- Lección 20: Modelos de datos (Pydantic) ---")

# ============================
# 🔹 1) Dict: flexible, pero sin validación
# ============================
print("\n--- Dict (sin validación) ---")

# Un dict guarda claves → valores; cualquiera puede cambiar tipos a mano.
usuario_dict = {"nombre": "Raúl", "edad": 35, "activo": True}
print("dict:", usuario_dict)
# Problema: nadie te impide usuario_dict["edad"] = "treinta"

# ============================
# 🔹 2) dataclass: estructura clara (stdlib)
# ============================
print("\n--- dataclass (estructura clara) ---")


@dataclass
class UsuarioDC:
    # Campos tipados: ayudan al editor y a quien lee el código.
    nombre: str
    edad: int
    activo: bool = True          # valor por defecto si no lo pasás
    email: str | None = None     # opcional (puede ser None)


# Creamos una instancia: los args nombrados van a cada campo.
u1 = UsuarioDC(nombre="Raúl", edad=35, email="raul@mail.com")
print("dataclass:", u1)
# asdict convierte la dataclass a un dict “normal” (útil para JSON manual).
print("como dict:", asdict(u1))
# Sigue sin validar tipos en runtime: UsuarioDC(nombre="Raúl", edad="35") "pasa"

# ============================
# 🔹 3) Pydantic: validación en runtime (como en FastAPI)
# ============================
print("\n--- Pydantic BaseModel ---")
try:
    # BaseModel = modelo con validación; Field = reglas; EmailStr = email válido.
    # ValidationError se lanza si los datos no cumplen.
    from pydantic import BaseModel, EmailStr, Field, ValidationError
except ImportError:
    print(
        "aviso:",
        "⚠️ pydantic no está instalado. "
        "Activá el venv e instalá: pip install 'pydantic[email]'. "
        "Luego: pip freeze > requirements.txt",
    )
    raise SystemExit(0)


class Usuario(BaseModel):
    # Field(min_length=1) → nombre no puede ser ""
    nombre: str = Field(min_length=1)
    # ge=0, le=120 → edad entre 0 y 120 inclusive
    edad: int = Field(ge=0, le=120)
    activo: bool = True
    # EmailStr exige formato de email (requiere el extra [email] / email-validator)
    email: EmailStr


# Creación válida: Pydantic valida y guarda los campos tipados.
usuario = Usuario(nombre="Raúl", edad=35, email="raul@mail.com")
print("pydantic model:", usuario)
# model_dump() → dict listo para JSON / APIs
print("model_dump():", usuario.model_dump())
# model_dump_json() → string JSON directamente
print("model_dump_json():", usuario.model_dump_json())

# ============================
# 🔹 Coerción / validación desde datos “tipo JSON”
# ============================
print("\n--- Coerción / validación desde JSON-like ---")

# En APIs la edad suele llegar como string ("28").
# model_validate acepta un dict y COERCE tipos cuando puede (str→int).
desde_api = Usuario.model_validate(
    {"nombre": "Ana", "edad": "28", "email": "ana@mail.com"}
)
print("desde JSON-like:", desde_api)

# ============================
# 🔹 Error de validación (esperado)
# ============================
print("\n--- ValidationError (esperado) ---")

try:
    # nombre vacío, edad negativa, email inválido → debe fallar.
    Usuario(nombre="", edad=-1, email="no-es-email")
except ValidationError as e:
    # e.errors() es una lista de dicts con type, loc, msg, etc.
    # Mostramos el primero: tipo de error y ubicación del campo.
    print("error type:", e.errors()[0]["type"], "→", e.errors()[0]["loc"])

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
# - dict: rápido, sin garantías de tipos ni reglas
# - dataclass: tipado estructural (desarrollo), poca validación runtime
# - Pydantic BaseModel: validación + serialización → base de FastAPI
# - Field / EmailStr: reglas de negocio sobre cada campo
# - model_dump / model_dump_json: modelo → dict / string JSON
# - model_validate: dict (p.ej. JSON de API) → modelo validado
# - ValidationError: datos inválidos; en FastAPI → 422
# 💡 En FastAPI, tipar el parámetro con tu BaseModel valida el body solo
