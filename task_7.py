"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 3000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 3000}]

Подсказка: использовать менеджеры контекста.
"""

import json

firms = {}
profit = {"average_profit": 0}
amnt_firm_profit = 0
with open("text_7.txt", "r", encoding="utf-8") as f:
    for str in f:
        str_arr = str.split()
        firms[str_arr[0]] = int(str_arr[2]) - int(str_arr[3])
        if firms[str_arr[0]] > 0:
            amnt_firm_profit += 1

if amnt_firm_profit != 0:
    profit["average_profit"] = sum([val for _, val in firms.items() if val > 0]) / amnt_firm_profit

json_data = [firms, profit]

print(json_data)

with open("text_7.json", "w", encoding="utf-8") as fwj:
    json.dump(json_data, fwj, indent=4, ensure_ascii=False)
