"""
Области видимости переменных
"""

# Глобальная переменная
global_var = "Глобальная"

def show_global() -> None:

    """Функция читает глобальную переменную"""

    print(global_var)


# Локальная переменная
def local_example() -> None:

    """Переменная внутри функции - локальная"""

    local_var = "Локальная"
    print(local_var)


# Попытка изменить глобальную переменную
def change_global_bad() -> None:

    """Попытка изменить глобальную переменную без global"""

    global_var = "Локальная внутри функции"
    print(f"Внутри функции: {global_var}")


# Изменение глобальной переменной
def change_global_good() -> None:

    """Изменяет глоабльную переменную с помощью global"""

    global global_var
    global_var = "Изменена через global"


# Переменная, замыкающаяся во вложенной функции
def outer_function() -> None:

    """Функция с вложенной функцией и nonlocal"""

    outer_var = "Из внешней функции"
    print(f"Внутри outer: {outer_var}")

    def inner_function() -> None:
        nonlocal outer_var
        outer_var = "Изменена через nonlocal"
        print(f"Внутри inner: {outer_var}")

    inner_function()
    print(f"Внутри outer после изменения: {outer_var}")


# Сравнение локальной и глобальной переменной
shadow_var = "Глобальная"

def shadow_example(shadow_var: str) -> None:

    """Параметр функции 'затеняет' глобальную переменную"""

    print(f"Внутри функции: {shadow_var}")


# Тесты
print("=== Чтение глобальной переменной ===")
show_global()

print("\n=== Локальная переменная ===")
local_example()
print("print(local_var) Ошибка - переменная не существует вне функции")

print("\n=== Попытка изменить глобальную без global ===")
print(f"До вызова: {global_var}")
change_global_bad()
print(f"После вызова: {global_var} - не изменилась")

print("\n=== Изменение глобальной с global ===")
print(f"До вызова: {global_var}")
change_global_good()
print(f"После вызова: {global_var}")

print("\n=== nonlocal ===")
outer_function()

print("\n=== Затенение ===")
print(f"Снаружи: {shadow_var}")
shadow_example('Переданная в функцию')
print(f"Снаружи после вызова: {shadow_var}")

