'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, >3<, 2.
Пользователь ввел число 8. Результат: >8<, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, >1<.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]
usr_int = None
while usr_int == None:
    try:
        usr_int = int(input("Введите число: "))
    except:
        print("Что-то пошло не так, попробуй ещё раз.")

unq_list = list(set(my_list))
if usr_int in unq_list:
    shft = my_list.count(usr_int)
    pos = my_list.index(usr_int) + shft
    my_list.insert(pos, usr_int)
elif usr_int > max(unq_list):
    my_list.insert(0, usr_int)
elif usr_int < min(unq_list):
    my_list.append(usr_int)
else:
    for indx, val in enumerate(my_list):
        if val < usr_int:
            my_list.insert(indx, usr_int)
            break

print(my_list)
