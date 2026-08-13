# ============================
# 📘 Decoradores en Python
# ============================
# Un decorador es una función que "envuelve" otra función para agregar
# funcionalidad extra SIN modificar la función original.
# Usan el símbolo @ antes de la definición de la función decorada.
# Son un caso especial de Higher Order Functions.

# ============================
# 🔹 Sin decorador (forma manual)
# ============================
print("--- Sin decorador (forma manual) ---")
def require_auth(func):
    """Decorador que verifica si el usuario es admin."""
    def wrapper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"
    return wrapper

def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"

# Aplicar el decorador manualmente:
protected_dashboard = require_auth(admin_dashboard)
print('protected_dashboard("Admin"):', protected_dashboard("Admin"))      # Bienvenido al panel, Admin
print('protected_dashboard("Invitado"):', protected_dashboard("Invitado"))   # Acceso denegado

# ============================
# 🔹 Con decorador (forma elegante con @)
# ============================
print("\n--- Con decorador (@) ---")
@require_auth  # Esto es lo mismo que: admin_panel = require_auth(admin_panel)
def admin_panel(user):
    return f"Panel de administración para {user}"

print('admin_panel("ADMIN"):', admin_panel("ADMIN"))      # Bienvenido...
print('admin_panel("usuario"):', admin_panel("usuario"))    # Acceso denegado

# ============================
# 🔹 Decorador con logging (ejemplo práctico)
# ============================
print("\n--- Decorador con logging ---")
def log_call(func):
    """Decorador que registra cada vez que se llama una función."""
    def wrapper(*args, **kwargs):
        print(f"📝 Llamando a '{func.__name__}' con args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ '{func.__name__}' retornó: {result}")
        return result
    return wrapper

@log_call
def sumar(a, b):
    return a + b

@log_call
def saludar(nombre):
    return f"Hola, {nombre}"

sumar(3, 5)
saludar("Raúl")

# ============================
# 🔹 Decorador con parámetros
# ============================
print("\n--- Decorador con parámetros (repetir) ---")
def repetir(veces):
    """Decorador que ejecuta la función N veces."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

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
    """Decorador que mide cuánto tarda una función en ejecutarse."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️ '{func.__name__}' tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def proceso_lento():
    time.sleep(1)
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
        self.routes = {}  # (method, path) -> función

    def get(self, path: str):
        def decorator(func):
            self.routes[("GET", path)] = func
            return func  # la función original se mantiene usable
        return decorator

    def post(self, path: str):
        def decorator(func):
            self.routes[("POST", path)] = func
            return func
        return decorator

    def handle(self, method: str, path: str, **kwargs):
        handler = self.routes.get((method, path))
        if not handler:
            return {"error": "404 Not Found"}
        return handler(**kwargs)


app = MiniApp()


@app.get("/hola")
def hola():
    return {"msg": "hola"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "nombre": f"user-{user_id}"}


@app.post("/users")
def create_user(nombre: str):
    return {"id": 1, "nombre": nombre}


print("Rutas registradas:", list(app.routes.keys()))
print('handle GET /hola:', app.handle("GET", "/hola"))
print('handle GET /users/{user_id}:', app.handle("GET", "/users/{user_id}", user_id=7))
print('handle POST /users:', app.handle("POST", "/users", nombre="Raúl"))
print('handle GET /no-existe:', app.handle("GET", "/no-existe"))

# ============================
# 🔹 Resumen
# ============================
# - Un decorador es una función que recibe una función y retorna una nueva función "mejorada"
# - Se aplican con @nombre_decorador arriba de la función
# - *args y **kwargs permiten que el wrapper acepte cualquier cantidad de argumentos
# - Casos de uso comunes: autenticación, logging, caché, validación, medición de tiempo
# - @app.get / @app.post en FastAPI = decoradores que registran rutas
