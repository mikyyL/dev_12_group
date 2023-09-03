class TriangleChecker:
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("С отрицательными числами ничего не выйдет!")

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


triangle = TriangleChecker(5, 7, 9)
print(triangle.is_triangle())
