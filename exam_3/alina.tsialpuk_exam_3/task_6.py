"""
 Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
 По умолчанию name = Ivan, age = 18, groupNumber = 10A.
 Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
 Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения
 данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы
 конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
 метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо
  создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

"""
class Student:

    def __init__(self, name='Ivan', group_number='10A', age=18):
        self.name = name
        self.group_number = group_number
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name_age(self, name, age):
        self.name = name
        self.age = age

    def set_group_number(self, group_number):
        self.group_number = group_number

#5 экземпляров класса
student1 = Student('Alina', '208Db', 32)
student2 = Student('Alex', '20F', 30)
student3 = Student('Vanya', '40M', 20)
student4 = Student('Lev', '30A', 22)
student5 = Student('Den', '12A', 25)
