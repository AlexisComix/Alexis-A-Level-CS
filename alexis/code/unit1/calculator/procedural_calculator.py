"""
A calculator using the hierarchy chart (procedural).
"""

import sys

def display_choices():
    """
    Displays the choices to the terminal
    Returns a string with either +, -, *, or /
    """
    print("Welcome to the calculator. Choose an operation:")
    print("+ Add")
    print("- Subtract")
    print("* Multiply")
    print("/ Divide")

def get_valid_choice():
    operator = None                         # init operator variable
    while operator is None:                 # while no valid input
        inp = input("Enter operation: ")    # get input
        if "q" in inp:                      # exit on "q" input
            print("Exiting...")
            sys.exit()
        elif inp in " \n":                  # return error if blank
            print("Cannot be blank")
        elif inp in "+=*/":                 # check if valid
            operator = inp                  # if valid, assign operator
        else:                               # if not valid
            print("Invalid input")

    return operator

def get_valid_inputs():
    """
    Gets valid operand inputs from the user
    Returns a tuple with the operands
    """
    # initialise operand variables
    first_operand = None
    second_operand = None

    # while no valid input for first operand
    while first_operand is None:
        inp = input("Enter first operand: ")    # get input
        if "q" in inp:                          # exit on "q" input
            print("Exiting...")
            sys.exit()
        try:                            # try to convert input to float
            first_operand = float(inp)  # assign operand to input
        except ValueError:              # if error then input not valid
            print("Bad input. Please try again.")

    # second operand
    while second_operand is None:
        inp = input("Enter second operand: ")
        if "q" in inp:
            print("Exiting...")
            sys.exit()
        try:
            second_operand = float(inp)
        except ValueError:
            print("Bad input. Please try again.")

    return (first_operand, second_operand)

# calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x + y

def display_results(result):
    print(result)

def main():
    """
    Main program method
    """
    display_choices()               # display choices
    operation = get_valid_choice()  # get operation
    a, b = get_valid_inputs()       # get operands

    result = None                   # init result var
    
    # do the correct operation procedure depending on the operation var
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        print("Unknown choice")
        print("Exiting...")
        sys.exit()

    display_results(result)         # display results

# main program
if __name__ == "__main__":
    main()