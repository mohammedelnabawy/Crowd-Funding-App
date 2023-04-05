import DisplayData
from registerAndlogin import sign
import ReadWriteData
DisplayData.display_data(["     choose an option    "], ["1 - login  ", "2 - Register", "3 - Exit   "])

while True:
    no = input('Enter choise: ')
    if no.isdigit():
        break
    else:
        print('Invalid Choice')

def choice(no):
    if(no==1):
        token = sign.login()
        DisplayData.display_data(["     choose an option    "], ["1 - Create project  ", "2 - List projects  ", "3 - Edit project   ", "4 - Delete project ", "5 - Exit           "])
    elif(no==2):
       user = sign.registeration_user()
       ReadWriteData.add_data("./Data/users.txt", user)
    elif(no==3):
        print("Three")
    else:
        print("Invalid Choice")

    
choice(int(no))