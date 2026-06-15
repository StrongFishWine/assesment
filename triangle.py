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

def triangleArea():
    area_how = not_blank("Do you know all the sides of the triangle or only the base/height: ")

    if area_how == "sides" or area_how == "s":
        tri_areaHL()
    if area_how == "base" or area_how == "b/h" or area_how == "height" or area_how == "b" or area_how == "h"or area_how == "base/height":
        tri_areaBH()
    else:
        print("Please enter either 'sides' (s) or 'base/height' (b/h)")
        return triangleArea()

def tri_areaBH():
    base = num_check("Base length: ")
    height = num_check("Triangle Height: ")

    area = base*height*0.5

    print(f"Triangle area: {area:.2f}")

def tri_areaHL():
    side1 = num_check("Side one length: ")
    side2 = num_check("Side two length: ")
    side3 = num_check("Side three length: ")

    semi = (side1+side2+side3)/2

    area = math.sqrt(semi*(semi-side1)*(semi-side2)*(semi*side3))

    print(f"Triangle area: {area:.2f}")

def tri_perimeter():

    side1 = num_check("First side length: ")
    side2 = num_check("Second side length: ")
    side3 = num_check("Third side length: ")

    perimeter = side1+side2+side3
    print(f"Triangle perimeter: {perimeter}")
    return perimeter

def triangle():
    tri_output = not_blank( "Do you need the area or perimeter for your triangle?: ")
    if tri_output == "area" or tri_output == "a":
        return triangleArea()
    elif tri_output == "perimeter" or tri_output == "p":
        return tri_perimeter()
    else:
        print("Please enter either 'area' (a) or 'perimeter' (p)")
        return triangle()



triangle()