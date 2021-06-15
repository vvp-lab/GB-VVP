"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

import os, json

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'task7.txt')
file_to_write_path = os.path.join(DIR, 'task7.json')

result = []
profit = {}
average = []

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    counter = 1
    while True:
        line = file_read.readline().split()

        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1

result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_to_write_path, 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write)
