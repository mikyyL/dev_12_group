"""
Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого создайте класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
Ура, можно построить треугольник!
С отрицательными числами ничего не выйдет!
Жаль, но из этого треугольник не сделать.

"""
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        elif self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return "Ура, можно построить треугольник!"
        elif self.a == self.b == self.c:
            return "Ура, можно построить равнобедренный треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


checker = TriangleChecker(1, 2, 3)
result = checker.is_triangle()
print(result)
checker1 = TriangleChecker(2, 3, 4)
result1 = checker1.is_triangle()
print(result1)
checker2 = TriangleChecker(-2, -3, -4)
result2 = checker2.is_triangle()
print(result2)
checker3 = TriangleChecker(3, 3, 3)
result3 = checker3.is_triangle()
print(result3)