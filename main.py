import argparse
import re

def csv_type(arg_value):
    pat=re.compile(r"\w+\.csv$")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError("invalid value")
    return arg_value

parser = argparse.ArgumentParser(description='Подсчет ЗП')
parser.add_argument('csv_file', type=csv_type, nargs='+', help='bar help')
args = parser.parse_args()
print(args)