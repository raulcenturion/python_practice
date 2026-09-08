# ============================
# 📝 Ejercicios: HOF y Decoradores
# 📘 Teoría: teoria_decoradores.py, teoria_hof.py (misma carpeta)
# ============================

from functools import reduce

# 🔸 Ejemplo:
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

def mi_decorador(func):
    def wrapper(*args):
        print("Antes de la función")
        resultado = func(*args)
        print("Después de la función")
        return resultado
    return wrapper

# ============================
# HOF (Higher Order Functions)
# ============================

# Ejercicio 1: map() / list comprehension
# Dada una lista de nombres en minúsculas, pasalos a mayúsculas.
# Con map sería: list(map(str.upper, nombres))
# Acá usamos list comprehension (misma idea, más clara para el linter).
print("Ejercicio 1: map()")
nombres = ["juan", "maria", "pedro", "ana"]
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(nombres_mayusculas)


# Ejercicio 2: filter()
# Dada una lista de números del 1 al 20, filtrá solo los divisibles por 3.
print("Ejercicio 2: filter()")
numeros = list(range(1, 21))
numeros_divisibles_por_3 = [numero for numero in numeros if numero % 3 == 0]
print(numeros_divisibles_por_3)


# Ejercicio 3: reduce()
# Usá reduce() para multiplicar todos los elementos de [1, 2, 3, 4, 5].
# (importá reduce de functools)
print("Ejercicio 3: reduce()")
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)


# Ejercicio 4: sorted() con key
# Dada una lista de dicts [{nombre, edad}, ...], ordenalos por edad.
print("Ejercicio 4: sorted() con key")
personas = [{"nombre": "juan", "edad": 25}, {"nombre": "maria", "edad": 30}, {"nombre": "pedro", "edad": 20}]
personas_ordenadas = sorted(personas, key=lambda x: x["edad"])
print(personas_ordenadas)

# ============================
# DECORADORES
# ============================

# Ejercicio 5: Decorador de log
# Creá un decorador @log que imprima el nombre de la función antes de ejecutarla.
# Aplicalo a una función saludar(nombre).
print("Ejercicio 5: Decorador de log")
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@log
def saludar(nombre):
    print(f"Hola, {nombre}!")
saludar("Juan")


# Ejercicio 6: Decorador de autenticación
# Creá un decorador @requiere_admin que solo ejecute la función si
# el argumento usuario == "admin". Si no, imprimí "Acceso denegado".
print("Ejercicio 6: Decorador de autenticación")


def requiere_admin(func):
    def wrapper(*args, **kwargs):
        # Acepta usuario por keyword o como primer argumento posicional.
        usuario = kwargs.get("usuario")
        if usuario is None and args:
            usuario = args[0]
        if usuario != "admin":
            print("Acceso denegado")
            return
        return func(*args, **kwargs)

    return wrapper


@requiere_admin
def panel_admin(usuario):
    print(f"Bienvenido al panel, {usuario}")


panel_admin("admin")
panel_admin("invitado")
# --- Decorador de autenticación ---
#
# def requiere_admin(func): → define un decorador que recibe una función.
# def wrapper(*args, **kwargs): → función interna que controla el acceso.
#   usuario = kwargs.get("usuario") → busca argumento 'usuario' por keyword.
#   if usuario is None and args: → si no está, toma el primer argumento posicional.
#   if usuario != "admin": → si no es admin, imprime "Acceso denegado" y no ejecuta la función.
#   return func(*args, **kwargs) → si es admin, ejecuta la función original.
# return wrapper → devuelve la función interna como reemplazo.
#
# @requiere_admin → aplica el decorador a la función panel_admin.
# def panel_admin(usuario): → función que imprime bienvenida.
#
# panel_admin("admin") → acceso permitido, imprime "Bienvenido al panel, admin".
# panel_admin("invitado") → acceso denegado, imprime "Acceso denegado".
#
# --- Conceptos ---
# - Decorador: modifica el comportamiento de una función.
# - wrapper: función interna que decide si ejecutar o no la original.
# - *args, **kwargs: permiten recibir cualquier tipo de argumentos.
# - Control de acceso: solo usuario == "admin" puede entrar.


