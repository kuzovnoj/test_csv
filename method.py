import argparse
import re
import json


# Проверка корректности имени csv-файла
def csv_type(arg_value: str) -> str:
    pat=re.compile(r".+\.csv$")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError("Please input correct csv")
    return arg_value


def become_rate(data: list[dict]) -> None:    
    for emp in data:
        if 'hourly_rate' in emp:
            emp['rate'] = emp.pop('hourly_rate')
        if 'salary' in emp:
            emp['rate'] = emp.pop('salary')


class Reports():
    def __init__(self, report_name: str, data: list[str], output_file: str = None) -> None:
        # при добавлении нового метода (отчета), необходимо прописать его название в reports
        reports = {'payout', 'salary'}
        if report_name not in reports:
            raise ValueError(f'There is no such report: {report_name}')
        self.report_name = report_name
        self.data = data
        self.output_file = output_file
    
    def report(self) -> None:
        eval('self.' + self.report_name + '()')
    
    def payout(self) -> None:
        departments = {}
        for employee in self.data:
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
        if self.output_file is None:
            with open('payout.json', 'w') as file2:
                json.dump(report1, file2)
        else:
            with open(self.output_file, 'w') as file2:
                json.dump(report1, file2)

    def salary(self) -> None:
        print('report salary')