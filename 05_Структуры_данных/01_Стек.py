"""
Стек - структура данных LIFO (Last In, First Out)
"""

class Stack:
    
    """Реализация стека на основе списка"""

    def __init__(self):
        self._items = []

    
    def push(self, item) -> None:

        """Добавляет элемент на вершину стека"""

        self._items.append(item)
    

    def pop(self):

        """Удаляет и возвращает жлементы с вершины стека"""

        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()


    def peek(self):

        """Возвращает верхний элемент стека без удаления"""

        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]


    def is_empty(self) -> bool:

        """Проверяет, пуст ли стек"""

        return len(self._items) == 0


    def size(self) -> int:

        """Возвращает количество элементов в стеке"""

        return len(self._items)


    def __str__(self) -> str:
        return f"Stack({self._items})"


# Тесты
print("=== Создание стека ===")
stack = Stack()
print(stack)

print("\n=== Добавление элементов ===")
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)

print("\n=== Просмотр верхнего элемента ===")
print(f"peek(): {stack.peek()}")
print(f"Размер стека: {stack.size()}")

print("\n=== Удаление элементов ===")
print(f"pop(): {stack.pop()}")
print(f"pop(): {stack.pop()}")
print(f"pop(): {stack.pop()}")
print(stack)

print("\n=== Проверка на пустоту ===")
print(f"is_empty(): {stack.is_empty()}")

print("\n=== Обработка ошибки ===")
try:
    stack.pop()
except IndexError as Error:
    print(f"Ошибка: {Error}")