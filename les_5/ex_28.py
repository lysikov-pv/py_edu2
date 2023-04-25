# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.
# Пример:
# 2 2
# 4 

def sum_recurs(a, b):
    if b == 0: return a
    return sum_recurs(a, b-1) + 1

# Тест 1
a = 2
b = 2
expected_result = 4
actual_result = sum_recurs(2, 2)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
a = 20
b = 20
expected_result = 40
actual_result = sum_recurs(20, 20)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 3
a = 2
b = 0
expected_result = 2
actual_result = sum_recurs(2, 0)
print('\nТест 3')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 4
a = 0
b = 2
expected_result = 2
actual_result = sum_recurs(0, 2)
print('\nТест 4')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 