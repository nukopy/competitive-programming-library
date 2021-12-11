import pytest

from library.algorithm.math.is_prime import is_prime


@pytest.mark.parametrize(
    "num, expected",
    [
        # 1 以下の整数は素数でない
        (-1, False),
        (0, False),
        (1, False),
        # 2 は素数
        (2, True),
        # 2 より大きい整数
        (3, True),  # 素数
        (4, False),
        (5, True),  # 素数
        (6, False),
        (7, True),  # 素数
        (8, False),
        (9, False),
        (10, False),
        (11, True),  # 素数
        (12, False),
        (13, True),  # 素数
        (14, False),
        (15, False),
        (16, False),
        (17, True),  # 素数
        (18, False),
        (19, True),  # 素数
        (20, False),
    ],
)
def test_is_prime(num, expected):
    actual = is_prime(num)
    assert actual == expected
