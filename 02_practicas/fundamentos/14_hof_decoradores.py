# ============================
# 📝 Ejercicios: HOF y Decoradores
# 📘 Teoría: Clases_teoria/fundamentos/24_hof.py + 25_decoradores.py
# ============================

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

# Ejercicio 1: map()
# Dada una lista de nombres en minúsculas, usá map() para ponerlos en mayúsculas.


# Ejercicio 2: filter()
# Dada una lista de números del 1 al 20, filtrá solo los divisibles por 3.


# Ejercicio 3: reduce()
# Usá reduce() para multiplicar todos los elementos de [1, 2, 3, 4, 5].
# (importá reduce de functools)


# Ejercicio 4: sorted() con key
# Dada una lista de dicts [{nombre, edad}, ...], ordenalos por edad.


# ============================
# DECORADORES
# ============================

# Ejercicio 5: Decorador de log
# Creá un decorador @log que imprima el nombre de la función antes de ejecutarla.
# Aplicalo a una función saludar(nombre).


# Ejercicio 6: Decorador de autenticación
# Creá un decorador @requiere_admin que solo ejecute la función si
# el argumento usuario == "admin". Si no, imprimí "Acceso denegado".

