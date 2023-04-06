import DisplayData
import ReadWriteData
from registerAndlogin import sign
from CRUD import operations
from colorama import Fore, Back, Style


login_menu = ["1 - login  ", "2 - Register", "3 - Exit   "]
project_CRUD_menue = ["1 - Create project  ", "2 - List projects  ", "3 - Edit project   ", "4 - Delete project ", "5 - Exit           "]
project_menue = ['Id', 'Owner_id', 'Project title', 'Project desc','Project budget', 'Project start date', 'Project End data']
project_editing_menue = ['1 - Project title    ', '2 - Project desc     ','3 - Project budget    ', '4 - Project start date', '5 - Project End data ']



def Enter_choice(name):
    while True:
        no = input(f'Enter {name}: ')
        if no.isdigit():
            return no
        else:
            print(Fore.RED + f'\n Invalid {name} \n' + Style.RESET_ALL)

def call_menue(token):
        DisplayData.display_data(["     choose an option    "], project_CRUD_menue)
        menu_val = Enter_choice('Choice')
        menue(int(menu_val), token) 

def call_login_menue():
    DisplayData.display_data(["     choose an option    "], login_menu)
    choice(int(Enter_choice('Choice')))


def choice(no):
    if(no==1):
        token = sign.login()
        call_menue(token)
    elif(no==2):
        user = sign.registeration_user()
        flag = ReadWriteData.add_data("./Data/users.txt", user)
        if flag == True:
            print(Fore.GREEN + '\n   users added successfully \n' + Style.RESET_ALL)
        call_login_menue()
    elif(no==3):
        print(Fore.GREEN + '\n  Exit \n' + Style.RESET_ALL)
    else:
        print(Fore.RED + '\n Invalid Choice \n' + Style.RESET_ALL)
        call_login_menue()


def menue(no, token):
    if(no==1):
        project_data = project_data = operations.Create_project(token)
        flag = ReadWriteData.add_data('Data/projects.txt', project_data)
        if flag == True:
            print(Fore.GREEN + '\n   project added successfully \n' + Style.RESET_ALL)
        call_menue(token)
    elif(no==2):
        data = ReadWriteData.read_data('./Data/projects.txt')
        DisplayData.display_data(project_menue, data)
        call_menue(token)
    elif(no==3):
        DisplayData.display_data(['choose an item'], project_editing_menue)
        while True:
            feildnum = Enter_choice('Choice')
            if int(feildnum) <= 5 and int(feildnum) >= 1:
                break
            else:
                print(Fore.RED + '\n Invalid Choice \n' + Style.RESET_ALL)
                
        row_id = Enter_choice('Project Id')
        message = operations.edit_data(int(row_id), int(feildnum), int(token))
        print(Fore.GREEN + '\n  ' + message + '\n' + Style.RESET_ALL)
        call_menue(token)
    elif(no==4):
        row_id = Enter_choice('Id')
        message = operations.delete_project(int(row_id), int(token))
        print(Fore.GREEN + '\n  ' + message + '\n' + Style.RESET_ALL)
        call_menue(token)
    elif(no==5):
        call_login_menue()
    else:
        print(Fore.RED + '\n Invalid Choice \n' + Style.RESET_ALL)
        call_menue(token)



call_login_menue()