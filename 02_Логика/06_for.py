"""
Цикл for - перебор коллекций, диапазонов, словарей
"""

# Базовый for по списку
print("=== Перебор списка ===")
fruits = ['яблоко', 'банан', 'вишня']
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# range() - генерация последовательностей
print("\n=== range() ===")
print(f"range(5) -> {list(range(5))}")
print(f"range(2, 5) -> {list(range(2, 5))}")
print(f"range(0, 5, 2) -> {list(range(0, 5, 2))}")
print(f"range(10, 0, -2) -> {list(range(10, 0, -2))}")

# enumerate() - индекс + элемент
print("\n=== enumerate() ===")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Перебор по индексам
print("\n=== Перебор по индексам ===")
for i in range(len(fruits)):
    print(f"Индекс {i} - {fruits[i]}")

# Перебор строки
print("\n=== Перебор строки ===")
word = "Python"
for char in word:
    print(f"Символ: {char}")

# Перебор кортежа
print("\n=== Перебор кортежа ===")
coords = (10, 20, 30)
for coord in coords:
    print(f"Координата: {coord}")

# Перебор словаря (ключи, значения, пары)
print("\n=== Перебор словаря ===")
person = {"name": "Toothless", "age": 20}

print("- Ключи:")
for key in person:
    print(f"{key}")

print("- Значения:")
for value in person.values():
    print(f"{value}")

print("- Пары (ключ, значение):")
for key, value in person.items():
    print(f"{key}: {value}")

# Вложенные циклы
print("\n=== Вложенные циклы ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end = " ")
    print()

# break и continue внутри for
print("\n=== break и continue ===")
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end = " ")

# else в for (выполняется, если цикл завершился без break)
print("\n=== else в for ===")
for i in range(3):
    print(f"Итерация {i}")
else:
    print("Цикл завершен без break")

for i in range(5):
    if i == 2:
        print("Нашли 2, break")
        break
    print(f"Итерация {i}")
else:
    print("Этот else не выролняется, потому что был break")

print("--- Поиск элемента с else ---")
numbers = [2, 3, 4, 6]
target = 5
for num in numbers:
    if num == target:
        print(f"Нашли {target}")
        break
else:
    print(f"{target} не найден в списке")

# zip() - параллельный перебор нескольких коллекций
print("\n=== zip() ===")
names = ["Огонь", "Вода", "Земля", "Воздух"]
elements = ["Fire", "Water", "Earth", "Air"]
for name, element in zip(names, elements):
    print(f"{name}: {element}")

# reversed() - обратный порядок
print("\n=== reversed() ===")
print(f"Список: {fruits}")
for fruit in reversed(fruits):
    print(f"Обратный порядок: {fruit}")

# sorted() - сортировака без изменения оригинала
print("\n=== sorted() ===")
unsorted = [5, 2, 8, 1, 9]
for num in sorted(unsorted):
    print(num, end = " ")

# for с распаковкой кортежей
print("\n=== Распаковка в for ===")
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(f"a = {a}, b = {b}")

# for с условием-фильтров (тернарный)
print("\n=== Фильтрация на лету ===")
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    if num % 2 == 0:
        print(f"{num} - чётное")
    else:
        print(f"{num} - нечётное")