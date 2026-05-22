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
print(protected_dashboard("Admin"))      # Bienvenido al panel, Admin
print(protected_dashboard("Invitado"))   # Acceso denegado

# ============================
# 🔹 Con decorador (forma elegante con @)
# ============================
@require_auth  # Esto es lo mismo que: admin_panel = require_auth(admin_panel)
def admin_panel(user):
    return f"Panel de administración para {user}"

print(admin_panel("ADMIN"))      # Bienvenido...
print(admin_panel("usuario"))    # Acceso denegado

# ============================
# 🔹 Decorador con logging (ejemplo práctico)
# ============================
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
# 🔹 Resumen
# ============================
# - Un decorador es una función que recibe una función y retorna una nueva función "mejorada"
# - Se aplican con @nombre_decorador arriba de la función
# - *args y **kwargs permiten que el wrapper acepte cualquier cantidad de argumentos
# - Casos de uso comunes: autenticación, logging, caché, validación, medición de tiempo
