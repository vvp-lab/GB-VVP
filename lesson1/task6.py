# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = float(input("Сколько км пробежит спортсмен в первый день: "))
b = float(input("Какая цель в км: "))

d = 1
print("{}-ый день:{}".format(d, round(a,2)));
while a < b:
    a = a * 1.1
    d = d + 1
    print("{}-ый день:{}".format(d, round(a,2)));

print("Ответ: на {}-й день спортсмен достиг результата — не менее {} км.".format(d, int(a)));