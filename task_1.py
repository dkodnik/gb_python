"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

with open("text_1.txt", "w", encoding="utf-8") as f:
    exit_input = False
    nmbr_str = 0
    while not exit_input:
        str_input = input(": ")
        if len(str_input) != 0:
            if nmbr_str != 0:
                f.write("\n")
            f.write(str_input)
            nmbr_str += 1
        else:
            exit_input = True
