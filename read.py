
from os import X_OK
import sys
from lexer import lexing_line, OPERATOR
from parse import if_parser

def check_if_operator(line):
    for opera in OPERATOR:
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
    rules, facts, queries = [], None, None
    tmp = lexing_line(line)
    if tmp:
        tmp_parser = if_parser(tmp)
    
    print(tmp_parser.print_equation())
    return rules, facts, queries