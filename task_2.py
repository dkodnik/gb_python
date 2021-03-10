"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def usr_inf1(name, surname, year, city, email, tel):
    print(f'{name} {surname}, {year}, {city}, {email}, {tel}')


def usr_inf2(**kwargs):
    print(
        f'{kwargs["name"]} {kwargs["surname"]}, {kwargs["year"]}, {kwargs["city"]}, {kwargs["email"]}, {kwargs["tel"]}')


def usr_inf3(**kwargs):
    print(', '.join(list(kwargs.values())))


usr_inf1(surname="Иванов", name="Иван", year=1945, city="Казань", email="ii@ya.ru", tel="124354215")
usr_inf2(surname="Иванов", name="Иван", year=1945, city="Казань", email="ii@ya.ru", tel="124354215")
usr_inf3(surname="Иванов", name="Иван", year="1945", city="Казань", email="ii@ya.ru", tel="124354215")
