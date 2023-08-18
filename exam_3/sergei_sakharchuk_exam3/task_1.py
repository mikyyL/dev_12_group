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
        else:
            return "Жаль, но из этого треугольник не сделать."


checker = TriangleChecker(3, 4, 5)
result = checker.is_triangle()
print(result)