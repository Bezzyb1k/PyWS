"""
Инкапсуляция - скрытие внутреннего состояния объекта и контроль доступа к нему
"""

class BankAccount:

    """Банковский счёт с защищенными данными"""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance # Приватный атрибут
        self.__transactions: list[str] = [] # Приватный список операций 


    def deposit(self, amount: float) -> None:

        """Пополнение счета"""

        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        self.__balance += amount
        self.__transactions.append(f"Пополнение: +{amount}")
        print(f"Счет пополнен на {amount}. Баланс {self.__balance}")


    def withdraw(self, amount: float) -> None:

        """Снятие со счёта"""

        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        if amount > self.__balance:
            print(f"Недостаточно средств. Баланс: {self.__balance}")
            return

        self.__balance -= amount
        self.__transactions.append(f"Снятие: -{amount}")
        print(f"Снято {amount}. Баланс: {self.__balance}")


    def get_balance(self) -> float:

        """Получить текущий баланс (геттер)"""

        return self.__balance


    def get_transactions(self) -> list[str]:

        """Получить историю операций (геттер)"""

        return self.__transactions.copy() # Возвращает копию, чтобы не изменили оригинал


    def __str__(self) -> str:
        return f"Владелец: {self.owner} | Баланс: {self.__balance}"


# Пример с игровым персонажем
class Player:

    """Игрок с защищенным здоровьем"""

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.__health = health
        self.__max_health = health


    def take_damage(self, damage: int) -> None:

        """Получить урон"""

        if damage < 0:
            print("Урон не может быть отрицательным")
            return

        self.__health -= damage

        if self.__health <= 0:
            self.__health = 0
            print(f"{self.name} Погиб")
        else:
            print(f"{self.name} получил {damage} урона. Осталось {self.__health} HP")


    def heal(self, amount: int) -> None:

        """Лечение"""

        if amount < 0:
            print("Лечение не может быть отрицательным")
            return

        self.__health += amount

        if self.__health > self.__max_health:
            self.__health = self.__max_health

        print(f"{self.name} восстановил {amount} HP. Текущее здоровье {self.__health}")


    def get_health(self) -> int:

        """Получить текущее здоровье (геттер)"""

        return self.__health


    def is_alive(self) -> bool:

        """Проверка, жив ли игрок"""

        return self.__health > 0


    def __str__(self) -> str:
        status = 'жив' if self.is_alive() else "мёртв"
        return f"{self.name} | HP: {self.__health}/{self.__max_health} | {status}"


# Тесты
print("=== Банковский счет ===")
account = BankAccount('Toothless', 1000)
print(account)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000) # недостаточно средств

print(f"Текущий баланс: {account.get_balance()}")
print(f"История операция: {account.get_transactions()}")

# Попытка изменить приватный атрибут напрямую (не сработает)
# account.__balance = 9999 - ОШИБКА


print("\n=== Игрок ===")
player = Player("toothless", 100)
print(player)

player.take_damage(30)
player.take_damage(50)
player.heal(20)
print(player)

# Попытка изменить здорвье напрямую (НЕ СРАБОТАЕТ)
# player.__health = 999 - ОШИБКА