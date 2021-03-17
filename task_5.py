"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random


def is_int(el):
    try:
        int(el)
    except ValueError:
        # Файл содержит посторонние символы
        return False
    else:
        return True


AMNT_NMBR = 10

with open("text_5.txt", "w", encoding="utf-8") as f:
    arr_n = [str(random.randint(-int(el) * 1000, int(el) * 1000)) for el in range(AMNT_NMBR + 1) if el != 0]
    print(" ".join(arr_n), file=f)

with open("text_5.txt", "r", encoding="utf-8") as f:
    f_arr = [int(el) for el in f.read().split() if is_int(el)]
    print(f_arr)
    print(f"Сумма чисел {sum(f_arr)}")
