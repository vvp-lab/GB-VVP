# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input("Введите число секунд: "))
print("Вы ввели секунд", user_time);

hour = user_time // 3600
second_hour = user_time % 3600
minutes = second_hour // 60
second = second_hour % 60

print("{:02d}:{:02d}:{:02d}".format(hour, minutes, second))
