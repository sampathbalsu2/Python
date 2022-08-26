import argparse

parser =argparse.ArgumentParser()

parser.add_argument("number1",help="first number")
parser.add_argument("number2",help="second number")
parser.add_argument("--operation",help="operation",choices= \
                    ["add","subtract","multply"])

args = parser.parse_known_args()

print(args[0].number1)
print(args[0].number2)

print("sum of {a} {b} is ".format(a=args[0].number1,b=args[0].number2),(int(args[0].number1)+int(args[0].number2)))
print("optional orguement is {}".format(args[0].operation))
print(args[1])