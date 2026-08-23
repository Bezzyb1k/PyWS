"""
Классы и объекты. Основы ООП
"""

# Определение класса
class Player:

    """Простой класс игрока"""

    # Конструктор - вызывается при создании объекта
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.level = 1
        self.is_alive = True


    # Иетод - функция внутри класса
    def take_damage(self, damage: int) -> None:

        """Уменьшает здоровье на damage"""

        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"{self.name} погиб")
        else:
            print(f"{self.name} получил {damage} урона. Осталось {self.health} здоровья")


    def heal(self, amount: int) -> None:

        """Восстановление здоровья"""

        if not self.is_alive:
            print(f"{self.name} мёртв, лучение невозможно")
            return

        self.health += amount
        print(f"{self.name} восстановил {amount} HP. Теперь {self.health} HP")


    def level_up(self) -> None:

        """Повышение уровня"""

        self.level += 1
        print(f"{self.name} повысил уровень до {self.level}")


    def __str__(self) -> str:

        """Встроковое представление объекта"""

        status = "жив" if self.is_alive else "мёртв"
        return f"Игрок: {self.name} | Уровень: {self.level} | HP: {self.health} | Статус: {status}"



# Тест
print("=== Создание игроков ===")
player1 = Player("Беззубик", 100)
player2 = Player("Тень", 50)

print(player1)
print(player2)

print("\n=== Бой ===")
player1.take_damage(30)
player1.take_damage(50)
player1.heal(20)
player1.level_up()

print("\n=== Проверка состояния ===")
print(player1)

print("\n=== Смерть ===")
player1.take_damage(100)
print(player1)
player1.heal(10)