"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные
для каждого типа оргтехники.

5. Продолжить работу над первым заданием (№4). Разработайте методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием (№5). Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Stock:
    reg_equipment = []
    reg_amnt = {}

    def __str__(self):
        return f"На складе {len(self.reg_equipment)} оборудования."

    def set_equipment(self, *args):
        for equipment in args:
            self.reg_equipment.append(equipment)
            # if str(type(equipment)) in self.reg_amnt.keys():
            if equipment.my_name() in self.reg_amnt.keys():
                # self.reg_amnt[str(type(equipment))] += 1
                self.reg_amnt[equipment.my_name()] += 1
            else:
                # self.reg_amnt[str(type(equipment))] = 1
                self.reg_amnt[equipment.my_name()] = 1

    def get_equipment(self, equipment):
        if equipment in self.reg_equipment:
            self.reg_equipment.remove(equipment)
            # self.reg_amnt[str(type(equipment))] -= 1
            self.reg_amnt[equipment.my_name()] -= 1
        else:
            print("ОШИБКА: Данное оборудование отсутствует на складе")

    def get_eq_amnt(self, cls, amnt):
        list_move_eq = []
        try:
            amnt = int(amnt)
        except ValueError:
            print("Не число")
        else:
            # if self.reg_amnt[str(type(cls))] >= amnt:
            if self.reg_amnt[cls.my_name()] >= amnt:
                print(f"{cls.my_name()} в количестве {amnt}шт есть в наличие")
                list_move_eq = [el for el in self.reg_equipment if type(el) == type(cls)]
                for el in list_move_eq:
                    self.get_equipment(el)
            else:
                print(f"Такого {amnt} количества '{cls.my_name()}' нет в наличие")
        return list_move_eq  # список отправленного оборудования

    def print_stock(self):
        print([f"{el}" for el in self.reg_equipment])


class Equipment:
    brand = ""  # брэнд
    model = ""  # модель
    sn = ""  # серийный номер
    prod_year = 2000  # год производтсва

    def __str__(self):
        return f"{self.brand} - {self.model} (s/n:{self.sn})"


class Printer(Equipment):
    print_speed = 0  # скорость печати
    color = False  # цветной
    dpi = 0  # точность, количество точек

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if key == "brand":
                self.brand = val
            elif key == "model":
                self.model = val
            elif key == "sn":
                self.sn = val
            elif key == "prod_year":
                self.prod_year = val
            elif key == "dpi":
                self.dpi = int(val)
            elif key == "color":
                self.color = bool(val)
            elif key == "print_speed":
                self.print_speed = int(val)

    def __str__(self):
        return super(Printer, self).__str__()

    @classmethod
    def my_name(cls):
        return cls.__name__


class Scaner(Equipment):
    dpi = 0  # точность, количество точек
    stack_doc = False  # сканирование пачки документов

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if key == "brand":
                self.brand = val
            elif key == "model":
                self.model = val
            elif key == "sn":
                self.sn = val
            elif key == "prod_year":
                self.prod_year = int(val)
            elif key == "dpi":
                self.dpi = int(val)
            elif key == "stack_doc":
                self.stack_doc = bool(val)

    def __str__(self):
        return super(Scaner, self).__str__()

    @classmethod
    def my_name(cls):
        return cls.__name__


class Photocopier(Equipment):  # ! Xerox - брэнд
    copy_speed = 0

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if key == "brand":
                self.brand = val
            elif key == "model":
                self.model = val
            elif key == "sn":
                self.sn = val
            elif key == "prod_year":
                self.prod_year = int(val)
            elif key == "copy_speed":
                self.copy_speed = int(val)

    def __str__(self):
        return super(Photocopier, self).__str__()

    @classmethod
    def my_name(cls):
        return cls.__name__


sk = Stock()
pr1 = Printer(brand="HP", model="LaserJet 3310", sn="324t34tg4g43554g", color=False)
pr2 = Printer(brand="HP", model="LaserJet 30i", sn="324t345gegbhrtyr", color="False")
sc1 = Scaner(brand="Lexmark", model="Tablo", sn="14/g34t", dpi=600)
sc2 = Scaner(brand="Samsung", model="H-3000", sn="vgbrt6", dpi=600)
pc1 = Photocopier(brand="Xerox", copy_speed=200, sn="asd1")
pc2 = Photocopier(brand="Xerox", copy_speed=200, sn="asd2")

# поместить оборудование
sk.set_equipment(pr1)
sk.set_equipment(pr2)
sk.set_equipment(sc1, sc2)
sk.set_equipment(pc1)
sk.set_equipment(pc2)
# --
print(sk)
print(sk.reg_amnt)
sk.print_stock()  # print(sk.reg_equipment)

# забрать определенное оборудование
sk.get_equipment(sc1)
print(sc1)
# --
print(sk)
print(sk.reg_amnt)
sk.print_stock()  # print(sk.reg_equipment)

# забрать N оборудование
sk.get_eq_amnt(Printer(), "q1")
sk.get_eq_amnt(Printer(), 10)
skl2 = sk.get_eq_amnt(Printer(), 2)
print(f"Забрали со склада {[f'{el}' for el in skl2]}")
# --
print(sk)
print(sk.reg_amnt)
sk.print_stock()  # print(sk.reg_equipment)
