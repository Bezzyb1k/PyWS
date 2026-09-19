"""
Быстрая сортировка (Quick Sort) - один из самых эффективных алгоритмов
"""

def quick_sort(arr: list) -> list:

    """
    Сортирует список по возрастанию
    Возвращает новый список, не меняя оригинал
    """

    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr: list, low: int = 0, high: int = None) -> None:

    """
    Сортирует список на месте (in-place), меняя оригинал
    """

    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)


def partition(arr: list, low: int, high: int) -> int:

    """Разделяет список относительно опорного элемента"""

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

# Тесты

print("=== Быстрая сортировка (новый список) ===")

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"До сортировки: {numbers}")

sorted_numbers = quick_sort(numbers)
print(f"После сортировки: {sorted_numbers}")
print(f"Оригинал не изменился: {numbers}")

print("\n=== Быстрая сортировка (in-place) ===")

numbers2 = [64, 34, 25, 12, 22, 11, 90]
print(f"До сортировки: {numbers2}")

quick_sort_in_place(numbers2)
print(f"После сортировки: {numbers2}")
print(f"Оригинал изменился: {numbers2}")