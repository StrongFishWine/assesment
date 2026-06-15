import math
def rectangle():
    length = num_check("Length: ")
    width = num_check("Width: ")

    area = width*length
    perimeter = 2*(width+length)

    print(f"Rectangle area: {area:.2f}")
    print(f"Rectangle perimeter: {perimeter:.2f}")

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


