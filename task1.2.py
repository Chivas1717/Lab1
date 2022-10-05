import math
import argparse
import operator as operators

parser = argparse.ArgumentParser(description="calculator")
parser.add_argument('operator', help="enter your operator")
parser.add_argument('numbers', nargs="+",  type=int, help="enter first number")

args = parser.parse_args()


def math_function(numbers, operator):
    try:
        operator = getattr(operators, operator)
        if operator:
            return operator(*numbers)
        operator = getattr(math, operator)
        return operator(*numbers)
    except AttributeError:
        return "Try another function"


print(math_function(args.numbers, args.operator))