'''
4. Пользователь вводит целое положительное число. Найдите самую
большую цифру в числе. Для решения используйте цикл while и
арифметические операции.
'''

org_number = int(input('Введите число: '))
arr_number = []
tmp_number = org_number
while tmp_number != 0:
    arr_number.append(tmp_number % 10)
    tmp_number //= 10

print(f'Самая большая цифра в числе {org_number} это {max(arr_number)}')
