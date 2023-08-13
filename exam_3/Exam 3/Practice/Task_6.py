print('Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. '
      'По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: '
      'getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени '
      'конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, '
      'vетод setGroupNumberнужен для получения данных о номере группы конкретного студента. Метод SetNameAge позволяет '
      'изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы '
      'установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student, установить им '
      'разные имена, возраст и номер группы.')


class Student:

    def __init__(self, name='Ivan', group_number='10A', age=18):
        self.name = name
        self.group_number = group_number
        self.age = age

    def get_name(self):
        return f'Имя студента из {self.group_number} группы в возрасте {self.age} лет: {self.name}'

    def get_age(self):
        return f'Возраст студента {self.name}: {self.age}'

    def get_group_number(self):
        return f'Группа студента {self.name}: {self.group_number}'

    def set_name_age(self, name, age):
        self.name = name
        self.age = age
        return f'Новая информация о студенте: {self.name}, {self.group_number} группа, {self.age} лет'

    def set_group_number(self, group_number):
        self.group_number = group_number
        return f'Новая группа студента {self.name}: {self.group_number} '


st1 = Student()
st2 = Student('Lia', '211', 20)
st3 = Student()
st4 = Student('Emmy', '22/7', 20)
st5 = Student('TK', '10-12', 18)
print(st1.set_name_age('Mike', 12))
print(st2.get_name())
print(st3.set_group_number('1N'))
print(st4.get_age())
print(st5.get_group_number())
