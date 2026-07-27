"""
Списки в Python
"""

# Создание
print("=== Создание списков ===")
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, 3.14, False, "Python"]
print(f"Пустой список: {empty}")
print(f"Список из чисел: {numbers}")
print(f"Смешанный список: {mixed}")

# Индексация и срезы
print("\n=== Индексация и срезы ===")
lst = [0, 1, 2, 3, 4]
print(f"lst[0] = {lst[0]}")
print(f"lst[-1] = {lst[-1]}")
print(f"lst[0:3] = {lst[0:3]}")
print(f"lst[::-1] = {lst[::-1]}")

# Операции
print("\n=== Операции ===")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"2 in a = {2 in a}")
print(f"10 in b = {10 in b}")

# Методы
print("\n=== Методы ===")
lst.append(5)
print(f"lst.append(5) = {lst}")
lst.insert(1, 10)
print(f"lst.insert(1, 10) = {lst}")
lst.pop()
print(f"lst.pop() = {lst}")
lst.remove(10)
print(f"lst.remove(10) = {lst}")
lst.sort()
print(f"lst.sort() = {lst}")
lst.reverse()
print(f"lst.reverse() = {lst}")

# Копирование
print("\n=== Копирование ===")
origin = [1, 2, 3]
ref = origin # Ссылка
copy = origin.copy() # Копия
ref.append(4)
print(f"origin после изменения в ref: {origin}")
print(f"copy не изменилась: {copy}")

# Вложенные списки
print("\n=== Вложенные списки ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"matrix[0] = {matrix[0]}")
print(f"matrix[0][0] = {matrix[0][0]}")

# Полезные фишки
print("\n=== Полезные фишки ===")
nums = [1, 2, 3, 4, 5]
print(f"max(nums): {max(nums)}")
print(f"min(nums): {min(nums)}")
print(f"sum(nums): {sum(nums)}")