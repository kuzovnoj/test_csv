import argparse
import re

def csv_type(arg_value):
    pat=re.compile(r"\w+\.csv$")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError("invalid value")
    return arg_value

parser = argparse.ArgumentParser(description='Подсчет ЗП')
parser.add_argument('csv_file', type=csv_type, nargs='+', help='name of csv_file')
parser.add_argument('--report', type=str, default='payout', help='name of report')
args = parser.parse_args()

spisok = []
for i in args.csv_file:
    with open(i, 'r', encoding='utf-8') as file1:
        spisok += file1.readlines()

print(spisok)