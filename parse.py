from lexer import OPERATOR

class ast():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def atom_parser(stream):
    if not stream:
        raise SyntaxError("Unexcepted EOF")
    if stream[0].isupper() == True or stream[0].islower() == True or stream[0].replace(".", "", 1).isdigit() == True:
        return ast(stream[0], None, None), 1
    print('stream[0]', stream[0])
    if stream[0] == '(':
        right, current_r = plus_parser(stream[1:])
        print("Ok")
        if current_r < len(stream) and stream[current_r + 1] == ')':
            print("Parenthese :", current_r, stream[current_r])
            return right, current_r + 2
        raise SyntaxError("Missing )")
    print(stream[0])
    raise SyntaxError("Missing operand")

def exposant_parser(stream):
    left, current = atom_parser(stream)
    if stream[0] == '^':
        right, current_r = exposant_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1
    return left, current

def multiplcation_parser(stream):
    left, current = exposant_parser(stream)
    if current < len(stream) and stream[current] == '*':
        right, current_r = multiplcation_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1
    else:
        right, current_r = exposant_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1

def plus_parser(stream):
    left, current = multiplcation_parser(stream)
    if current < len(stream) and stream[current] in ['+', '-']:
        right, current_r = plus_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1
    elif current < len(stream) and stream[current] != '=':
        right, current_r = multiplcation_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1
    else:
        return left, current

def if_parser(stream):
    left_part, current = plus_parser(stream)
    if current >= len(stream):
        raise SyntaxError("Missing assignation and expression")
    if stream[current] != '=':
        raise SyntaxError("Missing assignation")
    if not stream[current + 1:]:
        raise SyntaxError("Missing expression after assignation")
    right_part, current_r = plus_parser(stream[current + 1:])
    return ast(stream[current], left_part, right_part)
