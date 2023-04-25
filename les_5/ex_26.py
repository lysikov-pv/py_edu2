# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exp_recurs(a, b): # a**b
    if b == 0: return 1
    return exp_recurs(a, b-1) * a

# Тест 1
a = 2
b = 3
expected_result = 8
actual_result = exp_recurs(2, 3)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
a = 3
b = 5
expected_result = 243
actual_result = exp_recurs(3, 5)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 3
a = 3
b = 0
expected_result = 1
actual_result = exp_recurs(3, 0)
print('\nТест 3')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 