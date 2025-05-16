import pytest
from method import become_rate, csv_type, Reports
import argparse
import json
import os
import sys

data1 = [{'department': 'STO', 'name': 'Petrovich', 'hours_worked': '100', 'rate': '30'}]

def test_create_json():
    temp_report = Reports('payout', data1, 'temp.json')
    temp_report.report()
    with open('temp.json', 'r') as file1:
        temp_data = json.load(file1)
        assert temp_data['STO'][1]['total payout'] == '$3000'
    os.remove('temp.json')

def test_no_report_error():
    try:
        temp_report = Reports('hour_count', data1, 'temp.json')
    except ValueError as e1:
        assert type(e1) == ValueError

def test_print_payment():
    temp_report = Reports('payout', data1, 'temp.json')
    temp = sys.stdout
    sys.stdout = open('temp2.txt', 'w')
    temp_report.report()
    sys.stdout.close()
    sys.stdout = temp
    with open('temp2.txt', 'r') as file1:
        first_string = file1.readline().split()
        assert first_string[3] == 'payout'
    os.remove('temp.json')
    os.remove('temp2.txt')

def test_become_rate():
    data = [{'salary': '20'}, {'hourly_rate': '12'}]
    become_rate(data)
    assert data[0]['rate'] == '20'
    assert data[1]['rate'] == '12'


def test_csv_type():
    assert csv_type('file.csv') == 'file.csv'
    try:
        csv_type('file.txt')
    except argparse.ArgumentTypeError as e1:
        assert type(e1) == argparse.ArgumentTypeError





