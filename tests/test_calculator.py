# test_calculator.py

"""
This test module contains unit tests for the 'app/calculator.py' module.
Each test demonstrates good testing practices using the Arrange-Act-Assert (AAA) pattern.
"""

import pytest
from io import StringIO

# Import the functions to be tested
from app.calculator import *

def test_display_help(capsys):
    """
    Test the display_help function to ensure it prints the correct help message.

    AAA Pattern:
    - Arrange: No special setup required for this function.
    - Act: Call the display_help function.
    - Assert: Capture the output and verify it matches the expected help message.
    """
    # Arrange
    # No arrangement needed since display_help doesn't require any input or setup.

    # Act
    display_help()

    # Assert
    # Capture the printed output
    captured = capsys.readouterr()
    expected_output = """
Calculator REPL Help
--------------------
Usage:
    <number1> <operation> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        +       : Adds two numbers.
        -       : Subtracts the second number from the first.
        *       : Multiplies two numbers.
        /       : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    10 + 5
    15.5 - 3.2
    7 * 8
    20 / 4
"""
    # Remove leading/trailing whitespace for comparison
    assert captured.out.strip() == expected_output.strip()

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("2 + 2", ("add", 2.0, 2.0)),
        ("2 - 2",("sub", 2.0, 2.0)),
        ("2 * 2", ("mul", 2.0, 2.0)),
        ("2 / 2", ("div", 2.0, 2.0)),
    ],
    ids=[
        "add_operation",
        "substract_operation",
        "multiply_operation",
        "divide_operation",
    ],
)
def test_parse_input(inputs, expected):
    output = parse_input(inputs)
    assert expected == output

def test_parse_input_unsupported_operation(capsys):

    with pytest.raises(ValueError, match="Unsupported operation") as e:
        parse_input("3 ^ 3")

    assert "Unsupported operation." in str(e.value)

def test_display_history_empty(capsys):
    """
    Test the display_history function when the history is empty.

    AAA Pattern:
    - Arrange: Create an empty history list.
    - Act: Call the display_history function with the empty history.
    - Assert: Capture the output and verify it indicates no calculations have been performed.
    """
    # Arrange
    history = []

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."

def test_display_history_with_entries(capsys):
    """
    Test the display_history function when there are entries in the history.

    AAA Pattern:
    - Arrange: Create a history list with sample calculation entries.
    - Act: Call the display_history function with the populated history.
    - Assert: Capture the output and verify it displays the calculations correctly.
    """
    # Arrange
    history = [
        "AddCalculation: 10.0 Add 5.0 = 15.0",
        "SubtractCalculation: 20.0 Sub 3.0 = 17.0",
        "MultiplyCalculation: 7.0 Mul 8.0 = 56.0",
        "DivideCalculation: 20.0 Div 4.0 = 5.0"
    ]

    # Act
    display_history(history)

    # Assert
    captured = capsys.readouterr()
    expected_output = """Calculation History:
1. AddCalculation: 10.0 Add 5.0 = 15.0
2. SubtractCalculation: 20.0 Sub 3.0 = 17.0
3. MultiplyCalculation: 7.0 Mul 8.0 = 56.0
4. DivideCalculation: 20.0 Div 4.0 = 5.0"""
    assert captured.out.strip() == expected_output.strip()

