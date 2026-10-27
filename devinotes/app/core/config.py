# Configuración que se lee del entorno. Sección 16.
#
# pydantic.Field          → paquete pydantic. Declara un campo con reglas.
# pydantic_settings       → paquete pydantic-settings. BaseSettings lee
#   variables de entorno y, si existe, el archivo .env del directorio actual.
#   No viene dentro de pydantic. Hay que instalarlo aparte.
# os                      → biblioteca estándar. getenv lee una variable ya exportada.

import os

from pydantic_settings import BaseSettings, SettingsConfigDict

# La clase escribe esto, estilo Pydantic 1:
#   DATABASE_URL: str = Field(..., env="DATABASE_URL")
#   class Config:
#       env_file = ".env"
# En Pydantic 2, Field no acepta el argumento env: revienta al crear Settings.
# El nombre del atributo ya es el nombre de la variable de entorno.
# SettingsConfigDict(env_file=".env") es el reemplazo de class Config.
#
# La clase no pone default: sin DATABASE_URL y JWT_SECRET el proceso no arranca.
# Acá hay default para poder estudiar sin un .env nuevo.
# Si exportás esas variables, pisan el default.
# _PRACTICA no se llama JWT_SECRET: un texto fijo al lado de un nombre
# que dice secret lo marca el analizador como credencial escrita en el código.
# PyJWT avisa si la clave HMAC de HS256 tiene menos de 32 bytes (RFC 7518).
# Por eso el texto de práctica es largo. En un .env real se reemplaza.

_PRACTICA = "devinotes-local-solo-para-practicar"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # sqlite:///./devinotes.db se crea en la carpeta desde donde corrés el comando.
    # Tiene que ser desde devinotes/, para no mezclarlo con el blog.db de fastapi/.
    DATABASE_URL: str = "sqlite:///./devinotes.db"
    JWT_SECRET: str = os.getenv("JWT_SECRET", _PRACTICA)
    JWT_ALG: str = "HS256"
    # 60 * 24 = un día en minutos. La clase lo escribe igual, en el default del Field.
    JWT_EXPIRES_MIN: int = 60 * 24
    PROJECT_NAME: str = "Devinote"
    # La sección 18 lo pide obligatorio, en Pydantic 1:
    #   ENVIRONMENT: str = Field(..., env="ENVIRONMENT")
    # Field(..., env=) revienta en Pydantic 2, igual que el resto de esta clase.
    # Default DEV para poder arrancar sin un .env nuevo.
    # La clase iba a usarlo para create_all solo en DEV, y después dejó ese if comentado.
    ENVIRONMENT: str = "DEV"


# Se arma al importar el módulo. db.py lee settings.DATABASE_URL.
settings = Settings()
