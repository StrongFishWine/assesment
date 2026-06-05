import math
def square(side):
    return {"area": side**2, "perimeter": side*4,}

    side = num_check("side length: ")

    print(f"Circle area: {square(side)['area']}")
    print(f"Circle circumference: {square(side)['perimeter']}")

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


