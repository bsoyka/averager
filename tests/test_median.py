from pytest import mark, raises

from averager import median


@mark.parametrize(
    'values,expected',
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3], 2),
        ([1.5, 1.5, 1.5], 1.5),
        ([3.21, 4.56, 12.34], 4.56),
    ],
)
def test_median_odd_values_len(values, expected):
    result = median(*values)

    assert result == expected


@mark.parametrize(
    'values,expected',
    [([1, 2, 3, 4, 5, 6], 3.5), ([1, 2], 1.5), ([5, 1, 3], 3)],
)
def test_median_even_values_len(values, expected):
    result = median(*values)

    assert result == expected
    assert type(result) == type(expected)


def test_median_empty_list():
    with raises(IndexError):
        median()


def test_median_one_value():
    assert median(1) == 1
