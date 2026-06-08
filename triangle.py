import math

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

def tri_areaBH():
    base = num_check("Base length: ")
    height = num_check("Triangle Height: ")

    area = base*height

    print(f"Triangle area: {area:.2f}")

def tri_perimeter():

    side1 = num_check("First side length: ")
    side2 = num_check("Second side length: ")
    side3 = num_check("Third side length: ")

    perimeter = side1+side2+side3
    print(f"Triangle perimeter: {perimeter}")

def triangle():
    trioutput = input("Do you need the area or perimeter for your triangle?: ")
    if trioutput == "area" or "a":
        tri_areaBH()
    elif trioutput == "perimeter" or "p":
        tri_perimeter()
