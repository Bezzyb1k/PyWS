"""
Словари в Python
"""

# Создание 
empty = {}
dict_empty = dict()
user = {"name": "Беззубик", "age": 20}
via_constructor = dict(name = "Беззубик", age = 20)
print(f"Пустой словарь: {empty}, {dict_empty}")
print(f"Словарь: {user}")
print(f"Через dict(): {via_constructor}")

# Доступ к элементам
print("\n=== Доступ ===")
print(f"user[name] = {user['name']}")
print(f"user.get('name') = {user.get('name')}")
print(f"user.get('job', 'отсутствует') = {user.get('job', 'отсутствует')}")

# Добавление и изменение
print("\n=== Добавление и изменение ===")
user['number'] = 13
user["name"] = 'Toothless'
print(f"После добавления и изменения: {user}")

# Удаление
print("\n=== Удаление ===")
removed = user.pop('number')
print(f"Удалено 'number': {removed}")
print(f"После удаления: {user}")
last = user.popitem() # Удаляет последнюю добавленную пару
print(f"Последняя удаленная пара: {last}")
print(f"После удаления: {user}")

# Проверка наличия ключа
print("\n=== Проверка ===")
print(f"'name' in user: {'name' in user}")
print(f"'name' not in user: {'name' not in user}")

# Перебор элементов
print("\n=== Перебор ===")
user["age"] = 20
for key, value in user.items():
    print(f"{key}: {value}")

# Ключи, значения, пары
print("\n=== Ключи, значения, пары ===")
print(f"Ключи: {user.keys()}")
print(f"Значения: {user.values()}")
print(f"Пары: {user.items()}")

# Обновление словаря
print("\n=== Обновление ===")
new_data = {"key": 'abc123', "value": 13}
print(f"До обновления словаря: {user}")
user.update(new_data)
print(f"После обновления словаря: {user}")