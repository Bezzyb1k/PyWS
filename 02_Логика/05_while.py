"""
Цикл while - повторяет код, пока условие истинно
"""

# Базовый счетчик
print("=== Базовый счетчик ===")
i = 0
while i < 5:
    print(f"Шаг {i}")
    i += 1
print("Цикл завершен")

# Сумма чисел от 1 до N
print("\n=== Сумма чисел от 1 до N ===")
n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Сумма чисел от 1 до {n} = {total}")

# Ожидание правильного ввода
print("\n=== Ожидание правильного ввода ===")
user_input = ""
while user_input.lower() != "да":
    user_input = input("Введите 'да', чтобы продолжить: ")
print("Продолжаем")

# Бесконечный цикл с break
print("\n=== Бесконечный цикл с break ===")
tick = 0
while True:
    print(f"Кадр {tick}")
    tick += 1
    if tick >= 5:
        print("Достигнут лимит кадров, выходим из цикла")
        break
print("Цикл завершен")

# Поиск первого чётного числа в списке
print("\n=== Поиск первого четного числа ===")
numbers = [3, 7, 11, 4, 9, 12]
i = 0
found = False
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(f"Первое четное число: {numbers[i]} на позиции {i}")
        found = True
        break
    i += 1
if not found:
    print("Четных чисел в списке нет")

# Перебор списка
print("=== Перебор списка ===")
fruits = ['яблоко', 'банан', 'вишня', 'киви']
i = 0
while i < len(fruits):
    print(f"Фрукт: {fruits[i]}")
    i += 1

# Удаление всех отрицательных чисел из списка
print("\n=== Удаление отрицательных чисел их списка ===")
data = [5, -2, 10, -8]
i = 0
while i < len(data):
    if data[i] < 0:
        data.pop(i)
    else:
        i += 1
print(f"Список без отрицательных чисел: {data}")

# Бесконечный цикл с условием
print("\n=== Бесконечный цикл с условием ===")
run = True
i = 0
while run:
    print(f"Итерация {i}")
    i += 1
    if i >= 3:
        run = False
print("Цикл завершен")

