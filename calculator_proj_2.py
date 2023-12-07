# calculator_gui.py
import tkinter as tk
from tkinter import messagebox
from formulas_final_proj_2 import Calculator


class CalculatorApp:
    """
    Calculator application using Tkinter.
    """
    def __init__(self, root: tk.Tk):
        """
        Initialize the calculator app.

        Parameters:
            root (tk.Tk): The main Tkinter window.
        """
        self.root = root # creates the window
        self.root.title("Simple Calculator")  # give window a title

        self.entry = tk.Entry(root, width=20)  # creates Entry widget
        self.entry.grid(row=0, column=0, columnspan=4)  # the entry widget at 0,0 width of 4

        # The desired order of the buttons
        buttons = [
            '1', '2', '3', '+', 'C',
            '4', '5', '6', '-', '<-',
            '7', '8', '9', '*', 'Quit',
            '0', '.', '=', '/'
        ]
        # define button labels for order
        row_val = 1
        col_val = 0

        self.calculator = Calculator()  # Create an instance of the Calculator class
        # iterate through button labels
        # creates a button for each label and associates it with the on_button_click
        for button in buttons:
            # parent widget, text on the button, when button is clicked, call this function
            tk.Button(root, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            # brings button over one column, if greater than 4, it adds a new row and resets to 0
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, button: str) -> None:
        """
        Handle button clicks.

        Parameters:
            button (str): The button clicked.
        """
        # grab current text in entry widget
        current_text = self.entry.get().upper()

        if button == '=':  # attempt calculation if '='
            try:
                result = self.calculate(current_text)  # get result from calc function
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif button == 'C':
            self.entry.delete(0, tk.END)  # Clear the entry field
        elif button == '<-':
            current_text = current_text[:-1]  # Remove the last character
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text)
        elif button == 'Quit':
            self.root.quit()  # Quit the application
        else:
            self.entry.insert(tk.END, button)

    def calculate(self, expression: str) -> float:
        """
        Calculate the result of the given expression.

        Parameters:
            expression (str): The mathematical expression.

        Returns:
            float: The calculated result.
        """
        try:
            # Split the expression into individual characters
            tokens = [char for char in expression]

            # Separate numeric values and operators
            values = []
            operators = []
            current_value = ""

            for token in tokens:
                if token.isdigit() or token == '.':
                    current_value += token
                else:
                    if current_value:
                        values.append(float(current_value))
                        current_value = ""
                    if token in {'+', '-', '*', '/'}:
                        operators.append(token)

            if current_value:
                values.append(float(current_value))

            # If no operator is present, return the entered number
            if not operators and len(values) == 1:
                return values[0]

            # If more than one operator is present, use evaluate_expression
            if len(operators) > 1:
                return self.calculate_eval(expression)

            # Continue with PEMDAS logic
            operator = operators[0]
            result = None

            if operator == '+':
                result = self.calculator.add(values)
            elif operator == '-':
                result = self.calculator.subtract(values)
            elif operator == '*':
                result = self.calculator.multiply(values)
            elif operator == '/':
                try:
                    result = self.calculator.divide(values)
                except Calculator.DivisionByZeroError as e:
                    messagebox.showerror("Error", str(e))
                    return ''  # Don't proceed further in case of division by zero

            if result is not '':
                return result

            raise ValueError("Invalid expression")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return ''

    def calculate_eval(self, expression: str) -> float:
        """
        Evaluate the expression using eval for more than 1 operator

        Parameters:
            expression (str): The mathematical expression.

        Returns:
            float: The calculated result.
        """
        try:
            result = self.calculator.evaluate_expression(expression)
            return result
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return ''


def main() -> None:
    """
    Main function to run the calculator application.
    """
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