# ============================
# ESTILO FASTAPI (@app.get / @app.post)
# ============================

# Ejercicio 7: Mini router
# Creá una clase MiniApp con:
# - self.routes = {}
# - método get(path) que retorne un decorador y registre ("GET", path) -> func
# - método handle(method, path, **kwargs) que ejecute el handler o retorne 404
# Luego:
#   app = MiniApp()
#   @app.get("/ping")
#   def ping():
#       return {"status": "ok"}
#   print(app.handle("GET", "/ping"))
print("Ejercicio 7: Mini router")


class MiniApp:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[("GET", path)] = func
            return func

        return decorator

    def post(self, path):
        # Igual que get, pero registra con método "POST".
        def decorator(func):
            self.routes[("POST", path)] = func
            return func

        return decorator

    def handle(self, method, path, **kwargs):
        if (method, path) in self.routes:
            return self.routes[(method, path)](**kwargs)
        return "404 Not Found"


app = MiniApp()


@app.get("/ping")
def ping():
    return {"status": "ok"}


print(app.handle("GET", "/ping"))

# --- Mini router estilo FastAPI ---
#
# class MiniApp: → clase que simula una app web.
# __init__: inicializa self.routes = {} (diccionario de rutas).
#
# def get(path) / def post(path): → métodos que devuelven un decorador.
#   def decorator(func): → registra la función en self.routes con clave (método, path).
#   return func → devuelve la función original.
# return decorator → permite usar @app.get("/ruta") o @app.post("/ruta").
#
# def handle(method, path, **kwargs): → simula una petición HTTP.
#   if (method, path) in self.routes: → busca si la ruta existe.
#   return self.routes[(method, path)](**kwargs) → ejecuta la función asociada.
#   else: return "404 Not Found" → ruta no encontrada.
#
# app = MiniApp() → instancia de la aplicación.
# @app.get("/ping") → registra la función ping como endpoint GET /ping.
# def ping(): return {"status": "ok"} → handler que devuelve respuesta.
#
# print(app.handle("GET", "/ping")) → simula petición GET /ping, imprime {"status": "ok"}.
#
# --- Conceptos ---
# - Decoradores (@app.get / @app.post) registran funciones como endpoints.
# - Diccionario self.routes guarda las rutas y sus handlers.
# - handle() actúa como router: ejecuta función o devuelve 404.
# - Ejemplo simplificado de cómo funciona FastAPI internamente.


# Ejercicio 8: También POST
# Agregá post(path) a MiniApp.
# Registrá @app.post("/echo") que reciba mensaje: str y retorne {"echo": mensaje}.
# Probá app.handle("POST", "/echo", mensaje="hola").
print("Ejercicio 8: También POST")


@app.post("/echo")
def echo(mensaje):
    return {"echo": mensaje}


print(app.handle("POST", "/echo", mensaje="hola"))

# --- Ejercicio 8: También POST ---
#
# @app.post("/echo") → registra la función echo como endpoint POST /echo.
# def echo(mensaje): → handler que recibe un argumento 'mensaje'.
# return {"echo": mensaje} → devuelve un diccionario con el mismo mensaje.
#
# print(app.handle("POST", "/echo", mensaje="hola"))
#   → simula una petición POST a /echo con mensaje="hola".
#   → ejecuta echo("hola") → devuelve {"echo": "hola"}.
#
# --- Conceptos ---
# - Decoradores (@app.get, @app.post) registran funciones como endpoints.
# - Diccionario app.routes guarda las rutas y sus handlers.
# - handle() actúa como router: ejecuta función o devuelve 404.
# - Ejemplo simplificado de cómo frameworks como FastAPI manejan GET y POST.
