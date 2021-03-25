"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix():
    def __init__(self, matrix):
        # проверка матрицы на её корректность
        correct = True
        for str in matrix:
            if len(matrix[0]) != len(str):
                correct = False
        if correct == True:
            self.__mtrx = list(matrix)
        else:
            print("ERROR: Matrix not correct!")
            self.__mtrx = []

    def __str__(self):
        ret_data = ""
        for str_m in self.__mtrx:
            ret_data += "| "
            for el in str_m:
                ret_data += str(el) + " "
            ret_data += "|\n"
        return ret_data

    def get_size(self):
        if len(self.__mtrx) > 0:
            return [len(self.__mtrx), len(self.__mtrx[0])]
        else:
            return [0, 0]

    def __getitem__(self, index):
        if index + 1 > len(self.__mtrx):
            raise IndexError("matrix index out of range")
        return self.__mtrx[index]

    def __add__(self, other):
        # проверка матриц, на то что они одинокового размера
        ms1 = self.get_size()
        ms2 = other.get_size()
        if len(ms1) != len(ms2):
            raise ValueError(f"M1 {len(ms1)}x.. != M2 {len(ms2)}x..")
        elif ms1[0] != ms2[0] or ms1[1] != ms2[1]:
            raise ValueError(f"M1 {ms1[0]}x{ms1[1]} != M2 {ms2[0]}x{ms2[1]}")

        new_matrix = []
        for nmbr_str, _ in enumerate(self.__mtrx):
            new_str = []
            for nmbr_el, _ in enumerate(self.__mtrx[nmbr_str]):
                new_str.append(self.__mtrx[nmbr_str][nmbr_el] + other[nmbr_str][nmbr_el])
            new_matrix.append(new_str)

        return Matrix(new_matrix)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m1)
m2 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m2)
m3 = Matrix([[1, 2, 3], [4, 5]])  # плохая матрица
print(m3)
m4 = Matrix([[1, 2], [4, 5]])
print(m4)
m5 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m5)
print("-" * 40)
try:
    print(m1 + m2)
except ValueError as err:
    print("Error:", err)
try:
    print(m1 + m4)
except ValueError as err:
    print("Error:", err)
