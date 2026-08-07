"""
Генераторы списков - компактное создание списков
"""

# Базовый генератор
print("=== Базовый генератор ===")
squares = [x**2 for x in range(5)]
print(f"Квадраты чисел от 0 до 4: {squares}")

# C условием (фильтр)
print("\n=== Только четные числа ===")
evens = [x for x in range(20) if x % 2 == 0]
print(f"Чётные числа 0-19: {evens}")

# C преобразованием и условием
print("\n=== Чётное/Нечетное ===")
labels = ["Чётное" if x % 2 == 0 else "Нечётное" for x in range(5)]
print(f"Метки для чисел 0-4: {labels}")

# Вложенные циклы
print("\n=== Все пары координат ===")
coords = [(x, y) for x in range(3) for y in range(3)]
print(f"Координаты 3x3: {coords}")

# Изменение регистра
print("\n=== Верхний регистр ===")
word = "Python"
chars = [char.upper() for char in word]
result = "".join(chars)
print(f"Строка: {word} в верхнем регистре: {result}")

# Генератор словаря
print("\n=== Генератор словаря ===")
squares_dict = {x: x**2 for x in range(5)}
print(f"Число -> квадрат: {squares_dict}")

# Генератор множества 
print("\n=== Генератор множества ===")
text = "Hello, World"
unique_chars = {char.lower() for char in text if char != " "}
print(f"Уникальные буквы в {text}: {unique_chars}")

