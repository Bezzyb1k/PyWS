"""
Бинарный поиск (Binary Search) — поиск в отсортированном списке.
"""


def binary_search(arr: list, target) -> int:

    """
    Ищет target в отсортированном списке arr.
    Возвращает индекс элемента или -1, если не найден.
    """

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr: list, target, left: int = 0, right: int = None) -> int:

    """
    Рекурсивная версия бинарного поиска.
    """

    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Тесты


print("=== Бинарный поиск (итеративный) ===")

numbers = [11, 12, 22, 25, 34, 64, 90]
print(f"Список: {numbers}")

print(f"Поиск 25: индекс {binary_search(numbers, 25)}")
print(f"Поиск 90: индекс {binary_search(numbers, 90)}")
print(f"Поиск 11: индекс {binary_search(numbers, 11)}")
print(f"Поиск 100: индекс {binary_search(numbers, 100)}")

print("\n=== Бинарный поиск (рекурсивный) ===")
print(f"Поиск 34: индекс {binary_search_recursive(numbers, 34)}")
print(f"Поиск 12: индекс {binary_search_recursive(numbers, 12)}")
print(f"Поиск 99: индекс {binary_search_recursive(numbers, 99)}")

print("\n=== Сравнение с линейным поиском ===")

def linear_search(arr: list, target) -> int:

    """Линейный поиск — перебирает все элементы по порядку."""
    
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

big_list = list(range(1000))
print(f"Линейный поиск 999: индекс {linear_search(big_list, 999)}")
print(f"Бинарный поиск 999: индекс {binary_search(big_list, 999)}")