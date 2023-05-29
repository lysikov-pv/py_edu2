# Задача 37: Создать телефонный справочник с возможностью импорта и экспорта
# данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления
# данных. Пользователь также может ввести имя или фамилию, и Вы должны
# реализовать функционал для изменения и удаления данных

import os

FILE_PATH = r"les_8\base.txt"

def read_base():
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
    return list(enumerate(lines))

def print_records(records):
    numerated_records=list(enumerate(records))
    for record in numerated_records:
        print(f'{record[0]+1}. {record[1][1].replace(";", ": ").strip()}')

def print_record(record):
    print(f'{record[1].replace(";", ": ").strip()}')

def print_base():
    base=read_base()
    os.system('cls')
    print_records(base)

def find_records():
    os.system('cls')
    str=input('Строка для поиска: ')
    base=read_base()
    result = []
    for record in base:
        if str.lower() in record[1].lower():
            result.append(record)
    return result

def find_n_print():
    records=find_records()
    os.system('cls')
    print_records(records)

def add_record():
    os.system('cls')
    name=input('Введите имя: ')
    phone=input('Введите телефон: ')
    with open(FILE_PATH, 'a') as f:
        f.write(f'\n{name};{phone}')

def save_base(base):
    with open(FILE_PATH, 'w') as f:
        for record in base:
            f.write(record[1])

def del_record():
    base=read_base()
    os.system('cls')
    print_records(base)
    num=int(input('Введите номер записи для удаления: '))
    base.pop(num-1)
    base[-1]=base[-1][0],base[-1][1].strip()
    save_base(base)

def edit_record():
    base=read_base()
    os.system('cls')
    print_records(base)
    num=int(input('Введите номер записи для редактирования: '))
    os.system('cls')
    print(f'Запись для редактирования:')
    print_record(base[num-1])
    name,phone=base[num-1][1].split(';')
    option=int(input('\n1. Удалить\n2. Имя\n3. Телефон\nУкажите какое поле редактируем: '))
    if option==2:
        name=input('Введите новое имя: ')
    if option==3:        
        phone=input('Введите новый телефон: ')
    base[num-1] = base[num-1][0],f'{name};{phone}\n' if num<len(base) else  f'{name};{phone}'
    if option==1:
        base.pop(num-1)
        base[-1]=base[-1][0],base[-1][1].strip()
    save_base(base)

def find_n_edit():
    base=read_base()
    records=find_records()
    os.system('cls')
    print_records(records)
    num=int(input('Введите номер записи для редактирования: '))
    os.system('cls')
    print(f'Запись для редактирования:')
    print_record(records[num-1])
    name,phone=records[num-1][1].split(';')
    option=int(input('\n1. Удалить\n2. Имя\n3. Телефон\nУкажите какое поле редактируем: '))
    if option==2:
        name=input('Введите новое имя: ')
    if option==3:        
        phone=input('Введите новый телефон: ')
    base[records[num-1][0]] = records[num-1][0],f'{name};{phone}\n' if num<len(base) else  f'{name};{phone}'
    if option==1:
        base.pop(records[num-1][0])
        base[-1]=base[-1][0],base[-1][1].strip()
    save_base(base)

def menu():
    while True:
        os.system('cls')
        print('1. Вывести телефонную книгу')
        print('2. Поиск по тефонной книге')
        print('3. Добавить запись')
        print('4. Удалить запись')
        print('5. Редактировать запись')
        print('6. Найти и редактировать запись')
        print('0. Выход')
        input_num = int(input('Введите номер: '))
        if input_num == 1:
            print_base()
        elif input_num == 2:
            find_n_print()
        elif input_num == 3:
            add_record()
        elif input_num == 4:
            del_record()
        elif input_num == 5:
            edit_record()
        elif input_num == 6:
            find_n_edit()
        elif input_num == 0:
            break    
        input('Нажмите Enter для продолжения...')
menu()