from lexer import OPERATORS

class ast():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def reduce_equation(self, negative_first_part, negative_second_part):
        over = False
        left_equation = {}
        while over == False:
            ret, over = self.return_deepest_operation(self.left, '-' if negative_first_part else '+')
            if over == True:
                self.left = None
            if not ret['degree'] in left_equation:
                left_equation[ret['degree']] = ret['val']
            else:
                left_equation[ret['degree']] += ret['val']

        over = False
        if self.right.value != '0':
            while over == False:
                ret, over = self.return_deepest_operation(self.right, '-' if negative_second_part else '+')
                if over == True:
                    self.right = None
                if not ret['degree'] in left_equation:
                    left_equation[ret['degree']] = -ret['val']
                else:
                    left_equation[ret['degree']] -= ret['val']
        return left_equation

    def return_deepest_operation(self, current_node, current_op):
        if current_node.left and current_node.left.value in ['+', '-']:
            ret, destroy_left = self.return_deepest_operation(current_node.left, current_node.value)
            if destroy_left:
                current_node.left = None
            return ret, False
        elif current_node.right and current_node.right.value in ['+', '-']:
            ret, destroy_right = self.return_deepest_operation(current_node.right, current_node.value)
            if destroy_right:
                current_node.right = None
            return ret, False
        elif current_node.right and current_node.right.value == '*':
            value = float(current_node.right.left.value) if current_node.value == '+' else -float(current_node.right.left.value)
            ret = {'val': value, 'degree': int(current_node.right.right.right.value), 'sign': current_node.value}
            current_node.right = None
            return ret, False
        elif current_node.left and current_node.left.value == '*':
            value = float(current_node.left.left.value) if current_op == '+' else -float(current_node.left.left.value)
            ret = {'val': value, 'degree': int(current_node.left.right.right.value), 'sign': current_op}
            current_node.left = None
            return ret, True

    def print_equation(self):
        if self.value in OPERATORS:
            return f"{self.left.print_equation()} {self.value} {self.right.print_equation()}"
        else:
            return str(self.value)

def atom_parser(stream):
    if not stream:
        raise SyntaxError("Unexcepted EOF")
    if stream[0].isupper() or stream[0].islower() or stream[0].replace(".", "", 1).isdigit():
        return ast(stream[0], None, None), 1
    if stream[0] == '(':
        right, current_r = plus_parser(stream[1:])
        if current_r < len(stream) and stream[current_r + 1] == ')':
            return right, current_r + 2
        raise SyntaxError("Missing )")
    raise SyntaxError("Missing operand")

def exposant_parser(stream):
    left, current = atom_parser(stream)

    if current < len(stream) and stream[current] == ')':
        return left, current

    if current < len(stream) and stream[current] == '^':
        right, current_r = exposant_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1
    return left, current

def multiplcation_parser(stream):
    left, current = exposant_parser(stream)

    if current < len(stream) and stream[current] == ')':
        return left, current

    if current < len(stream) and stream[current] == '*':
        right, current_r = multiplcation_parser(stream[current + 1:])
        return ast(stream[current], left, right), current + current_r + 1
    return left, current

def plus_parser(stream):
    left, current = multiplcation_parser(stream)

    if current < len(stream) and stream[current] == ')':
        return left, current
    
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
