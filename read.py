
from os import X_OK
import sys
from lexer import lexing_line, OPERATORS
from parse import if_parser

def check_if_operator(line):
    for opera in OPERATORS:
        if line.startswith(opera):
            return opera
    return ""

def read_input(line):
    """
    Read line by line file in sys.argv and delete space backslash n and backslash t. Split with
    # and extract first ele
    params: None
    return: rules -> list of list tokens
            facts -> list of tokens
            queries -> list of tokens
    """
    tmp, negative_first_part, negative_second_part = lexing_line(line)
    if tmp:
        tmp_parser = if_parser(tmp)
    tmp_parser.reduce_equation(negative_first_part, negative_second_part)
    return None