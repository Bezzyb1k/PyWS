"""
Рекурсия - функция вызывает саму себя
"""

# Факториал (классический пример)
def factorial(n: int) -> int:

    """
    Возвращает факториал числа n (n!)
    n! = n * (n - 1) * (n - 2) * ... * 1
    """

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("=== Факториал ===")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(7) = {factorial(7)}")

# Сумма чисел от 1 до n
def sum_range(n: int) -> int:

    """Возвращает сумму всех чисел от 1 до n"""

    if n == 0:
        return 0
    return n + sum_range(n - 1)


print("\n=== Сумма чисел ===")
print(f"sum_range(5) = {sum_range(5)}")
print(f"sum_range(10) = {sum_range(10)}")


# Числа Фибоначчи
def fibonacci(n: int) -> int:

    """
    Возвращает n-e число Фибоначчи
    f(0) = 0, f(1) = 1, f(n) = f(n - 1) + f(n - 2)
    """

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"\n=== Числа Фибоначчи ===")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")


# Рекурсивный обход списка
def print_list_recursive(arr: list, index: int = 0) -> None:

    """Выводит элементы списка рекурсивно"""

    if index >= len(arr):
        return
    print(arr[index], end = " ")
    print_list_recursive(arr, index + 1)


print("\n=== Рекурсивный обход списка ===")
data = [1, 2, 3, 4, 5]
print_list_recursive(data)


# Рекурсивный поиск в глубину
def tree_depth(node: dict) -> int:

    """
    Возвращает максимальную глубину дерева
    Каждый узел - словарь с ключом 'children' (список узлов)
    """

    if not node.get("children"):
        return 1
    return 1 + max(tree_depth(child) for child in node["children"])


print("\n=== Глубина дерева ===")
tree = {
    "name": "корень",
    "children": [
        {"name": "узел1", "children": [
            {"name": "лист1", "children": []}
        ]},
        {"name": "узел2", "children": [
            {"name": "лист2", "children": []},
            {"name": "лист3", "children": []}
        ]}
    ]
}
print(f"Глубина дерева: {tree_depth(tree)}")