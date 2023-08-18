class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()


student1.setNameAge('John', 20)
student2.setNameAge('Sarah', 19)
student3.setNameAge('Michael', 21)
student4.setGroupNumber('11B')
student5.setNameAge('Emma', 18)

print(f"Имя: {student1.getName()}, Возраст: {student1.getAge()}, Группа: {student1.getGroupNumber()}")
print(f"Имя: {student2.getName()}, Возраст: {student2.getAge()}, Группа: {student2.getGroupNumber()}")
print(f"Имя: {student3.getName()}, Возраст: {student3.getAge()}, Группа: {student3.getGroupNumber()}")
print(f"Имя: {student4.getName()}, Возраст: {student4.getAge()}, Группа: {student4.getGroupNumber()}")
print(f"Имя: {student5.getName()}, Возраст: {student5.getAge()}, Группа: {student5.getGroupNumber()}")