""""
Whenever you are developing applications into server, there is no VS code to fix your bugs. you have to use command line tools to do that. that's why command line tools learning is very important to make application production
"""
import argparse
import sys

# arithmetic calculator
def calculator(args):
    if args.op == 'add':
        return args.num1 + args.num2
    elif args.op == 'sub':
        return args.num1 - args.num2
    elif args.op == 'mul':
        return args.num1 * args.num2
    elif args.op == 'div':
        if args.num2 != 0:
            return args.num1 / args.num2
        else:
            return 'Divide by zero is not supported'
    elif args.op == '%':
        return args.num1 % args.num2
    else:
        return 'invalid operation type'
    

parser = argparse.ArgumentParser() # gives a parser object
parser.add_argument("--num1", type=float, default=1.0) # add argument
parser.add_argument("--num2", type=float, default=2.0) # add argument
parser.add_argument("--op", type=str, default='add') # add argument

args = parser.parse_args() # parse those arguments and return a object

sys.stdout.write(str(calculator(args))) # passe this args to function and also system