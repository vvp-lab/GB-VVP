# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = [1, 2, 'как тебя зовут?', 'меня Владимир', None]

list.append('Почему Вы решили пойти учиться?');

list.append('Я пошел для себя лично, повысить квалификацию.');

print(list);

for i in list:
    print(i, "имеет тип=", type(i))
