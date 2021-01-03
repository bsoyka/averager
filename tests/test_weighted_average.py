from pytest import mark, raises
from random import random
from averager import weighted_average


@mark.parametrize(
    "test_input,expected",
    [
        [[(50, 15), (76, 20), (80, 20), (98, 45)], 82.8],
        [[(20, 7), (45, 3), (15, 4), (0, 2)], 20.9375],
    ],
)
def test_weighted_average(test_input, expected):
    assert weighted_average(test_input) == expected
    assert type(weighted_average(test_input)) == type(expected)


def test_weighted_average_no_values():
    with raises(ZeroDivisionError):
        weighted_average([])


def test_weighted_average_negative_weights():
    with raises(ValueError):
        weighted_average([(1, -1), (0, -2)])


@mark.parametrize("value", [1, 53, -4, 6.2, 2.4738])
def test_weighted_average_one_value(value):
    assert weighted_average([(value, random() * 100)]) == value
    assert type(weighted_average([(value, random() * 100)])) == type(value)
