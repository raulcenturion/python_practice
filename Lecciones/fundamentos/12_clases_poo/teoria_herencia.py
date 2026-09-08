# ============================
# 📘 Herencia y Polimorfismo
# ============================
# Herencia: una clase Hija reutiliza (y puede extender) una clase Padre.
#   class Perro(Animal):  ← Perro hereda de Animal
#
# Polimorfismo: "muchas formas".
#   El mismo método (hablar) se comporta distinto según la clase.
#
# isinstance(obj, Clase): True si obj es de esa clase o de una subclase.

# ============================
# 🔹 Herencia (Animal / Perro / Gato)
# ============================
print("--- Herencia (Animal / Perro / Gato) ---")


class Animal:
    # Clase BASE (padre): define lo común a todos los animales.
    def __init__(self, nombre):
        # Guarda el nombre en la instancia (self = el objeto creado).
        self.nombre = nombre

    def hablar(self):
        # No tiene implementación real acá: obliga a las subclases a definirla.
        # Si alguien llama hablar() en Animal puro → error claro.
        raise NotImplementedError("Subclase debe implementar este método")


class Perro(Animal):
    # Perro HEREDA de Animal: tiene __init__ y nombre sin reescribirlos.
    # Solo redefine (sobrescribe) hablar() con su propio comportamiento.
    def hablar(self):
        return "Guau"


class Gato(Animal):
    # Otra subclase: mismo método hablar(), distinto retorno.
    def hablar(self):
        return "Miau"


# Al crear Perro("Fido"), Python usa el __init__ heredado de Animal.
perro = Perro("Fido")
gato = Gato("Whiskers")

# perro.nombre viene del __init__ de Animal.
# perro.hablar() usa la versión de Perro (no la de Animal).
print(f"{perro.nombre} dice: {perro.hablar()}")
print(f"{gato.nombre} dice: {gato.hablar()}")


# ============================
# 🔹 Polimorfismo (misma interfaz, distinto comportamiento)
# ============================
print("\n--- Polimorfismo (hacer_hablar) ---")


def hacer_hablar(animal):
    """No le importa si es Perro o Gato.
    Solo asume que el objeto tiene .nombre y .hablar() → polimorfismo."""
    print(f"{animal.nombre} dice: {animal.hablar()}")


# La MISMA función funciona con tipos distintos.
hacer_hablar(perro)  # Fido dice: Guau
hacer_hablar(gato)   # Whiskers dice: Miau


# ============================
# 🔹 isinstance() — ¿de qué clase es?
# ============================
print("\n--- isinstance() ---")

# Un Perro ES un Animal (porque hereda) → True
print("isinstance(perro, Animal):", isinstance(perro, Animal))
print("isinstance(gato, Animal):", isinstance(gato, Animal))

# perro es Perro → True; gato NO es Perro → False
print("isinstance(perro, Perro):", isinstance(perro, Perro))
print("isinstance(gato, Perro):", isinstance(gato, Perro))


# ============================
# 🔹 Resumen
# ============================
# - Herencia: class Hija(Padre) → reutiliza atributos/métodos del padre
# - Sobrescribir: redefinir un método en la hija (ej. hablar)
# - Polimorfismo: mismo método, distinto comportamiento según la clase
# - NotImplementedError: obliga a implementar el método en subclases
# - isinstance(obj, Clase): True también si obj es de una subclase
# - Tip: para abstracción más estricta, mirá ABC + @abstractmethod
#   en teoria_clases.py
