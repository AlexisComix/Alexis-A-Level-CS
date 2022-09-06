"""
An example of an object-oriented calculator
"""

# Imports
import math
import tkinter
from tkinter import N, E, S, W, ttk 


# Main program class
class Calculator(tkinter.Tk):
    """
    Calculator class
    """
    def __init__(self):
        # Constants
        self.WIN_WIDTH = 400
        self.WIN_HEIGHT = 600

        # Initialise Window
        super().__init__()
        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.title("Alexis' Calculator")
        self.resizable(False, False) # Make the window not resizable

        self.configure_grid()

        # Variables
        self.operator = None   # x, /, +, -
        self.first_operand = None
        self.second_operand = None

        self.create_widgets()

    def configure_grid(self):
        """
        Configure a grid with 4 columns and 6 rows.
        """
        self.gridwidth = 4
        self.gridheight = 6
        for i in range(self.gridwidth):
            self.grid_columnconfigure(i, weight=1)
        for i in range(self.gridheight):
            self.grid_rowconfigure(i, weight=1)

    def get_display(self):
        """
        Gets what to desplay to the screen
        """
        output = ""
        if self.first_operand is not None:
            output += self.first_operand
        if self.second_operand is not None:
            output += self.operator
        if self.first_operand is not None:
            output += self.second_operand
        return output

    def create_widgets(self):
        """
        Creates the widgets
        """
        # Create the display
        to_display = self.get_display()
        text = tkinter.Label(self, text=to_display)
        text.config(font=("Arial", 40))
        text.grid(row=0, column=0, columnspan=self.gridwidth, sticky=E)

        # Create the numbers
        button_1 = tkinter.Button(self, text="1", command=self.one)

    def one(self):
        if self.operator is None:
            operand_str = str(self.first_operand)
            operand_str += "1"
            self.first_operand = int(operand_str)
        else:
            operand_str = str(self.second_operand)
            operand_str += "1"
            self.second_operand = int(operand_str)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()