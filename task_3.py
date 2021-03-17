"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

usr_arr = []

# Парсим файл:
with open("text_3.txt", "r", encoding="utf-8") as f:
    for str in f:
        str_arr = str.split()
        try:
            usr_d = {"user": str_arr[0], "salary": float(str_arr[1])}
        except ValueError:
            print(f"Ошибка: В строке '{str.rstrip()}' не корректные данные")
        except:
            print("Ошибка: Что-то не так пошло!")
        else:
            usr_arr.append(usr_d)

# print(usr_arr)

list_usr20k = [el["user"] for el in usr_arr if el["salary"] < 20000]
print("Список сотрудников с окладом менее 20тыс.: ", list_usr20k)

usrs_mean = sum([el["salary"] for el in usr_arr]) / len(usr_arr)
print("Средняя величина дохода сотрудников: ", usrs_mean)
