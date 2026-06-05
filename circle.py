import math
def circle(radius):
    return {"area": math.pi*radius**2, "perimeter": 2*math.pi*radius,}

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

radius = num_check("Radius: ")
print(f"Circle area: {circle(radius)['area']}")
print(f"Circle circumference: {circle(radius)['perimeter']}")