def test_calculator_exit(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'exit' command.

    AAA Pattern:
    - Arrange: Prepare the input 'exit' to simulate user typing 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the calculator exits gracefully and prints the exit message.
    """
    # Arrange
    user_input = 'exit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit) as exc_info:
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Good-bye" in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0  # Exit code 0 indicates a clean exit

def test_calculator_help_command(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'help' command.

    AAA Pattern:
    - Arrange: Prepare the input 'help' followed by 'exit' to simulate user interactions.
    - Act: Call the calculator function.
    - Assert: Verify that the help message is displayed and the calculator exits gracefully.
    """
    # Arrange
    user_input = 'help\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out
    assert "Good-bye" in captured.out

def test_calculator_invalid_input(monkeypatch, capsys):
    """
    Test the calculator function's handling of invalid input format.

    AAA Pattern:
    - Arrange: Prepare invalid input strings followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that appropriate error messages are displayed.
    """
    # Arrange
    user_input = 'invalid input\nadd 5\nsubtract\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "ERROR" in captured.out

def test_calculator_addition(monkeypatch, capsys):
    """
    Test the calculator's addition operation.

    AAA Pattern:
    - Arrange: Prepare the input 'add 10 5' followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the correct result is displayed.
    """
    # Arrange
    user_input = '10 + 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "15.0" in captured.out

def test_calculator_subtraction(monkeypatch, capsys):
    """
    Test the calculator's subtraction operation.

    AAA Pattern:
    - Arrange: Prepare the input 'subtract 20 5' followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the correct result is displayed.
    """
    # Arrange
    user_input = '20 - 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "15.0" in captured.out

def test_calculator_multiplication(monkeypatch, capsys):
    """
    Test the calculator's multiplication operation.

    AAA Pattern:
    - Arrange: Prepare the input 'multiply 7 8' followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the correct result is displayed.
    """
    # Arrange
    user_input = '7 * 8\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "56.0" in captured.out

def test_calculator_division(monkeypatch, capsys):
    """
    Test the calculator's division operation.

    AAA Pattern:
    - Arrange: Prepare the input 'divide 20 4' followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the correct result is displayed.
    """
    # Arrange
    user_input = '20 / 4\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "5.0" in captured.out

def test_calculator_division_by_zero(monkeypatch, capsys):
    """
    Test the calculator's handling of division by zero.

    AAA Pattern:
    - Arrange: Prepare the input 'divide 10 0' followed by 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that a zero division error message is displayed.
    """
    # Arrange
    user_input = '10 / 0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out

def test_calculator_history(monkeypatch, capsys):
    """
    Test the calculator's ability to display calculation history.

    AAA Pattern:
    - Arrange: Prepare a sequence of operations followed by 'history' and 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the history is displayed correctly.
    """
    # Arrange
    user_input = '10 + 5\n20 - 3\nhistory\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "15.0" in captured.out
    assert "17.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "2. SubCalculation: 20.0 Sub 3.0 = 17.0" in captured.out

# New Tests to Increase Coverage

def test_calculator_invalid_number_input(monkeypatch, capsys):
    """
    Test the calculator's handling of invalid number input.

    AAA Pattern:
    - Arrange: Prepare input where numbers are non-numeric strings.
    - Act: Call the calculator function.
    - Assert: Verify that appropriate error messages are displayed.
    """
    # Arrange
    user_input = 'add ten five\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "ERROR" in captured.out

# test_calculator.py

# ... [other imports and tests] ...

def test_calculator_unsupported_operation(monkeypatch, capsys):
    """
    Test the calculator's handling of an unsupported operation.

    AAA Pattern:
    - Arrange: Provide an operation that is not supported.
    - Act: Call the calculator function.
    - Assert: Verify that the appropriate error message is displayed.
    """
    # Arrange
    user_input = '2 ^ 3\nexit\n'  # Changed 'power' to 'modulus'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Unsupported operation." in captured.out

def test_calculator_unexpected_exception(monkeypatch, capsys):
    """
    Test the calculator's handling of unexpected exceptions during calculation execution.

    AAA Pattern:
    - Arrange: Mock the execute method to raise an unexpected exception.
    - Act: Call the calculator function.
    - Assert: Verify that the appropriate error message is displayed.
    """
    # Arrange
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, a, b):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    user_input = '10 + 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    with pytest.raises(SystemExit):
        Calculator()

    # Assert
    captured = capsys.readouterr()
    assert "An error occurred during calculation:" in captured.out
    assert "Please try again." in captured.out


"""
from app.calculator import *
from io import StringIO
import sys
import pytest

def simulate_expression_input(monkeypatch, inputs):

    next_input = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(next_input))

    captured_output = StringIO()
    sys.stdout = captured_output
    Calculator()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()
    


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["2 + ","exit"], "ERROR:  Wrong expression format."),
        ([" + 2","exit"], "ERROR:  Wrong expression format."),
        (["2 2","exit"], "ERROR:  Wrong expression format."),
        (["2+2","exit"], "ERROR:  Wrong expression format."),
        (["","exit"], "ERROR:  Wrong expression format."),

    ],
    ids=[
        "missing_first_number",
        "missing_second_number",
        "missing_operator",
        "no_spaces",
        "blank_expression",
    ],
)

def test_expression_format(monkeypatch, inputs, expected):
    output = simulate_expression_input(monkeypatch, inputs)
    assert expected in output, f"The inputs: {inputs} do not output: {expected}, but outputs {output}"

def test_exit(monkeypatch):
    inputs = ["exit"]
    output = simulate_expression_input(monkeypatch, inputs)
    assert "Good-bye" in output
"""