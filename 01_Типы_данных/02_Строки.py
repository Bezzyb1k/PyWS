"""
Строки в Python
"""

# Создание
s1 = 'Hello'
s2 = "World"
s3 = """Многострочная
строка"""

# Конкатенация и повторение
print("=== Конкатенация и повторение ===")
print(s1 + " " + s2)
print(s1 * 5)
print(s3)

# Индексация
print("\n=== Индексация ===")
text = 'Python'
print(f"text[0] = {text[0]}")
print(f"text[-1] = {text[-1]}")

# Срезы
print("\n=== Срезы ===")
print(f"text[0:3] = {text[0:3]}")
print(f"text[:3] = {text[:3]}")
print(f"text[::3] = {text[::3]}")
print(f"text[::-1] = {text[::-1]}")

# Методы
print("\n=== Методы ===")
s = "   Hello, World    "
print(f".upper(): {s.upper()}")
print(f".lower(): {s.lower()}")
print(f".strip(): {s.strip()}")
print(f".replace(): {s.replace('World', 'Python')}")
print(f".split(): {s.split(',')}")
print(f".find(): {s.find('World')}")
print(f".count(): {s.count('l')}")

# Проверки
print("\n=== Проверки ===")
print(f"abc123.isalnum(): {'abc123'.isalnum()}")
print(f"abc.isalpha(): {'abc'.isalpha()}")
print(f"123.isdigit(): {'123'.isdigit()}")

# Конвертация в строку
print("\n=== Конвертация ===")
num = 13
print(f"str(num): {str(num)} - {type(str(num))}")

# Полезные мелочи
print("\n=== Полезные мелочи ===")
print(f"len('Python'): {len('Python')}")
print(f"''.join(['a', 'b', 'c']): {''.join(['a', 'b', 'c'])}")
print(f"'a, b, c'.split(','): {'a, b, c'.split(',')}")
