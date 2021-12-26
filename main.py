import sys
import os.path
from read import read_input
from format import get_dict

def main():
    rules, facts, queries = read_input(sys.argv[1])
    # dictionnaire, facts, queries, initial_fatcs = get_dict(rules, facts, queries)

if __name__ == "__main__":
    ### check number argument, one argument must be present
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        sys.exit("Usage: pythonX.X string_to_analyse")
    main()