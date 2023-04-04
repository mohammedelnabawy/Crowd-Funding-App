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
            print(f"Invalid {Data_name}....")

def validate_confirm_pass():
    while True:
        password = enter_data("Password", pass_reges)
        confirm_password = enter_data("Password again", pass_reges)
        if password == confirm_password:
            return password

def registeration_user():
    id = round(time.time())
    f_name = enter_data("First name", name_regex)
    l_name = enter_data("Last name", name_regex)
    Email = check_mail()
    mobile = enter_data("mobile", mobile_regex)
    passwords = validate_confirm_pass()
    return (f'{id}:{f_name}:{l_name}:{Email}:{passwords}:{mobile}')

def check_mail():
    while True:
        Email = enter_data("Email", mail_regex)
        users = read_users()
        if users == False:
            return Email

        for user in users:
            if Email == user.split(':')[3]:
                print("Email is already exist")
                break
        else:
            return Email

def add_user():
    try:
        file1 = open("Data/users.txt", "a")
        file1.write(registeration_user())
        file1.write("\n")
    except Exception:
        print("unable to open file")



def login():
    Email = enter_email("Email")
    password = enter_password("password")
    users = read_users()
    for user in users:
        if Email == user.split(':')[3] and password == user.split(':')[4]:
            print("you are logged in")
            break
    else:
        print("Invalid credintial")


def read_users():
    try:
        file1 = open("Data/users.txt", "r")
    except Exception:
        return False
    else:
        users = file1.readlines()
        return users

# login()
add_user()
# read_users()
# registeration_user()