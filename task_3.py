"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(arg1, arg2, arg3):
    res = [arg1, arg2, arg3]
    res.pop(res.index(min(res)))
    return sum(res)


print(my_func(23, 45, 21))
