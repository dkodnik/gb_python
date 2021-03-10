"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""

total_sum = 0

spec = chr(100)  # d
print("Спец.символ:", spec)

spec_inp = False

while not spec_inp:
    str_nmbr = input("Числа: ")
    if str_nmbr.find(spec) != -1:
        str_nmbr = str_nmbr[:str_nmbr.index(spec)]
        spec_inp = True
    if str_nmbr:
        arr_nmbr = str_nmbr.split()
        arr_nmbr = [int(item) for item in arr_nmbr]
        # for i, item in enumerate(arr_nmbr):
        #    arr_nmbr[i]=int(item)
        total_sum += sum(arr_nmbr)
        print(total_sum)
