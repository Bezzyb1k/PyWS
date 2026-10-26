"""
Модуль random - генерация случайных чисел
"""

import random

# Случайное число с плавающей точкой
print("=== Случайное число от 0 до 1 ===")
print(f"random(): {random.random()}")
print(f"random(): {random.random()}")

# Случайное целое число
print("\n=== Случайное целое ===")
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"randrange(0, 100, 10): {random.randrange(0, 100, 10)}")

# Случайный выбор из списка
print("\n=== Случайный выбор ===")
towers = ["Fire", "Water", "Air", "Earth"]
print(f"choice(tower): {random.choice(towers)}")

# Несколько случайных элементов (без повторов)
print("\n=== Несколько элементов ===")
print(f"sample(towers, 2): {random.sample(towers, 2)}")
print(f"sample(towers, 2): {random.sample(towers, 2)}")

# Перемешивание списка
print("\n=== Перемешивание ===")
deck = [1, 2, 3, 4]
print(f"До: {deck}")
random.shuffle(deck)
print(f"После: {deck}")

# Случайное число с плавающей точкой в диапазоне
print("\n=== Случайное float в диапазоне ===")
print(f"uniform(1.0, 5.0): {random.uniform(1.0, 5.0)}")
print(f"uniform(1.0, 5.0): {random.uniform(1.0, 5.0)}")

# Случайный шанс (вероятность)
print("\n=== Случайный шанс ===")
chance = 0.3 # 30%
if random.random() < chance: print("Сработало!")
else: print("Не сработало")

# Seed (Воспроизводимость)
print("\n=== Seed ===")
random.seed(13)
print(f"С seed 13: {random.randint(1, 100)}")
print(f"С seed 13: {random.randint(1, 100)}")

random.seed(13)
print(f"Повтор с seed 13: {random.randint(1, 100)}")
print(f"Повтор с seed 13: {random.randint(1, 100)}")