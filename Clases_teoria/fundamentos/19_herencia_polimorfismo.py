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
# Resumen:
# - La herencia permite reutilizar código y crear jerarquías de clases.
# - El polimorfismo permite tratar objetos de diferentes clases de manera uniforme.
# - Es importante diseñar clases base con métodos que las subclases deben implementar.
# - La función `isinstance()` es útil para verificar el tipo de una instancia.
# - La herencia múltiple es posible en Python, pero debe usarse con precaución para evitar complicaciones.
# - Los métodos y atributos de la clase base pueden ser sobrescritos en las clases derivadas.
# - Se pueden llamar métodos de la clase base desde una clase derivada usando `super()`.
# - La herencia y el polimorfismo son conceptos fundamentales en la programación orientada a objetos.
# - Estos conceptos ayudan a crear código más modular, reutilizable y mantenible.
# - Es recomendable seguir principios de diseño como SOLID para aprovechar al máximo la herencia y el polimorfismo.
# - La documentación y los comentarios son importantes para entender la jerarquía de clases y las relaciones entre ellas.
# - La herencia puede facilitar la extensión de funcionalidades sin modificar el código existente.
# - El polimorfismo permite escribir funciones y métodos que pueden trabajar con diferentes tipos de objetos.
# - Es importante probar las clases y sus interacciones para asegurar que funcionan correctamente.
# - La comprensión de estos conceptos es esencial para cualquier desarrollador que trabaje con programación orientada a objetos.
# - La práctica y la experiencia son clave para dominar la herencia y el polimorfismo en Python.
# - No dudes en consultar la documentación oficial de Python y otros recursos para profundizar en estos temas.
