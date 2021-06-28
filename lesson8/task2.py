#Lesson 8 task 2

"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OopsDivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    devidend = int(input('Введите число, которое собираетесь разделить: '))
    division = int(input('Введите число, НА которое собираетесь разделить: '))
    if not division:
        raise OopsDivisionByZero('Oops! division by zero')
    print(f'Результат {devidend/division}')

except ValueError:
    print('вы ввели не числа')
except OopsDivisionByZero as error:
    print(error)

