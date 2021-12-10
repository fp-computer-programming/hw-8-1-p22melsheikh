# MEE 12/09/21


def grade_calculate(g):
    if g < 60:
        print("You get an F")
    elif g < 65:
        print("You get a D")
    elif g < 70:
        print("You get a D+")
    elif g < 73:
        print("You get a C-")
    elif g < 77:
        print("You get a C")
    elif g < 80:
        print("You get a C+")
    elif g < 83:
        print("You get a B-")
    elif g < 87:
        print("You get a B")
    elif g < 90:
        print("You get a B+")
    elif g < 93:
        print("You get a A-")
    else:
        print("You get an A!")

g = input("What is your grade for the quarter? ")
grade_calculate(int(g))

grade_calculate(80)
grade_calculate(100)
grade_calculate(94)