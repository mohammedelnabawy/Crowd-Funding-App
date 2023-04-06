from registerAndlogin import validation
from colorama import Fore, Back, Style
import ReadWriteData
import re
import time

mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
name_regex = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
mobile_regex = re.compile(r'^01[0215]+[0-9]{8}')
pass_reges = re.compile(r'[0-9a-zA-Z]{8,}')

def enter_data(Data_name, Data_regex=''):
    while True:
        add_data = input(f'Enter your {Data_name}: ')
        if len(add_data) and re.fullmatch(Data_regex, add_data):
            return add_data
        else:
            print(Fore.RED + f"\n   Invalid {Data_name}....\n" + Style.RESET_ALL)

def registeration_user():
    id = round(time.time())
    f_name = enter_data("First name", name_regex)
    l_name = enter_data("Last name", name_regex)
    Email = validation.check_mail()
    mobile = enter_data("mobile", mobile_regex)
    passwords = validation.validate_confirm_pass()
    return (f'{id}:{f_name}:{l_name}:{Email}:{passwords}:{mobile}')

def login():
    Email = enter_data("Email", mail_regex)
    password = enter_data("Password", pass_reges)
    users = ReadWriteData.read_data('Data/users.txt')
    if users == False:
        print(Fore.RED + '\n   Invalid credintial\n' + Style.RESET_ALL)
        return 
    for user in users:
        if Email == user.split(':')[3] and password == user.split(':')[4]:
            print(Fore.GREEN + '\n   you are loggedIn\n' + Style.RESET_ALL)
            return user.split(':')[0]
            break
    else:
        print(Fore.RED + '\n   Invalid credintial\n' + Style.RESET_ALL)
        login()
