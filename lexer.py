
import sys

OPERATORS = ('+', '-', '^', '=', '*', '(', ')')

def check_if_operator(line):
    for opera in OPERATORS:
        if line.startswith(opera):
            return opera
    return ""

def lexing_line(line):
    line = line.replace(' ', '')

    i = 0
    tokens = []
    follow_equal = False
    if line[0] == '-':
        i += 1
        negative_first_part = True
    else:
        negative_first_part =  False
    negative_second_part = False

    while (i < len(line)):
        operator = check_if_operator(line[i:])

        if operator == '=':
            follow_equal = True
        if operator == '-' and follow_equal:
            i += 1
            negative_second_part = True

        elif operator:
            i += len(operator)
            tokens.append(operator)
        else:
            if line[i].isspace() == False:
                tmp = ''
                while i < len(line) and line[i].isspace() == False and line[i] not in OPERATORS:
                    tmp += line[i]
                    i += 1
                i -= 1
                tokens.append(tmp)
            follow_equal = False
            i += 1
    return tokens, negative_first_part, negative_second_part