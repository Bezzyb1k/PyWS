"""
Замыкание (closures) - функция, которая запоминает состояние
"""

# Простейшее замыкание

def outer_function(message: str) -> str:

    """Внешняя функция, которая возвращает внутреннюю"""

    def inner_function():
        print(message)
    return inner_function


hello = outer_function('Hello')
hello()


# Замыкание с счётчиком

def counter():

    """Создает счетчик, который увеличивается при каждом вызове"""

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment 


print("\n=== Счетчик ===")
c1 = counter()
print(c1())
print(c1())
print(c1())


# Замыкание с параметрами
def multiplier(factor: int):

    """Возвращает функцию, которая умножает число на factor"""

    def multiply(x: int) -> int:
        return x * factor

    return multiply

print("\n=== Умножение ===")
double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))


# Замыкание для настройки поведения
def make_power(exponent: int):

    """Возвращает функцию, которая возводит число в степень exponent"""

    def power(base: int) -> int:
        return base ** exponent

    return power

print("\n=== Возведение в степень ===")
square = make_power(2)
cube = make_power(3)

print(square(4))
print(cube(4))


# Замыкание с изменяемым состоянием (список)
def history():

    """Сохраняет историю вызовов"""

    calls = []

    def add_call(value: str):
        calls.append(value)
        return calls

    return add_call


print("\n=== История вызовов ===")
log = history()
print(log('Первый вызов'))
print(log('Второй вызов'))
print(log('Третий вызов'))


# Замыкание для создания обработчиков
def create_game_settings(difficulty: str):

    """Создает настройки игры в зависимости от сложности"""

    settings = {
        "easy": {"lives": 10, "speed": 1.0},
        "medium": {"lives": 15, "speed": 1.5},
        "hard": {"lives": 20, "speed": 2.0}
    }.get(difficulty, {"lives": 15, "speed": 1.0})

    def get_settings():
        return settings

    return get_settings


print("\n=== Игровые настройки ===")
easy_game = create_game_settings("easy")
medium_game = create_game_settings("medium")

print(easy_game())
print(medium_game())