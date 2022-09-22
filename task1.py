import math
import argparse

parser = argparse.ArgumentParser(description="calculator")
parser.add_argument('firstNumber',  type=str, help="enter first number")
parser.add_argument('operator',  type=str, help="enter your operator")
parser.add_argument('secondNumber', type=str, help="enter second number")
args = parser.parse_args()

a = args.firstNumber
b = args.secondNumber
operator = args.operator
print(eval(a + operator + b))

