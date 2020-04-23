class Figure:
    name = 'Пустая фигура'
    area = 0
    angles = 0
    perimeter = 0

    def add_square(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise Exception("Метод принимает только обхекты класса figure")

        sum_area = self.perimeter + other_figure.perimeter
        print("Сумма площадей фигур: " + str(sum_area))

        # Возвращаю число, чтобы можно было протестить сложение площадей.
        # Не знаю, как протестить, что что-то именно вывелось(((
        return sum_area


class Circle(Figure):
    def __init__(self):
        self.name = 'Круг'
        self.area = 50
        self.angles = 0
        self.perimeter = 25


class Triangle(Figure):
    def __init__(self):
        self.name = 'Треугольник'
        self.area = 6
        self.angles = 3
        self.perimeter = 12


class Parallelogram(Figure):
    def __init__(self):
        self.name = 'Прямоугольник'
        self.area = 15
        self.angles = 4
        self.perimeter = 16


class Square(Parallelogram):
    def __init__(self):
        self.name = 'Квадрат'
        self.area = 16