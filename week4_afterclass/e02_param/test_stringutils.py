import pytest
from stringutils import is_palindrome


@pytest.mark.parametrize(
    "text,expected",
    [
        ("level", True),
        ("Anna", True),
        ("hello", False),
        ("a", True),
        ("  noon  ", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected
