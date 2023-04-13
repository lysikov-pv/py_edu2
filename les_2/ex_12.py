# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#  Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.
# Пример:
# 4 4 -> 2 6
# 5 6 -> 2 3

def gues_math(s, p):
    d = s**2 - 4*p
    if d < 0:
        result = None
    else:
        x1 = (s - d**0.5) / 2
        x2 = (s + d**0.5) / 2
        if int(x1) == x1 and int(x2) == x2:
            result = [int(x1), int(x2)]
        else:
            result = None
    return result

def gues_enum(s, p):
    result = None
    i = 1
    while i < s and result == None:
        if p == i * (s-i):
            result = [i, s-i]
        i += 1
    return result


# Тест 1
s = 4
p = 4
expected_result = [2, 2]
actual_result = gues_enum(s, p)
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 2
s = 5
p = 6
expected_result = [2, 3]
actual_result = gues_enum(s, p)
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 3
s = 5
p = 5
expected_result = None
actual_result = gues_enum(s, p)
print('\nТест 3')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 4
s = 4
p = 5
expected_result = None
actual_result = gues_enum(s, p)
print('\nТест 4')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')

# Тест 5
s = 10
p = 9
expected_result = [1, 9]
actual_result = gues_enum(s, p)
print('\nТест 5')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}')