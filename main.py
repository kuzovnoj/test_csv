import argparse
from method import become_rate, csv_type, Reports


parser = argparse.ArgumentParser(description='Подсчет ЗП')
parser.add_argument('csv_file', type=csv_type, nargs='+', help='name of csv_file')
parser.add_argument('--report', type=str, default='payout', help='name of report')
args = parser.parse_args()

employees = []
for file in args.csv_file:
    with open(file, 'r', encoding='utf-8') as file1:
        columns = file1.readline().rstrip('\n').split(',')
        rows = file1.readlines()
        for row in rows:
            employees.append(dict(zip(columns, row.rstrip('\n').split(','))))


become_rate(employees)
try:
    rep1 = Reports(args.report, employees)
    rep1.report()
except ValueError as e:
    print(e)
