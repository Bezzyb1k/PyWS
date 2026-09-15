"""
Связные списки - структура данных из узлов
Каждый узел хранит значение и ссылку на следующий узел
"""

class Node:

    """Узел связного списка"""

    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return f"None({self.value})"


class LinkedList:

    """Односвязный список"""

    def __init__(self):
        self.head = None
        self._size = 0


    def append(self, value) -> None:

        """Добавляет элемент в конец списка"""

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1


    def prepend(self, value) -> None:

        """Добавляет элемент в начало списка"""

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1


    def remove(self, value) -> bool:

        """Удаляет первое вхождение элемента. Возвращает True, если удалено"""

        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head

        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True

            current = current.next

        return False


    def find(self, value) -> bool:

        """Проверяет, если ли значение в списке"""

        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


    def is_empty(self) -> bool:

        """Проверяет, пуст ли список"""

        return self.head is None


    def size(self) -> int:

        """Возвращает количество элементов"""

        return self._size


    def __str__(self) -> str:
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Пустой список"



# Тесты
print("=== Создание списка ===")
lst = LinkedList()
print(lst)

print("\n=== Добавление в конец ===")
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)

print("\n=== Добавление в начало ===")
lst.prepend(5)
print(lst)

print("\n=== Поиск ===")
print(f"find(20): {lst.find(20)}")
print(f"find(99): {lst.find(99)}")

print("\n=== Удаление ===")
lst.remove(20)
print(lst)
lst.remove(99)
print(lst)

print("\n=== Размер ===")
print(f"size(): {lst.size()}")

print("\n=== Пустой список ===")
empty = LinkedList()
print(empty)
print(f"is_empty(): {empty.is_empty()}")