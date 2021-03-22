"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу
метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _lenght = 0
    _width = 0

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def full_weight(self, weight_kg, thickness_cm):
        return (self._lenght * self._width * weight_kg * thickness_cm) / 1000


lenght_m = 5000
width_m = 20
weight_kg = 25
thickness_cm = 5

rd = Road(lenght_m, width_m)
fw_t = rd.full_weight(weight_kg, thickness_cm)
print(f"{width_m}м * {lenght_m}м * {weight_kg}кг * {thickness_cm}см = {fw_t}т")
