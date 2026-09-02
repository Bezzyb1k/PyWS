"""
Статические методы и методы класса
"""

class Player:

    """Класс игрока с фабрикой создания"""

    # Атрибут класса (общий для всех объектов)
    max_health = 100
    game_version = "1.0"

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.heatlh = health

    @staticmethod
    def is_valid_name(name: str) -> bool:

        """Проверяет, подходит ли имя для игрока"""

        return len(name) >= 2 and name.isalnum()


    @classmethod
    def create_default(cls, name: str) -> "Player":

        """Создает игрока с настройками по умолчанию"""

        if not cls.is_valid_name(name):
            name = "Default"

        return cls(name)


    @classmethod
    def from_dict(cls, data: dict) -> "Player":

        """Создает игрока из словаря"""

        return cls(data.get("name", "Default"), data.get("health", 100))


# Тесты
print("=== Статический метод ===")
print(f"is_valid_name('Toothless'): {Player.is_valid_name("Toothless")}")
print(f"is_valid_name('A'): {Player.is_valid_name('A')}")
print(f"is_valid_name('User_Name'): {Player.is_valid_name("User_Name")}")

print("\n=== Метод класса (Фабрика) ===")
player1 = Player.create_default("Toothless")
player2 = Player.create_default("A") # Имя невалидное
print(f"Игрок 1: {player1.name}, здоровье: {player1.heatlh}")
print(f"Игрок 2: {player2.name}, здоровье: {player2.heatlh}")

print("\n=== Метод класса из словаря ===")
data = {"name": "Shadow", "health": 80}
player3 = Player.from_dict(data)
print(f"Игрок из словаря: {player3.name}, здоровье: {player3.heatlh}")

