from prettytable import PrettyTable

def display_data(metaDAta, data):
    t = PrettyTable(metaDAta)
    for item in data:
        item_values = item.split(':')
        t.add_row(item_values)
    else:
        print(t)
