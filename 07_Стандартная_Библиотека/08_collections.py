"""
Модуль collections - специальные коллекции
"""

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter - подсчёт элементов
print("=== Counter ===")
words = ["apple", "fire", "fire", "water"]
counter = Counter(words)

print(f"Слова: {words}")
print(f"Подсчет: {counter}")
print(f"Количество fire: {counter["fire"]}")
print(f"Самые частые: {counter.most_common(2)}")

# defaultdict - словарь со значением по умолчанию
print("\n=== defaultdict ===")
dd = defaultdict(list)
dd["Фрукты"].append("apple")
dd["Фрукты"].append("banana")
dd["Овощи"].append("carrot")

print(f"Словарь: {dict(dd)}")

# deque - двусторонняя очередь
print("\n=== deque ===")
dq = deque([1, 2, 3])
print(f"Изначально: {dq}")

dq.append(4)
dq.appendleft(0)
print(f"После добавления: {dq}")

dq.pop()
dq.popleft()
print(f"После удаления: {dq}")

# Ограниченная очередь
limited = deque(maxlen = 3)
for i in range(5):
    limited.append(i)
print(f"Ограничение (maxlen = 3): {limited}")


# namedtuple - именованный кортеж
print("\n=== namedtuple ===")
Point = namedtuple("Point", ['x', 'y'])
p = Point(3, 4)

print(f"Точка: {p}")
print(f"x: {p.x}, y: {p.y}")

# OrderedDict - словарь с порядком
print("\n=== OrderedDict ===")

od = OrderedDict()
od["Первый"] = 1
od["Второй"] = 2
od["Третий"] = 3

print(f"Словарь: {od}")
print(f"Ключи: {list(od.keys())}")