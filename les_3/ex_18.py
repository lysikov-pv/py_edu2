# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

def find_similar(lst, n):
    result = None
    result_dif = abs(lst[0]-n)
    for i in lst:
        i_dif = abs(i - n)
        if result_dif > i_dif:
            result = i
            result_dif = i_dif
    return result

# Тест 1
lst = [1, 2, 3, 4, 5]
n = 6
expected_result = 5
actual_result = find_similar(lst, n)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
lst = [1, 2, -3, 4, 5]
n = -2
expected_result = -3
actual_result = find_similar(lst, n)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 