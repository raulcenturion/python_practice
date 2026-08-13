###
# Listas metodos
# append, extend, insert, remove, pop, clear, index, count,
# sort, sorted, reverse, copy
###

DOG = "🐶"
PANDA = "🐼"
KOALA = "🐨"
NUMBERS = [3, 10, 2, 8, 99, 101]
FRUTAS_BASE = ["manzana", "pera", "manzana", "pera", "limón"]

print("--- insert() ---")
lista = [1, 2, 3, 4, 5, 6]
lista.insert(2, "nuevo")
print("lista:", lista)

print("\n--- del con rango ---")
lista1 = [PANDA, KOALA, DOG, "😿", "🐹"]
del lista1[1:3]
print("lista1:", lista1)

print("\n--- sort() (modifica la original) ---")
numbers = list(NUMBERS)
numbers.sort()
print("numbers:", numbers)

print("\n--- sorted() (nueva lista) ---")
sorted_numbers = sorted(NUMBERS)
print("sorted_numbers:", sorted_numbers)

print("\n--- sorted() con cadenas (minúsculas) ---")
sorted_frutas = sorted(FRUTAS_BASE)
print("sorted_frutas:", sorted_frutas)

print("\n--- sort(key=str.lower) ---")
frutas = ["manzana", "Pera", "Limón", "manzana", "pera", "limón"]
frutas.sort(key=str.lower)
print("frutas:", frutas)

print("\n--- len / count / in ---")
animals = [DOG, PANDA, KOALA, DOG]
print("len(animals):", len(animals))
print("count DOG:", animals.count(DOG))
print("PANDA in animals:", PANDA in animals)
print("hamster in animals:", "🐹" in animals)
