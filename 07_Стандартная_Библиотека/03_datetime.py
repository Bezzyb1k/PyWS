"""
Модуль datetime и time - работа с датами и временем
"""

from datetime import date, datetime, timedelta, time as my_times
import time

# Текущая дата и время
print("=== Текущая дата и время ===")
now = datetime.now()
print(f"Сейчас: {now}")
print(f"Год: {now.year}, Месяц: {now.month}, День: {now.day}")
print(f"Час: {now.hour}, Минута: {now.minute}, Секунда: {now.second}")

# Создание вручную
print("\n=== Создание вручную ===")
my_date = date(2026, 10, 18)
my_time = my_times(14, 30, 0)
my_datetime = datetime(2026, 10, 18, 14, 30, 0)

print(f"Дата: {my_date}")
print(f"Время: {my_time}")
print(f"Дата и время: {my_datetime}")

# Форматирование
print(f"\n=== Форматирование ===")
now = datetime.now()
print(f"ДД.ММ.ГГГГ: {now.strftime('%d.%m.%Y')}")
print(f"ЧЧ:ММ:СС: {now.strftime('%H:%M:%S')}")
print(f"День недели: {now.strftime('%A')}")
print(f"Месяц: {now.strftime('%B')}")

# Парсинг строки в дату
print("\n=== Парсинг ===")
date_string = "18.10.2026 14:30"
parsed = datetime.strptime(date_string, "%d.%m.%Y %H:%M")
print(f"Строка: {date_string}")
print(f"Распарсено: {parsed}")

# Разница между датами (timedelta)
print("\n=== Разница между датами ===")
date1 = datetime(2026, 10, 18)
date2 = datetime(2026, 12, 31)
diff = date2 - date1
print(f"Дней: {diff.days}")
print(f"Секунд: {diff.total_seconds()}")

# Прибавление времени
print("\n=== Прибавление времени ===")
now = datetime.now()
print(f"Сейчас: {now.strftime('%H:%M:%S')}")
print(f"Через 1 час: {(now + timedelta(hours = 1)).strftime('%H:%M:%S')}")
print(f"Через 7 дней: {(now + timedelta(days = 7)).strftime('%d.%m.%Y')}")

# Модуль time - пауза и UNIX время
print("\n=== Модуль time ===")
print("Пауза 2 секунды...")
time.sleep(2)
print("Прошло 2 секунды")

timestamp = time.time()
print(f"UNIX время: {timestamp}")

readable = time.ctime(timestamp)
print(f"Читаемая дата: {readable}")

# Время выполнение кода
print("\n=== Время выполнение кода ===")
time_start = time.time()

for i in range(10000000):
    i += i

time_end = time.time()
print(f"Время: {time_end - time_start}")