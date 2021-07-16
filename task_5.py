"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Srart of drawing.")

class Pen(Stationery):
    def draw(self):
        print(self.title, " draws.")


class Pencil(Stationery):
    def draw(self):
        print(self.title, " draws.")


class Handle(Stationery):
    def draw(self):
        print(self.title, " draws.")


stationery_1 = Pen("Pen")
stationery_2 = Pencil("Pencil")
stationery_3 = Handle("Handle")

stationery_1.draw()
stationery_2.draw()
stationery_3.draw()