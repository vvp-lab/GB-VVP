#4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.



class Car:

    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return print('Поехали')

    def stop(self):
        return print('Приехали')

    def turn(self, direction):
        return print(f'Направляемся {direction}')

    def show_speed(self):
        return self.speed


class PoliceCar(Car):
    is_police = True
    name = 'FORD'
    color = 'White and black'
    speed = 100.0

class TownCar(Car):
    is_police = False
    name = "Jiguli"
    color = "Rjavyi"
    speed = 80.0

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)

class WorkCar(Car):
    is_police = False
    name = 'Kamaz'
    color = 'Orange'
    speed = 80

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)

class SporCar(Car):
    is_police = False
    name = 'ferrari'
    color = 'Red'
    speed = 180.0



tc = TownCar()
pc = PoliceCar()
sc = SporCar()
wc = WorkCar()

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)

pc.go()
print(wc.turn(direction='туда'))
sc.speed = 10000

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)
