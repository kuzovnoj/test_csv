import argparse
import re
import json

def csv_type(arg_value: str) -> str:
    pat=re.compile(r".+\.csv$")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError("Please input correct csv")
    return arg_value

# Ниже идут формы отчетов
def payout(data: list[str]) -> None:
    departments = {}
    for employee in data:
        departments.setdefault(employee['department'], []).append((employee['name'], employee['hours_worked'], employee['rate']))

    print(' ' * 15 + 'name' + ' ' * 16 + 'hours   rate    payout' )
    report1 = {}
    for k in sorted(departments):
        print(k)
        hours = 0
        payout = 0
        for emp in departments[k]:
            report1.setdefault(k, []).append({'name': emp[0], 'hours': emp[1], 'rate': emp[2], 'payout': '$' + str(int(emp[1]) * int(emp[2]))})
            print('-' * 15 + emp[0] + ' ' * (20 - len(emp[0])) + emp[1] + ' ' * (8 - len(emp[1])) + emp[2] +
                  ' ' * (8 - len(emp[2])) + '$' + str(int(emp[1]) * int(emp[2])))
            hours += int(emp[1])
            payout += (int(emp[1]) * int(emp[2]))
        print(' ' * 35 + str(hours) + ' ' * (16 - len(str(hours))) + '$' + str(payout))
        report1[k].append({'total hours': str(hours), 'total payout': '$' + str(payout)})
    with open('payout.json', 'w') as file2:
        json.dump(report1, file2)

def salary(data: list[str]) -> None:
    print('report salary')

# В словарь reports необходимо будет добавить название отчета после добавления соответствующей функции
reports = {'payout', 'salary'}

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
    
for emp in employees:
    if 'hourly_rate' in emp:
        emp['rate'] = emp.pop('hourly_rate')
    if 'salary' in emp:
        emp['rate'] = emp.pop('salary')

if args.report not in reports:
    print('Please enter correct report name')
else:
    eval(args.report)(employees)

