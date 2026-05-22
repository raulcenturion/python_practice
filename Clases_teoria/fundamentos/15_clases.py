# Clases
# Una clase es una plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán.
# Se define utilizando la palabra clave class seguida del nombre de la clase y dos puntos.
# La convención es usar CamelCase para los nombres de las clases.
# La sintaxis básica es:
# class NombreClase:
#     def __init__(self, parametros):
#         self.atributo = valor
#     def metodo(self):
#         bloque_de_codigo
# Ejemplo de una clase simple
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def saludar(self):  # Método de instancia
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
# Crear una instancia de la clase Persona
persona1 = Persona("Alice", 30)
print(persona1.saludar())
# Crear otra instancia de la clase Persona
persona2 = Persona("Bob", 25)
print(persona2.saludar())
# Atributos de clase (compartidos por todas las instancias)
class Circulo:
    pi = 3.14159  # Atributo de clase

    def __init__(self, radio):
        self.radio = radio  # Atributo de instancia

    def area(self):
        return Circulo.pi * (self.radio ** 2)
# Crear una instancia de la clase Circulo
circulo1 = Circulo(5)
print("Área del círculo:", circulo1.area())
def externa(x):
        def interna(y):
            return x + y
        return interna(x * 2)
print("Función anidada:", externa(5))
# Herencia (una clase puede heredar atributos y métodos de otra clase)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera  # Nuevo atributo de instancia

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."
# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Charlie", 22, "Ingeniería")
print(estudiante1.saludar())
print(estudiante1.estudiar())
# Métodos especiales (como __str__, __repr__, etc.)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"
# Crear una instancia de la clase Punto
punto1 = Punto(3, 4)
print(punto1)          # Llama a __str__
print(repr(punto1))    # Llama a __repr__
# Encapsulamiento (atributos y métodos privados)
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (usa __ para indicar que es privado)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida."
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida o saldo insuficiente."
    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo}"
# Crear una instancia de la clase CuentaBancaria
cuenta1 = CuentaBancaria("David", 1000)
print(cuenta1.mostrar_saldo())
print(cuenta1.depositar(500))
print(cuenta1.retirar(200))
print(cuenta1.mostrar_saldo())
# Nota: En Python, los atributos y métodos privados son una convención y no una restricción estricta. Se pueden acceder desde fuera de la clase usando el nombre modificado (por ejemplo
# cuenta1._CuentaBancaria__saldo), pero no es recomendable hacerlo.
# Pass es una palabra clave que se utiliza como un marcador de posición para indicar que no se va a implementar nada en ese lugar.
# Se usa comúnmente en clases o funciones que aún no se han implementado.
class ClaseVacia:
    pass
# Crear una instancia de la clase ClaseVacia
clase_vacia = ClaseVacia()
print("Instancia de clase vacía creada:", clase_vacia)
# Fin de la clase sobre clases