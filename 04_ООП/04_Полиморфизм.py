"""
Полиморфизм - один интерфейс, множество реализаций
"""

class Tower:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage


    def attack(self) -> str:
        return f"{self.name} атакует с силой {self.damage}"


class FireTower(Tower):
    def attack(self) -> str:
        return f"{self.name} выпускает огненный шар! Урон: {self.damage}"


class IceTower(Tower):
    def attack(self) -> str:
        return f"{self.name} заморащивает врага! Урон: {self.damage}"


def tower_attack(tower: Tower) -> None:
    print(tower.attack())


def hit_enemy(tower: Tower) -> None:
    print(f"Башня {tower.name} наносит {tower.damage} урона")
    print(f"Эффект: {tower.attack()}")


# Тесты

print("=== Полиморфизм башен ===")

towers = [
    FireTower("Маг Огня", 25),
    IceTower("Маг Льда", 15)
]

for tower in towers:
    tower_attack(tower)

print("\n=== Универсальная атака ===")
hit_enemy(FireTower("Пламенный", 50))