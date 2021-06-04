# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_func(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return
    except ValueError:
        return


print(my_func(float(input('Введи число 1: ')), float(input('Введи число2: '))))
