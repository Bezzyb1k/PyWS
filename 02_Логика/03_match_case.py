"""
Структурное сопоставление match case
"""

# Базовый match case
print("=== Базовый match case ===")
value = 2
match value:
    case 1: 
        print('Один')
    case 2: 
        print('Два')
    case _: 
        print('Другое число')

# Несколько вариантов в одном case
print("\n=== Несколько вариантов ===")
greeting = "hi"
match greeting:
    case "hello" | "hi" | "hey":
        print('Приветствие')
    case "bye" | "goodbye":
        print("Прощание")
    case _:
        print("Неизствесное слово")

# Сопоставление с кортежем
print("\n=== Сопоставление с кортежем ===")
point = (0, 1)
match point:
    case (0, 0):
        print("Начало координат")
    case (0, y):
        print(f"На оси Y: {y}")
    case (x, 0):
        print(f"На оси X: {x}")
    case (x, y):
        print(f"Точка: ({x}, {y})")

# Сопоставление со словарем
print("\n=== Сопоставление со словарем ===")
person = {"name": "Toothless", "age": 20}
match person:
    case {"name": name, "age": age}:
        print(f"Имя: {name}, Возраст: {age}")
    case {"name": name}:
        print(f"Имя: {name}, возраст не указан")
    case _:
        print("Нету данных")

# Совмещение с if
print("\n=== Совмещение с if ===")
data = {"status": "ok", "value": 42}
if data.get("status") == "ok":
    match data:
        case {"value": value}:
            print(f"Значение: {value}")
        case _:
            print("Неизвестный формат")
else:
    print("Ошибка")

value = 10
match value:
    case x if x < 0:
        print("Число отрицательное")
    case x if x == 0:
        print("Число ноль")
    case x if x > 0:
        print("Число положительное")

status = "True"
user_type = "admin"
match (status, user_type):
    case("True", "admin"):
        print("Admin активен")
    case("True", _):
        print("Пользователь активен")
    case _:
        print("Неактивен")

        