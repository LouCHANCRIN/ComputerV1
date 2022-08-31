import sys
import math
from read import read_input

def print_equation(equation):
    degrees = list(equation.keys())
    degrees.sort(reverse=True)

    equation_string = 'Reduced form : '
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



def main():
    equation = read_input(sys.argv[1])
    degrees = list(equation.keys())
    for key in degrees:
        if equation[key] == 0:
            del equation[key]

    print_equation(equation)

    degree = max(equation.keys())
    print(f"Polynomial degree : {degree}")
    if degree > 2:
        print(f"Equation of degree {degree} are not handled")

    solve_equation(degree, equation[2] if 2 in equation else 0, equation[1] if 1 in equation else 0, equation[0] if 0 in equation else 0,)

if __name__ == "__main__":
    ### check number argument, one argument must be present
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        sys.exit("Usage: pythonX.X string_to_analyse")
    main()