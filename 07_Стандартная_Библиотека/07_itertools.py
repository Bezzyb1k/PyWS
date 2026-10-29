"""
Модуль itertools - инструмент для работы с итератороми
"""

import itertools

# Бесконечный счетчики
print("=== count (бесконечный счетчик) ===")
for i in itertools.count(start = 1, step = 2):
    if i > 10:
        break
    print(i, end = " ")
print()

print("\n=== cycle (беснечный цикл по коллекции) ===")
colors = ["red", "green", "blue"]
count = 0
for color in itertools.cycle(colors):
    if count >= 6:
        break
    print(color, end = " ")
    count += 1
print()

print("\n=== repeat (повторение) ===")
for item in itertools.repeat("A", 5):
    print(item, end = " ")
print()

# Комбинирование
print("\n=== product (декартово произведение) ===")
for combo in itertools.product([1, 2], ["a", "b"]):
    print(combo, end = " ")
print()

print("\n=== permutations (перестановки) ===")
for perm in itertools.permutations([1, 2, 3], 3):
    print(perm, end = " ")
print()

print("\n=== combinations (сочетания) ===")
for comb in itertools.combinations([1, 2, 3, 4], 2):
    print(comb, end = " ")
print()

print("\n=== combinations_with_replacement ===")
for comb in itertools.combinations_with_replacement([1, 2, 3], 2):
    print(comb, end = " ")
print()

# Цепочка и срезы
print("\n=== chain (объединение) ===")
for item in itertools.chain([1, 2], ['a', 'b'], [True, False]):
    print(item, end = " ")
print()

print("\n=== islice (срез итератора) ===")
for item in itertools.islice(itertools.count(), 5):
    print(item, end = " ")
print()

# Группировка
print('\n=== groupby (группировка) ===')
data = [("apple", 1), ("apple", 2), ("banana", 3), ("banana", 4)]
for key, group in itertools.groupby(data, key = lambda x: x[0]):
    print(f"{key}: {list(group)}")