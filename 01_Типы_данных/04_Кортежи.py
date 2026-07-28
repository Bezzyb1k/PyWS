"""
Кортежи в Python
"""

# Создание
print("=== Создание ===")
empty = ()
empty_tuple = tuple()
single = (5, )  # Обязательно запятая!
number = (1, 2, 3, 4, 5)
mixed = (1, 'Python', True, 3.14)
without_brackets = 1, 2, 3
print(f"Пустой: {empty} {empty_tuple}")
print(f"Один элемент: {single}")
print(f"Числовой: {number}")
print(f"Без скобок: {without_brackets}")

# Доступ к элементам
print("\n=== Доступ ===")
print(f"number[0] = {number[0]}")
print(f"number[-1] = {number[-1]}")
print(f"number[0:3] = {number[0:3]}")
print(f"number[::-1] = {number[::-1]}")

# Операции
print("\n=== Операции ===")
a = 1, 2, 3
b = 4, 5, 6
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"2 in a = {2 in a}")

# Распаковка 
notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
# Количетсов переменных должно совпадать с числом элементов
do, re, mi, fa, sol, la, si = notes
print(f"do = {do}")
print(f"mi = {mi}")

# Вложенный кортеж
box = ('firstbox', (1, 2, 3))
print(f"box[1][0] = {box[1][0]}")

# Встроенные функции
print("\n=== Встроенные функции ===")
my_tuple = (1, 3, 4, 2, 5)
print(f"len(my_tuple) = {len(my_tuple)}")
print(f"max(my_tuple) = {max(my_tuple)}")
print(f"min(my_tuple) = {min(my_tuple)}")
print(f"sum(my_tuple) = {sum(my_tuple)}")
print(f"sorted(my_tuple) = {sorted(my_tuple)}") # Возвращает список, при этом кортеж не изменяется

# Неизменяемость
print("\n=== Неизменяемость ===")
print(f"my_tuple[0] = 10 ОШИБКА! Кортеж нельзя изменить")
print('Попытка изменить кортеж приведет к ошибке TypeError')

# Конвертация
print("\n=== Конвертация ===")
lst = list(my_tuple)
print(f"Кортеж: {my_tuple}")
print(f"Список из кортежа: {lst}")
print(f"Кортеж из списка: {tuple(lst)}")