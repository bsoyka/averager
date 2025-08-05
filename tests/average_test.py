from pytest import approx, mark, raises

from averager import average


@mark.parametrize(
    'values,expected',
    [([1, 2], 1.5), ([2, 2, 2, 2, 2], 2), ([1, 2, 3, 4, 5], 3)],
)
def test_average(values, expected):
    result = average(*values)

    assert result == approx(expected)
    assert type(result) == type(expected)


def test_average_no_values():
    with raises(ZeroDivisionError):
        average()


@mark.parametrize('value', [-5, -2.5, -1, 0, 1, 2.5, 5])
def test_average_one_value(value):
    result = average(value)

    assert result == approx(value)
    assert type(result) == type(value)
