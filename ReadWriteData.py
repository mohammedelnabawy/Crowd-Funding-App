def add_data(path, data):
    try:
        file1 = open(path, "a")
        file1.write(data)
        file1.write("\n")
    except Exception:
        print("unable to open file")

def read_data(path):
    try:
        file1 = open(path, "r")
    except Exception:
        return False
    else:
        users = file1.readlines()
        return users

def overwrite_data(path, data):
    try:
        file1 = open(path, "w")
        file1.writelines(data)
    except Exception:
        print("unable to open file")