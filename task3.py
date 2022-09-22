import argparse

parser = argparse.ArgumentParser(description="calculator")
parser.add_argument('userInput', nargs='?', type=str, help="type your input")
args = parser.parse_args()
userInput = args.userInput
result = None
if not userInput:
    print('False', result)
else:
    if "++" in userInput or "--" in userInput:
        print('False', result)
    else:
        try:
            result = eval(userInput)
            print('True', result)
        except:
            print('False', result)