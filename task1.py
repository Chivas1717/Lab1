import math
import argparse

parser = argparse.ArgumentParser(description="calculator")
parser.add_argument('firstNumber',  type=int, help="enter first number")
parser.add_argument('operator',  type=str, help="enter your operator")
parser.add_argument('secondNumber', type=int, help="enter second number")
args = parser.parse_args()


def basic_math_function(a, operator, b):
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        return "Not an basic operator"
    elif operator == "/" and b == 0:
        return "error: division by zero"
    else:
        return "Result: ",  eval(str(a) + operator + str(b))


print(basic_math_function(args.firstNumber, args.operator, args.secondNumber))
