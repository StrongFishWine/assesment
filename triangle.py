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

def tri_perimeter(side1, side2, side3):
    return {"perimeter": side1+side2+side3}

    side1 = num_check("First side length: ")
    side2 = num_check("Second side length: ")
    side3 = num_check("Third side length: ")

    print(f"Triangle perimeter: {square(side)['perimeter']}")

