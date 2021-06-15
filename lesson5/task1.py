"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

DIR = 'files'
file_path = os.path.join(DIR, 'task1.txt')
file = open(file_path, 'a', encoding='utf-8')

while True:
    string = input('Введите любой набор символов и я запишу его в файл: ')

    if not string:
        file.close()
        print('Выход')
        break

    file.write(f'{string}\n')
