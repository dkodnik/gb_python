"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class Cmplx:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get(self):
        return self.__a, self.__b

    def __str__(self):
        if self.__b >= 0:
            return f"{self.__a}+{self.__b}j"
        else:
            return f"{self.__a}{self.__b}j"

    def __add__(self, other):
        other_a, other_b = other.get()
        return Cmplx(self.__a + other_a, self.__b + other_b)

    def __mul__(self, other):
        other_a, other_b = other.get()
        return Cmplx(self.__a * other_a, self.__b * other_b)


c1 = Cmplx(4, 6)
print(c1)
c2 = Cmplx(-2, 7)
print(c2)
c3 = Cmplx(3, -5)
print(c3)
c4 = c1 + c2
print(f"({c1}) + ({c2}) = ({c4})")
c5 = c2 * c3
print(f"({c2}) * ({c3}) = ({c5})")
