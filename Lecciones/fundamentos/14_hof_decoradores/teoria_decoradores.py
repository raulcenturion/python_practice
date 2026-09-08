# ============================
# 📘 Decoradores en Python
# ============================
# Un decorador es una función que "envuelve" otra función para agregar
# funcionalidad extra SIN modificar el código original.
# Se escriben con @nombre arriba de la función.
# Son un caso especial de Higher Order Functions (reciben y devuelven funciones).
#
# Idea mental:
#   @decorar
#   def f(): ...
# es lo mismo que:
#   def f(): ...
#   f = decorar(f)

# ============================
# 🔹 Sin decorador (forma manual)
# ============================
print("--- Sin decorador (forma manual) ---")


def require_auth(func):
    """Decorador: recibe una función (func) y devuelve otra (wrapper)."""

    def wrapper(user):
        # wrapper es la función NUEVA que reemplaza a la original.
        # Aquí agregamos la lógica extra (chequear si es admin).
        if user.lower() == "admin":
            # Si pasa el chequeo, llamamos a la función ORIGINAL.
            # func viene del parámetro de require_auth (closure).
            return func(user)
        else:
            return "Acceso denegado"

    # Devolvemos wrapper (no lo ejecutamos todavía).
    return wrapper


def admin_dashboard(user):
    # Función "normal": solo se preocupa por su trabajo.
    return f"Bienvenido al panel, {user}"


# Aplicamos el decorador A MANO:
# protected_dashboard = la versión envuelta de admin_dashboard.
protected_dashboard = require_auth(admin_dashboard)

# Al llamar protected_dashboard(...), en realidad corre wrapper(...).
print('protected_dashboard("Admin"):', protected_dashboard("Admin"))
print('protected_dashboard("Invitado"):', protected_dashboard("Invitado"))


# ============================
# 🔹 Con decorador (forma elegante con @)
# ============================
print("\n--- Con decorador (@) ---")


# @require_auth hace exactamente: admin_panel = require_auth(admin_panel)
@require_auth
def admin_panel(user):
    return f"Panel de administración para {user}"


# Cuando llamamos admin_panel(...), corre el wrapper de require_auth.
print('admin_panel("ADMIN"):', admin_panel("ADMIN"))
print('admin_panel("usuario"):', admin_panel("usuario"))


# ============================
# 🔹 Decorador con logging (ejemplo práctico)
# ============================
print("\n--- Decorador con logging ---")


def log_call(func):
    """Registra cada llamada: argumentos de entrada y valor de retorno."""

    def wrapper(*args, **kwargs):
        # *args / **kwargs permiten envolver funciones con CUALQUIER firma.
        print(f"📝 Llamando a '{func.__name__}' con args={args}, kwargs={kwargs}")
        # Ejecutamos la función original y guardamos el resultado.
        result = func(*args, **kwargs)
        print(f"✅ '{func.__name__}' retornó: {result}")
        return result  # Importante: devolver lo mismo que devolvería la original.

    return wrapper


@log_call
def sumar(a, b):
    return a + b


@log_call
def saludar(nombre):
    return f"Hola, {nombre}"


# Cada llamada imprime el log automáticamente (gracias al decorador).
sumar(3, 5)
saludar("Raúl")


# ============================
# 🔹 Decorador con parámetros
# ============================
print("\n--- Decorador con parámetros (repetir) ---")
# Cuando el decorador necesita argumentos (@repetir(3)), hay UNA capa más:
# repetir(veces) → devuelve decorator → decorator(func) → wrapper


def repetir(veces):
    """Fábrica de decoradores: recibe 'veces' y arma el decorador real."""

    def decorator(func):
        # decorator es el decorador "de verdad" (recibe la función).
        def wrapper(*args, **kwargs):
            # Ejecuta la función 'veces' veces.
            # 'veces' viene de la capa externa (closure).
            for _ in range(veces):
                result = func(*args, **kwargs)
            return result  # Devuelve el último resultado.

        return wrapper

    return decorator


# @repetir(veces=3) primero llama repetir(3) → obtiene decorator → aplica decorator.
@repetir(veces=3)
def decir_hola():
    print("¡Hola!")


decir_hola()  # Imprime "¡Hola!" 3 veces


# ============================
# 🔹 Decorador para medir tiempo de ejecución
# ============================
print("\n--- Decorador medir_tiempo ---")
import time


