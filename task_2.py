"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ""

    @abstractmethod
    def get_cons(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.__v = float(v)

    def __str__(self):
        return f"Пальто '{self.name}', размер(V)={self.__v}"

    @property
    def get_cons(self):
        return self.__v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.__h = float(h)

    def __str__(self):
        return f"Костюм '{self.name}', рост(H)={self.__h}"

    @property
    def get_cons(self):
        return self.__h * 2 + 0.3


coat_v33 = Coat(33)
coat_v33.name = "Весна"
print(f"{coat_v33}, ткани потребуется - {coat_v33.get_cons}")

costm_v18 = Costume(1.8)
costm_v18.name = "Бизнес"
print(f"{costm_v18}, ткани потребуется - {costm_v18.get_cons}")

print(f"Общий расход ткани: {coat_v33.get_cons + costm_v18.get_cons}")