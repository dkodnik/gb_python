"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def _car_name(self):
        return f"{self.name}-{self.color}"

    def go(self, speed):
        self.speed = speed
        print(f"{self._car_name()}: Go")

    def stop(self):
        self.speed = 0
        print(f"{self._car_name()}: Stop")

    def turn(self, direction):
        print(f"{self._car_name()}: Turn -> {direction}")

    def show_speed(self):
        print(f"{self._car_name()}: Speed = {self.speed}")


class TownCar(Car):
    def __init__(self):
        self.name = "Town"

    def show_speed(self):
        if self.speed > 60:
            print(f"{self._car_name()}: Over speed!")
        super().show_speed()


class SportCar(Car):
    def __init__(self):
        self.name = "Sport"


class WorkCar(Car):
    def __init__(self):
        self.name = "Work"

    def show_speed(self):
        if self.speed > 40:
            print(f"{self._car_name()}: Over speed!")
        super().show_speed()


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True
        self.name = "Police"


tc = TownCar()
tc.color = "yellow"
tc.go(100)
tc.show_speed()
tc.go(20)
tc.show_speed()
tc.turn("left")
tc.stop()

sc = SportCar()
sc.color = "red"
sc.go(100)
sc.show_speed()
sc.turn("left")
sc.stop()

wc = WorkCar()
wc.color = "green"
wc.go(100)
wc.show_speed()
wc.go(20)
wc.show_speed()
wc.turn("left")
wc.stop()

pc = PoliceCar()
pc.color = "black"
pc.go(100)
pc.show_speed()
pc.turn("left")
pc.stop()
