from projectsFiles import validate
import ReadWriteData
import time
import re

mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
name_regex = re.compile(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$')
mobile_regex = re.compile(r'^01[0215]+[0-9]{8}')
budget_regex = re.compile(r'^[1-9][0-9]*$')
date_regex = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
pass_reges = re.compile(r'[0-9a-zA-Z]{8,}')


def Create_project(loged_user):
    id = round(time.time())
    owner_id = loged_user
    title = validate.enter_data("Project title", name_regex)
    description = validate.enter_data("Project description", name_regex)
    budget = validate.enter_data("Project budget", budget_regex)
    start_date = validate.validate_date("Project start date")
    end_date = validate.validate_date("Project end date")
    return (f'{id}:{owner_id}:{title}:{description}:{budget}:{start_date}:{end_date}') 

def project_search(id, projects, token):
    for x, item in enumerate(projects):
        if id == int(item.split(':')[0]):
            if token == int(item.split(':')[1]):
                return x
            else:
                return -2
    else:
        return -1

def edit_data(id, feildnum, token):
    projects = ReadWriteData.read_data("Data/projects.txt")
    project_location=project_search(id, projects, token)
    if project_location == -1:
        return "project dosn't exist"
    elif project_location == -2:
        return "you are not authorized"

    project_data = projects[project_location].split(':')
    if feildnum==1:
        data = validate.enter_data("Project title", name_regex)
    elif feildnum==2:
        data = validate.enter_data("Project description", name_regex)
    elif feildnum==3:
        data = validate.enter_data("Project budget", budget_regex)
    elif feildnum==4:
        data = validate.validate_date("Project start date")
    elif feildnum==5:
        data = validate.validate_date("Project end date")
    else:
        return "Invalid item"

    project_data[feildnum+1]=data
    project_data_str = ':'.join(project_data[::])
    projects[project_location]=project_data_str
    ReadWriteData.overwrite_data('Data/projects.txt', projects)
    return 'Field updated succsessfuly'

def delete_project(id, token):
    projects = ReadWriteData.read_data("Data/projects.txt")
    project_location=project_search(id, projects, token)
    if project_location == -1:
        return "project dosn't exist"
    elif project_location == -2:
        return "you are not authorized"
    projects.pop(project_location)
    ReadWriteData.overwrite_data('Data/projects.txt', projects)
    return 'Field deleted succsessfuly'

