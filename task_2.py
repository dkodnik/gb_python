"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

amnt_str = 0
amnt_wrd = 0
with open("text_2.txt", "r", encoding="utf-8") as f:
    for content in f:
        amnt_str += 1
        amnt_wrd_str = len(content.split())
        print(f"{amnt_str}. {content.rstrip()} <- Количество слов: {amnt_wrd_str}")
        amnt_wrd += amnt_wrd_str

print("Всего строк:", amnt_str)
print("Всего слов:", amnt_wrd)
