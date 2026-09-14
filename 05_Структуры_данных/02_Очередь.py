"""
Очередь - структура данных FIFO (First In, First Out)
"""

class Queue:

    """Реализация очереди на основе списка"""

    def __init__(self):
        self._items = []


    def enqueue(self, item) -> None:

        """Добавляет элемент в конце очереди"""

        self._items.append(item)


    def dequeue(self):

        """Удаляет и возвращает первый элемент очереди"""

        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items.pop(0)


    def peek(self):

        """Возвращает первый элемент очереди без удаления"""

        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items[0]


    def is_empty(self) -> bool:

        """Проверяет, пуста ли очередь"""

        return len(self._items) == 0


    def size(self) -> int:

        """Возвращает количество элементов в очереди"""

        return len(self._items)


    def __str__(self) -> str:
        return f"Queue({self._items})"


# Тесты

print("=== Создание очереди ===")
queue = Queue()
print(queue)

print("\n=== Добавление элементов ===")
queue.enqueue('Первый')
queue.enqueue("Второй")
queue.enqueue("Третий")
print(queue)

print("\n=== Просмотр первого элемента ===")
print(f"peek(): {queue.peek()}")
print(f"Размер очереди: {queue.size()}")

print("\n=== Удаление элементов ===")
print(f"dequeue(): {queue.dequeue()}")
print(f"dequeue(): {queue.dequeue()}")
print(f"dequeue(): {queue.dequeue()}")
print(queue)

print("\n=== Проверка на пустоту ===")
print(f"is_empty(): {queue.is_empty()}")

print("\n=== Обработка ошибки ===")
try:
    queue.dequeue()
except IndexError as Error:
    print(f"Ошибка: {Error}")