"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
import time


class TrafficLight:
    __color = ""

    def __init__(self):
        self.__color = "красный"
        self.__tic_sec = 0
        self._time_red_sec = 7
        self._time_yellow_sec = 2
        self._time_green_sec = 4

    def running(self):
        print(self.__tic_sec + 1, self.__color)
        if self.__color == "красный":
            if self.__tic_sec < self._time_red_sec - 1:
                self.__tic_sec += 1
            else:
                self.__tic_sec = 0
                self.__color = "желтый"
        elif self.__color == "желтый":
            if self.__tic_sec < self._time_yellow_sec - 1:
                self.__tic_sec += 1
            else:
                self.__tic_sec = 0
                self.__color = "зеленый"
        elif self.__color == "зеленый":
            if self.__tic_sec < self._time_green_sec - 1:
                self.__tic_sec += 1
            else:
                self.__tic_sec = 0
                self.__color = "красный"


# время работы программы в сек.
FULL_TIC_SEC = 16
step = 0
tf = TrafficLight()
while FULL_TIC_SEC > step:
    tf.running()
    step += 1
    time.sleep(1)  # пауза 1сек
