# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример: 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

def find_similar(lst1, lst2):
    # return sorted(list(set(lst1).intersection(set(lst2))))
    return quicksort(list(set(lst1).intersection(set(lst2))))

def quicksort(lst):
	if len(lst) < 2:
		return lst
	else:
		less = [i for i in lst[1:] if i <= lst[0]]
		greater = [i for i in lst[1:] if i > lst[0]]
	return quicksort(less) + [lst[0]] + quicksort(greater)

# Тест 1
lst1 = [2, 4, 6, 8, 10, 12, 8, 6, 4, 2]
lst2 = [3, 6, 9, 12, 15, 18]
expected_result = [6, 12]
actual_result = find_similar(lst1, lst2)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
lst1 = [2, 4, 6, 8, 10, 12, 8, 6, 4, 2]
lst2 = [3, 9, 15, 18]
expected_result = []
actual_result = find_similar(lst1, lst2)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 