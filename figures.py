import math


class Figure:
    name = 'Пустая фигура'
    area = 0
    angles = 0
    perimeter = 0

    def add_square(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise Exception("Метод принимает только объекты класса Figure")

        sum_area = self.area + other_figure.area
        print("Сумма площадей фигур: " + str(sum_area))

        # Возвращаю число, чтобы можно было протестить сложение площадей.
        # Не знаю, как протестить, что что-то именно вывелось(((
        return sum_area


class Circle(Figure):
    def __init__(self, r):
        if type(r) is not int or r <= 0:
            raise Exception("радиус должен быть целым положительным числом > 0")

        self.name = 'Круг'
        self.r = r
        self.area = math.pi*(r**2)
        self.angles = 0
        self.perimeter = 2*math.pi*r


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if (type(side1) is not int or type(side2) is not int or type(side3) is not int
                or side1 <= 0 or side2 <= 0 or side3 <= 0):
            raise Exception("стороны должны быть целыми положительнми числами > 0")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise Exception("Сумма двух сторон должна быть меньше третьей стороны")

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = side1+side2+side3
        p = self.perimeter/2
        h_side1 = 2*math.sqrt(p*(p-side1)*(p-side2)*(p-side3))/side1
        self.area = (side1*h_side1)/2
        self.name = 'Треугольник'
        self.angles = 3


class Parallelogram(Figure):
    def __init__(self, h, w):
        if (type(h) is not int or type(w) is not int
                or h <= 0 or w <= 0):
            raise Exception("стороны должны быть целыми положительнми числами > 0")

        self.h = h
        self.w = w
        self.name = 'Прямоугольник'
        self.area = h*w
        self.angles = 4
        self.perimeter = h*2 + w*2


class Square(Parallelogram):
    def __init__(self, side):
        super(Square, self).__init__(side, side)
        self.name = 'Квадрат'
