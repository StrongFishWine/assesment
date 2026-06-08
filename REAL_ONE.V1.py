import math

def make_statement(statement,):
    return f"{statement}\n"

def yes_no_check(question):
    """Checks that users enter yes / no / y / n / maybe"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes" or response == "maybe":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")

def instructions():
    """make instructions: instructions"""
    print(make_statement("Instructions:"))
    print('''This a shape calculator

    ''')

def circle():
    radius = num_check("Radius length: ")

    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius

    print(f"Circle area: {area:.2f}")
    print(f"Circle circumference: {perimeter:.2f}")

def num_check(question, num_type="float"):

    if num_type == "float":
        error = "Please enter a number."
        zero = "Please enter a number more than 0."

    while True:

        response = input(question)

        try:
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(zero)

        except ValueError:
            print(error)

def tri_perimeter():

    side1 = num_check("First side length: ")
    side2 = num_check("Second side length: ")
    side3 = num_check("Third side length: ")

    perimeter = side1+side2+side3
    print(f"Triangle perimeter: {perimeter}")

print(make_statement("---|Souza's Shape Calc|---"))

print()
want_instructions = yes_no_check("Would you like to see the instructions? ")
print()

if want_instructions == "yes":
    instructions()

if want_instructions == "no":
    print(f"mb boss")

shape = input("What shape?: ")
if shape == "circle" or "c" or "round one":
    circle()
elif shape == "triangle" or "t":
    tri_perimeter()





