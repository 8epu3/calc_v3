# tests/test_operations.py

"""
Unit tests for the operations module using pytest.

This test suite covers both positive and negative scenarios for the Operation
class's static methods. It ensures that arithmetic operations perform correctly
and handle edge cases appropriately.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from app.operation import Operation


# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

def test_addition_positive():
    """
    Test the addition method with two positive numbers.
    
    This test verifies that adding two positive numbers returns the correct sum.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 15.0

    # Act
    result = Operation.add(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_negative_numbers():
    """
    Test the addition method with two negative numbers.
    
    This test verifies that adding two negative numbers returns the correct sum.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -15.0

    # Act
    result = Operation.add(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


def test_addition_positive_negative():
    """
    Test the addition method with one positive and one negative number.
    
    This test verifies that adding a positive and a negative number returns the correct sum.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 5.0

    # Act
    result = Operation.add(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + ({b}) to be {expected_result}, got {result}"


def test_addition_with_zero():
    """
    Test the addition method with zero as one of the operands.
    
    This test verifies that adding zero to a number returns the number itself.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.add(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} + {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

def test_subtraction_positive():
    """
    Test the subtraction method with two positive numbers.
    
    This test verifies that subtracting two positive numbers returns the correct difference.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 5.0

    # Act
    result = Operation.sub(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


def test_subtraction_negative_numbers():
    """
    Test the subtraction method with two negative numbers.
    
    This test verifies that subtracting two negative numbers returns the correct difference.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = -5.0

    # Act
    result = Operation.sub(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_positive_negative():
    """
    Test the subtraction method with one positive and one negative number.
    
    This test verifies that subtracting a negative number from a positive number returns the correct difference.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = 15.0

    # Act
    result = Operation.sub(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - ({b}) to be {expected_result}, got {result}"


def test_subtraction_with_zero():
    """
    Test the subtraction method with zero as one of the operands.
    
    This test verifies that subtracting zero from a number returns the number itself.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 10.0

    # Act
    result = Operation.sub(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} - {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

def test_multiplication_positive():
    """
    Test the multiplication method with two positive numbers.
    
    This test verifies that multiplying two positive numbers returns the correct product.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 50.0

    # Act
    result = Operation.mul(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_negative_numbers():
    """
    Test the multiplication method with two negative numbers.
    
    This test verifies that multiplying two negative numbers returns the correct product.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 50.0

    # Act
    result = Operation.mul(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


def test_multiplication_positive_negative():
    """
    Test the multiplication method with one positive and one negative number.
    
    This test verifies that multiplying a positive number by a negative number returns the correct product.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -50.0

    # Act
    result = Operation.mul(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * ({b}) to be {expected_result}, got {result}"


def test_multiplication_with_zero():
    """
    Test the multiplication method with zero as one of the operands.
    
    This test verifies that multiplying any number by zero returns zero.
    """
    # Arrange
    a = 10.0
    b = 0.0
    expected_result = 0.0

    # Act
    result = Operation.mul(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} * {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

def test_division_positive():
    """
    Test the division method with two positive numbers.
    
    This test verifies that dividing two positive numbers returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 2.0

    # Act
    result = Operation.div(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_negative_numbers():
    """
    Test the division method with two negative numbers.
    
    This test verifies that dividing two negative numbers returns the correct quotient.
    """
    # Arrange
    a = -10.0
    b = -5.0
    expected_result = 2.0

    # Act
    result = Operation.div(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_positive_negative():
    """
    Test the division method with one positive and one negative number.
    
    This test verifies that dividing a positive number by a negative number returns the correct quotient.
    """
    # Arrange
    a = 10.0
    b = -5.0
    expected_result = -2.0

    # Act
    result = Operation.div(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / ({b}) to be {expected_result}, got {result}"


def test_division_with_zero_divisor():
    """
    Test the division method with zero as the divisor.
    
    This test verifies that dividing any number by zero raises a ValueError.
    """
    # Arrange
    a = 10.0
    b = 0.0

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        Operation.div(a, b)
    
    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division by zero not allowed."


def test_division_with_zero_numerator():
    """
    Test the division method with zero as the numerator.
    
    This test verifies that dividing zero by a non-zero number returns zero.
    """
    # Arrange
    a = 0.0
    b = 5.0
    expected_result = 0.0

    # Act
    result = Operation.div(a, b)

    # Assert
    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.add, '10', 5.0, TypeError),
    (Operation.sub, 10.0, '5', TypeError),
    (Operation.mul, '10', '5', TypeError),
    (Operation.div, 10.0, '5', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """
    Test that arithmetic methods raise TypeError when provided with invalid input types.
    
    This test verifies that providing non-float inputs to the arithmetic methods raises
    a TypeError, as the operations are intended for floating-point numbers.
    """
    # Arrange
    # No setup needed as the invalid inputs are provided directly

    # Act & Assert
    with pytest.raises(expected_exception):
        calc_method(a, b)



"""
import pytest
from app.operation import *

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (3, 3, 6),
        (2, -3, -1),
        (-4, -3, -7),
        (0, 0, 0),
    ],
    ids=[
        "add_two_positive_numbers",
        "add_positive_and_negative_numbers",
        "add_two_negative_numbers",
        "add_two_zeros"
    ],
)
def test_add(num1, num2, expected):
    result =  add(num1, num2)
    assert result == expected, f"The expression: {num1} + {num2} is not equals to {expected}, got {result}"

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (3, 3, 0),
        (2, -3, 5),
        (-4, -3, -1),
        (0, 0, 0),
    ],
    ids=[
        "substract_two_positive_numbers",
        "substract_positive_and_negative_numbers",
        "substract_two_negative_numbers",
        "substract_two_zeros"
    ],
)
def test_sub(num1, num2, expected):
    result =  sub(num1, num2)
    assert result == expected, f"The expression: {num1} - {num2} is not equals to {expected}, got {result}"

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (3, 3, 9),
        (2, -3, -6),
        (-4, -3, 12),
        (4, 0, 0),
        (-4, 0, 0)
    ],
    ids=[
        "multiply_two_positive_numbers",
        "multiply_positive_and_negative_numbers",
        "multiply_two_negative_numbers",
        "multiply_positive_and_zero",
        "multiply_negative_and_zero",
    ],
)
def test_mul(num1, num2, expected):
    result =  mul(num1, num2)
    assert result == expected, f"The expression: {num1} * {num2} is not equals to {expected}, got {result}"

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (6, 3, 2),
        (6, -3, -2),
        (-6, -2, 3)
    ],
    ids=[
        "divide_two_positive_numbers",
        "divide_positive_by_negative_number",
        "divide_two_negative_numbers",
    ],
)
def test_div(num1, num2, expected):
    result =  div(num1, num2)
    assert result == expected, f"The expression: {num1} / {num2} is not equals to {expected}, got {result}"

@pytest.mark.parametrize(
    "num1, num2",
    [
        (1, 0),
        (-1, 0),
        (0, 0),
    ],
    ids=[
        "divide_positive_number_by_zero",
        "divide_negative_number_by_zero",
        "divide_zero_by_zero",
    ],
)
def test_div_by_zero(num1, num2):
    with pytest.raises(ValueError, match="Division by zero not allowed.") as e:
        div(num1, num2)
    
    assert "Division by zero not allowed." in str(e.value), \
        f"Expected error message 'Division by zero not allowed.', but got '{e.value}'"
"""