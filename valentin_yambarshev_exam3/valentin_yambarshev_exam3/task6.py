# Напишите программу с классом Student, в котором есть три атрибута:
# name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента,
# метод getAge нужен для получения данных о возрасте конкретного студента,
# vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена,
# возраст и номер группы.

class Student:

    def __init__(self, name='Ivan', group_number='10A', age=18):
        self.name = name
        self.group_number = group_number
        self.age = age

    def get_name(self):
        return f'Имя студента {self.name} из группы {self.group_number} в возрасте {self.age}'

    def get_age(self):
        return f'Возраст студента {self.name}: {self.age}'

    def get_group_number(self):
        return f'Группа студента {self.name}: {self.group_number}'

    def set_name_age(self, name, age):
        self.name = name
        self.age = age
        return f'Новое имя студента {self.name} в возрасте {self.age}'

    def set_group_number(self, group_number):
        self.group_number = group_number
        return f'Новая группа {self.group_number}'


anna = Student('Anna', '11a', 17)
oleg = Student('Oleg', '12b', 19)
petr = Student()
kate = Student()
ivan = Student()
print(anna.get_name())
print(ivan.get_name())
print(petr.set_name_age('Petr', 20))
print(petr.get_name())
print(kate.set_group_number('18D'))
print(kate.set_name_age('Kate', 21))
print(kate.get_name())