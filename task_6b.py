"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import cycle

str_cycle = [1,23,'2']
#str_cycle = "qwerty"

print(f"Это список элементов '{str_cycle}',")
try:
    nmbr_end = int(input("сколько раз его повторить: "))
except ValueError:
    print("Вводите только цифры.")

full_step = 1
for el in cycle(str_cycle):
    if full_step > nmbr_end * len(str_cycle):
        break
    else:
        print(el)
    full_step += 1
