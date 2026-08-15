"""
Лямбда-функции - анонимная функция
"""

# Базовый синтаксис
square = lambda x: x ** 2
print("=== Квадрат чисел ===")
print(f"square(5) = {square(5)}")

# Лямбда с несколькими параметрами
add = lambda a, b: a + b
print("\n=== Сложение ===")
print(f"add(3, 4) = {add(3, 4)}")

# Лямбда с тернарным оператором
is_even = lambda x: "четное" if x % 2 == 0 else "нечётное"
print("\n=== Проверка на чётность ===")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")

# Лямбда в map() - применить к каждому элементу
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("\n=== map() + лямбда ===")
print(f"Исходный список: {numbers}")
print(f"Квадрты: {squared_numbers}")

# Лямбда в filter() - отфильтровать элементы
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\n=== filter() = лямбда ===")
print(f"Исходный список: {numbers}")
print(f"Четные числа: {even_numbers}")

# Лямбда в sorted() - сортировка по ключу
people = [
    {"name": "Алиса", "age": 30},
    {"name": "Дима", "age": 35},
    {"name": "Аля", "age": 25}
]

sorted_by_age = sorted(people, key = lambda person: person["age"])
print("\n=== sorted() + лямбда ===")
for person in sorted_by_age:
    print(f"{person['name']} - {person['age']} лет")

