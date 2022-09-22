import math
import argparse
import operator as operators

parser = argparse.ArgumentParser(description="calculator")
parser.add_argument('operator',  type=str, help="enter your operator")
parser.add_argument('firstNumber',  type=int, help="enter first number")
parser.add_argument('secondNumber', type=int, nargs="?", help="enter second number")
args = parser.parse_args()

a = args.firstNumber
b = args.secondNumber
operator = args.operator

try:
    operator = getattr(operators, operator)
    print(operator(a, b))
except AttributeError:
    try:
        operator = getattr(math, operator)
        print(operator(a, b))
    except AttributeError:
        print("Try another function")