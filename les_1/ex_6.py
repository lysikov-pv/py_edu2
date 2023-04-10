# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с
# номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

def check_ticket(n):
    return 'yes' if (int(n[0]) + int(n[1]) + int(n[2])) == (int(n[3]) + int(n[4]) + int(n[5])) else 'no'

# Тест 1
tst_num = 385916
expected_result = 'yes'
actual_result = check_ticket(str(tst_num))
print('\nТест 1')
print(f'Номер билета: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
tst_num = 123456
expected_result = 'no'
actual_result = check_ticket(str(tst_num))
print('\nТест 2')
print(f'Номер билета: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
tst_num = '000000'
expected_result = 'yes'
actual_result = check_ticket(str(tst_num))
print('\nТест 3')
print(f'Номер билета: {tst_num}')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')
