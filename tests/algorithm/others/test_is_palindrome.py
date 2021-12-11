import pytest

from library.algorithm.other.is_palindrome import is_palindrome


# parametrize
@pytest.mark.parametrize(
    "string,expected",
    [
        ("level", True),
        ("algomethod", False),
        ("xxxxxx", True),
    ],
)
def test_is_palindrome(string, expected):
    actual = is_palindrome(string)
    assert actual == expected
