# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
import argparse

parser = argparse.ArgumentParser(description='Calculate salary')
parser.add_argument('--rate', type=float)
parser.add_argument('--hours', type=float)
parser.add_argument('--prize', default=None, type=float)

args = parser.parse_args(argv[1:])


def salary(rate: float, hours: float, prize: float):
    return rate * hours + prize


print(f'ЗП: {salary(rate=args.rate, hours=args.hours, prize=args.hours)} руб')
