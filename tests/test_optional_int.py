from pytest import mark

from averager import _optional_int


@mark.parametrize('test_input', [1, 2, 3, 4, 5])
def test_int_to_int(test_input):
    assert _optional_int(test_input) == test_input
    assert type(_optional_int(test_input)) == int


@mark.parametrize(
    'test_input,expected', [(1.0, 1), (2.0, 2), (3.0, 3), (4.0, 4), (5.0, 5)]
)
def test_float_to_int(test_input, expected):
    assert _optional_int(test_input) == expected
    assert type(_optional_int(test_input)) == int


@mark.parametrize('test_input', [1.2, 2.3, 3.4, 4.5])
def test_float_to_float(test_input):
    assert _optional_int(test_input) == test_input
    assert type(_optional_int(test_input)) == float
