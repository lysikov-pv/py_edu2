# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# Пример:
# 5 -> 1 0 1 1 0
# 2

def min_repeat(lst):
    side1 = 0
    side2 = 0
    for i in lst:
        if lst[i] == 1:
            side1 += 1
        else:
            side2 += 1
    return side1 if (0 < side1 < side2 or side2 == 0) else side2

# Тест 1
n = 5
lst = [1, 0, 1, 1, 0]
expected_result = 2
actual_result = min_repeat(lst)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
n = 7
lst = [1, 1, 1, 1, 1, 1, 1]
expected_result = 7
actual_result = min_repeat(lst)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
n = 4
lst = [0, 0, 0, 0]
expected_result = 4
actual_result = min_repeat(lst)
print('\nТест 3')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')