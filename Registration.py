import re
import time

mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
name_regex = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
mobile_regex = re.compile(r'^01[215]+[0-9]{8}')


def enter_name(name):
    while True:
        add_name = input(f'Enter the {name}......')
        if len(add_name) and re.fullmatch(name_regex, add_name):
            return add_name
        else:
            print("Enter Valid name ....")

def enter_email(email):
    while True:
        add_email = input(f'Enter the {email}......')
        if len(add_email) and re.fullmatch(mail_regex, add_email):
            return add_email
        else:
            print("Enter Valid email ....")

def enter_mobile(mobile):
    while True:
        add_phone = input(f'Enter the {mobile}......')
        if len(add_phone) and re.fullmatch(mobile_regex, add_phone):
            return add_phone
        else:
            print("Enter Valid mobile ....")

def enter_password(password):
    while True:
        add_password = input(f'Enter {password}......')
        if len(add_password) > 8:
            return add_password
        else:
            print("Enter Valid Password.....")

def validate_confirm_pass():
    while True:
        password = enter_password("password")
        confirm_password = enter_password("Confirm password")
        if password == confirm_password:
            return password


def registeration_user():
    id = round(time.time())
    f_name = enter_name("First name")
    l_name = enter_name("Last name")
    Email = enter_email("Email")
    mobile = enter_mobile("mobile")
    passwords = validate_confirm_pass()
    return (f'{id}:{f_name}:{l_name}:{Email}:{passwords}:{mobile}')


def add_user():
    try:
        file1 = open("users.txt", "a")
        file1.write("\n")
        file1.write(registeration_user())
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
        file1 = open("users.txt", "r")
    except Exception:
        print("unable to open file")
    else:
        users = file1.readlines()
        return users

login()
add_user()