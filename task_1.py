"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.__date_str = date

    def __str__(self):
        if not Date.valid(self.__date_str):
            return "Введены не корректные данные"
        else:
            date_arr = Date.trsform(self.__date_str)
            return f"Год: {date_arr[2]}, месяц: {date_arr[1]}, день: {date_arr[0]}"

    @classmethod
    def trsform(cls, date_str):
        return [int(el) for el in date_str.split("-") if str(el).isnumeric()]

    @staticmethod
    def valid(date_str: str) -> bool:
        date_arr = Date.trsform(date_str)
        if date_arr[2] < 0:
            return False
        v_year = False
        if not date_arr[2] % 4:
            v_year = True
        if not 1 <= date_arr[1] <= 12:
            return False
        elif v_year and date_arr[1] == 2 and not 1 <= date_arr[0] <= 29:
            return False
        elif not v_year and date_arr[1] == 2 and not 1 <= date_arr[0] <= 28:
            return False
        elif date_arr[1] in [1, 3, 5, 6, 7, 10, 12] and not 1 <= date_arr[0] <= 31:
            return False
        elif date_arr[1] not in [1, 2, 3, 5, 6, 7, 10, 12] and not 1 <= date_arr[0] <= 30:
            return False
        return True


dt1 = Date("31-03-2021")
print(dt1)
dt2 = Date("29-02-2021")
print(dt2)

# доп.проверки
print(Date.valid("01-00-2017"))  # bad
print(Date.valid("32-12-2017"))  # bad
print(Date.valid("01-13-2017"))  # bad
print(Date.valid("01-13-2017"))  # bad
print(Date.valid("28-02-2018"))
print(Date.valid("29-02-2018"))  # bad
print(Date.valid("29-02-2020"))
print(Date.valid("29-02-2021"))  # bad
print(Date.valid("31-05-2021"))
print(Date.valid("31-04-2021"))  # bad
