# Valor y referencia
# En Python, los tipos de datos se dividen en dos categorías principales: tipos mutables e inmutables.
# Los tipos inmutables incluyen: int, float, str, tuple, frozenset, etc.
# Los tipos mutables incluyen: list, dict, set, bytearray, etc.
# Cuando se asigna un valor a una variable, Python maneja la memoria de manera diferente según el tipo de dato.
# Ejemplo con tipos inmutables
a = 10
b = a  # b apunta a la misma dirección de memoria que a
print("Antes de cambiar a:")
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))
a = 20  # a ahora apunta a una nueva dirección de memoria
print("Después de cambiar a:")
print("a:", a, "id(a):", id(a))
print("b:", b, "id(b):", id(b))
# Ejemplo con tipos mutables
lista1 = [1, 2, 3]
lista2 = lista1  # lista2 apunta a la misma dirección de memoria que lista1
print("Antes de modificar lista1:")
print("lista1:", lista1, "id(lista1):", id(lista1))
print("lista2:", lista2, "id(lista2):", id(lista2))
lista1.append(4)  # Modificar lista1 afecta a lista2
print("Después de modificar lista1:")
print("lista1:", lista1, "id(lista1):", id(lista1))
print("lista2:", lista2, "id(lista2):", id(lista2))
# Copias superficiales y profundas
import copy
# Copia superficial (shallow copy)
lista_original = [[1, 2], [3, 4]]
copia_superficial = copy.copy(lista_original)
copia_superficial[0].append(5)  # Modificar un elemento interno
print("Después de modificar copia_superficial:")
print("lista_original:", lista_original)
print("copia_superficial:", copia_superficial)
# Copia profunda (deep copy)
lista_original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(lista_original)
copia_profunda[0].append(5)  # Modificar un elemento interno
print("Después de modificar copia_profunda:")
print("lista_original:", lista_original)
print("copia_profunda:", copia_profunda)
# Resumen:
# - Los tipos inmutables no pueden ser modificados después de su creación. Asignar un nuevo valor crea una nueva referencia en memoria.
# - Los tipos mutables pueden ser modificados. Las modificaciones afectan a todas las referencias que apuntan al mismo objeto en memoria.
# - Las copias superficiales crean una nueva referencia al mismo objeto, mientras que las copias profundas crean una copia independiente del objeto y sus elementos internos.
# - Es importante entender cómo Python maneja la memoria para evitar errores inesperados en el manejo de datos.
# - La función id() devuelve la dirección de memoria de un objeto, lo que ayuda a entender cómo se manejan las referencias.
# - El módulo copy proporciona funciones para crear copias superficiales y profundas de objetos mutables.
# - Usar copias profundas es crucial cuando se trabaja con estructuras de datos anidadas para evitar modificaciones no deseadas.
# - Comprender la diferencia entre valor y referencia es esencial para escribir código eficiente y evitar errores difíciles de depurar.
# - En general, es recomendable usar tipos inmutables cuando sea posible para evitar efectos secundarios no deseados.
# - Sin embargo, los tipos mutables son útiles cuando se necesita modificar datos de manera eficiente.
# - La elección entre usar tipos mutables o inmutables depende del caso de uso específico y de los requisitos del programa.
# - En resumen, entender cómo Python maneja el valor y la referencia es fundamental para escribir código robusto y eficiente.
# - Finalmente, practicar con ejemplos y experimentar con diferentes tipos de datos ayuda a solidificar la comprensión de estos conceptos.
# - La gestión adecuada de la memoria y las referencias es crucial para el rendimiento y la estabilidad de las aplicaciones en Python.
# - Además, es importante considerar el impacto en la legibilidad y mantenibilidad del código al elegir entre tipos mutables e inmutables.
# - En conclusión, dominar el manejo de valor y referencia en Python es una habilidad esencial para cualquier desarrollador que busque escribir código efectivo y libre de errores.
# - Recuerda siempre probar y validar tu código para asegurarte de que se comporta como esperas, especialmente cuando trabajas con estructuras de datos complejas.
# - La comprensión profunda de estos conceptos te permitirá aprovechar al máximo las capacidades de Python y desarrollar aplicaciones más robustas y eficientes.
# - No dudes en consultar la documentación oficial de Python y otros recursos para profundizar en estos temas y mejorar tus habilidades de programación.
# - ¡Feliz codificación!