# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def getsum_str(s):
    return (int(s[0]) + int(s[1]) + int(s[2]))

def getsum_int(n):
    return (n//100 + (n - n//100*100)//10 + n%10)

# Тест 1
tst_num = 123
expected_result = 6
actual_result = getsum_int(int(tst_num))
print('\nТест 1')
print(f'Число: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
tst_num = 100
expected_result = 1
actual_result = getsum_int(int(tst_num))
print('\nТест 2')
print(f'Число: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
tst_num = '001'
expected_result = 1
actual_result = getsum_int(int(tst_num))
print('\nТест 3')
print(f'Число: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')