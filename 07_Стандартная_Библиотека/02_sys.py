"""
Модуль sys - работа с системой и интерпретатором Python
"""

import sys

# Версия Python
print("=== Версия Python ===")
print(f"Версия: {sys.version}")

# Платформа
print("\n=== Платформа ===")
print(f"Платформа: {sys.platform}")

# Аргументы командной строки
print("\n=== Аргумент командной строки ===")
print(f"Аргументы: {sys.argv}")
print(f"Имя скрипта: {sys.argv[0]}")

# Путь поиска модулей
print("\n=== Путь поиска модулей ===")
for path in sys.path:
    print(f"{path}")

# Выход из программы
print("\n=== Выход из программы ===")
print("Эта строка выполнится")
# sys.exit(0) 
print("Эта строка не выполнится, если sys.exit(0) сработает")

# Размер объектов
print("\n=== Размер объектов ===")
print(f"Размер числа 13: {sys.getsizeof(13)} байт")
print(f"Размер строки 'hello': {sys.getsizeof('hello')} байт")
print(f"Размер списка [1, 2, 3]: {sys.getsizeof([1, 2, 3])} байт")

# Предел рекурсии
print("\n=== Предел рекурсии ===")
print(f"Предел рекурсии: {sys.getrecursionlimit()}")

# Стандартный вывод и ошибки
print("\n=== Стандартный вывод ===")
print("Это обычный вывод", file = sys.stdout)
print("Это вывод ошибки", file = sys.stderr)