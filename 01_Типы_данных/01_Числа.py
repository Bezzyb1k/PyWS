"""
Числа в Python: int и float
Все операции
"""

# Запись чисел
a = 10
b = 5
print("Запись чисел может проводиться разными способами")
print(f"a = {a}\nb = {b}")
a, b = 5, 10
print(f"a, b = {a}, {b}")

# 1. Целые числа
a = 10
b = 5

print("\n=== Целые числа ===")
print(f"{a} + {b} = {a + b}") # 15
print(f"{a} - {b} = {a - b}") # 5
print(f"{a} * {b} = {a * b}") # 50
print(f"{a} / {b} = {a / b}") # 2.0
print(f"{a} // {b} = {a // b}") # 2
print(f"{a} % {b} = {a % b}") # 0
print(f"{a} ** {b} = {a ** b}") # 100000

# 2. Сравнение
print("\n=== Сравнение ===")
print(f"{a} > {b} --> {a > b}")
print(f"{a} < {b} --> {a < b}")
print(f"{a} == {b} --> {a == b}")
print(f"{a} != {b} --> {a != b}")

# 3. Вещественные числа
a = 4.5
b = 5.25

print("\n=== Вещественные числа ===")
print(f"{a} + {b} = {a + b}") # 9.75
print(f"{a} - {b} = {a - b}") # -0.75
print(f"{a} * {b} = {a * b}") # 23.625
print(f"{a} / {b} = {a / b}") # 0.8571428571428571
print(f"{a} // {b} = {a // b}") # 0.0
print(f"{a} % {b} = {a % b}") # 4.5
print(f"{a} ** {b} = {a ** b}") # 2687.6065900824133

# 4. Встроенные функции
print("\n=== Встроенные функции ===")
print(f"abs(-5) = {abs(-5)}")
print(f"round(5.333, 2) = {round(5.333, 2)}")
print(f"pow(3, 3) = {pow(3, 3)}")

# 5. Конвертация чисел
print("\n=== Конвертация ===")
print(f"int(4.4) = {int(4.4)}")
print(f"float(4) = {float(4)}")
print(f"int('123') = {int('123')}")