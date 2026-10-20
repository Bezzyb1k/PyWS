"""
Модуль json - работа с JSON-данными
"""

import json

# Словарь Python
print("=== Python --> JSON (dumps) ===")

data = {
    "name": "Toothless",
    "age": 20,
    "is_alive": True,
}

json_string = json.dumps(data, ensure_ascii = False, indent = 2)
print(json_string)

# JSON-строка --> словарь Python (loads)
print("\n=== JSON --> Python (loads)")

json_string = '{"name": "Toothless", "age": 20, "is_alive": true}'
parsed = json.loads(json_string)

print(f"Тип: {type(parsed)}")
print(f"Словарь: {parsed}")
print(f"Имя: {parsed["name"]}")
print(f"Возраст: {parsed["age"]}")

# Запись в файл (dump)
print("\n=== Запись в файл (dump)")

data = {
    "name": "Toothless",
    "age": 20,
    "is_alive": True,
}

with open("save.json", "w", encoding = "utf-8") as file:
    json.dump(data, file, ensure_ascii = False, indent = 2)

print("Файл save.json записан")

# Чтение из файла (load)

print("\n=== Чтение из файла (load) ===")

with open("save.json", "r", encoding = "utf-8") as file:
    loaded = json.load(file)

print(f"Загружено: {loaded}")

# Вложенные структуры

print("\n=== Вложенные структуры ===")

data = {
    "player": {
        "name": "Беззубик",
        "stats": {
            "health": 100,
            "mana": 50,
        },
    },
    "enemies": [
        {"name": "Гоблин", "hp": 30},
        {"name": "Орк", "hp": 80},
    ],
}

json_string = json.dumps(data, ensure_ascii = False, indent = 2)
print(json_string)

# Список --> JSON
print("\n=== Список --> JSON ===")

numbers = [1, 2, 3, 4, 5]
json_string = json.dumps(numbers)
print(f"Список: {json_string}")

parsed = json.loads(json_string)
print(f"Обратно: {parsed}, тип: {type(parsed)}")

# Обработка ошибок
print("\n=== Обработка ошибок ===")

bad_json = "{name: 'Toothless'}" # невалидный JSON

try:
    parsed = json.loads(bad_json)
except json.JSONDecodeError as ERROR:
    print(f"Ошибка: {ERROR}")