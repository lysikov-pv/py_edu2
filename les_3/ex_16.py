# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N]. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих строках записаны N целых чисел
# Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

def simple_count(lst, n):
    return lst.count(n)

def alg_count(lst, n):
    count = 0
    for i in lst:
        if i == n: count += 1
    return count

# Тест 1
lst = [1, 2, 3, 4, 5]
n = 3
expected_result = 1
actual_result = alg_count(lst, n)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
lst = [1, 2, 3, 4, 5, 3]
n = 3
expected_result = 2
actual_result = alg_count(lst, n)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 3
lst = [1, 2, 3, 4, 5, 3]
n = -1
expected_result = 0
actual_result = alg_count(lst, n)
print('\nТест 3')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 