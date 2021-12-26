
from os import X_OK
import sys
from lexer import lexing_line, OPERATOR
from parse import if_parser


#     *
# 1           ^
#         X       0



#             ^
#     *           0
# 1       X

def print_tree(tree, current):
    print(current, tree.value)
    if tree.left is not None:
        print_tree(tree.left, "left")
    if tree.right is not None:
        print_tree(tree.right, "right")

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
        if tmp[0] == '=' and rules and queries is None:
            facts = tmp
        elif tmp[0] == '?' and rules and facts is not None:
            queries = tmp
        elif tmp[0] != '=' and tmp[0] != '?' and queries is None and facts is None:
            #print(tmp)
            tmp_parser = if_parser(tmp)
            # rule = {"règle": tmp_parser, "ligne": tmp}
            # print(tmp_parser.left, tmp_parser.value, tmp_parser.right)
            print_tree(tmp_parser.left, "center")
            print("\n.\n.\n.\n.\n")
            print_tree(tmp_parser.right, "center")


            # print_tree(tmp_parser, "center")
            #rules.append(rule)
            # rules.append(tmp_parser)
        else:
            raise Exception("Wrong formatage of file %s" %sys.argv[1])
    return rules, facts, queries