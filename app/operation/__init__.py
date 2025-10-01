class Operation:
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def mul(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def div(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero not allowed.")
        return a / b