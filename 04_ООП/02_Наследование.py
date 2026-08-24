"""
Наследование - создание нового класса на основе существующего
"""

# Базовый класс (родитель)
class Enemy:

    """Базовый класс для всех врагов"""

    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = True


    def take_damage(self, amount: int) -> None:

        """Уменьшает здоровье врага"""

        self.health -= amount

        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"{self.name} убит")
        else:
            print(f"{self.name} получил {amount} урона. Осталось {self.health} HP")


    def attack(self) -> None:

        """Атака (базовая)"""

        print(f"{self.name} атакует с силой {self.damage}")


    def __str__(self) -> str:
        status = "жив" if self.is_alive else "мёртв"
        return f"{self.name} | HP: {self.health} | Урон: {self.damage} | {status}" 


# Дочерние классы (наследование)

class Goblin(Enemy):

    """Гоблин - быстрый, но слабый враг"""

    def __init__(self, name: str = 'Гоблин'):
        # Вызываем конструктор родителя с фиксированными параметрами
        super().__init__(name, health = 30, damage = 5)
        self.speed = 3 # Новый атрибут


    def attack(self) -> None:

        """Переорпеделяем метод атаки"""

        print(f"{self.name} быстро атакует с силой {self.damage}")


    def run_away(self) -> None:

        """Новый методок, которого нет у родителя"""

        print(f"{self.name} убегает со скоростью {self.speed}")


class Orc(Enemy):

    """Орк - медленный, но сильный враг"""

    def __init__(self, name: str = "Орк"):
        super().__init__(name, health = 80, damage = 15)
        self.armor = 2 # Новый атрибут


    def attack(self) -> None:

        """Переопределяем метод атаки"""

        print(f"{self.name} мощно бьет с силой {self.damage}")


    def shout(self) -> None:

        """Новый метод"""

        print(f"{self.name} издает боевой клич")


class Boss(Enemy):

    """Босс - сильный враг с дополнительной фазой"""

    def __init__(self, name: str = "Босс"):
        super().__init__(name, health = 200, damage = 25)
        self.phase = 1 # Фаза боя


    def attack(self) -> None:

        """Переопределяем метод атаки"""

        if self.phase == 1:
            print(f"{self.name} атакует огнем с силой {self.damage}")
        else:
            print(f"{self.name} атакует молнией с силой {self.damage * 2}")


    def next_phase(self) -> None:

        """Переход на следующую фазу"""

        if self.phase == 1:
            self.phase = 2
            self.damage = 50
            print(f'{self.name} переходит во вторую фазу')
        else:
            print("Босс уже в последней фазе")



# Тесты
print("=== Создание врагов ===")
goblin = Goblin()
orc = Orc("Урук")
boss = Boss("Грозный")

print(goblin)
print(orc)
print(boss)

print("\n=== Бой ===")
goblin.attack()
orc.attack()
boss.attack()

print("\n=== Уникальные методы ===")
goblin.run_away()
orc.shout()
boss.next_phase()
boss.attack()

print("\n=== Получение урона ===")
orc.take_damage(30)
boss.take_damage(50)
print(boss)