# Herencia y Polimorfismo
# La herencia permite crear una nueva clase basada en una clase existente.
# La nueva clase (clase derivada) hereda atributos y métodos de la clase existente (clase base).
# El polimorfismo permite que diferentes clases puedan ser tratadas como instancias de una clase común.
# La función `isinstance()` se utiliza para verificar si una instancia pertenece a una clase específica o a una clase derivada.
# Ejemplo de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"
# Crear instancias de las clases derivadas
perro = Perro("Fido")
gato = Gato("Whiskers")
print(f"{perro.nombre} dice: {perro.hablar()}")
print(f"{gato.nombre} dice: {gato.hablar()}")
#return f"Punto({self.x}, {self.y})" # Representación oficial del objeto
# Crear una instancia de la clase Punto
#punto1 = Punto(3, 4)
#print(punto1)          # Llama a __str__
#print(repr(punto1))    # Llama a __repr__
# Ejemplo de polimorfismo
def hacer_hablar(animal):
    print(f"{animal.nombre} dice: {animal.hablar()}")
hacer_hablar(perro)  # Funciona con instancia de Perro
hacer_hablar(gato)   # Funciona con instancia de Gato
# Verificación de tipos con isinstance
print(isinstance(perro, Animal))  # True
print(isinstance(gato, Animal))    # True
print(isinstance(perro, Perro))    # True
print(isinstance(gato, Perro))      # False
# ============================
# 🔹 Resumen
# ============================
# - Herencia: una clase hija hereda atributos y métodos de la clase padre
# - Polimorfismo: distintas clases pueden tener el mismo método con comportamiento diferente
# - super().__init__(): llama al constructor de la clase padre
# - isinstance(): verifica si un objeto es instancia de una clase
# - raise NotImplementedError: obliga a las subclases a implementar un método
