"""
Магические методы - управление поведением объектов
"""

class Vector:
    """Простой вектор на плоскости"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __str__(self) -> str:

        """Строковое представление для пользователя"""

        return f"Vector({self.x}, {self.y})"


    def __repr__(self) -> str:

        """Строковое представление для отладки"""

        return f"Vector({self.x}, {self.y})"


    def __add__(self, other: "Vector") -> "Vector":

        """Сложение векторов"""

        return Vector(self.x + other.x, self.y + other.y)


    def __sub__(self, other: "Vector") -> "Vector":

        """Вычитание векторов"""

        return Vector(self.x - other.x, self.y - other.y)


    def __mul__(self, scalar: float) -> "Vector":

        """Умножение нп число"""

        return Vector(self.x * scalar, self.y * scalar)


    def __eq__(self, other: object) -> bool:

        """Сравнение на равенство"""

        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y


    def __len__(self) -> int:

        """Возвращает длину вектора"""

        return int((self.x ** 2 + self.y ** 2) ** 0.5)


    def __call__(self) -> str:

        """Повзоляет вызывать объект как функцию"""

        return f"Вызван вектор ({self.x}, {self.y})"


# Тесты

print("=== Создание ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"v1 = {v1}")
print(f"v2 = {v2}")

print("\n=== Арифметика ===")
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 2
print(f"v1 + v2 = {v3}")
print(f"v1 - v2 = {v4}")
print(f"v1 * 2 = {v5}")

print("\n=== Сравнение ===")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")

print("\n=== len() ===")
print(f"len(v1) = {len(v1)}")
print(f"len(v2) = {len(v2)}")

print("\n=== Вызов объекта как функции ===")
print(v1())

print("\n=== repr() ===")
print(repr(v1))