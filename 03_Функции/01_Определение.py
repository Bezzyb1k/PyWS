"""
Функции, определение и вызов
С аннотациями типов (type hints) для читаемости и самодокументирования
"""

# Простейшая функци
def say_hello() -> None:
    """Выводит приветсвие в консоль"""
    print('Hello')

say_hello()


# Функция с одном параметром, принимает строку и ничего не возвращает
def greet(name: str) -> None:
    """Выводит персонализированное приветствие"""
    print(f"Привет, {name}")

greet('Toothless')


# Функции с возратом значения, принимает два числа, возвращает число
def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b

print(add(5, 10))


# Функция с возвратом значения другого типа, принимает строку, возвращает число
def get_length(text: str) -> int:
    """Возвращает длину строки"""
    return len(text)

print(get_length('Python'))


# Функция, которая может вернуть None 
def divide(a: int, b: int) -> float | None:
    """Делит a на b. Если b == 0, возвращает None"""
    if b == 0:
        return None
    return a / b

print(divide(5, 5))
print(divide(5, 0))


# Документация функции (docstring) с указанием типов
def power(base: int, exp: int) -> int:
    """
    Возводит base в степень exp
    
    Args:
        base (int): Основание
        exp (int): Показатель степени
        
    Returns:
        int: Результат возведения в степень
    """
    return base ** exp

print(power(2, 3))

