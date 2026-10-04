"""
Модуль os - работа с файлами и папками
"""

import os

# Текущая директория

print("=== Текущая директория ===")
print(f"Текущая папка: {os.getcwd()}")

# Список файлов

print("\n=== Содержмое папки ===")
for item in os.listdir():
    print(f"{item}")

# Проверка существования

print("\n=== Проверка ===")
print(f"Файл существует: {os.path.exists('07_Стандартная_Библиотека/01_os.py')}")
print(f"Этот файл: {os.path.isfile("07_Стандартная_Библиотека/01_os.py")}")
print(f"Это папка: {os.path.isdir("07_Стандартная_Библиотека/01_os.py")}")

# Создание и удаление папки

print("\n=== Работа с папками ===")
folder = "test_folder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Папка {folder} создана")

if os.path.exists(folder):
    os.rmdir(folder)
    print(f"Пакпа {folder} удалена")

# Соединение и разделение путей

print("\n=== Путь ===")
path = os.path.join("data", "logs", "file.txt")
print(f"Соединенные путь: {path}")
print(f"Папка: {os.path.dirname(path)}")
print(f"Файл: {os.path.basename(path)}")

# Размер файла 
print("\n=== Размер файла ===")
if os.path.exists("07_Стандартная_Библиотека/01_os.py"):
    size = os.path.getsize("07_Стандартная_Библиотека/01_os.py")
    print(f"Размер: {size} байт")

# Обход папки (Только первый уровень)
print("\n=== Обход папки ===")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"Файл: {item}")
    elif os.path.isdir(item):
        print(f"Папка: {item}")