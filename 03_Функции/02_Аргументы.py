"""
Функции и аргументы
"""

# Позиционные аргументы
def greet(name: str, age: int) -> str:

    """Возвращает приветсвие с именем и возрастом"""

    return f"Привет, {name}! Тебе {age} лет"


# Аругменты со значением по умолчанию
def greet_default(name: str, age: int = 20) -> str:

    """Если возраст не указан, по умолчанию 20"""

    return f"Привет, {name}! Тебе {age} лет"


# Именованные аргументы
def info(name: str, city: str, age: int) -> str:
    return f"{name} из {city}, {age} лет"


# Произвольное количество позиционных аргументов *args
def sum_all(*args: int) -> int:

    """Принимает любое количество чисел и возвращает их сумму"""

    return sum(args)


# Произвольное количество именованных аргументов **kwargs
def print_data(**kwargs) -> None:

    """Принимает любые именованные аргументы и выводит их"""

    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Универскальная сумма
def sum_all_adcanced(*args) -> int | float:

    """
    Принимает числа, списки, кортежи и возвращает общую сумму
    Если элемент - список или кортеж суммирует его элементы
    """

    total = 0
    for item in args:
        if isinstance(item, (list, tuple)):
            total += sum(item)
        elif isinstance(item, (int, float)):
            total += item
    return total


# Гибкая обработка **kwargs с проверкой типов
def process_kwargs(**kwargs) -> None:

    """Принимает любые именованные аргументы и выводит их с указанием типа"""

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            print(f"{key}: число ({value})")
        elif isinstance(value, str):
            print(f"{key}: строка ({value})")
        elif isinstance(value, (list, tuple)):
            print(f"{key}: коллекция ({value})")
        else:
            print(f"{key}, другой тип ({value})")



# Сборка конфигурации с проверкой типов
def build_config(**kwargs) -> None:

    """Принимает настройки и возвращает готовый словарь конфигруации"""

    config = {
        "title": kwargs.get("title", "Untitled"),
        "version": kwargs.get("version", 1.0),
        "debug": kwargs.get("debug", False)
    }
    return config

# Комбинация
def full_profile(name: str, *args: str, **kwargs) -> None:
    print(f"Имя: {name} \nНавыки: {args} \nДополнительно:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Тесты
print("=== Позиционные аргументы ===")
print(greet('Toothless', 20))

print("\n=== Аргументы со значением по умолчанию ===")
print(greet_default("Алиса"))
print(greet_default("Ваня", 30))

print("\n=== Именованные аргументы ===")
print(info(city = "Санкт-Петербург", age = 33, name = 'Toothless'))
print(info("Вася", "Казань", 19))

print("\n=== *args ===")
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print("\n=== **kwargs ===")
print_data(name = "toothless", age = 20)

print("\n=== Универсальная сумма ===")
print(sum_all_adcanced(1, 2, [1, 2], (1, 2)))
print(sum_all_adcanced([10, 20], [1, 2, 3], [0, 0, -50]))

print("\n=== process_kwargs ===")
process_kwargs(name = 'Toothless', age = 20, skills = ["Python", "Godot"])

print("\n=== build_config ===")
config = build_config(title = "MageTD", version = 1.01)
for key, value in config.items():
    print(f"{key}: {value}")

print("\n=== Комбинация ===")
full_profile("toothless", "Python", "Godot", "AI", age = 20, city = "None")