"""
Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
успеваемость (список из пяти элементов).
Создать класс School:
Добавить возможность для добавления студентов в школу.
Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
Добавить возможность вывода учеников заданной группы.
Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)
"""


class Students:
    def __init__(self, name, group_number, progress):
        self.name = name
        self.group_number = group_number
        self.progress = progress

    def __str__(self):
        return f'{self.name}, группа {self.group_number}, оценки {self.progress}'

    def average_progress(self):
        return sum(self.progress) / len(self.progress)


class School:
    def __init__(self, students):
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def good_student(self):
        for student in self.students:
            if all(progress in [5, 6] for progress in student.progress):
                print(student.name, student.group_number)

    def group_student(self, group):
        for student in self.students:
            if student.group_number == group:
                print(student)

    def automatic_students(self):
        for student in self.students:
            if student.average_progress() >= 7:
                print(student)


s1 = Students("Иванов И.И.", 11, [5, 6, 6, 5, 6])
s2 = Students("Петров П.П.", 12, [4, 5, 4, 4, 5])
s3 = Students("Сидоров С.С.", 11, [6, 6, 6, 6, 6])
s4 = Students("Кузнецов К.К.", 12, [3, 4, 3, 3, 4])
s5 = Students("Смирнов С.М.", 11, [7, 8, 7, 8, 7])

school = School([s1, s2])
school.add_student(s3)
school.add_student(s4)
school.add_student(s5)

print("Студенты с хорошей успеваемостью:")
school.good_student()
print()


print("Студенты группы 11:")
school.group_student(11)
print()

print("Студенты группы 12:")
school.group_student(12)
print()

# Выводим учеников претендующих на автомат
print("Студенты претендующие на автомат:")
school.automatic_students()
