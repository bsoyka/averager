from pytest import mark

from averager import mode


@mark.parametrize(
    'values,expected',
    [
        ((1, 2, 3), {1, 2, 3}),
        ((1, 1, 1, 1), 1),
        ((1, 2, 2, 3), 2),
        ((1, 2, 1, 2), {1, 2}),
    ],
)
def test_mode(values, expected):
    result = mode(*values)

    assert result == expected
    assert type(result) == type(expected)
