"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'task5.txt')
file_to_write_path = os.path.join(DIR, 'task5.txt')
nums_list_to_write = []

while True:
    try:
        num = float(input('Введите число: '))
        nums_list_to_write.append(str(num))
    except ValueError:
        print('Ввод чисел прерван.')
        break

with open(file_to_write_path, 'w', encoding='utf-8') as file_write:
    print(f'{" ".join(nums_list_to_write)}', file=file_write)

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    nums_list = file_read.readline().split()
    nums_sum = 0
    for num in nums_list:
        nums_sum += float(num)

print(f'Сумма чисел:{nums_sum}')
