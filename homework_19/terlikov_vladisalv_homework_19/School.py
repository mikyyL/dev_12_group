from student import Student


class School:

    def __init__(self, students):
        self.students = students

    def get_list_of_students(self):
        return self.students

    def admission(self, student):
        self.students.append(student)

    def remove(self, student, group):
        if student.group == group:
            self.students.remove(student)

    def print_student_names(self):
        for student in self.students:
            print(student.name)

    def get_list_automate_student(self, auto_mark=7):
        list_students_automate = []
        for student in self.students:
            averege_grade = sum(student.progress) / len(student.progress)
            if averege_grade >= auto_mark:
                list_students_automate.append(student)
            return list_students_automate


    def get_list_of_student_with_needed_mark(self, grades):
        list_student = self.students.copy()
        for student in self.students

