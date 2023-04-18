# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки
# распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B,
# C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z –
# 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1
# очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З,
# Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Пример:
# ноутбук
# 12

def cost(n):
    for key in dic:
        if n in key:
            return dic.get(key)

def sum_costs(str):
    return sum(cost(n) for n in list(str))
 
dic = {
    'AEIOULNSTRАВЕИНОРСТ' : 1, 'DGДКЛМПУ' : 2, 'BCMPБГЁЬЯ' : 3,
    'FHVWYЙЫ' : 4, 'KЖЗХЦЧ' : 5, 'JXШЭЮ' : 8, 'QZФЩЪ' :10
    }

# Тест 1
str = 'ноутбук'
expected_result = 12
actual_result = sum_costs(str.upper())
print('\nТест 1')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 

# Тест 2
str = 'laptop'
expected_result = 10
actual_result = sum_costs(str.upper())
print('\nТест 2')
print(f'Результат: {actual_result}. Результат верен: {actual_result == expected_result}') 