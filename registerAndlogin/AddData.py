import re
def enter_data(Data_name, Data_regex=''):
    while True:
        add_data = input(f'Enter your {Data_name}: ')
        if len(add_data) and re.fullmatch(Data_regex, add_data):
            return add_data
        else:
            print(f"Invalid {Data_name}....")