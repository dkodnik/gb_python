"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

ru_list = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}

new_data = []
with open("text_4.txt", "r", encoding="utf-8") as f:
    for str in f:
        # вариант 1:
        # for el1,el2 in ru_list.items():
        #    str = str.replace(el1, el2)
        # вариант 2:
        str_arr = str.split()
        str_arr[0] = ru_list[str_arr[0]]
        str = f'{" ".join(str_arr)}\n'
        # -----------------------------
        new_data.append(str)

print(new_data)

with open("text_4w.txt", "w", encoding="utf-8") as f:
    f.writelines(new_data)
