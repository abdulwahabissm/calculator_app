class Calculator:
    """A simple calculator class."""

    @staticmethod
    def add(x, y):
        """Add Function"""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Subtract Function"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiply Function"""
        return x * y

    @staticmethod
    def divide(x, y):
        """Divide Function. Raises ValueError on division by zero."""
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
