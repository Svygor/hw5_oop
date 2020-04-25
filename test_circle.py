import pytest
import figures as f


@pytest.mark.parametrize('r, area, perimeter, exp_success, exp_error', [
    (4, 50.26548245743669, 25.132741228718345, True, ""),
    (0, 0, 0, False, "радиус должен быть целым положительным числом > 0")])
def test_create_circle(r, area, perimeter, exp_success, exp_error):
    circle = None
    try:
        circle = f.Circle(r)
    except Exception as e:
        error = str(e)

    if exp_success:
        assert circle is not None
        assert circle.r == r
        assert circle.area == area
        assert circle.perimeter == perimeter
    else:
        assert error == exp_error


@pytest.mark.parametrize('other_figure, exp_result', [(f.Circle(2), 25.132741228718345),
                                                      (f.Square(4), 28.566370614359172),
                                                      (None, "Метод принимает только объекты класса Figure")])
def test_add_square(other_figure, exp_result):
    circle = f.Circle(2)
    try:
        result = circle.add_square(other_figure)
    except Exception as e:
        result = str(e)

    assert result == exp_result
