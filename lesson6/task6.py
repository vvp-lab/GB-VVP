#6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        return 'some basic stuff'

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        return self.title

class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        return self.title


p = Pen()
pc = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(h.draw())
print(p.draw())