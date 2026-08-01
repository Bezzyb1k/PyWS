"""
Преобразование типов в Python
"""

# Явное преобразование
print("=== Явное преобразование ===")
print(f"int('1') = {int('1')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(13) = {str(13)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('Python') = {bool('Python')}")
print(f"list('abc') = {list('abc')}")
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}")

# Неявное преобразование
print("\n=== Неявное преобразование ===")
num = 1
pi = 3.14
result = num + pi
print(f"1 + 3.14 = {result}, тип: {type(result)}")