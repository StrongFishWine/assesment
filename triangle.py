import math

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

def triangle():
    area_how = not_blank("Do you know all the sides of the triangle or only the base/height: ")

    if area_how == "sides" or area_how == "s":
        print()
        tri_sides()
    elif area_how == "base" or area_how == "b/h" or area_how == "height" or area_how == "b" or area_how == "h"or area_how == "base/height":
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

    if (side1+side2<=side3) or (side1+side3<=side2) or (side3+side2<=side1):
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

def startshape():

    shape = not_blank("What shape?: ")

    if shape == "triangle" or shape == "t":
        print()
        triangle()
    else:
        print()
        print("Please enter one of the below")
        print(" 'triangle'  (t)")

        print()
        startshape()


startshape()