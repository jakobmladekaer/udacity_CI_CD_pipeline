import pytest
from app import add_two_numbers

def test_add_function():
    result = add_two_numbers(2,3)
    assert result == 5