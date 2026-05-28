import math
def make_statement(statement,):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{statement}\n"

def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes" or response == "maybe":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")

def instructions():
    """Displays instructions"""
    print(make_statement("Instructions:"))
    print('''This a shape calculator

    ''')

print(make_statement("---|Souza's Shape Calc|---"))

print()
want_instructions = yes_no_check("Would you like to see the instructions? ")
print()+

if want_instructions == "yes":
    instructions()

if want_instructions == "no":
    print(f"mb boss")

print()