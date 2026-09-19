"""
Big O нотация — оценка сложности алгоритмов.
"""

import time


# O(1) — Константная сложность

def get_first(arr: list):

    """Возвращает первый элемент. Время не зависит от размера."""

    return arr[0]


# O(n) — Линейная сложность

def find_max(arr: list) -> int:

    """Находит максимум. Проходит по всем элементам."""

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num

    return max_val


# O(n²) — Квадратичная сложность

def has_duplicates(arr: list) -> bool:

    """Проверяет дубликаты. Двойной цикл."""

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
            
    return False


# O(log n) — Логарифмическая сложность

def binary_search(arr: list, target) -> int:

    """Бинарный поиск. Каждый шаг делит список пополам."""

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


# O(n log n) — Линеарифмическая сложность

def quick_sort(arr: list) -> list:

    """Быстрая сортировка. Лучший случай O(n log n)."""

    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Тесты

print("=== O(1) — Константная сложность ===")
small = list(range(10))
big = list(range(1000000))

start = time.time()
print(f"get_first(small): {get_first(small)}")
end = time.time()
print(f"Время: {end - start:.6f} сек")

start = time.time()
print(f"get_first(big): {get_first(big)}")
end = time.time()
print(f"Время: {end - start:.6f} сек\n")

print("=== O(n) — Линейная сложность ===")

start = time.time()
print(f"find_max(1000): {find_max(list(range(1000)))}")
end = time.time()
print(f"Время: {end - start:.6f} сек\n")

print("=== O(log n) — Логарифмическая сложность ===")
sorted_big = list(range(1000000))

start = time.time()
print(f"binary_search(500000): индекс {binary_search(sorted_big, 500000)}")
end = time.time()
print(f"Время: {end - start:.6f} сек\n")

print("=== O(n²) — Квадратичная сложность ===")

start = time.time()
print(f"has_duplicates(100): {has_duplicates(list(range(100)))}")
end = time.time()
print(f"Время: {end - start:.6f} сек\n")

print("=== O(n log n) — Линеарифмическая сложность ===")
unsorted = [5, 2, 8, 1, 9, 3, 7, 4, 6]

start = time.time()
print(f"quick_sort: {quick_sort(unsorted)}")
end = time.time()
print(f"Время: {end - start:.6f} сек")