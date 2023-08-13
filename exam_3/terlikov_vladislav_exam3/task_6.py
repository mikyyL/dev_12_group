class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
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


students = [Student("John", 20, "11A"), Student("Jane", 21, "11B"), Student("Bob", 19, "10B"), Student("Alice", 18, "10A"), Student("Mike", 22, "12A")]

for student in students:
    print(student.getName(), student.getAge(), student.getGroupNumber())
