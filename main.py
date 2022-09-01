import sys
import math
from read import read_input

def print_equation(equation, degree):
    degrees = list(equation.keys())
    degrees.sort()

    equation_string = 'Reduced form : '
    if degree == None:
        print(f"{equation_string}0 = 0")
        return
    first = True
    for key in degrees:
        if first:
            if equation[key] > 0:
                equation_string += f"{equation[key]} * X ^ {key} "
            else:
                equation_string += f"- {equation[key] * -1} * X ^ {key} "
            first = False
        else:
            if equation[key] > 0:
                equation_string += f"+ {equation[key]} * X ^ {key} "
            else:
                equation_string += f"- {equation[key] * -1} * X ^ {key} "

    print(f"{equation_string}= 0")

def solve_equation(degree, a, b, c):
    # Gérer les divisions par 0
    print("# Gérer les divisions par 0")
    print(f"a = {a}, b = {b}, c = {c}")
    if degree == 2:
        discriminant = (b ** 2) + (4 * a * c)
        if discriminant < 0:
            print(f"Delta = {discriminant} : No solution for this equation")
        elif discriminant == 0:
            print(f"Delta = {discriminant} : the solution is {-b / (2 * a)}")
        else:
            print(f"Delta = {discriminant} : the solutions are {(-b - math.sqrt(discriminant)) / (2 * a)} and {(-b + math.sqrt(discriminant)) / (2 * a)}")
    elif degree == 1:
        print(f"The solution is {-c / b}")
    elif degree == 0:
        print(f"There is no solution to this equation")
    elif degree == None:
        print("All real numbers are a solution to this equation")


def main():
    equation = read_input(sys.argv[1])

    degree = None
    for key in equation.keys():
        if equation[key] != 0:
            if degree == None or key > degree:
                degree = key

    print_equation(equation, degree)

    print(f"Polynomial degree : {degree if degree else 0}")
    if degree and degree > 2:
        print(f"Equation of degree {degree if degree else 0} are not handled")

    solve_equation(degree, equation[2] if 2 in equation else 0, equation[1] if 1 in equation else 0, equation[0] if 0 in equation else 0,)

if __name__ == "__main__":
    ### check number argument, one argument must be present
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        sys.exit("Usage: pythonX.X string_to_analyse")
    main()