# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

def find_exp(n):
    result = []
    i = 0
    while 2**i <= n:
        result.append(2**i)
        i += 1
    return result

# Тест 1
n = 10
expected_result = [1, 2, 4, 8]
actual_result = find_exp(n)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
n = 1
expected_result = [1]
actual_result = find_exp(n)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 3
n = 30
expected_result = [1, 2, 4, 8, 16]
actual_result = find_exp(n)
print('\nТест 3')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 