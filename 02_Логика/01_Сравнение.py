"""
Операторы сравнения в Python
"""

# Сравнение чисел
print("=== Сравнение чисел ===")
a = 1
b = 2
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Сравнение строк
print("\n=== Сравнение строк ===")
str1 = "apple"
str2 = "banana"
print(f"str1 = {str1}, str2 = {str2}")
print(f"str1 == str2: {str1 == str2}")
print(f"str1 < str2: {str1 < str2}")

# is / ==
print("\n=== is / == ===")
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst1_1 = lst1
print(f"lst1 = {lst1}, lst2 = {lst2}, lst1_1 = {lst1_1}")
print(f"lst1 == lst2: {lst1 == lst2}") # Сравнивает значения
print(f"lst1 is lst2: {lst1 is lst2}") # Сравнивает идентичность объектов
print(f"lst1 == lst1_1: {lst1 == lst1_1}")
print(f"lst1 is lst1_1: {lst1 is lst1_1}") # Это один и тот же объект

# in / not in 
print(f"\n=== in / not in ===")
numbers_list = [1, 2, 3, 4, 5]
print(f"numbers_list = {numbers_list}")
print(f"2 in numbers_list: {2 in numbers_list}")
print(f"6 in numbers_list: {6 in numbers_list}")
print(f"10 not in numbers_list: {10 not in numbers_list}")

# Сравнение булевых значений
print("\n=== Булевые сравнения ===")
print(f"True == 1: {True == 1}")
print(f"False == 0: {False == 0}")
print(f"True is 1: {True is 1}")

# Цепочки сравнений
print("\n=== Цепочки сравнений ===")
x = 5
print(f"1 < x < 10: {1 < x < 10}")
print(f"1 < x and x < 10: {1 < x and x < 10}")