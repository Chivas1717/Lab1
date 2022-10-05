import argparse

parser = argparse.ArgumentParser(description="calculator")
parser.add_argument('userInput', nargs='?', type=str, help="type your input")
args = parser.parse_args()


def correct_formula(userInput):
    result = None
    if userInput:
        if "++" in userInput or "--" in userInput:
            return 'False', result
        else:
            try:
                result = eval(userInput)
                return 'True', result
            except:
                return 'False', result
    else:
        return 'False', result


print(correct_formula(args.userInput))
