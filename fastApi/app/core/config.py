# Sección 11. Un solo lugar para los datos del JWT.
# Antes vivían sueltos en core/security.py (SECRET_KEY, ALGORITHM, minutos).
#
# os.getenv          → biblioteca estándar. Lee el entorno del proceso.
# dotenv.load_dotenv → paquete python-dotenv. Carga el .env antes del getenv.
#   Si este archivo se importa antes que main.py, sin load_dotenv() el getenv
#   no ve SECRET_KEY y se queda el default "change-me-in-prod".

import os

from dotenv import load_dotenv

load_dotenv()


# La clase la nombra settings en minúscula y no crea una instancia.
# settings.JWT_SECRET funciona igual: son atributos de la clase.
# Lo habitual sería class Settings y settings = Settings().
class settings:
    # Misma variable de entorno que usaba security.py. No es un nombre nuevo del .env.
    JWT_SECRET: str = os.getenv("SECRET_KEY", "change-me-in-prod")
    # HS256: la misma clave firma y verifica. Es el algoritmo de PyJWT.
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # decode_token de la clase usa settings.SECRET_KEY y settings.ALGORITHM.
    # Este archivo, en la clase, solo define JWT_SECRET y JWT_ALG.
    # Esos dos nombres no existen, y el decode se rompería.
    # Acá apuntan al mismo valor para que las dos formas coincidan.
    SECRET_KEY: str = JWT_SECRET
    ALGORITHM: str = JWT_ALG
