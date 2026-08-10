"""
Обработка ошибок - исключения
"""

# Базовый try / except
print("=== Базовый try / except ===")
try:
    number = int(input("Введите число: "))
    print(f"Вы ввели: {number}")
except ValueError:
    print("Ошибка: нужно ввести число")

# Несколько except
print("\n=== Несколько except ===")
try:
    x = int(input("Числитель: "))
    y = int(input("Знаменатель: "))
    result = x / y
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: введите число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")

# Обработка нескольких ошибок в одном except
print("\n=== Несколько шибок в одном except ===")
try:
    x = int(input("Числитель: "))
    y = int(input("Знаменатель: "))
    result = x / y
    print(f"Результат: {result}")
except (ValueError, ZeroDivisionError) as Error:
    print(f"Ошибка: {Error}")

# except Exception (ловит все ошибки)
print("\n=== except Exception (ОСТОРОЖНО)")
try:
    x = int(input("Числитель: "))
    y = int(input("Знаменатель: "))
    result = x / y
    print(f"Результат: {result}")
except Exception as Error:
    print(f"Что-то пошло не так: {Error}")

# else (если ошибки не было)
print("\n=== else ===")
try:
    x = int(input("Введите число: "))
except ValueError:
    print("Это не число")
else:
    print(f"Число: {x}")

# finally
print("\n=== finally выполняется всегда ===")
try:
    x = int(input("Числитель: "))
    y = int(input("Знаменатель: "))
    result = x / y
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
finally:
    print("Блок finally выполнен")

# raise - выбросить ошибку вручную
print("\n=== raise ===")
try:
    age = int(input("Ваш возраст: "))
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    print(f"Ваш возраст: {age}")
except ValueError as Error:
    print(f"Ошибка: {Error}")

