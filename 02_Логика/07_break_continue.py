"""
Управление циклами: break, continue, pass, else
"""

# break - досрочный выход
print("=== break ===")
for i in range(5):
    if i == 2:
        break
    print(i, end = " ")

# continue - пропуск итерации
print("\n\n=== continue ===")
for i in range(5):
    if i % 2 == 0:
        continue
    print(i, end = " ")

# pass - заглушка
print("\n\n=== pass ===")
for i in range(5):
    if i == 1:
        pass
    else:
        print(i, end = " ")

# else в цикле - проверка на break
print("\n\n=== else ===")
items = [1, 3, 5, 7]
target = 4

for item in items:
    if item == target:
        print(f"Нашли {target}")
        break
else:
    print(f"{target} не найден в списке")