from colorama import Fore, Back, Style
import re
import datetime

mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
name_regex = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
mobile_regex = re.compile(r'^01[0215]+[0-9]{8}')
budget_regex = re.compile(r'^[1-9][0-9]*$')
date_regex = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
pass_reges = re.compile(r'[0-9a-zA-Z]{8,}')


def enter_data(Data_name, Data_regex=''):
    while True:
        add_data = input(f'Enter your {Data_name}: ')
        if len(add_data) and re.fullmatch(Data_regex, add_data):
            return add_data
        else:
            print(Fore.RED + f'\n  Invalid {Data_name}....\n' + Style.RESET_ALL)

def validate_date(Date_name):
    while True:
        date = enter_data(Date_name, date_regex)
        day, month, year = date.split('/')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if(isValidDate):
            return date
        else:
            print(Fore.RED + '\n    Date is not valid..\n' + Style.RESET_ALL)
            
