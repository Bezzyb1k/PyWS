"""
Пузырьковая сортировка (Bubble Sort) - простейший алгоритм сортировки
"""

def bubble_sort(arr: list) -> list:

    """
    Сортирует список по возрастанию
    Возвращает новый список, не меняя оригинал
    """

    result = arr.copy()
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result

# Тесты 
print("=== Пузырьковая сортировка ===")

numbers = [65, 64, 43, 32, 12, 22, 0, 15, 100]
print(f"До сортировки: {numbers}")

sorted_numbers = bubble_sort(numbers)
print(f"После сортировки: {sorted_numbers}")
print(f"Оригинал не изменился: {numbers}")