def medir_tiempo(func):
    """Mide cuánto tarda una función (útil para profiling simple)."""

    def wrapper(*args, **kwargs):
        inicio = time.time()              # Marca de tiempo ANTES
        resultado = func(*args, **kwargs)  # Ejecuta la función original
        fin = time.time()                 # Marca de tiempo DESPUÉS
        print(f"⏱️ '{func.__name__}' tardó {fin - inicio:.4f} segundos")
        return resultado

    return wrapper


@medir_tiempo
def proceso_lento():
    time.sleep(1)  # Simula trabajo lento (1 segundo)
    return "Listo"


proceso_lento()


# ============================
# 🔹 Puente a FastAPI: @app.get / @app.post
# ============================
# En FastAPI, @app.get("/ruta") NO es magia: es un decorador que
# registra la función como handler de esa ruta + método HTTP.

print("\n--- MiniApp (@app.get / @app.post) ---")


class MiniApp:
    """Router mínimo para entender @app.get / @app.post."""

    def __init__(self):
        # Diccionario: clave = (método, path) → valor = función handler.
        # Ej: ("GET", "/hola") → función hola
        self.routes = {}

    def get(self, path: str):
        # get(path) es una FÁBRICA de decoradores (como repetir(veces)).
        def decorator(func):
            # Al decorar, REGISTRAMOS la función en el diccionario de rutas.
            self.routes[("GET", path)] = func
            return func  # Devolvemos la original (sigue siendo usable)

        return decorator

    def post(self, path: str):
        def decorator(func):
            self.routes[("POST", path)] = func
            return func

        return decorator

    def handle(self, method: str, path: str, **kwargs):
        # Busca el handler registrado para (method, path).
        handler = self.routes.get((method, path))
        if not handler:
            return {"error": "404 Not Found"}
        # Llama a la función registrada pasando los kwargs (ej. user_id=7).
        return handler(**kwargs)


# Creamos la "app" (como app = FastAPI() en el mundo real).
app = MiniApp()


# @app.get("/hola") → registra hola en routes[("GET", "/hola")]
@app.get("/hola")
def hola():
    return {"msg": "hola"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    # user_id llega cuando handle(..., user_id=7) lo pasa como kwargs.
    return {"id": user_id, "nombre": f"user-{user_id}"}


@app.post("/users")
def create_user(nombre: str):
    return {"id": 1, "nombre": nombre}


# Vemos qué rutas quedaron registradas al aplicar los decoradores.
print("Rutas registradas:", list(app.routes.keys()))
print('handle GET /hola:', app.handle("GET", "/hola"))
print('handle GET /users/{user_id}:', app.handle("GET", "/users/{user_id}", user_id=7))
print('handle POST /users:', app.handle("POST", "/users", nombre="Raúl"))
print('handle GET /no-existe:', app.handle("GET", "/no-existe"))


# ============================
# 🔹 Resumen
# ============================
# - Decorador = función que recibe una función y retorna otra "mejorada"
# - @nombre arriba de def es azúcar sintáctico de: f = nombre(f)
# - wrapper usa *args/**kwargs para aceptar cualquier firma
# - Si el decorador tiene parámetros (@repetir(3)), hay 3 capas:
#     fábrica → decorador → wrapper
# - Casos típicos: auth, logging, caché, timing
# - @app.get / @app.post = decoradores que REGISTRAN rutas (idea de FastAPI)

# --- MiniApp: soporte de métodos HTTP ---
#
# Actualmente:
# - get(path): registra rutas GET.
# - post(path): registra rutas POST.
# → MiniApp soporta GET y POST.
#
# Se puede extender fácilmente:
# - put(path), delete(path), patch(path), etc.
# → basta con registrar ("PUT", path) o ("DELETE", path) en self.routes.
#
# --- Por qué usar una clase ---
# - Organización: encapsula rutas y lógica en un solo lugar.
# - Escalabilidad: fácil agregar más métodos sin dispersar funciones.
# - Estado compartido: self.routes guarda todas las rutas en la instancia.
# - Estilo framework: imita cómo funcionan FastAPI/Flask internamente.
#
# --- Mejores prácticas ---
# 1. Centralizar métodos dentro de la clase (evitar funciones sueltas).
# 2. Generalizar registro con add_route(method, path, func).
# 3. Usar clave consistente (method, path) → función en self.routes.
# 4. Separar lógica de negocio (handlers) de lógica de enrutamiento (MiniApp).
#
# --- En resumen ---
# MiniApp ahora soporta GET y POST.
# Lo recomendable es mantener todo en la clase y extender con más métodos.
# Así se logra un router limpio, escalable y cercano a frameworks reales.
