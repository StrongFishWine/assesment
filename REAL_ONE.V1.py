import math
import pandas
from tabulate import tabulate

def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")

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

def triangle():
    area_how = not_blank("Do you know all the sides of the triangle or only the base/height: ")

    if area_how == "sides" or area_how == "s":
        print()
        tri_sides()
    if area_how == "base" or area_how == "b/h" or area_how == "height" or area_how == "b" or area_how == "h"or area_how == "base/height":
        print()
        tri_BaseHeight()
    else:
        print()
        print("Please enter either 'sides' (s) or 'base/height' (b/h)")
        print()
        triangle()

def tri_BaseHeight():
    base = num_check("Base length: ")
    height = num_check("Triangle Height: ")

    area = base*height*0.5

    print()
    print(f"Triangle area: {area:.2f}")
    print()
    startshape()

def tri_sides():
    side1 = num_check("Side one length: ")
    side2 = num_check("Side two length: ")
    side3 = num_check("Side three length: ")

    if (side1+side2<side3) or (side1+side3<side2) or (side3+side2<side1):
        print("This triangle can't exist")
        print("Please try a real one")
        tri_sides()

    semi = (side1+side2+side3)/2
    area = math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
    perimeter = side1+side2+side3

    print()
    print(f"Triangle perimeter: {perimeter}")
    print(f"Triangle area: {area:.2f}")
    print()
    startshape()

def circle():
    radius = num_check("Radius length: ")

    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius

    print()
    print(f"Circle area: {area:.2f}")
    print(f"Circle circumference: {perimeter:.2f}")
    print()
    startshape()

def rectangle():
    length = num_check("Length: ")
    width = num_check("Width: ")

    area = width*length
    perimeter = 2*(width+length)

    print()
    print(f"Rectangle area: {area:.2f}")
    print(f"Rectangle perimeter: {perimeter:.2f}")
    print()
    startshape()

def square():
    side = num_check("side length: ")

    area = side ** 2
    perimeter = side * 4


    print()
    print(f"Square area: {area:.2f}")
    print(f"Square perimeter: {perimeter:.2f}")
    print()
    startshape()

def startshape():

    shape = not_blank("What shape?: ")
    if shape == "circle" or shape == "c" or shape == "round one":
        print()
        circle()
    elif shape == "triangle" or shape == "t":
        print()
        triangle()
    elif shape == "square" or shape == "s":
        print()
        square()
    elif  shape == "rectangle" or shape == "r":
        print()
        rectangle()
    elif shape == "xxx":
        return
    else:
        print()
        print("Please enter one of the below")
        print(" 'square'    (s)")
        print(" 'rectangle' (r)")
        print(" 'triangle'  (t)")
        print(" 'circle'    (c)")
        print()
        startshape()


all_shapes = []
all_areas = []
all_perimeters = []

namestuffnumber = {
    'shape': all_shapes,
    'area': all_areas,
    'perimeter': all_perimeters
}



# main
print(make_statement("---|Souza's Shape Calc|---"))

print()
want_instructions = yes_no_check("Would you like to see the instructions?: ")
print()

if want_instructions == "yes":
    print("here ya go :D")
    instructions()


if want_instructions == "no":
    print(f"mb boss")

startshape()

panda = tabulate(pandas.DataFrame(namestuffnumber), headers='keys', tablefmt='psql', showindex=False)
print(panda)


