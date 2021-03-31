"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyErr0(Exception):
    def __init__(self, txt):
        self.txt = txt


inp1 = input("Числитель: ")
inp2 = input("Знаменатель: ")

try:
    if int(inp2) == 0:
        raise MyErr0("Знаменатель = 0")
    res = int(inp1) / int(inp2)
except ValueError as err:
    print("ОШИБКА: ", err)
except MyErr0 as err:
    print("ОШИБКА: ", err)
else:
    print("Результат деления = ", res)
