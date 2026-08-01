"""
Булевые значения и логические операции
"""

# Создание
print("=== Создание ===")
T = True
F = False
print(f"True: {T}, False: {F}")

# Операторы сравнения
print("\n=== Сравнения ===")
print(f"1 > 2: {1 > 2}")
print(f"5 < 10: {5 < 10}")
print(f"5 == 5: {5 == 5}")
print(f"10 != 10: {10 != 10}")
print(f"1 is 1: {1 is 1}")

# Логические операторы
print("\n=== Логика ===")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")
print(f"1 and 1: {1 and 1}")
print(f"1 and 0: {1 and 0}")
print(f"1 or 0: {1 or 0}")
print(f"not 0: {not 0}")

# Комбинирование
print("\n=== Комбинирование ===")
a = 2
b = 3
c = 1
print(f"(a > b) or (b > c): {(a > b) or (b > c)}")
print(f"(a > b) and (b > c): {(a > b) and (b > c)}")
print(f"not (a == b): {not (a == b)}")

# Приоритет операторов
print("\n=== Приоритет ===")
print(f"True or False and False: {True or False and False}")
print(f"(True or False) and False: {(True or False) and False}")

# Что считается False
print("\n=== Что считается False ===")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

# Что считается True
print("\n=== Что считается True ===")
print(f"bool(1): {bool(1)}")
print(f"bool('Python'): {bool('Python')}")
print(f"bool([1, 2]): {bool([1, 2])}")

# bool как int
print("\n=== bool как int ===")
print(f"True + True: {True + True}")
print(f"sum([True, True, True, False]): {sum([True, True, True, False])}")
