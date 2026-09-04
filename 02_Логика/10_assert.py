"""
assert - проверка условий воо время выполнения
Если условие ложное - программа падает с AssertionError
"""

def divide(a: float, b: float) -> float:

    """Делит a на b. Если b == 0 - вызываем assert"""

    assert b != 0, "Делитель не может быть равен 0"

    return a / b


class Player:
    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.is_alive = True


    def take_damage(self, damage: int) -> None:

        """Наносит урон, но не позволяет здоровью стать отрицательным"""

        assert damage >= 0, "Урон не может быть отрицательным"

        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False


    def heal(self, amount: int) -> None:

        """Лечит, но не позволяет первысить 100 HP"""

        assert amount >= 0, "Лечение не может быть отрицательным" 

        self.health += amount
        if self.health > 100:
            self.health = 100


# Тесты


print("=== Тест функции divide ===")
print(divide(10, 2))
# print(divide(10, 0))      AssertionError: Делитель не может быть равен 0

print("\n=== Тест класса Player ===")
player = Player("toothless")
player.take_damage(30)
player.heal(50)
print(player.health)
# player.take_damage(-10)       AssertionError: Урон не может быть отрицательным
# player.heal(-20)      AssertionError: Лечение не может быть отрицательным