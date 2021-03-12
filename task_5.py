"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def przv(el1, el2):
    return el1 * el2


my_list = [el for el in range(100, 1001) if el % 2 == 0]
# print(my_list)
my_sum = reduce(przv, my_list)
print(my_sum)
