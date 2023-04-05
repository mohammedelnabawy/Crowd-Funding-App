import DisplayData
from registerAndlogin import sign
import ReadWriteData
from projectsFiles import projrct
DisplayData.display_data(["     choose an option    "], ["1 - login  ", "2 - Register", "3 - Exit   "])

project_menue = ['Id', 'Owner_id', 'Project title', 'Project desc','Project budget', 'Project start date', 'Project End data']
project_editing_menue = ['Project title', 'Project desc','Project budget', 'Project start date', 'Project End data']

def Enter_choice(name):
    while True:
        no = input(f'Enter {name}: ')
        if no.isdigit():
            return no
        else:
            print(f'Invalid {name}')

def choice(no):
    if(no==1):
        token = sign.login()
        DisplayData.display_data(["     choose an option    "], ["1 - Create project  ", "2 - List projects  ", "3 - Edit project   ", "4 - Delete project ", "5 - Exit           "])
        menu_val = Enter_choice('Choice')
        menue(int(menu_val), token) 
    elif(no==2):
       user = sign.registeration_user()
       ReadWriteData.add_data("./Data/users.txt", user)
    elif(no==3):
        print("Three")
    else:
        print("Invalid Choice")


def menue(no, token):
    if(no==1):
        project_data = project_data = projrct.Create_project(token)
        ReadWriteData.add_data('Data/projects.txt', project_data)
    elif(no==2):
        data = ReadWriteData.read_data('./Data/projects.txt')
        DisplayData.display_data(project_menue, data)
    elif(no==3):
        DisplayData.display_data(['choose an item'], project_editing_menue)
        feildnum = Enter_choice('Choice')
        row_id = Enter_choice('Id')
        message = projrct.edit_data(int(row_id), int(feildnum), int(token))
        print(message)
    elif(no==4):
        row_id = Enter_choice('Id')
        message = projrct.delete_project(int(row_id), int(token))
        print(message)
    elif(no==5):
        print("Three")
    else:
        print("Invalid Choice")




choice(int(Enter_choice('Choice')))