import re
import time
import datetime
from prettytable import PrettyTable


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

def add_data(path, data):
    try:
        file1 = open(path, "a")
        file1.write(data)
        file1.write("\n")
    except Exception:
        print("unable to open file")



def login():
    Email = enter_data("Email", mail_regex)
    password = enter_data("Password", pass_reges)
    users = read_users()
    if users == False:
        print("Invalid credintial")
        return 

    for user in users:
        if Email == user.split(':')[3] and password == user.split(':')[4]:
            print("you are logged in")
            return user.split(':')[0]
            break
    else:
        print("Invalid credintial")


def read_data(path):
    try:
        file1 = open(path, "r")
    except Exception:
        return False
    else:
        users = file1.readlines()
        return users



def Create_project():
    id = round(time.time())
    owner_id = loged_user
    title = enter_data("Project title", name_regex)
    description = enter_data("Project description", name_regex)
    budget = enter_data("Project budget", budget_regex)
    start_date = validate_date("Project start date")
    end_date = validate_date("Project end date")
    return (f'{id}:{owner_id}:{title}:{description}:{budget}:{start_date}:{end_date}') 

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
            print("Input date is not valid..")


# print(int(login()))
# add_user("Data/users.txt")
# read_users()
# registeration_user()

loged_user=1

# Create_project()

# add_data("Data/projects.txt",Create_project())

def display_data(metaDAta, data):
    t = PrettyTable(metaDAta)
    for item in data:
        item_values = item.split(':')
        t.add_row(item_values)
    else:
        print(t)


def project_search(id, projects):
    for x, item in enumerate(projects):
        if id == int(item.split(':')[0]):
            return x
    else:
        return -1



def edit_data(id, feildnum, data):
    projects = read_data("Data/projects.txt")
    project_location=project_search(id, projects)
    if project_location == -1:
        return "project dosn't exist"

    project_data = projects[project_location].split(':')
    project_data[feildnum]=data
    project_data_str = ':'.join(project_data[::])
    projects[project_location]=project_data_str
    return projects


def delete_project(id):
    projects = read_data("Data/projects.txt")
    project_location=project_search(id, projects)
    if project_location == -1:
        return "project dosn't exist"

    projects.pop(project_location)
    return projects


def overwrite_data(path, data):
    try:
        file1 = open(path, "w")
        file1.writelines(data)
    except Exception:
        print("unable to open file")





# print(delete_project(1680644836))
# print(edit_data(1680644836, 2, "mmmmmm"))
overwrite_data("Data/projects.txt",delete_project(1680644836))