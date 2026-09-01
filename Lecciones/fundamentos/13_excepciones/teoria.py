# Excepciones
# Las excepciones son eventos que pueden alterar el flujo normal de un programa. En Python, se pueden manejar utilizando bloques try y except.

print("--- try / except / else / finally ---")
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción
    print("Error: División por cero no permitida.")
else:
    # Código que se ejecuta si no ocurre ninguna excepción
    print("El resultado es:", resultado)
finally:
    # Código que se ejecuta siempre, ocurra o no una excepción
    print("Bloque finally ejecutado.")

# Tipos comunes de excepciones
# - ZeroDivisionError: División por cero.
# - ValueError: Valor incorrecto.
# - TypeError: Tipo de dato incorrecto.
# - IndexError: Índice fuera de rango.
# - KeyError: Clave no encontrada en un diccionario.
# - FileNotFoundError: Archivo no encontrado.

# --- try / except / else / finally ---
# try → bloque con código que puede fallar.
# except → se ejecuta si ocurre una excepción (ej: ZeroDivisionError).
# else → se ejecuta solo si NO ocurre ninguna excepción.
# finally → se ejecuta siempre, ocurra o no una excepción.
# Ejemplo: 10/0 lanza ZeroDivisionError → entra en except, luego finally.

# --- raise (lanzar excepciones) ---
# raise → sirve para lanzar una excepción manualmente.
# Ejemplo: si b == 0 → raise ValueError("El divisor no puede ser 0.")
# El try/except que rodea la llamada captura esa excepción.
#
# Diferencia:
# - try/except → captura y maneja errores.
# - raise → genera un error explícito cuando detectás una condición inválida.
# --- Diferencia práctica ---
# raise → se usa dentro de funciones para lanzar un error explícito
#         cuando detectás una condición inválida.
# try/except → se usa alrededor de código para capturar y manejar
#              errores (ya sean lanzados por Python o con raise).
#
# En resumen:
# - raise = genera el error (avisa que algo está mal).
# - try/except = captura el error (decide qué hacer con él).
# - Se usan juntos: la función valida con raise y el programa principal
#   protege con try/except.


print("\n--- raise (lanzar excepciones) ---")
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0.")
    return a / b
try:
    print("dividir(10, 2):", dividir(10, 2))
    print("dividir(10, 0):", dividir(10, 0))
except ValueError as e:
    print("Excepción capturada:", e)

print("\n--- Excepciones personalizadas ---")
class MiExcepcionPersonalizada(Exception):
    pass
try:
    raise MiExcepcionPersonalizada("Este es un error personalizado.")
except MiExcepcionPersonalizada as e:
    print("Excepción personalizada capturada:", e)

# Nota: El manejo adecuado de excepciones es crucial para crear programas robustos.
# Capturá solo las excepciones que esperás; else/finally son opcionales.

# ---------------------------
# Varias excepciones en un solo except (tupla)
# ---------------------------
# Idea: si el manejo es el MISMO para varios tipos de error,
# los agrupás: except (TipoA, TipoB) as e:
print("\n--- except con tupla (varios errores, mismo manejo) ---")
print("Idea: ValueError e IndexError se tratan igual acá")
datos = [10, 20, 30]
for texto in ("abc", "1"):  # "abc" → ValueError; "1" después puede ir a IndexError
    try:
        indice = int(texto)          # puede fallar → ValueError
        print("Valor:", datos[indice])  # puede fallar → IndexError
    except (ValueError, IndexError) as e:
        print(f"Entrada inválida ({type(e).__name__}):", e)

# Ejemplo más claro de IndexError aparte:
try:
    print("datos[99]:", datos[99])
except (ValueError, IndexError) as e:
    print(f"No se pudo acceder ({type(e).__name__}):", e)

# --- except con tupla ---
# except (ValueError, IndexError) as e:
#   → captura cualquiera de esos dos errores en la misma línea.
#   → e es el objeto de la excepción.
#
# print(f"No se pudo acceder ({type(e).__name__}):", e)
#   → f-string para mostrar información del error.
#   → type(e).__name__ → nombre de la excepción (ej: IndexError).
#   → e → mensaje del error (ej: "list index out of range").
#
# En resumen:
# - Se agrupan excepciones si el manejo es el mismo.
# - Se imprime tanto el tipo de error como su mensaje.


# ---------------------------
# try/except anidados
# ---------------------------
# Idea: un try interno maneja un error "local";
# si algo más grave pasa, lo atrapa el try externo.
print("\n--- try/except anidados ---")
print("Idea: interno = conversión; externo = división")
try:
    texto = "0"  # probá cambiar a "abc" o a "2"
    try:
        divisor = int(texto)  # ValueError si no es número
    except ValueError:
        print("No pude convertir a entero; uso divisor = 1")
        divisor = 1
    resultado = 10 / divisor  # ZeroDivisionError si divisor es 0
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error externo: división por cero")

# ---------------------------
# assert — verificar condiciones
# ---------------------------
# Idea: assert condición, "mensaje"
# Si la condición es False → lanza AssertionError.
# Útil en desarrollo/tests. Ojo: con python -O los assert se desactivan.
print("\n--- assert ---")


def verificar_edad(edad):
    assert edad >= 0, "La edad no puede ser negativa."
    return True


try:
    print("verificar_edad(25):", verificar_edad(25))  # OK
    print("verificar_edad(-5):", verificar_edad(-5))  # AssertionError
except AssertionError as e:
    print("Error de aserción:", e)

# Otro ejemplo: assert valida; try/except solo envuelve la LLAMADA
# (no el assert en sí — así se ve el AssertionError sin trampas de tests)


def verificar_stock(stock):
    assert stock > 0, "No hay stock"
    return stock


try:
    print("Hay stock:", verificar_stock(3))   # OK
    print("Hay stock:", verificar_stock(0))   # AssertionError
except AssertionError as e:
    print("assert falló:", e)

# ============================
# 🔹 Resumen
# ============================
# - try: código que puede fallar
# - except: captura el error específico
# - except (A, B): mismo manejo para varios tipos
# - try anidados: errores distintos en distintos niveles
# - else: se ejecuta si NO hubo error
# - finally: se ejecuta SIEMPRE (cerrar archivos, etc.)
# - raise: lanza una excepción manualmente
# - excepciones propias: heredan de Exception
# - assert: verifica condiciones → AssertionError si es False

# --- Diferencias entre try/except y raise ---
# try/except → se usa para capturar y manejar errores.
#   - try: bloque con código que puede fallar.
#   - except: se ejecuta si ocurre una excepción.
#   - else: se ejecuta si NO ocurre ninguna excepción.
#   - finally: se ejecuta siempre, ocurra o no una excepción.
#   → conviene usarlo cuando querés que el programa siga funcionando
#     y mostrar un mensaje amigable en caso de error.
#
# raise → se usa para lanzar un error explícito.
#   - sirve para marcar condiciones inválidas dentro de una función.
#   - ejemplo: si b == 0 → raise ValueError("El divisor no puede ser 0.")
#   → conviene usarlo cuando querés validar datos y avisar que algo está mal.
#
# En resumen:
# - raise = genera el error.
# - try/except = captura y maneja el error.
# - Se suelen usar juntos: la función lanza (raise) y el código que la llama
#   captura (try/except).
