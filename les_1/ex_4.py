# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def get_result_str(s):
    return str(int(s/6)) + ' ' + str(int(s/1.5)) + ' ' + str(int(s/6)) #1/6 + 4/6 + 1/6     

# Тест 1
tst_num = 6
expected_result = '1 4 1'
actual_result = get_result_str(int(tst_num))
print('\nТест 1')
print(f'Число: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
tst_num = 24
expected_result = '4 16 4'
actual_result = get_result_str(int(tst_num))
print('\nТест 2')
print(f'Число: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
tst_num = 60
expected_result = '10 40 10'
actual_result = get_result_str(int(tst_num))
print('\nТест 3')
print(f'Число: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')