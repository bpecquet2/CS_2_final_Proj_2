import sys


class Calculator:
    """
    A calculator class with arithmetic operations.
    """

    class DivisionByZeroError(Exception):
        """
        Exception class for division by zero.
        """
        pass

    def add(self, values: list[float]) -> float:
        """
        Add the given values.

        Parameters:
            values (list[float]): List of values to be added.

        Returns:
            float: The sum of the values.
        """
        x = 0
        for i in values:
            if i >= 0:
                x += i
            else:
                x += 0
        return x

    def subtract(self, values: list[float]) -> float:
        """
        Subtract the given values.

        Parameters:
            values (list[float]): List of values to be subtracted.

        Returns:
            float: The result of subtraction.
        """
        x = 0
        for i in values:
            if i > 0:
                x = abs(x) - i
        return x

    def multiply(self, values: list[float]) -> float:
        """
        Multiply the given values.

        Parameters:
            values (list[float]): List of values to be multiplied.

        Returns:
            float: The product of the values.
        """
        x = 1
        for i in values:
            if i != 0:
                x *= i
            else:
                x += 0
        return x

    def divide(self, values: list[float]) -> float:
        """
        Divide the given values.

        Parameters:
            values (list[float]): List of values to be divided.

        Returns:
            float: The result of division.

        Raises:
            DivisionByZeroError: If attempting to divide by zero.
        """
        x = values[0]
        for i in values[1:]:
            if i == 0:
                raise self.DivisionByZeroError('Cannot divide by 0')
            else:
                x /= i
        x = round(x, 10)
        return x

    def evaluate_expression(self, expression: str) -> float:
        """
        Evaluate the mathematical expression using eval.

        Parameters:
            expression (str): The mathematical expression.

        Returns:
            float: The result of the expression.

        Raises:
            ValueError: If the expression is invalid.
        """
        try:
            result = eval(expression)
            x = round(result, 10)
            return x
        except Exception as e:
            raise ValueError("Invalid expression") from e
