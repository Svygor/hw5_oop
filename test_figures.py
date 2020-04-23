import pytest
import figures as f


class TestData:
    areas = {
        'figure': 0,
        'circle': 50,
        'triangle': 6,
        'parallelogram': 15,
        'square': 16
    }
    figure = f.Figure()
    circle = f.Circle()
    triangle = f.Triangle()
    parallelogram = f.Parallelogram()
    square = f.Square()

    def generate_test_data(self, figure_type):
        figure_type = figure_type.lower()
        if figure_type not in self.areas:
            return []
        tests = [
            (self.figure, self.areas[figure_type] + 0),
            (self.circle, self.areas[figure_type] + 50),
            (self.triangle, self.areas[figure_type] + 6),
            (self.parallelogram, self.areas[figure_type] + 15),
            (self.square, self.areas[figure_type] + 16)
        ]
        return tests


class TestFigure:

    generator = TestData()

    @classmethod
    def setup_class(cls):
        cls.figure = f.Figure()
        cls.circle = f.Circle()
        cls.triangle = f.Triangle()
        cls.parallelogram = f.Parallelogram()
        cls.square = f.Square()

    @pytest.mark.parametrize('curr_fig, expected_area',  generator.generate_test_data('figure'))
    def test_check_figure(self, curr_fig, expected_area):
        assert self.figure.add_square(curr_fig) == expected_area

    @pytest.mark.parametrize('curr_fig, expected_area',  generator.generate_test_data('circle'))
    def test_check_circle(self, curr_fig, expected_area):
        assert self.circle.add_square(curr_fig) == expected_area

    @pytest.mark.parametrize('curr_fig, expected_area',  generator.generate_test_data('triangle'))
    def test_check_triangle(self, curr_fig, expected_area):
        assert self.triangle.add_square(curr_fig) == expected_area

    @pytest.mark.parametrize('curr_fig, expected_area',  generator.generate_test_data('parallelogram'))
    def test_check_parallelogram(self, curr_fig, expected_area):
        assert self.parallelogram.add_square(curr_fig) == expected_area

    @pytest.mark.parametrize('curr_fig, expected_area',  generator.generate_test_data('square'))
    def test_check_square(self, curr_fig, expected_area):
        assert self.square.add_square(curr_fig) == expected_area
