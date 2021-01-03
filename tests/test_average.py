from pytest import approx, mark, raises

from averager import average


@mark.parametrize(
    "values,expected",
    [([1, 2], 1.5), ([2, 2, 2, 2, 2], 2), ([1, 2, 3, 4, 5], 3)],
)
def test_average(values, expected):
    assert average(values) == approx(expected)


def test_average_no_values():
    with raises(ZeroDivisionError):
        average([])


@mark.parametrize("value", [-5, -2.5, -1, 0, 1, 2.5, 5])
def test_average_one_value(value):
    assert average([value]) == approx(value)
