"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        self.title = "Ручка"

    def draw(self):
        print("Запуск", self.title)


class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"

    def draw(self):
        print("Запуск", self.title)


class Handle(Stationery):
    def __init__(self):
        self.title = "Маркер"

    def draw(self):
        print("Запуск", self.title)


el1 = Stationery()
el2 = Pen()
el3 = Pencil()
el4 = Handle()

el1.draw()
el2.draw()
el3.draw()
el4.draw()
print("title=", el1.title)
