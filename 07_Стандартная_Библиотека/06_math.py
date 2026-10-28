"""
Модуль math - математические функции
"""

import math

# Константы
print("=== Константы ===")
print(f"Pi: {math.pi}")
print(f"e: {math.e}")

# Округление
print("\n=== Округление ===")
print(f"ceil(4.2): {math.ceil(4.2)}")
print(f"floor(4.8): {math.floor(4.8)}")
print(f"trunc(4.9): {math.trunc(4.9)}")

# Степени и корни
print("\n=== Степени и корни ===")
print(f"sqrt(16): {math.sqrt(16)}")
print(f"pow(2, 3): {math.pow(2, 3)}")
print(f"isqrt(17): {math.isqrt(17)}")

# Расстояние между точками
print("\n=== Расстояние ===")
x1, y1 = 1, 2
x2, y2 = 3, 4
distance = math.dist((x1, y1), (x2, y2))
print(f"Расстояние между ({x1},{y1}) и ({x2},{y2}): {distance}")

# Углы
print("\n=== Углы ===")
print(f"degress(pi): {math.degrees(math.pi)}")
print(f"radians(180): {math.radians(180)}")

# Тригонометрия
print("\n=== Тригонометрия ===")
print(f"sin(pi/2): {math.sin(math.pi / 2)}")
print(f"cos(0): {math.cos(0)}")
print(f"tan(pi/4): {math.tan(math.pi / 4)}")

# Логарифмы
print("\n=== Логарифмы ===")
print(f"log(e): {math.log(math.e)}")
print(f"log10(100): {math.log10(100)}")
print(f"log2(8): {math.log2(8)}")