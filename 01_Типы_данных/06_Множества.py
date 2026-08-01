"""
Множества в Python
"""

# Создание
print("=== Создание ===")
empty = set()
numbers = {1, 2, 3, 4, 5}
mixed =  {1, "Python", False}
from_list = set([1, 2, 3, 3, 4, 1])
print(f"Пустое множество: {empty}")
print(f"Числовое множество: {numbers}")
print(f"Множество из списка: {from_list} - дубликаты удалились")

# Добавление и удаление
print("\n=== Добавление и удаление ===")
my_set = {1, 2, 3}
print(f"Изначальное множество: {my_set}")
my_set.add(4)
print(f"my_set.add(4): {my_set}")
my_set.add(4)
print(f"my_set.add(4): {my_set} - ничего не изменилось так как уже 4 есть")
my_set.remove(3)
print(f"my_set.remove(3): {my_set}")
my_set.discard(5)
print(f"my_set.discardi(5): {my_set} - элемента 5 нету, ничего не произойдет")
pop = my_set.pop()
print(f"my_set.pop(): {pop}, осталось {my_set}")

# Проверка наличия
print("\n=== Проверка наличия ===")
print(f"2 in my_set: {2 in my_set}")
print(f"5 in my_set: {5 in my_set}")

# Операции над множествами
print("\n=== Операции над множествами ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a: {a}, b: {b}")
print(f"Объединение a | b: {a | b}")
print(f"Пересечение: a & b: {a & b}")
print(f"Разность a - b: {a - b}")
print(f"Разность b - a: {b - a}")
print(f"Симметричная разность: a ^ b: {a ^ b}")

# Преобразование в список (удаление дубликатов)
print("\n=== Удаление дубликатов ===")
lst = [1, 1, 2, 2, 3, 4, 5, 5]
unique = list(set(lst))
print(f"Было: {lst}")
print(f"Стало: {unique}")

# Подсчет уникальных символов в строке
print("\n=== Уникальные символы ===")
text = 'Hello, World'
unique_chars = set(text)
print(f"Уникальные символы: {unique_chars}")
print(f"Всего уникальных символов: {len(unique_chars)}")

# Сравнение множеств
print("\n=== Сравнение множеств ===")
a = {1, 2, 3}
b = {1, 2, 4}
c = {3, 2, 1}
print(f"a == b: {a == b}")
print(f"a == c: {a == c} - порядок не важен")