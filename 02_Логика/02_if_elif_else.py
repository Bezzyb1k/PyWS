"""
Условный оператор if / elif / else
"""

# Базовый if
print("=== Базовый if ===")
age = 18
if age >= 18:
    print("Ты совершеннолетний (-яя)")
else:
    print("Ты несовершеннолетний (-яя)")

# Множественные условия (elif)
print("\n=== elif ===")
score = 80
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print(f"Оценка: {grade}")

# Вложенные условия
print("\n=== Вложенные условия ===")
is_member = True
purchase = 150
if is_member:
    if purchase > 100:
        discount = 20
    else: 
        discount = 10
else:
    discount = 5
print(f"Скидка: {discount}")

# Проверка на None
print("\n=== Проверка на None ===")
user = None
if user is None:
    print("Пользователь не найден")
else:
    print(f"Привет, {user}")

# Сложные условия
print("\n=== Сложные условия ===")
age = 20
license = True
if age >= 18 and license:
    print("Можете водить автомобиль")
else:
    print("Не можете водить автомобиль")

    