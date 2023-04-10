# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку
# на два прямоугольника).
# Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def check_result(n, m, k):
    if n > m:
        result = 'yes' if (k%m == 0) and (n*m > k) else 'no'
    else:
        result = 'yes' if (k%n == 0) and (n*m > k) else 'no'
    return result

# Тест 1
n = 3
m = 2
k = 4
expected_result = 'yes'
actual_result = check_result(n, m, k)
print('\nТест 1')
print(f'n x m / k: {n} x {m} / {k}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
n = 3
m = 2
k = 1
expected_result = 'no'
actual_result = check_result(n, m, k)
print('\nТест 2')
print(f'n x m / k: {n} x {m} / {k}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
n = 3
m = 2
k = 6
expected_result = 'no'
actual_result = check_result(n, m, k)
print('\nТест 3')
print(f'n x m / k: {n} x {m} / {k}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 4
n = 2
m = 3
k = 2
expected_result = 'yes'
actual_result = check_result(n, m, k)
print('\nТест 4')
print(f'n x m / k: {n} x {m} / {k}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')