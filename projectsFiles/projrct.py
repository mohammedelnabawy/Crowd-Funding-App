from projectsFiles import validate

def Create_project(loged_user):
    id = round(time.time())
    owner_id = loged_user
    title = enter_data("Project title", name_regex)
    description = enter_data("Project description", name_regex)
    budget = enter_data("Project budget", budget_regex)
    start_date = validate.validate_date("Project start date")
    end_date = validate.validate_date("Project end date")
    return (f'{id}:{owner_id}:{title}:{description}:{budget}:{start_date}:{end_date}') 

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

