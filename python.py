# Create: tests/test_app.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
import pytest

def test_add_numbers():
    """Test addition function"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    """Test subtraction function"""
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 5) == -5

def test_multiply_numbers():
    """Test multiplication function"""
    assert multiply_numbers(4, 3) == 12
    assert multiply_numbers(0, 10) == 0

def test_divide_numbers():
    """Test division function"""
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(0, 5) == 0

def test_divide_by_zero():
    """Test division by zero raises error"""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide_numbers(5, 0)

if __name__ == "__main__":
    pytest.main([__file__])
