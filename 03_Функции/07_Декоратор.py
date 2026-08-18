"""
Декораторы - обертки для функций
"""

# Простейший декоратор
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


def add(a: int, b: int) -> int:
    return a + b

# Ручное применение декоратора (без @)
add = logger(add)
print(add(3, 5))


# Декоратор с синтаксическим сахаром 
@logger
def multiply(a: int, b: int) -> int:
    return a * b

print("\n=== Декоратор @logger ===")
print(multiply(4, 5))


# Декоратор с аргументами (повторение)
def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hello():
    print("Hello")

print("\n=== Повторение ===")
say_hello()