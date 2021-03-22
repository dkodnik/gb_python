"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name_position, wage):
        self.position = name_position
        self._income["wage"] = wage

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def add_worker(self, name, surname, bonus):
        self.name = name
        self.surname = surname
        self._income["bonus"] = bonus


progr = Position("Программист", 100000)
progr.add_worker("Иван", "Иванов", 25000)
print("Сотрудник:", progr.get_full_name())
print("Доход:", progr.get_total_income())
