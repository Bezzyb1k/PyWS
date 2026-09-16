"""
Хеш-таблица — структура данных для хранения пар ключ → значение.
Работает за счёт хеш-функции, которая превращает ключ в индекс.
"""


class HashTable:

    """Реализация хеш-таблицы методом цепочек."""


    def __init__(self, size: int = 10):
        self.size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0


    def _hash(self, key) -> int:

        """Превращает ключ в индекс от 0 до size-1."""

        return hash(key) % self.size


    def set(self, key, value) -> None:

        """Добавляет или обновляет пару ключ → значение."""

        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._count += 1


    def get(self, key):

        """Возвращает значение по ключу. Если ключа нет — None."""

        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None


    def remove(self, key) -> bool:

        """Удаляет пару по ключу. Возвращает True, если удалено."""

        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._count -= 1
                return True

        return False


    def contains(self, key) -> bool:

        """Проверяет, есть ли ключ в таблице."""

        return self.get(key) is not None


    def keys(self) -> list:

        """Возвращает все ключи."""

        result = []
        for bucket in self._buckets:
            for k, v in bucket:
                result.append(k)
        return result


    def values(self) -> list:

        """Возвращает все значения."""

        result = []
        for bucket in self._buckets:
            for k, v in bucket:
                result.append(v)
        return result


    def items(self) -> list:

        """Возвращает все пары ключ → значение."""

        result = []
        for bucket in self._buckets:
            for k, v in bucket:
                result.append((k, v))
        return result


    def size_of(self) -> int:

        """Возвращает количество элементов."""

        return self._count


    def __str__(self) -> str:

        return f"HashTable({self.items()})"


# ============================================================
# Тесты
# ============================================================

print("=== Создание таблицы ===")
table = HashTable()
print(table)

print("\n=== Добавление элементов ===")
table.set("name", "Беззубик")
table.set("age", 20)
table.set("city", "Moscow")
print(table)

print("\n=== Получение значений ===")
print(f"get('name'): {table.get('name')}")
print(f"get('age'): {table.get('age')}")
print(f"get('unknown'): {table.get('unknown')}")

print("\n=== Обновление значения ===")
table.set("age", 21)
print(f"get('age') после обновления: {table.get('age')}")

print("\n=== Проверка наличия ключа ===")
print(f"contains('name'): {table.contains('name')}")
print(f"contains('unknown'): {table.contains('unknown')}")

print("\n=== Удаление ===")
table.remove("city")
print(table)

print("\n=== Ключи и значения ===")
print(f"keys(): {table.keys()}")
print(f"values(): {table.values()}")
print(f"items(): {table.items()}")

print("\n=== Размер ===")
print(f"size_of(): {table.size_of()}")