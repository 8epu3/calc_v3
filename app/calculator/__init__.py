import sys

from app.calculation import CalculationFactory, Calculation
from typing import List

def display_help():
    help_message = """
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
    print(help_message)

def display_history(history: List[Calculation]) -> None:
    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

def parse_input(expression: str):
    
        parts = expression.split()
        
        if len(parts) != 3:
            raise ValueError("Wrong expression format.")

        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])
        except ValueError as e:
            raise ValueError(e)

        if op == '+':
            op = "add"
        elif op == '-':
          op = "sub"
        elif op == '*':
           op = "mul"
        elif op == '/':
            op = "div"
        else:
            raise ValueError("Unsupported operation.")
        
        return(op, num1, num2)

def Calculator() -> None:
    
    history: List[Calculation] = []

    

    print("Basic Calculator")
    print("Available commands are help, history, exit")
    while True:

        user_input: str = input(">>>").strip()

        if not user_input:
            continue

        command = user_input.lower()
        
        if command == 'exit':
            print("Good-bye")
            sys.exit(0)
        elif command == 'help':
            display_help()
            continue
        elif command == 'history':
            display_history(history)
            continue


        try:
            operation, a, b = parse_input(user_input)
        except ValueError as e:
            print("ERROR: ", e)
            continue
        
        try:
            calculation = CalculationFactory.create_calculation(operation, a, b)
        except ValueError as e:
            print("ERROR: ", e)
            continue

        try:
            print(calculation.exec())
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            continue
        except Exception as e:
            print(f"An error occurred during calculation: {e}")
            print("Please try again.\n")
            continue

        history.append(calculation)
        
