
from registerAndlogin import sign
import re

import ReadWriteData
mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pass_reges = re.compile(r'[0-9a-zA-Z]{8,}')



def validate_confirm_pass():
    while True:
        password = sign.enter_data("Password", pass_reges)
        confirm_password = sign.enter_data("Password again", pass_reges)
        if password == confirm_password:
            return password

def check_mail():
    while True:
        Email = sign.enter_data("Email", mail_regex)
        users = ReadWriteData.read_data('Data/users.txt')
        if users == False:
            return Email

        for user in users:
            if Email == user.split(':')[3]:
                print("Email is already exist")
                break
        else:
            return Email